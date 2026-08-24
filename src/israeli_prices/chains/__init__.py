"""Chain registry: every chain covered by the transparency law.

Source: the Ministry of Economy's official portal list
(gov.il, "מחירון מוצרי מזון" / price transparency page). Portal
usernames listed there are public. ``implemented=True`` marks chains
this library ships an adapter for today.
"""

from __future__ import annotations

from functools import partial

from ..core.http import HttpClient
from ..exceptions import ChainNotFound
from ..models import ChainInfo
from .base import ChainAdapter
from .bina import BINA_CHAINS, make_bina_adapter
from .carrefour import CarrefourAdapter
from .cerberus import CERBERUS_CHAINS, make_cerberus_adapter
from .hazihinam import HaziHinamAdapter
from .laib import LAIB_CHAINS, make_laib_adapter
from .shufersal import ShufersalAdapter
from .superpharm import SuperPharmAdapter
from .wolt import WoltAdapter

_ADAPTERS: dict = {
    "shufersal": ShufersalAdapter,
    "super-pharm": SuperPharmAdapter,
    "wolt": WoltAdapter,
    "carrefour": CarrefourAdapter,
    "hatzi-hinam": HaziHinamAdapter,
    **{c.slug: partial(make_cerberus_adapter, c.slug) for c in CERBERUS_CHAINS},
    **{c.slug: partial(make_bina_adapter, c.slug) for c in BINA_CHAINS},
    **{c.slug: partial(make_laib_adapter, c.slug) for c in LAIB_CHAINS},
}


CHAINS: list[ChainInfo] = [
    # --- self-hosted portals (one adapter each) ---
    ShufersalAdapter.info,
    SuperPharmAdapter.info,
    WoltAdapter.info,
    CarrefourAdapter.info,
    HaziHinamAdapter.info,
    # --- Cerberus shared portal (13 chains, one adapter) ---
    *CERBERUS_CHAINS,
    # --- Bina portals (10 chains, one adapter) ---
    *BINA_CHAINS,
    # --- Laib catalog (3 chains, one adapter) ---
    *LAIB_CHAINS,
    # Nativ HaHesed's portal (a bare-IP IIS host) answered HTTP 500 on
    # every path when this registry was built (2026-08-24) — registered
    # but not implemented until the portal comes back.
    ChainInfo(slug="nativ-hahesed", name="Nativ HaHesed", name_he="נתיב החסד",
              chain_id="7290058160839", portal_url="http://141.226.203.152",
              portal_family="webbase"),
]

_BY_SLUG = {c.slug: c for c in CHAINS}


def list_chains(implemented_only: bool = False) -> list[ChainInfo]:
    if implemented_only:
        return [c for c in CHAINS if c.implemented]
    return list(CHAINS)


def get_adapter(chain: str, client: HttpClient | None = None) -> ChainAdapter:
    if chain not in _BY_SLUG:
        raise ChainNotFound(
            f"unknown chain {chain!r} — see israeli_prices.list_chains()"
        )
    adapter_cls = _ADAPTERS.get(chain)
    if adapter_cls is None:
        raise ChainNotFound(
            f"chain {chain!r} is on the roadmap but has no adapter yet "
            f"(portal: {_BY_SLUG[chain].portal_url})"
        )
    return adapter_cls(client=client)
