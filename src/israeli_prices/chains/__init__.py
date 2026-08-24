"""Chain registry: every chain covered by the transparency law.

Source: the Ministry of Economy's official portal list
(gov.il, "מחירון מוצרי מזון" / price transparency page). Portal
usernames listed there are public. ``implemented=True`` marks chains
this library ships an adapter for today.
"""

from __future__ import annotations

from ..core.http import HttpClient
from ..exceptions import ChainNotFound
from ..models import ChainInfo
from .base import ChainAdapter
from .shufersal import ShufersalAdapter
from .superpharm import SuperPharmAdapter

_ADAPTERS: dict[str, type[ChainAdapter]] = {
    "shufersal": ShufersalAdapter,
    "super-pharm": SuperPharmAdapter,
}

_CERBERUS = "https://url.retail.publishedprices.co.il"


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
    # --- Cerberus shared portal (login form; usernames published on gov.il) ---
    ChainInfo(slug="rami-levy", name="Rami Levy", name_he="רמי לוי", chain_id="7290058140886",
              portal_url=_CERBERUS, portal_family="cerberus", username="RamiLevi"),
    ChainInfo(slug="tiv-taam", name="Tiv Taam", name_he="טיב טעם", chain_id="7290873255550",
              portal_url=_CERBERUS, portal_family="cerberus", username="TivTaam"),
    ChainInfo(slug="yochananof", name="Yochananof", name_he="יוחננוף",
              chain_id="7290803800003", portal_url=_CERBERUS, portal_family="cerberus",
              username="yohananof"),
    ChainInfo(slug="osher-ad", name="Osher Ad", name_he="אושר עד", chain_id="7290103152017",
              portal_url=_CERBERUS, portal_family="cerberus", username="osherad"),
    ChainInfo(slug="dor-alon", name="Dor Alon", name_he="דור אלון", chain_id="7290492000005",
              portal_url=_CERBERUS, portal_family="cerberus", username="doralon",
              sector="convenience"),
    ChainInfo(slug="keshet-teamim", name="Keshet Teamim", name_he="קשת טעמים",
              chain_id="7290785400000", portal_url=_CERBERUS, portal_family="cerberus",
              username="Keshet"),
    ChainInfo(slug="super-cofix", name="Super Cofix", name_he="סופר קופיקס",
              chain_id="7291056200008", portal_url=_CERBERUS, portal_family="cerberus",
              username="SuperCofixApp", sector="convenience"),
    ChainInfo(slug="politzer", name="Politzer", name_he="פוליצר", chain_id="7291059100008",
              portal_url=_CERBERUS, portal_family="cerberus", username="politzer"),
    ChainInfo(slug="stop-market", name="Stop Market", name_he="סטופ מרקט",
              chain_id="7290639000004", portal_url=_CERBERUS, portal_family="cerberus",
              username="Stop_Market"),
    ChainInfo(slug="fresh-market", name="Fresh Market", name_he="פרש מרקט",
              chain_id="7290876100000", portal_url=_CERBERUS, portal_family="cerberus",
              username="freshmarket"),
    ChainInfo(slug="salach-dabach", name="Salach Dabach", name_he="סאלח דבאח",
              chain_id="7290526500006", portal_url=_CERBERUS, portal_family="cerberus",
              username="SalachD"),
    ChainInfo(slug="super-yuda", name="Super Yuda", name_he="סופר יודה",
              chain_id="7290058177776", portal_url=_CERBERUS, portal_family="cerberus",
              username="yuda_ho"),
    ChainInfo(slug="yellow", name="Yellow", name_he="ילו", chain_id="7290644700005",
              portal_url=_CERBERUS, portal_family="cerberus", username="Paz_bo",
              sector="convenience"),
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
