# Chain health

**Coverage: 31/32 chains implemented** — the full government roster bar Nativ HaHesed, whose portal has returned HTTP 500 since July 2026 (it stays registered and will be enabled when it returns).

**Last nightly check (2026-11-20T15:56:46+00:00): 28/32 reachable.** The check runs from a GitHub-hosted runner outside Israel and fetches every file type of every chain. Daily reachability fluctuates: chains sometimes publish empty or late files, and some small chains publish sporadically — that's the chains' portals, not the library. `geo-blocked` = the portal only answers Israeli IPs (verified through an Israeli proxy). `degraded` = some file types were missing/empty at check time.

| Chain | Status | Stores | Prices | Promos | Note |
|---|---|---|---|---|---|
| `shufersal` | `ok` | 418 | 6539 | 13 |  |
| `super-pharm` | `down` | — | — | — | stores: FileNotFound: super-pharm: no Stores file | prices: FileNotFound: super-pharm: no PriceFull file | promos: FileNotFound: super-pharm: no PromoFull file |
| `wolt` | `ok` | 37 | 0 | 730 |  |
| `carrefour` | `geo-blocked` | 147 | 11135 | 1663 | reachable from Israeli IPs only (verified via proxy) |
| `hatzi-hinam` | `down` | — | — | — | stores: PortalError: GET https://shop.hazi-hinam.co.il/Prices -> HTTP 403 | prices: PortalError: GET https://shop.hazi-hinam.co.il/Prices -> HTTP 403 | promos: PortalError: GET https://shop.hazi-hinam.co.il/Prices -> HTTP 403 |
| `rami-levy` | `ok` | 99 | 14235 | 2663 |  |
| `tiv-taam` | `ok` | 54 | 52 | 17 |  |
| `yochananof` | `ok` | 51 | 11833 | 1401 |  |
| `osher-ad` | `ok` | 24 | 5968 | 863 |  |
| `dor-alon` | `ok` | 157 | 1681 | 335 |  |
| `keshet-teamim` | `ok` | 28 | 6405 | 1521 |  |
| `super-cofix` | `degraded` | 34 | — | — | prices: FileNotFound: super-cofix: no PriceFull file | promos: FileNotFound: super-cofix: no PromoFull file |
| `politzer` | `ok` | 8 | 14581 | 1214 |  |
| `stop-market` | `ok` | 11 | 15257 | 2839 |  |
| `fresh-market` | `ok` | 73 | 9263 | 1530 |  |
| `salach-dabach` | `ok` | 12 | 12314 | 2071 |  |
| `super-yuda` | `ok` | 26 | 6475 | 422 |  |
| `yellow` | `ok` | 242 | 1822 | 684 |  |
| `good-pharm` | `ok` | 84 | 3292 | 331 |  |
| `super-bareket` | `ok` | 15 | 4838 | 729 |  |
| `king-store` | `ok` | 48 | 2398 | 269 |  |
| `maayan-2000` | `ok` | 38 | 3019 | 432 |  |
| `meshnat-yosef` | `ok` | 4 | 5615 | 257 |  |
| `shefa-birkat-hashem` | `ok` | 22 | 3869 | 605 |  |
| `shuk-hayir` | `ok` | 26 | 1551 | 0 |  |
| `super-sapir` | `ok` | 130 | 20 | 1 |  |
| `zol-vebegadol` | `ok` | 35 | 4302 | 504 |  |
| `city-market` | `ok` | 69 | 4147 | 0 |  |
| `victory` | `geo-blocked` | 70 | 8695 | 4279 | reachable from Israeli IPs only (verified via proxy) |
| `mahsanei-hashuk` | `geo-blocked` | 72 | 12494 | 6229 | reachable from Israeli IPs only (verified via proxy) |
| `het-cohen` | `geo-blocked` | 5 | 7228 | 2216 | reachable from Israeli IPs only (verified via proxy) |
| `nativ-hahesed` | `down` | — | — | — | portal still unreachable (PortalError) |
