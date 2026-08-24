"""Carrefour Israel adapter (prices.carrefour.co.il).

The portal renders the current day's file list as a JavaScript literal
embedded in the page (``const path = 'YYYYMMDD'`` +
``const files = [...]``); files are served from /<path>/<name>.
"""

from __future__ import annotations

import json
import re
from collections.abc import Iterator
from urllib.parse import quote

from ..exceptions import PortalError
from ..models import ChainInfo, FileRef, FileType
from .base import ChainAdapter, parse_filename, same_store

BASE_URL = "https://prices.carrefour.co.il"

_PATH_RE = re.compile(r"const path = '(\d{8})'")
_FILES_RE = re.compile(r"const files = (\[.*?\])", re.S)

INFO = ChainInfo(
    slug="carrefour",
    name="Carrefour Israel",
    name_he="קרפור",
    chain_id="7290055700007",
    portal_url=BASE_URL,
    portal_family="self-hosted",
    implemented=True,
)


class CarrefourAdapter(ChainAdapter):
    info = INFO

    def iter_files(
        self,
        file_type: FileType | None = None,
        store_id: str | None = None,
    ) -> Iterator[FileRef]:
        page = self.client.get(f"{BASE_URL}/").text
        path_m = _PATH_RE.search(page)
        files_m = _FILES_RE.search(page)
        if not path_m or not files_m:
            raise PortalError("carrefour: file list not found in the portal page")
        day = path_m.group(1)
        rows = json.loads(files_m.group(1))

        parsed = []
        for row in rows:
            name = (row.get("name") or "").strip()
            if not name:
                continue
            ftype, fstore, published = parse_filename(name)
            if file_type is not None and ftype != file_type:
                continue
            if store_id is not None and not same_store(fstore, store_id):
                continue
            parsed.append((published, name, ftype, fstore))

        parsed.sort(key=lambda p: (p[0] is not None, p[0]), reverse=True)
        for published, name, ftype, fstore in parsed:
            yield FileRef(
                chain=self.info.slug,
                name=name,
                file_type=ftype or FileType.PRICE,
                url=f"{BASE_URL}/{day}/{quote(name)}",
                store_id=fstore,
                published_at=published,
            )
