"""Adapter for the Cerberus shared portal (url.publishedprices.co.il).

Thirteen chains publish through one Cerberus FTP web frontend, each
behind its own login. Credentials are public — they are listed on the
government's transparency page (password is empty for most chains).

Protocol (discovered live, 2026-08-24):

- login: GET /login carries a CSRF token in a ``<meta name="csrftoken">``
  tag plus a session cookie; POST /login/user with the form fields.
  A failed login lands back on /login; success redirects to /file and
  rotates the CSRF token.
- listing: POST /file/json/dir with ``cd`` (directory) and optional
  ``sSearch`` (server-side substring filter) returns a DataTables JSON
  payload; ``iDisplayLength`` accepts large values, so one request
  lists everything.
- download: GET /file/d/<path> with the session cookie.
- sessions expire after ~30 minutes: an expired call answers with the
  HTML login page instead of JSON, which triggers one re-login.

Quirks: chains publish placeholder ``NULL*`` files when nothing changed
(skipped); stray files from other chains appear in some folders
(filtered by chain id); Stores files may be bare .xml, sometimes UTF-16;
Super Yuda publishes everything under a /Yuda subfolder.
"""

from __future__ import annotations

import re
from collections.abc import Iterator
from datetime import datetime
from urllib.parse import quote

from ..core.http import HttpClient
from ..exceptions import PortalError
from ..models import ChainInfo, FileRef, FileType
from .base import ChainAdapter, parse_filename, same_store

BASE_URL = "https://url.publishedprices.co.il"

_CSRF_RE = re.compile(r'<meta name="csrftoken" content="([^"]+)"')


class CerberusAdapter(ChainAdapter):
    def __init__(
        self,
        info: ChainInfo,
        password: str = "",
        folder: str = "/",
        client: HttpClient | None = None,
    ):
        super().__init__(client=client)
        self.info = info
        self._password = password
        self._folder = folder
        self._csrf: str | None = None

    # -- session ------------------------------------------------------

    def _login(self) -> None:
        resp = self.client.get(f"{BASE_URL}/login")
        m = _CSRF_RE.search(resp.text)
        if not m:
            raise PortalError("cerberus: no CSRF token on the login page")
        resp = self.client.post(
            f"{BASE_URL}/login/user",
            data={
                "r": "",
                "username": self.info.username,
                "password": self._password,
                "Submit": "Sign in",
                "csrftoken": m.group(1),
            },
        )
        if resp.url.path.startswith("/login"):
            raise PortalError(
                f"cerberus: login rejected for user {self.info.username!r}"
            )
        m = _CSRF_RE.search(resp.text)
        if not m:
            raise PortalError("cerberus: no CSRF token after login")
        self._csrf = m.group(1)

    def _list_dir(self, folder: str, search: str = "") -> list[dict]:
        if self._csrf is None:
            self._login()
        for _ in range(2):  # one retry after a session-expiry re-login
            resp = self.client.post(
                f"{BASE_URL}/file/json/dir",
                data={
                    "iDisplayLength": 100000,
                    "sSearch": search,
                    "cd": folder,
                    "csrftoken": self._csrf,
                },
            )
            if "json" in resp.headers.get("content-type", ""):
                return resp.json().get("aaData", [])
            self._login()
        raise PortalError("cerberus: listing still not JSON after re-login")

    # -- files --------------------------------------------------------

    def iter_files(
        self,
        file_type: FileType | None = None,
        store_id: str | None = None,
    ) -> Iterator[FileRef]:
        search = file_type.value if file_type else ""
        rows = self._list_dir(self._folder, search=search)

        folder = self._folder
        parsed_rows = []
        for row in rows:
            name = row.get("fname", "")
            if row.get("type") != "file" or not name:
                continue
            if name.lower().startswith("null"):  # "no update" placeholder
                continue
            if self.info.chain_id and self.info.chain_id not in name:
                continue  # stray file from another chain
            ftype, fstore, published = parse_filename(name)
            if file_type is not None and ftype != file_type:
                continue
            if store_id is not None and not same_store(fstore, store_id):
                continue
            parsed_rows.append((published, name, ftype, fstore))

        # The portal's display ``time`` is not consistently sortable: live
        # responses can interleave week-old rows ahead of today's files. The
        # timestamp embedded in the mandated filename is the authoritative
        # ordering signal and keeps the ChainAdapter newest-first contract.
        parsed_rows.sort(
            key=lambda row: (row[0] is not None, row[0] or datetime.min, row[1]),
            reverse=True,
        )

        for published, name, ftype, fstore in parsed_rows:
            prefix = "" if folder == "/" else folder.strip("/") + "/"
            yield FileRef(
                chain=self.info.slug,
                name=name,
                file_type=ftype or FileType.PRICE,
                url=f"{BASE_URL}/file/d/{prefix}{quote(name)}",
                store_id=fstore,
                published_at=published,
            )

    def download(self, ref: FileRef) -> bytes:
        if self._csrf is None:
            self._login()
        resp = self.client.get(ref.url)
        if "text/html" in resp.headers.get("content-type", ""):
            self._login()  # session expired mid-run
            resp = self.client.get(ref.url)
        return resp.content


