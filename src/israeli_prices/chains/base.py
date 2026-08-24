"""Base class and helpers shared by chain adapters."""

from __future__ import annotations

import re
from abc import ABC, abstractmethod
from collections.abc import Iterator
from datetime import datetime

from ..core.http import HttpClient
from ..exceptions import FileNotFound
from ..models import ChainInfo, FileRef, FileType

# longest prefixes first so "PriceFull" wins over "Price"
_TYPE_PREFIXES = (
    ("PriceFull", FileType.PRICE_FULL),
    ("PromoFull", FileType.PROMO_FULL),
    ("StoresFull", FileType.STORES),
    ("Price", FileType.PRICE),
    ("Promo", FileType.PROMO),
    ("Stores", FileType.STORES),
)

_FILENAME_RE = re.compile(r"^([A-Za-z]+)(\d{13})-(.+?)\.(?:gz|xml|zip)$", re.IGNORECASE)


def parse_filename(name: str) -> tuple[FileType | None, str | None, datetime | None]:
    """Extract (file_type, store_id, published_at) from a transparency
    file name, e.g. ``PriceFull7290027600007-001-001-20260824-030000.gz``.

    Segment layout between the chain id and the extension varies per
    chain. The timestamp is either a YYYYMMDD segment (optionally
    followed by HHMMSS) or a single YYYYMMDDHHMM segment. The store id
    is the last numeric segment before the timestamp when at least two
    segments precede it (sub-chain, store); when only one does, it is
    the store for per-store file types and the sub-chain for Stores
    files.
    """
    file_type = None
    for prefix, ft in _TYPE_PREFIXES:
        if name.lower().startswith(prefix.lower()):
            file_type = ft
            break

    m = _FILENAME_RE.match(name)
    if not m:
        return file_type, None, None

    segments = m.group(3).split("-")
    date_idx = next(
        (i for i, s in enumerate(segments) if len(s) in (8, 12) and s.isdigit()),
        None,
    )
    store_id = None
    published_at = None
    if date_idx is not None:
        if date_idx >= 2:
            store_id = segments[date_idx - 1]
        elif date_idx == 1 and file_type not in (FileType.STORES, None):
            store_id = segments[0]
        seg = segments[date_idx]
        try:
            if len(seg) == 12:
                published_at = datetime.strptime(seg, "%Y%m%d%H%M")
            else:
                published_at = datetime.strptime(seg, "%Y%m%d")
                nxt = segments[date_idx + 1] if date_idx + 1 < len(segments) else ""
                if len(nxt) == 6 and nxt.isdigit():
                    published_at = datetime.strptime(seg + nxt, "%Y%m%d%H%M%S")
        except ValueError:
            published_at = None
    return file_type, store_id, published_at


def same_store(a: str | None, b: str | None) -> bool:
    """Compare store ids leniently: '1', '001' and '0001' all match."""
    if a is None or b is None:
        return False
    if a.isdigit() and b.isdigit():
        return int(a) == int(b)
    return a == b


class ChainAdapter(ABC):
    """Fetches transparency files from one chain's portal."""

    info: ChainInfo

    def __init__(self, client: HttpClient | None = None):
        self.client = client or HttpClient()

    @abstractmethod
    def iter_files(
        self,
        file_type: FileType | None = None,
        store_id: str | None = None,
    ) -> Iterator[FileRef]:
        """Yield files listed on the portal, newest first."""

    def latest(self, file_type: FileType, store_id: str | None = None) -> FileRef:
        """The most recent file of ``file_type`` (optionally for one store)."""
        for ref in self.iter_files(file_type=file_type, store_id=store_id):
            return ref
        raise FileNotFound(
            f"{self.info.slug}: no {file_type.value} file"
            + (f" for store {store_id}" if store_id else "")
        )

    def download(self, ref: FileRef) -> bytes:
        """Download a file's raw payload (usually gzipped XML)."""
        return self.client.get(ref.url).content
