"""Hatzi Hinam adapter (shop.hazi-hinam.co.il/Prices).

Self-hosted listing page with ``t`` (1=prices, 2=promos, 3=stores) and
``p`` (page) query parameters; download links point straight at Azure
blob storage, unsigned.
"""

from __future__ import annotations

import re
from typing import Iterator

from ..models import ChainInfo, FileRef, FileType
from .base import ChainAdapter, parse_filename, same_store

BASE_URL = "https://shop.hazi-hinam.co.il"

_T_CODES = {
    None: "",
    FileType.PRICE: "1",
    FileType.PRICE_FULL: "1",
    FileType.PROMO: "2",
    FileType.PROMO_FULL: "2",
    FileType.STORES: "3",
}

_LINK_RE = re.compile(r'href="(https://[^"]+?\.(?:gz|xml)[^"]*)"')

INFO = ChainInfo(
    slug="hatzi-hinam",
    name="Hatzi Hinam",
    name_he="חצי חינם",
    chain_id="7290700100008",
    portal_url=f"{BASE_URL}/Prices",
    portal_family="self-hosted",
    implemented=True,
)


class HaziHinamAdapter(ChainAdapter):
    info = INFO

    def iter_files(
        self,
        file_type: FileType | None = None,
        store_id: str | None = None,
    ) -> Iterator[FileRef]:
        page = 1
        seen: set[str] = set()
        while True:
            resp = self.client.get(
                f"{BASE_URL}/Prices", params={"t": _T_CODES[file_type], "p": page}
            )
            new = 0
            for url in _LINK_RE.findall(resp.text):
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