# -- the thirteen chains ----------------------------------------------

def _chain(slug, name, name_he, chain_id, username, sector="supermarket"):
    return ChainInfo(
        slug=slug, name=name, name_he=name_he, chain_id=chain_id,
        portal_url=f"{BASE_URL}/login", portal_family="cerberus",
        username=username, sector=sector, implemented=True,
    )


# slug -> (info, password, folder); passwords are public (gov.il)
CERBERUS_SPECS: dict[str, tuple[ChainInfo, str, str]] = {
    spec[0].slug: spec
    for spec in [
        (_chain("rami-levy", "Rami Levy", "רמי לוי", "7290058140886", "RamiLevi"), "", "/"),
        (_chain("tiv-taam", "Tiv Taam", "טיב טעם", "7290873255550", "TivTaam"), "", "/"),
        (_chain("yochananof", "Yochananof", "יוחננוף", "7290803800003", "yohananof"), "", "/"),
        (_chain("osher-ad", "Osher Ad", "אושר עד", "7290103152017", "osherad"), "", "/"),
        (_chain("dor-alon", "Dor Alon", "דור אלון", "7290492000005", "doralon", "convenience"), "", "/"),
        (_chain("keshet-teamim", "Keshet Teamim", "קשת טעמים", "7290785400000", "Keshet"), "", "/"),
        (_chain("super-cofix", "Super Cofix", "סופר קופיקס", "7291056200008", "SuperCofixApp", "convenience"), "", "/"),
        (_chain("politzer", "Politzer", "פוליצר", "7291059100008", "politzer"), "", "/"),
        (_chain("stop-market", "Stop Market", "סטופ מרקט", "7290639000004", "Stop_Market"), "", "/"),
        (_chain("fresh-market", "Fresh Market", "פרש מרקט", "7290876100000", "freshmarket"), "", "/"),
        (_chain("salach-dabach", "Salach Dabach", "סאלח דבאח", "7290526500006", "SalachD"), "12345", "/"),
        (_chain("super-yuda", "Super Yuda", "סופר יודה", "7290058177776", "yuda_ho"), "Yud@147", "/Yuda"),
        (_chain("yellow", "Yellow", "ילו", "7290644700005", "Paz_bo", "convenience"), "paz468", "/"),
    ]
}

CERBERUS_CHAINS: list[ChainInfo] = [spec[0] for spec in CERBERUS_SPECS.values()]


def make_cerberus_adapter(slug: str, client: HttpClient | None = None) -> CerberusAdapter:
    info, password, folder = CERBERUS_SPECS[slug]
    return CerberusAdapter(info, password=password, folder=folder, client=client)
