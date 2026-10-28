# Chain health

**Coverage: 31/32 chains implemented** — the full government roster bar Nativ HaHesed, whose portal has returned HTTP 500 since July 2026 (it stays registered and will be enabled when it returns).

**Last nightly check (2026-10-28T13:52:31+00:00): 25/32 reachable.** The check runs from a GitHub-hosted runner outside Israel and fetches every file type of every chain. Daily reachability fluctuates: chains sometimes publish empty or late files, and some small chains publish sporadically — that's the chains' portals, not the library. `geo-blocked` = the portal only answers Israeli IPs (verified through an Israeli proxy). `degraded` = some file types were missing/empty at check time.

| Chain | Status | Stores | Prices | Promos | Note |
|---|---|---|---|---|---|
| `shufersal` | `ok` | 418 | 6571 | 1 |  |
| `super-pharm` | `down` | — | — | — | stores: FileNotFound: super-pharm: no Stores file | prices: FileNotFound: super-pharm: no PriceFull file | promos: FileNotFound: super-pharm: no PromoFull file |
| `wolt` | `ok` | 34 | 0 | 525 |  |
| `carrefour` | `geo-blocked` | 147 | 9431 | 1541 | reachable from Israeli IPs only (verified via proxy) |
| `hatzi-hinam` | `down` | — | — | — | stores: PortalError: GET https://shop.hazi-hinam.co.il/Prices -> HTTP 403 | prices: PortalError: GET https://shop.hazi-hinam.co.il/Prices -> HTTP 403 | promos: PortalError: GET https://shop.hazi-hinam.co.il/Prices -> HTTP 403 |
| `rami-levy` | `ok` | 99 | 5218 | 1082 |  |
| `tiv-taam` | `ok` | 54 | 76 | 24 |  |
| `yochananof` | `ok` | 51 | 11774 | 1355 |  |
| `osher-ad` | `ok` | 24 | 6168 | 731 |  |
| `dor-alon` | `ok` | 157 | 2094 | 325 |  |
| `keshet-teamim` | `ok` | 28 | 6347 | 1695 |  |
| `super-cofix` | `degraded` | 34 | — | — | prices: FileNotFound: super-cofix: no PriceFull file | promos: FileNotFound: super-cofix: no PromoFull file |
| `politzer` | `ok` | 8 | 14474 | 1202 |  |
| `stop-market` | `ok` | 11 | 17494 | 2766 |  |
| `fresh-market` | `ok` | 46 | 9181 | 1367 |  |
| `salach-dabach` | `ok` | 12 | 12387 | 1791 |  |
| `super-yuda` | `ok` | 26 | 6402 | 378 |  |
| `yellow` | `ok` | 242 | 2278 | 657 |  |
| `good-pharm` | `ok` | 83 | 3363 | 363 |  |
| `super-bareket` | `ok` | 15 | 4554 | 685 |  |
| `king-store` | `ok` | 48 | 2333 | 301 |  |
| `maayan-2000` | `ok` | 38 | 2758 | 371 |  |
| `meshnat-yosef` | `ok` | 4 | 5415 | 214 |  |
| `shefa-birkat-hashem` | `ok` | 22 | 3688 | 564 |  |
| `shuk-hayir` | `ok` | 26 | 1356 | 0 |  |
| `super-sapir` | `ok` | 130 | 2236 | 0 |  |
| `zol-vebegadol` | `ok` | 35 | 4267 | 488 |  |
| `city-market` | `ok` | 71 | 4325 | 0 |  |
| `victory` | `down` | — | — | — | stores: PortalError: GET https://laibcatalog.co.il/webapi/api/getfiles failed after 3 attempts: 401 Auth Failed (code: ip_blacklisted) | prices: PortalError: GET https://laibcatalog.co.il/webapi/api/getfiles failed after 3 attempts: 401 Auth Failed (code: ip_blacklisted) | promos: PortalError: GET h |
| `mahsanei-hashuk` | `down` | — | — | — | stores: PortalError: GET https://laibcatalog.co.il/webapi/api/getfiles failed after 3 attempts: 401 Auth Failed (code: ip_blacklisted) | prices: PortalError: GET https://laibcatalog.co.il/webapi/api/getfiles failed after 3 attempts: 401 Auth Failed (code: ip_blacklisted) | promos: PortalError: GET h |
| `het-cohen` | `down` | — | — | — | stores: PortalError: GET https://laibcatalog.co.il/webapi/api/getfiles failed after 3 attempts: 401 Auth Failed (code: ip_blacklisted) | prices: PortalError: GET https://laibcatalog.co.il/webapi/api/getfiles failed after 3 attempts: 401 Auth Failed (code: ip_blacklisted) | promos: PortalError: GET h |
| `nativ-hahesed` | `down` | — | — | — | portal still unreachable (PortalError) |
