# Chain health

**Coverage: 31/32 chains implemented** — the full government roster bar Nativ HaHesed, whose portal has returned HTTP 500 since July 2026 (it stays registered and will be enabled when it returns).

**Last nightly check (2026-11-22T15:05:51+00:00): 28/32 reachable.** The check runs from a GitHub-hosted runner outside Israel and fetches every file type of every chain. Daily reachability fluctuates: chains sometimes publish empty or late files, and some small chains publish sporadically — that's the chains' portals, not the library. `geo-blocked` = the portal only answers Israeli IPs (verified through an Israeli proxy). `degraded` = some file types were missing/empty at check time.

| Chain | Status | Stores | Prices | Promos | Note |
|---|---|---|---|---|---|
| `shufersal` | `ok` | 418 | 6526 | 13 |  |
| `super-pharm` | `down` | — | — | — | stores: FileNotFound: super-pharm: no Stores file | prices: FileNotFound: super-pharm: no PriceFull file | promos: FileNotFound: super-pharm: no PromoFull file |
| `wolt` | `ok` | 37 | 5497 | 0 |  |
| `carrefour` | `geo-blocked` | 147 | 11125 | 1671 | reachable from Israeli IPs only (verified via proxy) |
| `hatzi-hinam` | `down` | — | — | — | stores: PortalError: GET https://shop.hazi-hinam.co.il/Prices -> HTTP 403 | prices: PortalError: GET https://shop.hazi-hinam.co.il/Prices -> HTTP 403 | promos: PortalError: GET https://shop.hazi-hinam.co.il/Prices -> HTTP 403 |
| `rami-levy` | `ok` | 99 | 5324 | 1083 |  |
| `tiv-taam` | `ok` | 54 | 52 | 17 |  |
| `yochananof` | `ok` | 51 | 11811 | 2826 |  |
| `osher-ad` | `ok` | 24 | 5974 | 871 |  |
| `dor-alon` | `ok` | 157 | 1304 | 335 |  |
| `keshet-teamim` | `ok` | 28 | 6416 | 1494 |  |
| `super-cofix` | `degraded` | 34 | — | — | prices: FileNotFound: super-cofix: no PriceFull file | promos: FileNotFound: super-cofix: no PromoFull file |
| `politzer` | `ok` | 8 | 13945 | 1212 |  |
| `stop-market` | `ok` | 11 | 17599 | 2831 |  |
| `fresh-market` | `ok` | 73 | 8290 | 0 |  |
| `salach-dabach` | `ok` | 12 | 12325 | 2053 |  |
| `super-yuda` | `ok` | 26 | 6479 | 422 |  |
| `yellow` | `ok` | 242 | 1140 | 696 |  |
| `good-pharm` | `ok` | 84 | 3296 | 331 |  |
| `super-bareket` | `ok` | 15 | 4837 | 717 |  |
| `king-store` | `ok` | 48 | 2348 | 265 |  |
| `maayan-2000` | `ok` | 38 | 2905 | 425 |  |
| `meshnat-yosef` | `ok` | 4 | 5621 | 261 |  |
| `shefa-birkat-hashem` | `ok` | 22 | 3890 | 602 |  |
| `shuk-hayir` | `ok` | 26 | 1430 | 0 |  |
| `super-sapir` | `ok` | 130 | 20 | 1 |  |
| `zol-vebegadol` | `ok` | 35 | 4298 | 506 |  |
| `city-market` | `ok` | 69 | 4137 | 0 |  |
| `victory` | `geo-blocked` | 70 | 9661 | 4306 | reachable from Israeli IPs only (verified via proxy) |
| `mahsanei-hashuk` | `geo-blocked` | 72 | 12462 | 6213 | reachable from Israeli IPs only (verified via proxy) |
| `het-cohen` | `geo-blocked` | 5 | 10812 | 2925 | reachable from Israeli IPs only (verified via proxy) |
| `nativ-hahesed` | `down` | — | — | — | portal still unreachable (PortalError) |
