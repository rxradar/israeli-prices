# Chain health

**Coverage: 31/32 chains implemented** — the full government roster bar Nativ HaHesed, whose portal has returned HTTP 500 since July 2026 (it stays registered and will be enabled when it returns).

**Last nightly check (2026-10-15T12:30:28+00:00): 27/32 reachable.** The check runs from a GitHub-hosted runner outside Israel and fetches every file type of every chain. Daily reachability fluctuates: chains sometimes publish empty or late files, and some small chains publish sporadically — that's the chains' portals, not the library. `geo-blocked` = the portal only answers Israeli IPs (verified through an Israeli proxy). `degraded` = some file types were missing/empty at check time.

| Chain | Status | Stores | Prices | Promos | Note |
|---|---|---|---|---|---|
| `shufersal` | `down` | — | — | — | stores: PortalError: GET https://prices.shufersal.co.il/FileObject/UpdateCategory failed after 3 attempts: The read operation timed out | prices: PortalError: GET https://prices.shufersal.co.il/FileObject/UpdateCategory failed after 3 attempts: The read operation timed out | promos: PortalError: GET |
| `super-pharm` | `down` | — | — | — | stores: FileNotFound: super-pharm: no Stores file | prices: FileNotFound: super-pharm: no PriceFull file | promos: FileNotFound: super-pharm: no PromoFull file |
| `wolt` | `ok` | 34 | 6000 | 456 |  |
| `carrefour` | `ok` | 147 | 11133 | 1554 |  |
| `hatzi-hinam` | `down` | — | — | — | stores: PortalError: GET https://shop.hazi-hinam.co.il/Prices -> HTTP 403 | prices: PortalError: GET https://shop.hazi-hinam.co.il/Prices -> HTTP 403 | promos: PortalError: GET https://shop.hazi-hinam.co.il/Prices -> HTTP 403 |
| `rami-levy` | `ok` | 99 | 5203 | 1075 |  |
| `tiv-taam` | `ok` | 54 | 125 | 40 |  |
| `yochananof` | `ok` | 51 | 11780 | 1306 |  |
| `osher-ad` | `ok` | 24 | 6378 | 711 |  |
| `dor-alon` | `ok` | 157 | 3246 | 348 |  |
| `keshet-teamim` | `ok` | 27 | 6380 | 1693 |  |
| `super-cofix` | `degraded` | 34 | — | — | prices: FileNotFound: super-cofix: no PriceFull file | promos: FileNotFound: super-cofix: no PromoFull file |
| `politzer` | `ok` | 8 | 13567 | 1187 |  |
| `stop-market` | `ok` | 12 | 14330 | 2716 |  |
| `fresh-market` | `ok` | 46 | 9173 | 1339 |  |
| `salach-dabach` | `ok` | 12 | 12498 | 1783 |  |
| `super-yuda` | `ok` | 26 | 6397 | 381 |  |
| `yellow` | `ok` | 242 | 1880 | 661 |  |
| `good-pharm` | `ok` | 82 | 3369 | 341 |  |
| `super-bareket` | `ok` | 15 | 3678 | 621 |  |
| `king-store` | `ok` | 48 | 2341 | 304 |  |
| `maayan-2000` | `ok` | 38 | 2760 | 354 |  |
| `meshnat-yosef` | `ok` | 4 | 5415 | 204 |  |
| `shefa-birkat-hashem` | `ok` | 22 | 3520 | 514 |  |
| `shuk-hayir` | `ok` | 26 | 1755 | 0 |  |
| `super-sapir` | `ok` | 73 | 1160 | 78 |  |
| `zol-vebegadol` | `ok` | 35 | 4270 | 488 |  |
| `city-market` | `ok` | 28 | 4319 | 0 |  |
| `victory` | `geo-blocked` | 70 | 8724 | 4476 | reachable from Israeli IPs only (verified via proxy) |
| `mahsanei-hashuk` | `geo-blocked` | 71 | 5719 | 6046 | reachable from Israeli IPs only (verified via proxy) |
| `het-cohen` | `geo-blocked` | 5 | 10697 | 2749 | reachable from Israeli IPs only (verified via proxy) |
| `nativ-hahesed` | `down` | — | — | — | portal still unreachable (PortalError) |
