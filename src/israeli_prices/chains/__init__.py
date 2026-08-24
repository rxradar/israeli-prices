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
from .cerberus import CERBERUS_CHAINS, make_cerberus_adapter
from .shufersal import ShufersalAdapter
from .superpharm import SuperPharmAdapter

_ADAPTERS: dict = {
    "shufersal": ShufersalAdapter,
    "super-pharm": SuperPharmAdapter,
    **{c.slug: partial(make_cerberus_adapter, c.slug) for c in CERBERUS_CHAINS},
}


def _bina(prefix: str) -> str:
    return f"https://{prefix}.binaprojects.com"


CHAINS: list[ChainInfo] = [
    ShufersalAdapter.info,
    SuperPharmAdapter.info,
    # --- self-hosted portals, no auth ---
    ChainInfo(slug="wolt", name="Wolt Market", name_he="וולט", chain_id="7290058249350",
              portal_url="https://wm-gateway.wolt.com/isr-prices/public/v1/index.html",
              portal_family="self-hosted", sector="delivery"),
    ChainInfo(slug="hatzi-hinam", name="Hatzi Hinam", name_he="חצי חינם", chain_id="7290700100008",
              portal_url="https://shop.hazi-hinam.co.il/Prices", portal_family="self-hosted"),
    ChainInfo(slug="carrefour", name="Carrefour Israel", name_he="קרפור", chain_id="7290055700007",
              portal_url="https://prices.carrefour.co.il", portal_family="self-hosted"),
    # --- Cerberus shared portal (13 chains, one adapter) ---
    *CERBERUS_CHAINS,
    # --- Bina portals, no auth ---
    ChainInfo(slug="good-pharm", name="Good Pharm", name_he="גוד פארם",
              chain_id="7290058197699", portal_url=_bina("goodpharm"),
              portal_family="bina", sector="pharmacy"),
    ChainInfo(slug="super-bareket", name="Super Bareket", name_he="סופר ברקת",
              chain_id="7290875100001", portal_url=_bina("superbareket"), portal_family="bina"),
    ChainInfo(slug="king-store", name="King Store", name_he="קינג סטור",
              chain_id="7290058108879", portal_url=_bina("kingstore"), portal_family="bina"),
    ChainInfo(slug="maayan-2000", name="Maayan 2000", name_he="מעיין 2000",
              chain_id="7290058159628", portal_url=_bina("maayan2000"), portal_family="bina"),
    ChainInfo(slug="meshnat-yosef", name="Meshnat Yosef", name_he="משנת יוסף",
              chain_id="7290058289400", portal_url=_bina("ktshivuk"), portal_family="bina"),
    ChainInfo(slug="shefa-birkat-hashem", name="Shefa Birkat Hashem", name_he="שפע ברכת השם",
              chain_id="7290058134977", portal_url=_bina("shefabirkathashem"),
              portal_family="bina"),
    ChainInfo(slug="shuk-hayir", name="Shuk Hayir", name_he="שוק העיר",
              chain_id="7290058148776", portal_url=_bina("shuk-hayir"), portal_family="bina"),
    ChainInfo(slug="super-sapir", name="Super Sapir", name_he="סופר ספיר",
              chain_id="7290058156016", portal_url=_bina("supersapir"), portal_family="bina"),
    ChainInfo(slug="zol-vebegadol", name="Zol VeBegadol", name_he="זול ובגדול",
              chain_id="7290058173198", portal_url=_bina("zolvebegadol"), portal_family="bina"),
    ChainInfo(slug="city-market", name="City Market", name_he="סיטי מרקט",
              chain_id="7290058288526", portal_url=_bina("citymarketkiryatgat"),
              portal_family="bina"),
    # --- Laib catalog (ex-Matrix; matrixcatalog.co.il is defunct) ---
    ChainInfo(slug="victory", name="Victory", name_he="ויקטורי", chain_id="7290696200003",
              portal_url="https://laibcatalog.co.il/victory/index.html",
              portal_family="laib"),
    ChainInfo(slug="mahsanei-hashuk", name="Mahsanei HaShuk", name_he="מחסני השוק",
              chain_id="7290661400001", portal_url="https://laibcatalog.co.il/mshuk/index.html",
              portal_family="laib"),
    ChainInfo(slug="het-cohen", name="Het Cohen", name_he="ח. כהן", chain_id="7290455000004",
              portal_url="https://laibcatalog.co.il/hcohen/index.html",
              portal_family="laib"),
    # --- one-off endpoints ---
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
