# Chain health

**Coverage: 31/32 chains implemented** — the full government roster bar Nativ HaHesed, whose portal has returned HTTP 500 since July 2026 (it stays registered and will be enabled when it returns).

**Last nightly check (2026-11-23T19:01:41+00:00): 28/32 reachable.** The check runs from a GitHub-hosted runner outside Israel and fetches every file type of every chain. Daily reachability fluctuates: chains sometimes publish empty or late files, and some small chains publish sporadically — that's the chains' portals, not the library. `geo-blocked` = the portal only answers Israeli IPs (verified through an Israeli proxy). `degraded` = some file types were missing/empty at check time.

| Chain | Status | Stores | Prices | Promos | Note |
|---|---|---|---|---|---|
| `shufersal` | `ok` | 418 | 6526 | 21 |  |
| `super-pharm` | `down` | — | — | — | stores: FileNotFound: super-pharm: no Stores file | prices: FileNotFound: super-pharm: no PriceFull file | promos: FileNotFound: super-pharm: no PromoFull file |
| `wolt` | `ok` | 37 | 0 | 0 |  |
| `carrefour` | `geo-blocked` | 147 | 11140 | 1690 | reachable from Israeli IPs only (verified via proxy) |
| `hatzi-hinam` | `down` | — | — | — | stores: PortalError: GET https://shop.hazi-hinam.co.il/Prices -> HTTP 403 | prices: PortalError: GET https://shop.hazi-hinam.co.il/Prices -> HTTP 403 | promos: PortalError: GET https://shop.hazi-hinam.co.il/Prices -> HTTP 403 |
| `rami-levy` | `ok` | 99 | 4751 | 1085 |  |
| `tiv-taam` | `ok` | 54 | 52 | 17 |  |
| `yochananof` | `ok` | 51 | 11831 | 1432 |  |
| `osher-ad` | `ok` | 24 | 5959 | 867 |  |
| `dor-alon` | `ok` | 157 | 5269 | 911 |  |
| `keshet-teamim` | `ok` | 28 | 14615 | 2415 |  |
| `super-cofix` | `degraded` | 34 | — | — | prices: FileNotFound: super-cofix: no PriceFull file | promos: FileNotFound: super-cofix: no PromoFull file |
| `politzer` | `ok` | 8 | 13755 | 1212 |  |
| `stop-market` | `ok` | 11 | 17594 | 2860 |  |
| `fresh-market` | `ok` | 73 | 9260 | 1535 |  |
| `salach-dabach` | `ok` | 12 | 12313 | 2062 |  |
| `super-yuda` | `ok` | 26 | 6473 | 422 |  |
| `yellow` | `ok` | 242 | 1322 | 696 |  |
| `good-pharm` | `ok` | 84 | 3301 | 331 |  |
| `super-bareket` | `ok` | 15 | 4839 | 730 |  |
| `king-store` | `ok` | 48 | 2346 | 262 |  |
| `maayan-2000` | `ok` | 38 | 2903 | 423 |  |
| `meshnat-yosef` | `ok` | 4 | 5601 | 263 |  |
| `shefa-birkat-hashem` | `ok` | 22 | 3858 | 579 |  |
| `shuk-hayir` | `ok` | 26 | 1674 | 0 |  |
| `super-sapir` | `ok` | 130 | 20 | 1 |  |
| `zol-vebegadol` | `ok` | 35 | 4301 | 511 |  |
| `city-market` | `ok` | 69 | 4127 | 0 |  |
| `victory` | `geo-blocked` | 70 | 8712 | 4443 | reachable from Israeli IPs only (verified via proxy) |
| `mahsanei-hashuk` | `geo-blocked` | 72 | 8506 | 4011 | reachable from Israeli IPs only (verified via proxy) |
| `het-cohen` | `geo-blocked` | 5 | 8934 | 2959 | reachable from Israeli IPs only (verified via proxy) |
| `nativ-hahesed` | `down` | — | — | — | portal still unreachable (PortalError) |
