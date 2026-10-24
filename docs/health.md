# Chain health

**Coverage: 31/32 chains implemented** — the full government roster bar Nativ HaHesed, whose portal has returned HTTP 500 since July 2026 (it stays registered and will be enabled when it returns).

**Last nightly check (2026-10-24T11:52:57+00:00): 28/32 reachable.** The check runs from a GitHub-hosted runner outside Israel and fetches every file type of every chain. Daily reachability fluctuates: chains sometimes publish empty or late files, and some small chains publish sporadically — that's the chains' portals, not the library. `geo-blocked` = the portal only answers Israeli IPs (verified through an Israeli proxy). `degraded` = some file types were missing/empty at check time.

| Chain | Status | Stores | Prices | Promos | Note |
|---|---|---|---|---|---|
| `shufersal` | `ok` | 416 | 6568 | 1 |  |
| `super-pharm` | `down` | — | — | — | stores: FileNotFound: super-pharm: no Stores file | prices: FileNotFound: super-pharm: no PriceFull file | promos: FileNotFound: super-pharm: no PromoFull file |
| `wolt` | `ok` | 34 | 5930 | 580 |  |
| `carrefour` | `geo-blocked` | 147 | 11087 | 1645 | reachable from Israeli IPs only (verified via proxy) |
| `hatzi-hinam` | `down` | — | — | — | stores: PortalError: GET https://shop.hazi-hinam.co.il/Prices -> HTTP 403 | prices: PortalError: GET https://shop.hazi-hinam.co.il/Prices -> HTTP 403 | promos: PortalError: GET https://shop.hazi-hinam.co.il/Prices -> HTTP 403 |
| `rami-levy` | `ok` | 99 | 5214 | 1078 |  |
| `tiv-taam` | `ok` | 54 | 125 | 41 |  |
| `yochananof` | `ok` | 51 | 11752 | 1336 |  |
| `osher-ad` | `ok` | 24 | 6260 | 714 |  |
| `dor-alon` | `ok` | 157 | 1670 | 325 |  |
| `keshet-teamim` | `ok` | 28 | 6347 | 1696 |  |
| `super-cofix` | `degraded` | 34 | — | — | prices: FileNotFound: super-cofix: no PriceFull file | promos: FileNotFound: super-cofix: no PromoFull file |
| `politzer` | `ok` | 8 | 14490 | 1201 |  |
| `stop-market` | `ok` | 11 | 14306 | 2738 |  |
| `fresh-market` | `ok` | 46 | 8257 | 698 |  |
| `salach-dabach` | `ok` | 12 | 12409 | 1801 |  |
| `super-yuda` | `ok` | 26 | 4881 | 381 |  |
| `yellow` | `ok` | 242 | 1024 | 709 |  |
| `good-pharm` | `ok` | 83 | 3432 | 353 |  |
| `super-bareket` | `ok` | 15 | 4475 | 689 |  |
| `king-store` | `ok` | 48 | 2363 | 295 |  |
| `maayan-2000` | `ok` | 38 | 2938 | 383 |  |
| `meshnat-yosef` | `ok` | 4 | 5414 | 215 |  |
| `shefa-birkat-hashem` | `ok` | 22 | 3882 | 572 |  |
| `shuk-hayir` | `ok` | 26 | 1856 | 0 |  |
| `super-sapir` | `ok` | 130 | 2189 | 0 |  |
| `zol-vebegadol` | `ok` | 35 | 4282 | 489 |  |
| `city-market` | `ok` | 71 | 4297 | 0 |  |
| `victory` | `geo-blocked` | 70 | 8710 | 4364 | reachable from Israeli IPs only (verified via proxy) |
| `mahsanei-hashuk` | `geo-blocked` | 71 | 12338 | 6005 | reachable from Israeli IPs only (verified via proxy) |
| `het-cohen` | `geo-blocked` | 5 | 7198 | 2777 | reachable from Israeli IPs only (verified via proxy) |
| `nativ-hahesed` | `down` | — | — | — | portal still unreachable (PortalError) |
