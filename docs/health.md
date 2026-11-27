# Chain health

**Coverage: 31/32 chains implemented** — the full government roster bar Nativ HaHesed, whose portal has returned HTTP 500 since July 2026 (it stays registered and will be enabled when it returns).

**Last nightly check (2026-11-27T17:16:36+00:00): 28/32 reachable.** The check runs from a GitHub-hosted runner outside Israel and fetches every file type of every chain. Daily reachability fluctuates: chains sometimes publish empty or late files, and some small chains publish sporadically — that's the chains' portals, not the library. `geo-blocked` = the portal only answers Israeli IPs (verified through an Israeli proxy). `degraded` = some file types were missing/empty at check time.

| Chain | Status | Stores | Prices | Promos | Note |
|---|---|---|---|---|---|
| `shufersal` | `ok` | 418 | 6507 | 22 |  |
| `super-pharm` | `down` | — | — | — | stores: FileNotFound: super-pharm: no Stores file | prices: FileNotFound: super-pharm: no PriceFull file | promos: FileNotFound: super-pharm: no PromoFull file |
| `wolt` | `ok` | 37 | 0 | 0 |  |
| `carrefour` | `geo-blocked` | 147 | 11114 | 1709 | reachable from Israeli IPs only (verified via proxy) |
| `hatzi-hinam` | `down` | — | — | — | stores: PortalError: GET https://shop.hazi-hinam.co.il/Prices -> HTTP 403 | prices: PortalError: GET https://shop.hazi-hinam.co.il/Prices -> HTTP 403 | promos: PortalError: GET https://shop.hazi-hinam.co.il/Prices -> HTTP 403 |
| `rami-levy` | `ok` | 99 | 5311 | 1080 |  |
| `tiv-taam` | `ok` | 54 | 69 | 27 |  |
| `yochananof` | `ok` | 51 | 11875 | 2924 |  |
| `osher-ad` | `ok` | 24 | 5908 | 893 |  |
| `dor-alon` | `ok` | 157 | 1292 | 336 |  |
| `keshet-teamim` | `ok` | 28 | 15937 | 2600 |  |
| `super-cofix` | `degraded` | 34 | — | — | prices: FileNotFound: super-cofix: no PriceFull file | promos: FileNotFound: super-cofix: no PromoFull file |
| `politzer` | `ok` | 8 | 15000 | 1234 |  |
| `stop-market` | `ok` | 11 | 17560 | 3886 |  |
| `fresh-market` | `ok` | 73 | 8293 | 812 |  |
| `salach-dabach` | `ok` | 12 | 12279 | 2091 |  |
| `super-yuda` | `ok` | 26 | 6477 | 429 |  |
| `yellow` | `ok` | 242 | 1584 | 700 |  |
| `good-pharm` | `ok` | 85 | 3333 | 353 |  |
| `super-bareket` | `ok` | 15 | 4921 | 739 |  |
| `king-store` | `ok` | 48 | 2309 | 266 |  |
| `maayan-2000` | `ok` | 38 | 2928 | 435 |  |
| `meshnat-yosef` | `ok` | 4 | 5606 | 273 |  |
| `shefa-birkat-hashem` | `ok` | 22 | 3889 | 616 |  |
| `shuk-hayir` | `ok` | 26 | 1954 | 0 |  |
| `super-sapir` | `ok` | 130 | 28 | 1 |  |
| `zol-vebegadol` | `ok` | 35 | 4309 | 513 |  |
| `city-market` | `ok` | 73 | 4122 | 0 |  |
| `victory` | `geo-blocked` | 70 | 9857 | 3847 | reachable from Israeli IPs only (verified via proxy) |
| `mahsanei-hashuk` | `geo-blocked` | 72 | 12496 | 6367 | reachable from Israeli IPs only (verified via proxy) |
| `het-cohen` | `geo-blocked` | 5 | 10845 | 2987 | reachable from Israeli IPs only (verified via proxy) |
| `nativ-hahesed` | `down` | — | — | — | portal still unreachable (PortalError) |
