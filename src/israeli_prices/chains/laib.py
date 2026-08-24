"""Adapter for the Laib catalog (laibcatalog.co.il).

Three chains publish through the same JSON API (the former
matrixcatalog.co.il host is defunct):

- listing: GET /webapi/api/getfiles?edi=<chain_id> returns a JSON array
  of ``{branchNumber, fileName, fileType, fileDate, fileSize}`` rows.
- download: GET /webapi/<chain_id>/<fileName>.
"""

from __future__ import annotations

from collections.abc import Iterator
from urllib.parse import quote

from ..core.http import HttpClient
from ..exceptions import PortalError
from ..models import ChainInfo, FileRef, FileType
from .base import ChainAdapter, parse_filename, same_store

BASE_URL = "https://laibcatalog.co.il"


class LaibAdapter(ChainAdapter):
    def __init__(self, info: ChainInfo, client: HttpClient | None = None):
        super().__init__(client=client)
        self.info = info

    def iter_files(
        self,
        file_type: FileType | None = None,
        store_id: str | None = None,
    ) -> Iterator[FileRef]:
        resp = self.client.get(
            f"{BASE_URL}/webapi/api/getfiles", params={"edi": self.info.chain_id}
        )
        try:
            rows = resp.json()
        except ValueError as exc:
            raise PortalError(f"{self.info.slug}: listing is not JSON") from exc

        # fileDate is "YYYY-MM-DD HH:MM:SS" — sorts lexicographically
        rows.sort(key=lambda r: r.get("fileDate", ""), reverse=True)
        for row in rows:
            name = (row.get("fileName") or "").strip()
            if not name:
                continue
            ftype, fstore, published = parse_filename(name)
            if file_type is not None and ftype != file_type:
                continue
            if store_id is not None and not same_store(fstore, store_id):
                continue
            yield FileRef(
                chain=self.info.slug,
                name=name,
                file_type=ftype or FileType.PRICE,
                url=f"{BASE_URL}/webapi/{self.info.chain_id}/{quote(name)}",
                store_id=fstore,
                published_at=published,
            )


def _chain(slug, name, name_he, chain_id, page):
    return ChainInfo(
        slug=slug, name=name, name_he=name_he, chain_id=chain_id,
        portal_url=f"{BASE_URL}/{page}/index.html", portal_family="laib",
        implemented=True,
    )


LAIB_SPECS: dict[str, ChainInfo] = {
    info.slug: info
    for info in [
        _chain("victory", "Victory", "ויקטורי", "7290696200003", "victory"),
        _chain("mahsanei-hashuk", "Mahsanei HaShuk", "מחסני השוק", "7290661400001", "mshuk"),
        _chain("het-cohen", "Het Cohen", "ח. כהן", "7290455000004", "hcohen"),
    ]
}

LAIB_CHAINS: list[ChainInfo] = list(LAIB_SPECS.values())


def make_laib_adapter(slug: str, client: HttpClient | None = None) -> LaibAdapter:
    return LaibAdapter(LAIB_SPECS[slug], client=client)
