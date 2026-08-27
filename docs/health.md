# Chain health

**Coverage: 31/32 chains implemented** — the full government roster bar Nativ HaHesed, whose portal has returned HTTP 500 since July 2026 (it stays registered and will be enabled when it returns).

**Last nightly check (2026-08-27T18:08:00+00:00): 29/32 reachable.** The check runs from a GitHub-hosted runner outside Israel and fetches every file type of every chain. Daily reachability fluctuates: chains sometimes publish empty or late files, and some small chains publish sporadically — that's the chains' portals, not the library. `geo-blocked` = the portal only answers Israeli IPs (verified through an Israeli proxy). `degraded` = some file types were missing/empty at check time.

| Chain | Status | Stores | Prices | Promos | Note |
|---|---|---|---|---|---|
| `shufersal` | `ok` | 417 | 6543 | 1 |  |
| `super-pharm` | `geo-blocked` | 306 | 8175 | 1018 | reachable from Israeli IPs only (verified via proxy) |
| `wolt` | `ok` | 34 | 5270 | 1019 |  |
| `carrefour` | `ok` | 147 | 11214 | 2305 |  |
| `hatzi-hinam` | `geo-blocked` | 13 | 596 | 774 | reachable from Israeli IPs only (verified via proxy) |
| `rami-levy` | `ok` | 99 | 5245 | 1287 |  |
| `tiv-taam` | `ok` | 54 | 119 | 40 |  |
| `yochananof` | `ok` | 51 | 11506 | 1688 |  |
| `osher-ad` | `ok` | 24 | 6586 | 897 |  |
| `dor-alon` | `ok` | 156 | 768 | 323 |  |
| `keshet-teamim` | `ok` | 27 | 14866 | 2917 |  |
| `super-cofix` | `degraded` | 34 | — | — | prices: FileNotFound: super-cofix: no PriceFull file | promos: FileNotFound: super-cofix: no PromoFull file |
| `politzer` | `ok` | 8 | 13966 | 1484 |  |
| `stop-market` | `ok` | 11 | 18028 | 3814 |  |
| `fresh-market` | `degraded` | — | 8419 | 735 | stores: ParseError: not valid XML: no element found: line 1, column 0 |
| `salach-dabach` | `ok` | 10 | 13207 | 2072 |  |
| `super-yuda` | `ok` | 26 | 6696 | 437 |  |
| `yellow` | `ok` | 242 | 2874 | 645 |  |
| `good-pharm` | `ok` | 82 | 3418 | 671 |  |
| `super-bareket` | `ok` | 14 | 6833 | 1459 |  |
| `king-store` | `ok` | 29 | 2309 | 303 |  |
| `maayan-2000` | `ok` | 38 | 2474 | 385 |  |
| `meshnat-yosef` | `ok` | 4 | 5478 | 294 |  |
| `shefa-birkat-hashem` | `ok` | 22 | 3479 | 636 |  |
| `shuk-hayir` | `ok` | 26 | 1562 | 0 |  |
| `super-sapir` | `ok` | 70 | 3512 | 0 |  |
| `zol-vebegadol` | `ok` | 35 | 3804 | 1198 |  |
| `city-market` | `ok` | 28 | 2886 | 321 |  |
| `victory` | `geo-blocked` | 70 | 8588 | 5287 | reachable from Israeli IPs only (verified via proxy) |
| `mahsanei-hashuk` | `geo-blocked` | 71 | 9843 | 5068 | reachable from Israeli IPs only (verified via proxy) |
| `het-cohen` | `geo-blocked` | 5 | 7154 | 3197 | reachable from Israeli IPs only (verified via proxy) |
| `nativ-hahesed` | `down` | — | — | — | portal still unreachable (PortalError) |
