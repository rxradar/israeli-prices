# Chain health

**Coverage: 31/32 chains implemented** — the full government roster bar Nativ HaHesed, whose portal has returned HTTP 500 since July 2026 (it stays registered and will be enabled when it returns).

**Last nightly check (2026-11-24T18:42:06+00:00): 28/32 reachable.** The check runs from a GitHub-hosted runner outside Israel and fetches every file type of every chain. Daily reachability fluctuates: chains sometimes publish empty or late files, and some small chains publish sporadically — that's the chains' portals, not the library. `geo-blocked` = the portal only answers Israeli IPs (verified through an Israeli proxy). `degraded` = some file types were missing/empty at check time.

| Chain | Status | Stores | Prices | Promos | Note |
|---|---|---|---|---|---|
| `shufersal` | `ok` | 418 | 6525 | 22 |  |
| `super-pharm` | `down` | — | — | — | stores: FileNotFound: super-pharm: no Stores file | prices: FileNotFound: super-pharm: no PriceFull file | promos: FileNotFound: super-pharm: no PromoFull file |
| `wolt` | `ok` | 37 | 0 | 0 |  |
| `carrefour` | `geo-blocked` | 147 | 11124 | 1711 | reachable from Israeli IPs only (verified via proxy) |
| `hatzi-hinam` | `down` | — | — | — | stores: PortalError: GET https://shop.hazi-hinam.co.il/Prices -> HTTP 403 | prices: PortalError: GET https://shop.hazi-hinam.co.il/Prices -> HTTP 403 | promos: PortalError: GET https://shop.hazi-hinam.co.il/Prices -> HTTP 403 |
| `rami-levy` | `ok` | 99 | 5322 | 1107 |  |
| `tiv-taam` | `ok` | 54 | 52 | 17 |  |
| `yochananof` | `ok` | 51 | 11858 | 1476 |  |
| `osher-ad` | `ok` | 24 | 5931 | 868 |  |
| `dor-alon` | `ok` | 157 | 1473 | 337 |  |
| `keshet-teamim` | `ok` | 28 | 6349 | 1498 |  |
| `super-cofix` | `degraded` | 34 | — | — | prices: FileNotFound: super-cofix: no PriceFull file | promos: FileNotFound: super-cofix: no PromoFull file |
| `politzer` | `ok` | 8 | 13821 | 1214 |  |
| `stop-market` | `ok` | 11 | 14448 | 2853 |  |
| `fresh-market` | `ok` | 73 | 9243 | 1540 |  |
| `salach-dabach` | `ok` | 12 | 12316 | 2062 |  |
| `super-yuda` | `ok` | 26 | 6467 | 427 |  |
| `yellow` | `ok` | 242 | 1293 | 699 |  |
| `good-pharm` | `ok` | 85 | 3311 | 331 |  |
| `super-bareket` | `ok` | 15 | 4872 | 735 |  |
| `king-store` | `ok` | 48 | 2330 | 264 |  |
| `maayan-2000` | `ok` | 38 | 2878 | 428 |  |
| `meshnat-yosef` | `ok` | 4 | 5611 | 267 |  |
| `shefa-birkat-hashem` | `ok` | 22 | 3832 | 610 |  |
| `shuk-hayir` | `ok` | 26 | 1635 | 0 |  |
| `super-sapir` | `ok` | 130 | 20 | 1 |  |
| `zol-vebegadol` | `ok` | 35 | 4305 | 529 |  |
| `city-market` | `ok` | 69 | 4180 | 0 |  |
| `victory` | `geo-blocked` | 70 | 9872 | 4384 | reachable from Israeli IPs only (verified via proxy) |
| `mahsanei-hashuk` | `geo-blocked` | 72 | 12484 | 6280 | reachable from Israeli IPs only (verified via proxy) |
| `het-cohen` | `geo-blocked` | 5 | 10820 | 2963 | reachable from Israeli IPs only (verified via proxy) |
| `nativ-hahesed` | `down` | — | — | — | portal still unreachable (PortalError) |
