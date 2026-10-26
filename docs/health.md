# Chain health

**Coverage: 31/32 chains implemented** — the full government roster bar Nativ HaHesed, whose portal has returned HTTP 500 since July 2026 (it stays registered and will be enabled when it returns).

**Last nightly check (2026-10-26T13:58:25+00:00): 28/32 reachable.** The check runs from a GitHub-hosted runner outside Israel and fetches every file type of every chain. Daily reachability fluctuates: chains sometimes publish empty or late files, and some small chains publish sporadically — that's the chains' portals, not the library. `geo-blocked` = the portal only answers Israeli IPs (verified through an Israeli proxy). `degraded` = some file types were missing/empty at check time.

| Chain | Status | Stores | Prices | Promos | Note |
|---|---|---|---|---|---|
| `shufersal` | `ok` | 417 | 6567 | 1 |  |
| `super-pharm` | `down` | — | — | — | stores: PortalError: GET https://prices.super-pharm.co.il failed after 3 attempts: 502 Proxy Error: server_error Error creating ext request: Destination host connect timeout | prices: PortalError: GET https://prices.super-pharm.co.il failed after 3 attempts: 502 Proxy Error: server_error Error creat |
| `wolt` | `ok` | 34 | 6019 | 0 |  |
| `carrefour` | `geo-blocked` | 147 | 11089 | 1680 | reachable from Israeli IPs only (verified via proxy) |
| `hatzi-hinam` | `down` | — | — | — | stores: PortalError: GET https://shop.hazi-hinam.co.il/Prices -> HTTP 403 | prices: PortalError: GET https://shop.hazi-hinam.co.il/Prices -> HTTP 403 | promos: PortalError: GET https://shop.hazi-hinam.co.il/Prices -> HTTP 403 |
| `rami-levy` | `ok` | 99 | 5215 | 1082 |  |
| `tiv-taam` | `ok` | 54 | 125 | 41 |  |
| `yochananof` | `ok` | 51 | 11755 | 1374 |  |
| `osher-ad` | `ok` | 24 | 6222 | 722 |  |
| `dor-alon` | `ok` | 157 | 1918 | 325 |  |
| `keshet-teamim` | `ok` | 28 | 15643 | 2610 |  |
| `super-cofix` | `degraded` | 34 | — | — | prices: FileNotFound: super-cofix: no PriceFull file | promos: FileNotFound: super-cofix: no PromoFull file |
| `politzer` | `ok` | 8 | 12181 | 1205 |  |
| `stop-market` | `ok` | 11 | 14328 | 2737 |  |
| `fresh-market` | `ok` | 46 | 9175 | 1367 |  |
| `salach-dabach` | `ok` | 12 | 12391 | 1786 |  |
| `super-yuda` | `ok` | 26 | 6394 | 380 |  |
| `yellow` | `ok` | 242 | 1344 | 656 |  |
| `good-pharm` | `ok` | 83 | 3379 | 352 |  |
| `super-bareket` | `ok` | 15 | 4526 | 676 |  |
| `king-store` | `ok` | 48 | 2333 | 297 |  |
| `maayan-2000` | `ok` | 38 | 2775 | 380 |  |
| `meshnat-yosef` | `ok` | 4 | 5388 | 212 |  |
| `shefa-birkat-hashem` | `ok` | 22 | 3771 | 547 |  |
| `shuk-hayir` | `ok` | 26 | 1816 | 0 |  |
| `super-sapir` | `ok` | 130 | 2213 | 0 |  |
| `zol-vebegadol` | `ok` | 35 | 4281 | 488 |  |
| `city-market` | `ok` | 71 | 4319 | 0 |  |
| `victory` | `geo-blocked` | 70 | 8694 | 4569 | reachable from Israeli IPs only (verified via proxy) |
| `mahsanei-hashuk` | `geo-blocked` | 71 | 12375 | 6021 | reachable from Israeli IPs only (verified via proxy) |
| `het-cohen` | `geo-blocked` | 5 | 8919 | 2870 | reachable from Israeli IPs only (verified via proxy) |
| `nativ-hahesed` | `down` | — | — | — | portal still unreachable (PortalError) |
