# Chain health

**Coverage: 31/32 chains implemented** — the full government roster bar Nativ HaHesed, whose portal has returned HTTP 500 since July 2026 (it stays registered and will be enabled when it returns).

**Last nightly check (2026-10-30T13:53:09+00:00): 27/32 reachable.** The check runs from a GitHub-hosted runner outside Israel and fetches every file type of every chain. Daily reachability fluctuates: chains sometimes publish empty or late files, and some small chains publish sporadically — that's the chains' portals, not the library. `geo-blocked` = the portal only answers Israeli IPs (verified through an Israeli proxy). `degraded` = some file types were missing/empty at check time.

| Chain | Status | Stores | Prices | Promos | Note |
|---|---|---|---|---|---|
| `shufersal` | `ok` | 418 | 6561 | 1 |  |
| `super-pharm` | `down` | — | — | — | stores: FileNotFound: super-pharm: no Stores file | prices: FileNotFound: super-pharm: no PriceFull file | promos: FileNotFound: super-pharm: no PromoFull file |
| `wolt` | `ok` | 37 | 0 | 568 |  |
| `carrefour` | `geo-blocked` | 147 | 11069 | 1686 | reachable from Israeli IPs only (verified via proxy) |
| `hatzi-hinam` | `down` | — | — | — | stores: PortalError: GET https://shop.hazi-hinam.co.il/Prices -> HTTP 403 | prices: PortalError: GET https://shop.hazi-hinam.co.il/Prices -> HTTP 403 | promos: PortalError: GET https://shop.hazi-hinam.co.il/Prices -> HTTP 403 |
| `rami-levy` | `ok` | 99 | 5218 | 1081 |  |
| `tiv-taam` | `ok` | 54 | 74 | 24 |  |
| `yochananof` | `ok` | 51 | 11774 | 1368 |  |
| `osher-ad` | `ok` | 24 | 6129 | 738 |  |
| `dor-alon` | `ok` | 157 | 1487 | 325 |  |
| `keshet-teamim` | `ok` | 28 | 14306 | 2584 |  |
| `super-cofix` | `degraded` | 34 | — | — | prices: FileNotFound: super-cofix: no PriceFull file | promos: FileNotFound: super-cofix: no PromoFull file |
| `politzer` | `ok` | 8 | 12224 | 1206 |  |
| `stop-market` | `ok` | 11 | 17471 | 3591 |  |
| `fresh-market` | `ok` | 48 | 8284 | 705 |  |
| `salach-dabach` | `ok` | 12 | 12371 | 1793 |  |
| `super-yuda` | `ok` | 26 | 6403 | 380 |  |
| `yellow` | `ok` | 242 | 1016 | 662 |  |
| `good-pharm` | `ok` | 83 | 3384 | 372 |  |
| `super-bareket` | `ok` | 15 | 4598 | 699 |  |
| `king-store` | `ok` | 48 | 2366 | 311 |  |
| `maayan-2000` | `ok` | 38 | 2790 | 371 |  |
| `meshnat-yosef` | `ok` | 4 | 5425 | 218 |  |
| `shefa-birkat-hashem` | `ok` | 22 | 3791 | 562 |  |
| `shuk-hayir` | `ok` | 26 | 1752 | 0 |  |
| `super-sapir` | `ok` | 130 | 2257 | 0 |  |
| `zol-vebegadol` | `ok` | 35 | 4264 | 487 |  |
| `city-market` | `ok` | 71 | 4278 | 0 |  |
| `victory` | `geo-blocked` | 70 | 8691 | 4396 | reachable from Israeli IPs only (verified via proxy) |
| `mahsanei-hashuk` | `geo-blocked` | 71 | 12382 | 6150 | reachable from Israeli IPs only (verified via proxy) |
| `het-cohen` | `degraded` | — | 7215 | 2179 | stores: FileNotFound: het-cohen: no Stores file |
| `nativ-hahesed` | `down` | — | — | — | portal still unreachable (PortalError) |
