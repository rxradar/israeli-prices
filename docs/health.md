# Chain health

**Coverage: 31/32 chains implemented** — the full government roster bar Nativ HaHesed, whose portal has returned HTTP 500 since July 2026 (it stays registered and will be enabled when it returns).

**Last nightly check (2026-10-19T14:25:30+00:00): 28/32 reachable.** The check runs from a GitHub-hosted runner outside Israel and fetches every file type of every chain. Daily reachability fluctuates: chains sometimes publish empty or late files, and some small chains publish sporadically — that's the chains' portals, not the library. `geo-blocked` = the portal only answers Israeli IPs (verified through an Israeli proxy). `degraded` = some file types were missing/empty at check time.

| Chain | Status | Stores | Prices | Promos | Note |
|---|---|---|---|---|---|
| `shufersal` | `ok` | 417 | 6573 | 1 |  |
| `super-pharm` | `down` | — | — | — | stores: FileNotFound: super-pharm: no Stores file | prices: FileNotFound: super-pharm: no PriceFull file | promos: FileNotFound: super-pharm: no PromoFull file |
| `wolt` | `ok` | 34 | 6007 | 0 |  |
| `carrefour` | `ok` | 147 | 8233 | 1406 |  |
| `hatzi-hinam` | `down` | — | — | — | stores: PortalError: GET https://shop.hazi-hinam.co.il/Prices -> HTTP 403 | prices: PortalError: GET https://shop.hazi-hinam.co.il/Prices -> HTTP 403 | promos: PortalError: GET https://shop.hazi-hinam.co.il/Prices -> HTTP 403 |
| `rami-levy` | `ok` | 99 | 5217 | 1072 |  |
| `tiv-taam` | `ok` | 54 | 125 | 40 |  |
| `yochananof` | `ok` | 51 | 11766 | 2632 |  |
| `osher-ad` | `ok` | 24 | 6328 | 688 |  |
| `dor-alon` | `ok` | 158 | 1488 | 315 |  |
| `keshet-teamim` | `ok` | 28 | 6370 | 1694 |  |
| `super-cofix` | `degraded` | 34 | — | — | prices: FileNotFound: super-cofix: no PriceFull file | promos: FileNotFound: super-cofix: no PromoFull file |
| `politzer` | `ok` | 8 | 10657 | 1193 |  |
| `stop-market` | `ok` | 11 | 17499 | 2712 |  |
| `fresh-market` | `ok` | 46 | 9181 | 1356 |  |
| `salach-dabach` | `ok` | 12 | 12461 | 1790 |  |
| `super-yuda` | `ok` | 26 | 6414 | 381 |  |
| `yellow` | `ok` | 242 | 1768 | 654 |  |
| `good-pharm` | `ok` | 82 | 3399 | 351 |  |
| `super-bareket` | `ok` | 15 | 4072 | 643 |  |
| `king-store` | `ok` | 48 | 2328 | 302 |  |
| `maayan-2000` | `ok` | 38 | 2739 | 353 |  |
| `meshnat-yosef` | `ok` | 4 | 5392 | 207 |  |
| `shefa-birkat-hashem` | `ok` | 22 | 3814 | 532 |  |
| `shuk-hayir` | `ok` | 26 | 1848 | 0 |  |
| `super-sapir` | `ok` | 71 | 1191 | 81 |  |
| `zol-vebegadol` | `ok` | 35 | 4283 | 488 |  |
| `city-market` | `ok` | 28 | 4357 | 0 |  |
| `victory` | `geo-blocked` | 70 | 8716 | 4557 | reachable from Israeli IPs only (verified via proxy) |
| `mahsanei-hashuk` | `geo-blocked` | 71 | 12384 | 5989 | reachable from Israeli IPs only (verified via proxy) |
| `het-cohen` | `geo-blocked` | 5 | 8929 | 2785 | reachable from Israeli IPs only (verified via proxy) |
| `nativ-hahesed` | `down` | — | — | — | portal still unreachable (PortalError) |
