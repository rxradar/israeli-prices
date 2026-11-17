# Chain health

**Coverage: 31/32 chains implemented** — the full government roster bar Nativ HaHesed, whose portal has returned HTTP 500 since July 2026 (it stays registered and will be enabled when it returns).

**Last nightly check (2026-11-17T16:44:39+00:00): 28/32 reachable.** The check runs from a GitHub-hosted runner outside Israel and fetches every file type of every chain. Daily reachability fluctuates: chains sometimes publish empty or late files, and some small chains publish sporadically — that's the chains' portals, not the library. `geo-blocked` = the portal only answers Israeli IPs (verified through an Israeli proxy). `degraded` = some file types were missing/empty at check time.

| Chain | Status | Stores | Prices | Promos | Note |
|---|---|---|---|---|---|
| `shufersal` | `ok` | 417 | 6557 | 13 |  |
| `super-pharm` | `down` | — | — | — | stores: FileNotFound: super-pharm: no Stores file | prices: FileNotFound: super-pharm: no PriceFull file | promos: FileNotFound: super-pharm: no PromoFull file |
| `wolt` | `ok` | 37 | 0 | 708 |  |
| `carrefour` | `geo-blocked` | 147 | 11094 | 1643 | reachable from Israeli IPs only (verified via proxy) |
| `hatzi-hinam` | `down` | — | — | — | stores: PortalError: GET https://shop.hazi-hinam.co.il/Prices -> HTTP 403 | prices: PortalError: GET https://shop.hazi-hinam.co.il/Prices -> HTTP 403 | promos: PortalError: GET https://shop.hazi-hinam.co.il/Prices -> HTTP 403 |
| `rami-levy` | `ok` | 99 | 5326 | 1099 |  |
| `tiv-taam` | `ok` | 54 | 52 | 17 |  |
| `yochananof` | `ok` | 51 | 11819 | 1415 |  |
| `osher-ad` | `ok` | 24 | 5971 | 850 |  |
| `dor-alon` | `ok` | 157 | 1786 | 334 |  |
| `keshet-teamim` | `ok` | 28 | 6417 | 1504 |  |
| `super-cofix` | `degraded` | 34 | — | — | prices: FileNotFound: super-cofix: no PriceFull file | promos: FileNotFound: super-cofix: no PromoFull file |
| `politzer` | `ok` | 8 | 13773 | 1210 |  |
| `stop-market` | `ok` | 11 | 14445 | 2835 |  |
| `fresh-market` | `ok` | 73 | 8299 | 0 |  |
| `salach-dabach` | `ok` | 12 | 12324 | 2031 |  |
| `super-yuda` | `ok` | 26 | 6465 | 418 |  |
| `yellow` | `ok` | 242 | 806 | 683 |  |
| `good-pharm` | `ok` | 84 | 3294 | 326 |  |
| `super-bareket` | `ok` | 15 | 4770 | 719 |  |
| `king-store` | `ok` | 48 | 2376 | 263 |  |
| `maayan-2000` | `ok` | 38 | 3052 | 432 |  |
| `meshnat-yosef` | `ok` | 4 | 5568 | 232 |  |
| `shefa-birkat-hashem` | `ok` | 22 | 3857 | 553 |  |
| `shuk-hayir` | `ok` | 26 | 1578 | 0 |  |
| `super-sapir` | `ok` | 130 | 19 | 0 |  |
| `zol-vebegadol` | `ok` | 35 | 4288 | 519 |  |
| `city-market` | `ok` | 69 | 4274 | 0 |  |
| `victory` | `geo-blocked` | 70 | 8964 | 3684 | reachable from Israeli IPs only (verified via proxy) |
| `mahsanei-hashuk` | `geo-blocked` | 72 | 12480 | 6314 | reachable from Israeli IPs only (verified via proxy) |
| `het-cohen` | `geo-blocked` | 5 | 7208 | 2897 | reachable from Israeli IPs only (verified via proxy) |
| `nativ-hahesed` | `down` | — | — | — | portal still unreachable (PortalError) |
