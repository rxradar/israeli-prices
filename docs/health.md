# Chain health

**Coverage: 31/32 chains implemented** — the full government roster bar Nativ HaHesed, whose portal has returned HTTP 500 since July 2026 (it stays registered and will be enabled when it returns).

**Last nightly check (2026-10-29T13:58:31+00:00): 25/32 reachable.** The check runs from a GitHub-hosted runner outside Israel and fetches every file type of every chain. Daily reachability fluctuates: chains sometimes publish empty or late files, and some small chains publish sporadically — that's the chains' portals, not the library. `geo-blocked` = the portal only answers Israeli IPs (verified through an Israeli proxy). `degraded` = some file types were missing/empty at check time.

| Chain | Status | Stores | Prices | Promos | Note |
|---|---|---|---|---|---|
| `shufersal` | `ok` | 418 | 6571 | 1 |  |
| `super-pharm` | `down` | — | — | — | stores: FileNotFound: super-pharm: no Stores file | prices: FileNotFound: super-pharm: no PriceFull file | promos: FileNotFound: super-pharm: no PromoFull file |
| `wolt` | `ok` | 34 | 5838 | 569 |  |
| `carrefour` | `geo-blocked` | 147 | 11056 | 1687 | reachable from Israeli IPs only (verified via proxy) |
| `hatzi-hinam` | `down` | — | — | — | stores: PortalError: GET https://shop.hazi-hinam.co.il/Prices -> HTTP 403 | prices: PortalError: GET https://shop.hazi-hinam.co.il/Prices -> HTTP 403 | promos: PortalError: GET https://shop.hazi-hinam.co.il/Prices -> HTTP 403 |
| `rami-levy` | `ok` | 99 | 5214 | 1081 |  |
| `tiv-taam` | `ok` | 54 | 76 | 24 |  |
| `yochananof` | `ok` | 51 | 11766 | 2726 |  |
| `osher-ad` | `ok` | 24 | 6147 | 736 |  |
| `dor-alon` | `ok` | 157 | 1851 | 324 |  |
| `keshet-teamim` | `ok` | 28 | 6347 | 1377 |  |
| `super-cofix` | `degraded` | 34 | — | — | prices: FileNotFound: super-cofix: no PriceFull file | promos: FileNotFound: super-cofix: no PromoFull file |
| `politzer` | `ok` | 8 | 13652 | 1198 |  |
| `stop-market` | `ok` | 11 | 18288 | 3592 |  |
| `fresh-market` | `ok` | 48 | 9177 | 1368 |  |
| `salach-dabach` | `ok` | 12 | 16972 | 1783 |  |
| `super-yuda` | `ok` | 26 | 6400 | 378 |  |
| `yellow` | `ok` | 242 | 1650 | 710 |  |
| `good-pharm` | `ok` | 83 | 3370 | 364 |  |
| `super-bareket` | `ok` | 15 | 4566 | 687 |  |
| `king-store` | `ok` | 48 | 2346 | 303 |  |
| `maayan-2000` | `ok` | 38 | 2759 | 369 |  |
| `meshnat-yosef` | `ok` | 4 | 5398 | 217 |  |
| `shefa-birkat-hashem` | `ok` | 22 | 3601 | 545 |  |
| `shuk-hayir` | `ok` | 26 | 1463 | 0 |  |
| `super-sapir` | `ok` | 130 | 2243 | 0 |  |
| `zol-vebegadol` | `ok` | 35 | 4272 | 487 |  |
| `city-market` | `ok` | 71 | 4319 | 0 |  |
| `victory` | `down` | — | — | — | stores: PortalError: GET https://laibcatalog.co.il/webapi/api/getfiles failed after 3 attempts: 502 Proxy Error: server_error Error creating ext request: Destination host connect timeout | prices: PortalError: GET https://laibcatalog.co.il/webapi/api/getfiles failed after 3 attempts: 502 Proxy Error |
| `mahsanei-hashuk` | `down` | — | — | — | stores: PortalError: GET https://laibcatalog.co.il/webapi/api/getfiles failed after 3 attempts: 502 Proxy Error: server_error Error creating ext request: Destination host connect timeout | prices: PortalError: GET https://laibcatalog.co.il/webapi/api/getfiles failed after 3 attempts: 502 Proxy Error |
| `het-cohen` | `down` | — | — | — | stores: PortalError: GET https://laibcatalog.co.il/webapi/api/getfiles failed after 3 attempts: 502 Proxy Error: server_error Error creating ext request: Destination host connect timeout | prices: PortalError: GET https://laibcatalog.co.il/webapi/api/getfiles failed after 3 attempts: 502 Proxy Error |
| `nativ-hahesed` | `down` | — | — | — | portal still unreachable (PortalError) |
