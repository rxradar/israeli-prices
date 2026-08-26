"""Email an alert when chain health changes.

Compares the previous docs/health.json to the fresh one and sends a
plain-text summary through Amazon SES when chains regress, recover, or
a down portal starts answering again. Sends nothing when nothing
changed. With --run-failed, reports that the health run itself crashed.

Env:
- ALERT_EMAIL      recipient (required — without it the script exits 0)
- ALERT_FROM       sender identity (default no-reply@rxradar.xyz)
- AWS_REGION       SES region (default us-east-2)
- AWS credentials  with ses:SendEmail (standard boto3 resolution)

Usage: health_alert.py prev.json new.json | health_alert.py --run-failed
"""

from __future__ import annotations

import json
import os
import sys

REPORT_URL = "https://github.com/rxradar/israeli-prices/blob/main/docs/health.md"

# lower is healthier; equal ranks never alert
RANKS = {"ok": 0, "geo-blocked": 0, "attention": 1, "degraded": 1, "down": 2}


def send(subject: str, body: str) -> None:
    recipient = os.environ.get("ALERT_EMAIL")
    if not recipient:
        print("ALERT_EMAIL not set — skipping alert", file=sys.stderr)
        return
    import boto3

    ses = boto3.client("ses", region_name=os.environ.get("AWS_REGION", "us-east-2"))
    ses.send_email(
        Source=os.environ.get("ALERT_FROM", "no-reply@rxradar.xyz"),
        Destination={"ToAddresses": [recipient]},
        Message={
            "Subject": {"Data": subject},
            "Body": {"Text": {"Data": body}},
        },
    )
    print(f"alert sent: {subject}", file=sys.stderr)


def main() -> None:
    if "--run-failed" in sys.argv:
        send(
            "[israeli-prices] nightly health run FAILED",
            "The nightly health workflow crashed before producing a report.\n"
            "Runs: https://github.com/rxradar/israeli-prices/actions\n",
        )
        return

    prev_path, new_path = sys.argv[1], sys.argv[2]
    prev = {c["slug"]: c for c in json.load(open(prev_path))["chains"]}
    new = json.load(open(new_path))
    changes = []
    for chain in new["chains"]:
        slug = chain["slug"]
        old_status = prev.get(slug, {}).get("status")
        if old_status is None or old_status == chain["status"]:
            continue
        if RANKS.get(chain["status"], 2) == RANKS.get(old_status, 2):
            continue  # sideways move (e.g. ok <-> geo-blocked), not news
        worse = RANKS.get(chain["status"], 2) > RANKS.get(old_status, 2)
        note = chain.get("note", "")
        changes.append((worse, f"{slug}: {old_status} -> {chain['status']}"
                               + (f" — {note[:160]}" if note else "")))

    if not changes:
        print("no status changes — no alert", file=sys.stderr)
        return

    regressions = [line for worse, line in changes if worse]
    recoveries = [line for worse, line in changes if not worse]
    live = sum(1 for c in new["chains"] if c["status"] in ("ok", "geo-blocked"))
    total = len(new["chains"])

    if regressions:
        subject = f"[israeli-prices] {len(regressions)} chain(s) regressed ({live}/{total} live)"
    else:
        subject = f"[israeli-prices] {len(recoveries)} chain(s) recovered ({live}/{total} live)"

    body = ""
    if regressions:
        body += "Regressed:\n" + "\n".join(f"  - {line}" for line in regressions) + "\n\n"
    if recoveries:
        body += "Recovered:\n" + "\n".join(f"  - {line}" for line in recoveries) + "\n\n"
    body += f"Checked at: {new['checked_at']}\nFull report: {REPORT_URL}\n"
    send(subject, body)


if __name__ == "__main__":
    main()
