"""Super-Pharm portal adapter (prices.super-pharm.co.il).

Self-hosted portal, no auth. Files are listed in a server-rendered
MVC.Grid (20 rows per page, newest first) filterable with query
parameters like ``?Category-equals=PriceFull&page=2``. Download links
are relative (``/Download/<name>.gz?bucketName=...``) and serve the
gzipped XML directly.
"""

from __future__ import annotations

import html
import re
from typing import Iterator

from ..models import ChainInfo, FileRef, FileType
from .base import ChainAdapter, parse_filename, same_store

BASE_URL = "https://prices.super-pharm.co.il"

_CATEGORIES = {
    FileType.PRICE: "Price",
    FileType.PRICE_FULL: "PriceFull",
    FileType.PROMO: "Promo",
    FileType.PROMO_FULL: "PromoFull",
    FileType.STORES: "Stores",
}

_DOWNLOAD_LINK_RE = re.compile(r'href="(/Download/[^"]+)"')
_TOTAL_ROWS_RE = re.compile(r'data-total-rows="(\d+)"')
_ROWS_PER_PAGE = 20

INFO = ChainInfo(
    slug="super-pharm",
    name="Super-Pharm",
    name_he="סופר פארם",
    chain_id="7290172900007",
    portal_url=BASE_URL,
    portal_family="self-hosted",
    sector="pharmacy",
    implemented=True,
)


class SuperPharmAdapter(ChainAdapter):
    info = INFO

    def iter_files(
        self,
        file_type: FileType | None = None,
        store_id: str | None = None,
    ) -> Iterator[FileRef]:
        params: dict = {}
        if file_type is not None:
            params["Category-equals"] = _CATEGORIES[file_type]
        page = 1
        total_pages = None
        while total_pages is None or page <= total_pages:
            resp = self.client.get(BASE_URL, params={**params, "page": page})
            if total_pages is None:
                m = _TOTAL_ROWS_RE.search(resp.text)
                total = int(m.group(1)) if m else 0
                total_pages = max(1, -(-total // _ROWS_PER_PAGE))
            links = _DOWNLOAD_LINK_RE.findall(resp.text)
            if not links:
                return
            for link in links:
                path = html.unescape(link)
                name = path.split("?")[0].rsplit("/", 1)[-1]
                ftype, fstore, published = parse_filename(name)
                if file_type is not None and ftype != file_type:
                    continue
                if store_id is not None and not same_store(fstore, store_id):
                    continue
                yield FileRef(
                    chain=self.info.slug,
                    name=name,
                    file_type=ftype or FileType.PRICE,
                    url=BASE_URL + path,
                    store_id=fstore,
                    published_at=published,
                )
            page += 1
