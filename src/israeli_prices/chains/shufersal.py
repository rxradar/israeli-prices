"""Shufersal portal adapter (prices.shufersal.co.il).

Self-hosted portal, no auth. Files are listed on a paginated HTML page
(newest first) and served from Azure blob storage through signed URLs
that expire after a few minutes — download soon after listing.

The Shufersal feed also covers the Be Pharm drugstore sub-chain.
"""

from __future__ import annotations

import html
import re
from collections.abc import Iterator

from ..models import ChainInfo, FileRef, FileType
from .base import ChainAdapter, parse_filename, same_store

BASE_URL = "https://prices.shufersal.co.il"

_CAT_IDS = {
    None: 0,  # all categories
    FileType.PRICE: 1,
    FileType.PRICE_FULL: 2,
    FileType.PROMO: 3,
    FileType.PROMO_FULL: 4,
    FileType.STORES: 5,
}

_BLOB_LINK_RE = re.compile(r'href="(https://[^"]+?\.gz[^"]*)"')

INFO = ChainInfo(
    slug="shufersal",
    name="Shufersal",
    name_he="שופרסל",
    chain_id="7290027600007",
    portal_url=BASE_URL,
    portal_family="self-hosted",
    sector="supermarket",
    implemented=True,
)


class ShufersalAdapter(ChainAdapter):
    info = INFO

    def iter_files(
        self,
        file_type: FileType | None = None,
        store_id: str | None = None,
    ) -> Iterator[FileRef]:
        cat_id = _CAT_IDS[file_type]
        page = 1
        seen: set[str] = set()
        while True:
            resp = self.client.get(
                f"{BASE_URL}/FileObject/UpdateCategory",
                params={"catID": cat_id, "storeId": 0, "page": page},
            )
            links = _BLOB_LINK_RE.findall(resp.text)
            new = 0
            for link in links:
                url = html.unescape(link)
                name = url.split("?")[0].rsplit("/", 1)[-1]
                if name in seen:
                    continue
                seen.add(name)
                new += 1
                ftype, fstore, published = parse_filename(name)
                if file_type is not None and ftype != file_type:
                    continue
                if store_id is not None and not same_store(fstore, store_id):
                    continue
                yield FileRef(
                    chain=self.info.slug,
                    name=name,
                    file_type=ftype or FileType.PRICE,
                    url=url,
                    store_id=fstore,
                    published_at=published,
                )
            if new == 0:
                return
            page += 1
