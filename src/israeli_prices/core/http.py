"""Thin HTTP layer shared by all chain adapters: retries, timeouts, proxy."""

from __future__ import annotations

import time

import httpx

from ..exceptions import PortalError

USER_AGENT = "israeli-prices/0.1 (+https://github.com/rxradar/israeli-prices)"
DEFAULT_TIMEOUT = 30.0
DEFAULT_RETRIES = 3


class HttpClient:
    """httpx wrapper with simple exponential-backoff retries.

    Some portals are geo-restricted to Israeli IPs; pass ``proxy`` (any
    httpx-compatible proxy URL) to route requests through one.
    """

    def __init__(
        self,
        timeout: float = DEFAULT_TIMEOUT,
        retries: int = DEFAULT_RETRIES,
        proxy: str | None = None,
    ):
        self.retries = retries
        self._client = httpx.Client(
            timeout=timeout,
            proxy=proxy,
            headers={"User-Agent": USER_AGENT},
            follow_redirects=True,
        )

    def get(self, url: str, params: dict | None = None) -> httpx.Response:
        return self._request("GET", url, params=params)

    def post(self, url: str, data: dict | None = None) -> httpx.Response:
        return self._request("POST", url, data=data)

    def _request(self, method: str, url: str, **kwargs) -> httpx.Response:
        last_exc: Exception | None = None
        for attempt in range(self.retries):
            try:
                resp = self._client.request(method, url, **kwargs)
                if resp.status_code >= 500:
                    raise PortalError(f"{method} {url} -> HTTP {resp.status_code}")
                resp.raise_for_status()
                return resp
            except httpx.HTTPStatusError as exc:
                # 4xx client error (5xx is raised as PortalError above and
                # retried): retrying will not change the outcome, so fail fast.
                raise PortalError(
                    f"{method} {url} -> HTTP {exc.response.status_code}"
                ) from exc
            except (httpx.HTTPError, PortalError) as exc:
                last_exc = exc
                if attempt < self.retries - 1:
                    time.sleep(2**attempt)
        raise PortalError(
            f"{method} {url} failed after {self.retries} attempts: {last_exc}"
        )

    def close(self) -> None:
        self._client.close()
