"""Nightly chain health check.

Fetches and parses the latest Stores / PriceFull / PromoFull file of
every implemented chain, probes the portals of unimplemented ones, and
writes docs/health.json, docs/health.md and the shields.io badge JSON.

Some portals only answer Israeli IPs (observed 2026-08-24: Super-Pharm
serves an empty listing, Hatzi Hinam answers 403, laibcatalog drops the
connection). When the optional ``IL_PROXY`` env var is set (an
httpx-compatible proxy URL with Israeli egress), chains that fail the
direct check are retried through it and reported as ``geo-blocked``
(working, but only from Israel) instead of ``down``.

Run from anywhere: python scripts/health_check.py
"""

from __future__ import annotations

import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

import israeli_prices as ilp
from israeli_prices import FileType
from israeli_prices.core.http import HttpClient

DOCS = Path(__file__).resolve().parent.parent / "docs"
IL_PROXY = os.environ.get("IL_PROXY")

CHECKS = (
    (FileType.STORES, "stores", "stores"),
    (FileType.PRICE_FULL, "prices", "items"),
    (FileType.PROMO_FULL, "promos", "promotions"),
)


def check_chain(slug: str, proxy: str | None = None) -> dict:
    client = HttpClient(proxy=proxy) if proxy else None
    adapter = ilp.get_adapter(slug, client=client)
    result: dict = {"slug": slug}
    errors = []
    for file_type, key, attr in CHECKS:
        try:
            ref = adapter.latest(file_type)
            parsed = ilp.parse(adapter.download(ref))
            result[key] = len(getattr(parsed, attr))
        except Exception as exc:  # noqa: BLE001 — a health check reports, never raises
            result[key] = None
            errors.append(f"{key}: {type(exc).__name__}: {exc}")
    failed = sum(1 for _, key, _ in CHECKS if result[key] is None)
    result["status"] = "ok" if failed == 0 else "down" if failed == len(CHECKS) else "degraded"
    if errors:
        result["note"] = " | ".join(errors)[:300]
    return result


def check_chain_geo_aware(slug: str) -> dict:
    result = check_chain(slug)
    if result["status"] == "ok" or not IL_PROXY:
        return result
    retried = check_chain(slug, proxy=IL_PROXY)
    if retried["status"] == "ok":
        retried["status"] = "geo-blocked"
        retried["note"] = "reachable from Israeli IPs only (verified via proxy)"
    return retried


def probe_portal(info) -> dict:
    """For unimplemented chains: is the portal alive again?"""
    try:
        resp = HttpClient(retries=1, timeout=15).get(info.portal_url)
        return {
            "slug": info.slug,
            "status": "attention",
            "note": f"portal answered HTTP {resp.status_code} — time to implement the adapter",
        }
    except Exception as exc:  # noqa: BLE001
        return {
            "slug": info.slug,
            "status": "down",
            "note": f"portal still unreachable ({type(exc).__name__})",
        }


def main() -> None:
    checked_at = datetime.now(timezone.utc).isoformat(timespec="seconds")
    rows = []
    for info in ilp.list_chains():
        print(f"checking {info.slug}...", file=sys.stderr, flush=True)
        rows.append(check_chain_geo_aware(info.slug) if info.implemented else probe_portal(info))

    total = len(rows)
    # coverage = chains this library implements (stable — the headline claim);
    # reachable = chains that passed every file-type check on this run (varies
    # with the portals: chains occasionally publish empty or late files).
    covered = sum(1 for c in ilp.list_chains() if c.implemented)
    reachable = sum(1 for r in rows if r["status"] in ("ok", "geo-blocked"))

    DOCS.joinpath("health.json").write_text(
        json.dumps({"checked_at": checked_at, "covered": covered, "total": total,
                    "reachable": reachable, "chains": rows}, ensure_ascii=False, indent=2)
        + "\n"
    )
    # the README badge shows COVERAGE, not daily liveness — a transient empty
    # file from a chain's portal should not drag the project's headline number.
    DOCS.joinpath("health-badge.json").write_text(
        json.dumps(
            {"schemaVersion": 1, "label": "chains", "message": f"{covered}/{total}",
             "color": "brightgreen"}
        )
        + "\n"
    )

    lines = [
        "# Chain health",
        "",
        f"**Coverage: {covered}/{total} chains implemented** — the full government "
        "roster bar Nativ HaHesed, whose portal has returned HTTP 500 since "
        "July 2026 (it stays registered and will be enabled when it returns).",
        "",
        f"**Last nightly check ({checked_at}): {reachable}/{total} reachable.** "
        "The check runs from a GitHub-hosted runner outside Israel and fetches "
        "every file type of every chain. Daily reachability fluctuates: chains "
        "sometimes publish empty or late files, and some small chains publish "
        "sporadically — that's the chains' portals, not the library. "
        "`geo-blocked` = the portal only answers Israeli IPs (verified through "
        "an Israeli proxy). `degraded` = some file types were missing/empty at "
        "check time.",
        "",
        "| Chain | Status | Stores | Prices | Promos | Note |",
        "|---|---|---|---|---|---|",
    ]
    for r in rows:
        lines.append(
            f"| `{r['slug']}` | `{r['status']}` "
            f"| {r.get('stores', '—') if r.get('stores') is not None else '—'} "
            f"| {r.get('prices', '—') if r.get('prices') is not None else '—'} "
            f"| {r.get('promos', '—') if r.get('promos') is not None else '—'} "
            f"| {r.get('note', '')} |"
        )
    DOCS.joinpath("health.md").write_text("\n".join(lines) + "\n")
    print(f"done: coverage {covered}/{total}, reachable {reachable}/{total}", file=sys.stderr)


if __name__ == "__main__":
    main()
