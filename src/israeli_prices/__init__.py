"""israeli-prices — typed Python client for Israel's retail
price-transparency data (prices, promotions, stores).

Quickstart::

    import israeli_prices as ilp

    ilp.list_chains()                            # every covered chain
    ilp.get_stores("super-pharm")                # -> StoresFile
    ilp.get_prices("shufersal", store_id="001")  # -> PriceFile
    ilp.get_promos("super-pharm", store_id="209")  # -> PromoFile
"""

from __future__ import annotations

from pathlib import Path

from .chains import get_adapter, list_chains
from .core.parse import parse
from .exceptions import (
    ChainNotFound,
    FileNotFound,
    IsraeliPricesError,
    ParseError,
    PortalError,
)
from .gtin import group_by_gtin, is_valid_gtin, to_gtin14
from .models import (
    ChainInfo,
    FileRef,
    FileType,
    PriceFile,
    PriceItem,
    PromoFile,
    Promotion,
    PromotionItem,
    Store,
    StoresFile,
)

__version__ = "0.2.0"

__all__ = [
    "list_chains",
    "get_adapter",
    "list_files",
    "get_stores",
    "get_prices",
    "get_promos",
    "download",
    "parse",
    "to_gtin14",
    "is_valid_gtin",
    "group_by_gtin",
    "ChainInfo",
    "FileRef",
    "FileType",
    "PriceFile",
    "PriceItem",
    "PromoFile",
    "Promotion",
    "PromotionItem",
    "Store",
    "StoresFile",
    "IsraeliPricesError",
    "ChainNotFound",
    "PortalError",
    "FileNotFound",
    "ParseError",
]


def list_files(
    chain: str,
    file_type: FileType | None = None,
    store_id: str | None = None,
    limit: int | None = None,
) -> list[FileRef]:
    """List files currently published on a chain's portal, newest first."""
    refs = []
    for ref in get_adapter(chain).iter_files(file_type=file_type, store_id=store_id):
        refs.append(ref)
        if limit is not None and len(refs) >= limit:
            break
    return refs


def download(ref: FileRef, dest: Path | str | None = None) -> bytes | Path:
    """Download a file's raw payload; write it to ``dest`` if given."""
    payload = get_adapter(ref.chain).download(ref)
    if dest is None:
        return payload
    path = Path(dest)
    if path.is_dir():
        path = path / ref.name
    path.write_bytes(payload)
    return path


def get_stores(chain: str) -> StoresFile:
    """Fetch and parse the chain's latest store list."""
    adapter = get_adapter(chain)
    ref = adapter.latest(FileType.STORES)
    return parse(adapter.download(ref))


def get_prices(chain: str, store_id: str, full: bool = True) -> PriceFile:
    """Fetch and parse the latest price file for one store.

    ``full=True`` (default) uses the PriceFull snapshot; ``full=False``
    uses the latest incremental Price update.
    """
    adapter = get_adapter(chain)
    ref = adapter.latest(FileType.PRICE_FULL if full else FileType.PRICE, store_id=store_id)
    return parse(adapter.download(ref))


def get_promos(chain: str, store_id: str, full: bool = True) -> PromoFile:
    """Fetch and parse the latest promotions file for one store."""
    adapter = get_adapter(chain)
    ref = adapter.latest(FileType.PROMO_FULL if full else FileType.PROMO, store_id=store_id)
    return parse(adapter.download(ref))
