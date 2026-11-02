# Chain health

**Coverage: 31/32 chains implemented** — the full government roster bar Nativ HaHesed, whose portal has returned HTTP 500 since July 2026 (it stays registered and will be enabled when it returns).

**Last nightly check (2026-11-02T16:52:42+00:00): 28/32 reachable.** The check runs from a GitHub-hosted runner outside Israel and fetches every file type of every chain. Daily reachability fluctuates: chains sometimes publish empty or late files, and some small chains publish sporadically — that's the chains' portals, not the library. `geo-blocked` = the portal only answers Israeli IPs (verified through an Israeli proxy). `degraded` = some file types were missing/empty at check time.

| Chain | Status | Stores | Prices | Promos | Note |
|---|---|---|---|---|---|
| `shufersal` | `ok` | 418 | 6547 | 1 |  |
| `super-pharm` | `down` | — | — | — | stores: FileNotFound: super-pharm: no Stores file | prices: FileNotFound: super-pharm: no PriceFull file | promos: FileNotFound: super-pharm: no PromoFull file |
| `wolt` | `ok` | 34 | 0 | 669 |  |
| `carrefour` | `geo-blocked` | 147 | 11070 | 1674 | reachable from Israeli IPs only (verified via proxy) |
| `hatzi-hinam` | `down` | — | — | — | stores: PortalError: GET https://shop.hazi-hinam.co.il/Prices -> HTTP 403 | prices: PortalError: GET https://shop.hazi-hinam.co.il/Prices -> HTTP 403 | promos: PortalError: GET https://shop.hazi-hinam.co.il/Prices -> HTTP 403 |
| `rami-levy` | `ok` | 99 | 5229 | 1097 |  |
| `tiv-taam` | `ok` | 54 | 57 | 19 |  |
| `yochananof` | `ok` | 51 | 11761 | 1114 |  |
| `osher-ad` | `ok` | 24 | 6109 | 650 |  |
| `dor-alon` | `ok` | 157 | 4488 | 638 |  |
| `keshet-teamim` | `ok` | 28 | 6356 | 1491 |  |
| `super-cofix` | `degraded` | 34 | — | — | prices: FileNotFound: super-cofix: no PriceFull file | promos: FileNotFound: super-cofix: no PromoFull file |
| `politzer` | `ok` | 8 | 13601 | 758 |  |
| `stop-market` | `ok` | 11 | 17520 | 1872 |  |
| `fresh-market` | `ok` | 48 | 9204 | 1453 |  |
| `salach-dabach` | `ok` | 12 | 12346 | 1941 |  |
| `super-yuda` | `ok` | 26 | 6431 | 0 |  |
| `yellow` | `ok` | 242 | 1628 | 667 |  |
| `good-pharm` | `ok` | 83 | 3351 | 274 |  |
| `super-bareket` | `ok` | 15 | 4636 | 681 |  |
| `king-store` | `ok` | 48 | 2356 | 254 |  |
| `maayan-2000` | `ok` | 38 | 2868 | 303 |  |
| `meshnat-yosef` | `ok` | 4 | 5453 | 197 |  |
| `shefa-birkat-hashem` | `ok` | 22 | 3741 | 475 |  |
| `shuk-hayir` | `ok` | 26 | 1624 | 0 |  |
| `super-sapir` | `ok` | 130 | 2302 | 0 |  |
| `zol-vebegadol` | `ok` | 35 | 4263 | 401 |  |
| `city-market` | `ok` | 70 | 4291 | 0 |  |
| `victory` | `geo-blocked` | 70 | 8667 | 3523 | reachable from Israeli IPs only (verified via proxy) |
| `mahsanei-hashuk` | `geo-blocked` | 71 | 12376 | 4952 | reachable from Israeli IPs only (verified via proxy) |
| `het-cohen` | `geo-blocked` | 5 | 7209 | 1671 | reachable from Israeli IPs only (verified via proxy) |
| `nativ-hahesed` | `down` | — | — | — | portal still unreachable (PortalError) |
