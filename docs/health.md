# Chain health

**Coverage: 31/32 chains implemented** — the full government roster bar Nativ HaHesed, whose portal has returned HTTP 500 since July 2026 (it stays registered and will be enabled when it returns).

**Last nightly check (2026-11-18T16:15:58+00:00): 28/32 reachable.** The check runs from a GitHub-hosted runner outside Israel and fetches every file type of every chain. Daily reachability fluctuates: chains sometimes publish empty or late files, and some small chains publish sporadically — that's the chains' portals, not the library. `geo-blocked` = the portal only answers Israeli IPs (verified through an Israeli proxy). `degraded` = some file types were missing/empty at check time.

| Chain | Status | Stores | Prices | Promos | Note |
|---|---|---|---|---|---|
| `shufersal` | `ok` | 418 | 6551 | 13 |  |
| `super-pharm` | `down` | — | — | — | stores: FileNotFound: super-pharm: no Stores file | prices: FileNotFound: super-pharm: no PriceFull file | promos: FileNotFound: super-pharm: no PromoFull file |
| `wolt` | `ok` | 37 | 0 | 0 |  |
| `carrefour` | `geo-blocked` | 147 | 11097 | 1644 | reachable from Israeli IPs only (verified via proxy) |
| `hatzi-hinam` | `down` | — | — | — | stores: PortalError: GET https://shop.hazi-hinam.co.il/Prices -> HTTP 403 | prices: PortalError: GET https://shop.hazi-hinam.co.il/Prices -> HTTP 403 | promos: PortalError: GET https://shop.hazi-hinam.co.il/Prices -> HTTP 403 |
| `rami-levy` | `ok` | 99 | 5325 | 1077 |  |
| `tiv-taam` | `ok` | 54 | 52 | 17 |  |
| `yochananof` | `ok` | 51 | 11831 | 1393 |  |
| `osher-ad` | `ok` | 24 | 5973 | 855 |  |
| `dor-alon` | `ok` | 157 | 1488 | 334 |  |
| `keshet-teamim` | `ok` | 28 | 6417 | 1511 |  |
| `super-cofix` | `degraded` | 34 | — | — | prices: FileNotFound: super-cofix: no PriceFull file | promos: FileNotFound: super-cofix: no PromoFull file |
| `politzer` | `ok` | 8 | 13782 | 1213 |  |
| `stop-market` | `ok` | 11 | 17570 | 2836 |  |
| `fresh-market` | `ok` | 73 | 8297 | 796 |  |
| `salach-dabach` | `ok` | 12 | 12333 | 2066 |  |
| `super-yuda` | `ok` | 26 | 6466 | 421 |  |
| `yellow` | `ok` | 242 | 1526 | 683 |  |
| `good-pharm` | `ok` | 84 | 3299 | 327 |  |
| `super-bareket` | `ok` | 15 | 4801 | 723 |  |
| `king-store` | `ok` | 48 | 2389 | 268 |  |
| `maayan-2000` | `ok` | 38 | 3077 | 442 |  |
| `meshnat-yosef` | `ok` | 4 | 5593 | 247 |  |
| `shefa-birkat-hashem` | `ok` | 22 | 3789 | 576 |  |
| `shuk-hayir` | `ok` | 26 | 1481 | 0 |  |
| `super-sapir` | `ok` | 130 | 19 | 1 |  |
| `zol-vebegadol` | `ok` | 35 | 4293 | 503 |  |
| `city-market` | `ok` | 69 | 4214 | 0 |  |
| `victory` | `geo-blocked` | 70 | 8632 | 4249 | reachable from Israeli IPs only (verified via proxy) |
| `mahsanei-hashuk` | `geo-blocked` | 72 | 12494 | 6311 | reachable from Israeli IPs only (verified via proxy) |
| `het-cohen` | `geo-blocked` | 5 | 7217 | 2204 | reachable from Israeli IPs only (verified via proxy) |
| `nativ-hahesed` | `down` | — | — | — | portal still unreachable (PortalError) |
