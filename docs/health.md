# Chain health

**Coverage: 31/32 chains implemented** — the full government roster bar Nativ HaHesed, whose portal has returned HTTP 500 since July 2026 (it stays registered and will be enabled when it returns).

**Last nightly check (2026-11-21T15:08:51+00:00): 28/32 reachable.** The check runs from a GitHub-hosted runner outside Israel and fetches every file type of every chain. Daily reachability fluctuates: chains sometimes publish empty or late files, and some small chains publish sporadically — that's the chains' portals, not the library. `geo-blocked` = the portal only answers Israeli IPs (verified through an Israeli proxy). `degraded` = some file types were missing/empty at check time.

| Chain | Status | Stores | Prices | Promos | Note |
|---|---|---|---|---|---|
| `shufersal` | `ok` | 418 | 6535 | 13 |  |
| `super-pharm` | `down` | — | — | — | stores: FileNotFound: super-pharm: no Stores file | prices: FileNotFound: super-pharm: no PriceFull file | promos: FileNotFound: super-pharm: no PromoFull file |
| `wolt` | `ok` | 37 | 5816 | 0 |  |
| `carrefour` | `geo-blocked` | 147 | 11134 | 1645 | reachable from Israeli IPs only (verified via proxy) |
| `hatzi-hinam` | `down` | — | — | — | stores: PortalError: GET https://shop.hazi-hinam.co.il/Prices -> HTTP 403 | prices: PortalError: GET https://shop.hazi-hinam.co.il/Prices -> HTTP 403 | promos: PortalError: GET https://shop.hazi-hinam.co.il/Prices -> HTTP 403 |
| `rami-levy` | `ok` | 99 | 5321 | 1081 |  |
| `tiv-taam` | `ok` | 54 | 52 | 17 |  |
| `yochananof` | `ok` | 51 | 11830 | 1348 |  |
| `osher-ad` | `ok` | 24 | 5968 | 848 |  |
| `dor-alon` | `ok` | 157 | 1786 | 338 |  |
| `keshet-teamim` | `ok` | 28 | 6471 | 1500 |  |
| `super-cofix` | `degraded` | 34 | — | — | prices: FileNotFound: super-cofix: no PriceFull file | promos: FileNotFound: super-cofix: no PromoFull file |
| `politzer` | `ok` | 8 | 13967 | 1212 |  |
| `stop-market` | `ok` | 11 | 17590 | 2839 |  |
| `fresh-market` | `ok` | 73 | 9283 | 1517 |  |
| `salach-dabach` | `ok` | 12 | 12329 | 2066 |  |
| `super-yuda` | `ok` | 26 | 4863 | 413 |  |
| `yellow` | `ok` | 242 | 2299 | 684 |  |
| `good-pharm` | `ok` | 84 | 3331 | 334 |  |
| `super-bareket` | `ok` | 15 | 4893 | 715 |  |
| `king-store` | `ok` | 48 | 2368 | 266 |  |
| `maayan-2000` | `ok` | 38 | 3131 | 442 |  |
| `meshnat-yosef` | `ok` | 4 | 5638 | 220 |  |
| `shefa-birkat-hashem` | `ok` | 22 | 3987 | 610 |  |
| `shuk-hayir` | `ok` | 26 | 1653 | 0 |  |
| `super-sapir` | `ok` | 130 | 1375 | 78 |  |
| `zol-vebegadol` | `ok` | 35 | 4298 | 504 |  |
| `city-market` | `ok` | 69 | 4134 | 0 |  |
| `victory` | `geo-blocked` | 70 | 8694 | 4277 | reachable from Israeli IPs only (verified via proxy) |
| `mahsanei-hashuk` | `geo-blocked` | 72 | 12469 | 6216 | reachable from Israeli IPs only (verified via proxy) |
| `het-cohen` | `geo-blocked` | 5 | 10826 | 2906 | reachable from Israeli IPs only (verified via proxy) |
| `nativ-hahesed` | `down` | — | — | — | portal still unreachable (PortalError) |
