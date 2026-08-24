"""Wolt Market adapter (wm-gateway.wolt.com/isr-prices).

Wolt is an online-only aggregator covered by the law through the online
sales threshold. Its feed covers only Wolt Market — Wolt's own
dark-store venues — not the partner retailers selling on the Wolt
platform. It publishes a static index of daily pages
(``v1/YYYY-MM-DD.html``), each a plain link list to that day's files
(``download/YYYY-MM-DD/<name>``). "Stores" here are Wolt's virtual
market venues, not physical branches.
"""

from __future__ import annotations

import re
from typing import Iterator

from ..models import ChainInfo, FileRef, FileType
from .base import ChainAdapter, parse_filename, same_store

BASE_URL = "https://wm-gateway.wolt.com/isr-prices/public/v1"

_DATE_RE = re.compile(r'href="(\d{4}-\d{2}-\d{2})\.html"')
_FILE_RE = re.compile(r'href="(download/[^"]+)"')

INFO = ChainInfo(
    slug="wolt",
    name="Wolt Market",
    name_he="וולט",
    chain_id="7290058249350",
    portal_url=f"{BASE_URL}/index.html",
    portal_family="self-hosted",
    sector="delivery",
    implemented=True,
)


class WoltAdapter(ChainAdapter):
    info = INFO

    def iter_files(
        self,
        file_type: FileType | None = None,
        store_id: str | None = None,
    ) -> Iterator[FileRef]:
        index = self.client.get(f"{BASE_URL}/index.html").text
        for date in sorted(_DATE_RE.findall(index), reverse=True):
            page = self.client.get(f"{BASE_URL}/{date}.html").text
            day: list[FileRef] = []
            for rel in _FILE_RE.findall(page):
                name = rel.rsplit("/", 1)[-1]
                ftype, fstore, published = parse_filename(name)
                if file_type is not None and ftype != file_type:
                    continue
                if store_id is not None and not same_store(fstore, store_id):
                    continue
                day.append(
                    FileRef(
                        chain=self.info.slug,
                        name=name,
                        file_type=ftype or FileType.PRICE,
                        url=f"{BASE_URL}/{rel}",
                        store_id=fstore,
                        published_at=published,
                    )
                )
            day.sort(key=lambda r: (r.published_at is not None, r.published_at), reverse=True)
            yield from day
