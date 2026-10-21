# Chain health

**Coverage: 31/32 chains implemented** — the full government roster bar Nativ HaHesed, whose portal has returned HTTP 500 since July 2026 (it stays registered and will be enabled when it returns).

**Last nightly check (2026-10-21T12:46:09+00:00): 27/32 reachable.** The check runs from a GitHub-hosted runner outside Israel and fetches every file type of every chain. Daily reachability fluctuates: chains sometimes publish empty or late files, and some small chains publish sporadically — that's the chains' portals, not the library. `geo-blocked` = the portal only answers Israeli IPs (verified through an Israeli proxy). `degraded` = some file types were missing/empty at check time.

| Chain | Status | Stores | Prices | Promos | Note |
|---|---|---|---|---|---|
| `shufersal` | `degraded` | — | 6564 | 1 | stores: PortalError: GET https://prices.shufersal.co.il/FileObject/UpdateCategory failed after 3 attempts: The read operation timed out |
| `super-pharm` | `down` | — | — | — | stores: FileNotFound: super-pharm: no Stores file | prices: FileNotFound: super-pharm: no PriceFull file | promos: FileNotFound: super-pharm: no PromoFull file |
| `wolt` | `ok` | 34 | 5187 | 322 |  |
| `carrefour` | `ok` | 147 | 11097 | 1657 |  |
| `hatzi-hinam` | `down` | — | — | — | stores: PortalError: GET https://shop.hazi-hinam.co.il/Prices -> HTTP 403 | prices: PortalError: GET https://shop.hazi-hinam.co.il/Prices -> HTTP 403 | promos: PortalError: GET https://shop.hazi-hinam.co.il/Prices -> HTTP 403 |
| `rami-levy` | `ok` | 99 | 5206 | 1074 |  |
| `tiv-taam` | `ok` | 54 | 125 | 40 |  |
| `yochananof` | `ok` | 51 | 11760 | 1328 |  |
| `osher-ad` | `ok` | 24 | 6294 | 694 |  |
| `dor-alon` | `ok` | 157 | 5286 | 631 |  |
| `keshet-teamim` | `ok` | 28 | 6347 | 1694 |  |
| `super-cofix` | `degraded` | 34 | — | — | prices: FileNotFound: super-cofix: no PriceFull file | promos: FileNotFound: super-cofix: no PromoFull file |
| `politzer` | `ok` | 8 | 13595 | 1197 |  |
| `stop-market` | `ok` | 11 | 17484 | 2713 |  |
| `fresh-market` | `ok` | 46 | 9174 | 1356 |  |
| `salach-dabach` | `ok` | 12 | 12444 | 1794 |  |
| `super-yuda` | `ok` | 26 | 6398 | 0 |  |
| `yellow` | `ok` | 242 | 1654 | 709 |  |
| `good-pharm` | `ok` | 83 | 3403 | 351 |  |
| `super-bareket` | `ok` | 15 | 4237 | 668 |  |
| `king-store` | `ok` | 48 | 2336 | 301 |  |
| `maayan-2000` | `ok` | 38 | 2734 | 355 |  |
| `meshnat-yosef` | `ok` | 4 | 5377 | 209 |  |
| `shefa-birkat-hashem` | `ok` | 22 | 3621 | 548 |  |
| `shuk-hayir` | `ok` | 26 | 1717 | 0 |  |
| `super-sapir` | `ok` | 130 | 2157 | 0 |  |
| `zol-vebegadol` | `ok` | 35 | 4284 | 489 |  |
| `city-market` | `ok` | 71 | 4327 | 0 |  |
| `victory` | `geo-blocked` | 70 | 8717 | 4372 | reachable from Israeli IPs only (verified via proxy) |
| `mahsanei-hashuk` | `geo-blocked` | 71 | 12394 | 6046 | reachable from Israeli IPs only (verified via proxy) |
| `het-cohen` | `geo-blocked` | 5 | 7195 | 2765 | reachable from Israeli IPs only (verified via proxy) |
| `nativ-hahesed` | `down` | — | — | — | portal still unreachable (PortalError) |
