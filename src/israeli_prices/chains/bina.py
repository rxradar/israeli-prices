"""Adapter for Bina portals ({prefix}.binaprojects.com).

Ten chains publish through identical Bina-hosted portals, one subdomain
per chain, no auth.

Protocol (discovered live, 2026-08-24):

- listing: POST /MainIO_Hok.aspx with ``WFileType`` (0=all, 1=stores,
  2=prices, 3=promos, 4=full prices, 5=full promos), ``WStore`` and
  ``WDate`` (both optional) returns a JSON array of
  ``{FileNm, Store, TypeFile, DateFile, ...}`` rows, capped at 1000 and
  covering the current day.
- download: files are served directly at /Download/<FileNm> (the
  portal's own Download.aspx indirection is not needed).

Quirks: several chains serve ZIP archives under a .gz file name (the
parser sniffs magic bytes); file names mix the legacy 12-digit
timestamp style with the standard one, and some chains uppercase the
.GZ extension.
"""

from __future__ import annotations

from datetime import datetime
from typing import Iterator
from urllib.parse import quote

from ..core.http import HttpClient
from ..exceptions import PortalError
from ..models import ChainInfo, FileRef, FileType
from .base import ChainAdapter, parse_filename, same_store

_FILE_TYPE_CODES = {
    None: "0",
    FileType.STORES: "1",
    FileType.PRICE: "2",
    FileType.PROMO: "3",
    FileType.PRICE_FULL: "4",
    FileType.PROMO_FULL: "5",
}


class BinaAdapter(ChainAdapter):
    def __init__(self, info: ChainInfo, prefix: str, client: HttpClient | None = None):
        super().__init__(client=client)
        self.info = info
        self._base = f"https://{prefix}.binaprojects.com"

    def iter_files(
        self,
        file_type: FileType | None = None,
        store_id: str | None = None,
    ) -> Iterator[FileRef]:
        resp = self.client.post(
            f"{self._base}/MainIO_Hok.aspx",
            data={"WStore": "", "WDate": "", "WFileType": _FILE_TYPE_CODES[file_type]},
        )
        try:
            rows = resp.json()
        except ValueError as exc:
            raise PortalError(f"{self.info.slug}: listing is not JSON") from exc

        parsed = []
        for row in rows:
            name = (row.get("FileNm") or "").strip()
            if not name:
                continue
            ftype, fstore, published = parse_filename(name)
            if file_type is not None and ftype != file_type:
                continue
            if store_id is not None and not same_store(fstore, store_id):
                continue
            parsed.append((published or datetime.min, name, ftype, fstore))

        parsed.sort(key=lambda p: p[0], reverse=True)
        for published, name, ftype, fstore in parsed:
            yield FileRef(
                chain=self.info.slug,
                name=name,
                file_type=ftype or FileType.PRICE,
                url=f"{self._base}/Download/{quote(name)}",
                store_id=fstore,
                published_at=None if published == datetime.min else published,
            )


# -- the ten chains -----------------------------------------------------

def _chain(slug, name, name_he, chain_id, prefix, sector="supermarket"):
    info = ChainInfo(
        slug=slug, name=name, name_he=name_he, chain_id=chain_id,
        portal_url=f"https://{prefix}.binaprojects.com/Main.aspx",
        portal_family="bina", sector=sector, implemented=True,
    )
    return info, prefix


# slug -> (info, subdomain prefix)
BINA_SPECS: dict[str, tuple[ChainInfo, str]] = {
    spec[0].slug: spec
    for spec in [
        _chain("good-pharm", "Good Pharm", "גוד פארם", "7290058197699", "goodpharm", "pharmacy"),
        _chain("super-bareket", "Super Bareket", "סופר ברקת", "7290875100001", "superbareket"),
        _chain("king-store", "King Store", "קינג סטור", "7290058108879", "kingstore"),
        _chain("maayan-2000", "Maayan 2000", "מעיין 2000", "7290058159628", "maayan2000"),
        _chain("meshnat-yosef", "Meshnat Yosef", "משנת יוסף", "7290058289400", "ktshivuk"),
        _chain("shefa-birkat-hashem", "Shefa Birkat Hashem", "שפע ברכת השם", "7290058134977", "shefabirkathashem"),
        _chain("shuk-hayir", "Shuk Hayir", "שוק העיר", "7290058148776", "shuk-hayir"),
        _chain("super-sapir", "Super Sapir", "סופר ספיר", "7290058156016", "supersapir"),
        _chain("zol-vebegadol", "Zol VeBegadol", "זול ובגדול", "7290058173198", "zolvebegadol"),
        _chain("city-market", "City Market", "סיטי מרקט", "7290058266241", "citymarketkiryatgat"),
    ]
}

BINA_CHAINS: list[ChainInfo] = [spec[0] for spec in BINA_SPECS.values()]


def make_bina_adapter(slug: str, client: HttpClient | None = None) -> BinaAdapter:
    info, prefix = BINA_SPECS[slug]
    return BinaAdapter(info, prefix, client=client)
