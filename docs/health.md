# Chain health

**Coverage: 31/32 chains implemented** — the full government roster bar Nativ HaHesed, whose portal has returned HTTP 500 since July 2026 (it stays registered and will be enabled when it returns).

**Last nightly check (2026-11-19T16:23:38+00:00): 28/32 reachable.** The check runs from a GitHub-hosted runner outside Israel and fetches every file type of every chain. Daily reachability fluctuates: chains sometimes publish empty or late files, and some small chains publish sporadically — that's the chains' portals, not the library. `geo-blocked` = the portal only answers Israeli IPs (verified through an Israeli proxy). `degraded` = some file types were missing/empty at check time.

| Chain | Status | Stores | Prices | Promos | Note |
|---|---|---|---|---|---|
| `shufersal` | `ok` | 418 | 6541 | 13 |  |
| `super-pharm` | `down` | — | — | — | stores: FileNotFound: super-pharm: no Stores file | prices: FileNotFound: super-pharm: no PriceFull file | promos: FileNotFound: super-pharm: no PromoFull file |
| `wolt` | `ok` | 37 | 5204 | 0 |  |
| `carrefour` | `geo-blocked` | 147 | 11119 | 1650 | reachable from Israeli IPs only (verified via proxy) |
| `hatzi-hinam` | `down` | — | — | — | stores: PortalError: GET https://shop.hazi-hinam.co.il/Prices -> HTTP 403 | prices: PortalError: GET https://shop.hazi-hinam.co.il/Prices -> HTTP 403 | promos: PortalError: GET https://shop.hazi-hinam.co.il/Prices -> HTTP 403 |
| `rami-levy` | `ok` | 99 | 6204 | 1074 |  |
| `tiv-taam` | `ok` | 54 | 52 | 17 |  |
| `yochananof` | `ok` | 51 | 11826 | 1400 |  |
| `osher-ad` | `ok` | 24 | 5969 | 865 |  |
| `dor-alon` | `ok` | 157 | 1485 | 336 |  |
| `keshet-teamim` | `ok` | 28 | 6405 | 1521 |  |
| `super-cofix` | `degraded` | 34 | — | — | prices: FileNotFound: super-cofix: no PriceFull file | promos: FileNotFound: super-cofix: no PromoFull file |
| `politzer` | `ok` | 8 | 13952 | 1214 |  |
| `stop-market` | `ok` | 11 | 18395 | 2837 |  |
| `fresh-market` | `ok` | 73 | 8306 | 796 |  |
| `salach-dabach` | `ok` | 12 | 12323 | 2067 |  |
| `super-yuda` | `ok` | 26 | 6473 | 0 |  |
| `yellow` | `ok` | 242 | 279 | 684 |  |
| `good-pharm` | `ok` | 84 | 3300 | 330 |  |
| `super-bareket` | `ok` | 15 | 4789 | 720 |  |
| `king-store` | `ok` | 48 | 2388 | 263 |  |
| `maayan-2000` | `ok` | 38 | 3019 | 427 |  |
| `meshnat-yosef` | `ok` | 4 | 5590 | 252 |  |
| `shefa-birkat-hashem` | `ok` | 22 | 3652 | 580 |  |
| `shuk-hayir` | `ok` | 26 | 1324 | 0 |  |
| `super-sapir` | `ok` | 130 | 19 | 1 |  |
| `zol-vebegadol` | `ok` | 35 | 4298 | 505 |  |
| `city-market` | `ok` | 69 | 4203 | 0 |  |
| `victory` | `geo-blocked` | 70 | 7847 | 3552 | reachable from Israeli IPs only (verified via proxy) |
| `mahsanei-hashuk` | `geo-blocked` | 72 | 12501 | 6272 | reachable from Israeli IPs only (verified via proxy) |
| `het-cohen` | `geo-blocked` | 5 | 7227 | 2923 | reachable from Israeli IPs only (verified via proxy) |
| `nativ-hahesed` | `down` | — | — | — | portal still unreachable (PortalError) |
