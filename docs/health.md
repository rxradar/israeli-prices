# Chain health

**Coverage: 31/32 chains implemented** — the full government roster bar Nativ HaHesed, whose portal has returned HTTP 500 since July 2026 (it stays registered and will be enabled when it returns).

**Last nightly check (2026-10-18T11:58:15+00:00): 28/32 reachable.** The check runs from a GitHub-hosted runner outside Israel and fetches every file type of every chain. Daily reachability fluctuates: chains sometimes publish empty or late files, and some small chains publish sporadically — that's the chains' portals, not the library. `geo-blocked` = the portal only answers Israeli IPs (verified through an Israeli proxy). `degraded` = some file types were missing/empty at check time.

| Chain | Status | Stores | Prices | Promos | Note |
|---|---|---|---|---|---|
| `shufersal` | `ok` | 417 | 6573 | 1 |  |
| `super-pharm` | `down` | — | — | — | stores: FileNotFound: super-pharm: no Stores file | prices: FileNotFound: super-pharm: no PriceFull file | promos: FileNotFound: super-pharm: no PromoFull file |
| `wolt` | `ok` | 34 | 0 | 0 |  |
| `carrefour` | `ok` | 147 | 11117 | 1609 |  |
| `hatzi-hinam` | `down` | — | — | — | stores: PortalError: GET https://shop.hazi-hinam.co.il/Prices -> HTTP 403 | prices: PortalError: GET https://shop.hazi-hinam.co.il/Prices -> HTTP 403 | promos: PortalError: GET https://shop.hazi-hinam.co.il/Prices -> HTTP 403 |
| `rami-levy` | `ok` | 99 | 5212 | 1071 |  |
| `tiv-taam` | `ok` | 54 | 125 | 40 |  |
| `yochananof` | `ok` | 51 | 11759 | 1299 |  |
| `osher-ad` | `ok` | 24 | 6339 | 686 |  |
| `dor-alon` | `ok` | 158 | 4798 | 633 |  |
| `keshet-teamim` | `ok` | 28 | 6423 | 1695 |  |
| `super-cofix` | `degraded` | 34 | — | — | prices: FileNotFound: super-cofix: no PriceFull file | promos: FileNotFound: super-cofix: no PromoFull file |
| `politzer` | `ok` | 8 | 12168 | 1189 |  |
| `stop-market` | `ok` | 11 | 10679 | 2718 |  |
| `fresh-market` | `ok` | 46 | 8249 | 692 |  |
| `salach-dabach` | `ok` | 12 | 12467 | 1781 |  |
| `super-yuda` | `ok` | 26 | 6408 | 0 |  |
| `yellow` | `ok` | 242 | 1247 | 655 |  |
| `good-pharm` | `ok` | 82 | 3395 | 349 |  |
| `super-bareket` | `ok` | 15 | 3955 | 652 |  |
| `king-store` | `ok` | 48 | 2346 | 304 |  |
| `maayan-2000` | `ok` | 38 | 2705 | 345 |  |
| `meshnat-yosef` | `ok` | 4 | 5413 | 206 |  |
| `shefa-birkat-hashem` | `ok` | 22 | 3805 | 545 |  |
| `shuk-hayir` | `ok` | 26 | 1864 | 0 |  |
| `super-sapir` | `ok` | 73 | 1175 | 0 |  |
| `zol-vebegadol` | `ok` | 35 | 4285 | 488 |  |
| `city-market` | `ok` | 28 | 4350 | 0 |  |
| `victory` | `geo-blocked` | 70 | 8720 | 4611 | reachable from Israeli IPs only (verified via proxy) |
| `mahsanei-hashuk` | `geo-blocked` | 71 | 8564 | 4092 | reachable from Israeli IPs only (verified via proxy) |
| `het-cohen` | `geo-blocked` | 5 | 8907 | 2693 | reachable from Israeli IPs only (verified via proxy) |
| `nativ-hahesed` | `down` | — | — | — | portal still unreachable (PortalError) |
