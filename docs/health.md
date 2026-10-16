# Chain health

**Coverage: 31/32 chains implemented** — the full government roster bar Nativ HaHesed, whose portal has returned HTTP 500 since July 2026 (it stays registered and will be enabled when it returns).

**Last nightly check (2026-10-16T12:08:06+00:00): 27/32 reachable.** The check runs from a GitHub-hosted runner outside Israel and fetches every file type of every chain. Daily reachability fluctuates: chains sometimes publish empty or late files, and some small chains publish sporadically — that's the chains' portals, not the library. `geo-blocked` = the portal only answers Israeli IPs (verified through an Israeli proxy). `degraded` = some file types were missing/empty at check time.

| Chain | Status | Stores | Prices | Promos | Note |
|---|---|---|---|---|---|
| `shufersal` | `down` | — | — | — | stores: PortalError: GET https://prices.shufersal.co.il/FileObject/UpdateCategory failed after 3 attempts: The read operation timed out | prices: PortalError: GET https://prices.shufersal.co.il/FileObject/UpdateCategory failed after 3 attempts: The read operation timed out | promos: PortalError: GET |
| `super-pharm` | `down` | — | — | — | stores: FileNotFound: super-pharm: no Stores file | prices: FileNotFound: super-pharm: no PriceFull file | promos: FileNotFound: super-pharm: no PromoFull file |
| `wolt` | `ok` | 34 | 6010 | 480 |  |
| `carrefour` | `ok` | 147 | 11133 | 1575 |  |
| `hatzi-hinam` | `down` | — | — | — | stores: PortalError: GET https://shop.hazi-hinam.co.il/Prices -> HTTP 403 | prices: PortalError: GET https://shop.hazi-hinam.co.il/Prices -> HTTP 403 | promos: PortalError: GET https://shop.hazi-hinam.co.il/Prices -> HTTP 403 |
| `rami-levy` | `ok` | 99 | 5221 | 1071 |  |
| `tiv-taam` | `ok` | 54 | 125 | 40 |  |
| `yochananof` | `ok` | 51 | 11787 | 1306 |  |
| `osher-ad` | `ok` | 24 | 6364 | 709 |  |
| `dor-alon` | `ok` | 158 | 5995 | 633 |  |
| `keshet-teamim` | `ok` | 27 | 6400 | 1695 |  |
| `super-cofix` | `degraded` | 34 | — | — | prices: FileNotFound: super-cofix: no PriceFull file | promos: FileNotFound: super-cofix: no PromoFull file |
| `politzer` | `ok` | 8 | 10679 | 1190 |  |
| `stop-market` | `ok` | 11 | 17472 | 2716 |  |
| `fresh-market` | `ok` | 46 | 8267 | 699 |  |
| `salach-dabach` | `ok` | 12 | 12488 | 1792 |  |
| `super-yuda` | `ok` | 26 | 6394 | 0 |  |
| `yellow` | `ok` | 242 | 1887 | 712 |  |
| `good-pharm` | `ok` | 82 | 3398 | 343 |  |
| `super-bareket` | `ok` | 15 | 3838 | 652 |  |
| `king-store` | `ok` | 48 | 2352 | 309 |  |
| `maayan-2000` | `ok` | 38 | 2774 | 359 |  |
| `meshnat-yosef` | `ok` | 4 | 5428 | 206 |  |
| `shefa-birkat-hashem` | `ok` | 22 | 3772 | 533 |  |
| `shuk-hayir` | `ok` | 26 | 2066 | 0 |  |
| `super-sapir` | `ok` | 73 | 1175 | 79 |  |
| `zol-vebegadol` | `ok` | 35 | 4283 | 488 |  |
| `city-market` | `ok` | 28 | 4301 | 0 |  |
| `victory` | `geo-blocked` | 70 | 9914 | 4294 | reachable from Israeli IPs only (verified via proxy) |
| `mahsanei-hashuk` | `geo-blocked` | 71 | 12397 | 6060 | reachable from Israeli IPs only (verified via proxy) |
| `het-cohen` | `geo-blocked` | 5 | 8939 | 2453 | reachable from Israeli IPs only (verified via proxy) |
| `nativ-hahesed` | `down` | — | — | — | portal still unreachable (PortalError) |
