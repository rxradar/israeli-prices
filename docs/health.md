# Chain health

**Coverage: 31/32 chains implemented** — the full government roster bar Nativ HaHesed, whose portal has returned HTTP 500 since July 2026 (it stays registered and will be enabled when it returns).

**Last nightly check (2026-11-16T16:49:31+00:00): 28/32 reachable.** The check runs from a GitHub-hosted runner outside Israel and fetches every file type of every chain. Daily reachability fluctuates: chains sometimes publish empty or late files, and some small chains publish sporadically — that's the chains' portals, not the library. `geo-blocked` = the portal only answers Israeli IPs (verified through an Israeli proxy). `degraded` = some file types were missing/empty at check time.

| Chain | Status | Stores | Prices | Promos | Note |
|---|---|---|---|---|---|
| `shufersal` | `ok` | 417 | 6570 | 13 |  |
| `super-pharm` | `down` | — | — | — | stores: FileNotFound: super-pharm: no Stores file | prices: FileNotFound: super-pharm: no PriceFull file | promos: FileNotFound: super-pharm: no PromoFull file |
| `wolt` | `ok` | 37 | 0 | 0 |  |
| `carrefour` | `geo-blocked` | 147 | 11099 | 1609 | reachable from Israeli IPs only (verified via proxy) |
| `hatzi-hinam` | `down` | — | — | — | stores: PortalError: GET https://shop.hazi-hinam.co.il/Prices -> HTTP 403 | prices: PortalError: GET https://shop.hazi-hinam.co.il/Prices -> HTTP 403 | promos: PortalError: GET https://shop.hazi-hinam.co.il/Prices -> HTTP 403 |
| `rami-levy` | `ok` | 99 | 5326 | 1077 |  |
| `tiv-taam` | `ok` | 54 | 52 | 17 |  |
| `yochananof` | `ok` | 51 | 11799 | 1375 |  |
| `osher-ad` | `ok` | 24 | 5966 | 831 |  |
| `dor-alon` | `ok` | 157 | 5167 | 604 |  |
| `keshet-teamim` | `ok` | 28 | 6009 | 1500 |  |
| `super-cofix` | `degraded` | 34 | — | — | prices: FileNotFound: super-cofix: no PriceFull file | promos: FileNotFound: super-cofix: no PromoFull file |
| `politzer` | `ok` | 8 | 13936 | 1155 |  |
| `stop-market` | `ok` | 11 | 17580 | 2826 |  |
| `fresh-market` | `ok` | 73 | 8311 | 793 |  |
| `salach-dabach` | `ok` | 12 | 17144 | 2013 |  |
| `super-yuda` | `ok` | 26 | 6459 | 417 |  |
| `yellow` | `ok` | 242 | 1881 | 687 |  |
| `good-pharm` | `ok` | 84 | 3303 | 326 |  |
| `super-bareket` | `ok` | 15 | 4762 | 713 |  |
| `king-store` | `ok` | 48 | 2371 | 262 |  |
| `maayan-2000` | `ok` | 38 | 3062 | 419 |  |
| `meshnat-yosef` | `ok` | 4 | 5547 | 230 |  |
| `shefa-birkat-hashem` | `ok` | 22 | 3918 | 531 |  |
| `shuk-hayir` | `ok` | 26 | 1699 | 0 |  |
| `super-sapir` | `ok` | 130 | 19 | 1 |  |
| `zol-vebegadol` | `ok` | 35 | 4282 | 501 |  |
| `city-market` | `ok` | 69 | 4295 | 0 |  |
| `victory` | `geo-blocked` | 70 | 8565 | 4356 | reachable from Israeli IPs only (verified via proxy) |
| `mahsanei-hashuk` | `geo-blocked` | 72 | 12485 | 6198 | reachable from Israeli IPs only (verified via proxy) |
| `het-cohen` | `geo-blocked` | 5 | 8936 | 2896 | reachable from Israeli IPs only (verified via proxy) |
| `nativ-hahesed` | `down` | — | — | — | portal still unreachable (PortalError) |
