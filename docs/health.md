# Chain health

**Coverage: 31/32 chains implemented** — the full government roster bar Nativ HaHesed, whose portal has returned HTTP 500 since July 2026 (it stays registered and will be enabled when it returns).

**Last nightly check (2026-10-13T14:51:21+00:00): 30/32 reachable.** The check runs from a GitHub-hosted runner outside Israel and fetches every file type of every chain. Daily reachability fluctuates: chains sometimes publish empty or late files, and some small chains publish sporadically — that's the chains' portals, not the library. `geo-blocked` = the portal only answers Israeli IPs (verified through an Israeli proxy). `degraded` = some file types were missing/empty at check time.

| Chain | Status | Stores | Prices | Promos | Note |
|---|---|---|---|---|---|
| `shufersal` | `ok` | 417 | 6589 | 1 |  |
| `super-pharm` | `geo-blocked` | 307 | 9006 | 740 | reachable from Israeli IPs only (verified via proxy) |
| `wolt` | `ok` | 34 | 5908 | 476 |  |
| `carrefour` | `ok` | 147 | 11159 | 1588 |  |
| `hatzi-hinam` | `geo-blocked` | 13 | 608 | 554 | reachable from Israeli IPs only (verified via proxy) |
| `rami-levy` | `ok` | 99 | 5188 | 1097 |  |
| `tiv-taam` | `ok` | 54 | 140 | 42 |  |
| `yochananof` | `ok` | 51 | 11776 | 1337 |  |
| `osher-ad` | `ok` | 24 | 6424 | 662 |  |
| `dor-alon` | `ok` | 157 | 5249 | 631 |  |
| `keshet-teamim` | `ok` | 27 | 6288 | 1688 |  |
| `super-cofix` | `degraded` | 34 | — | — | prices: FileNotFound: super-cofix: no PriceFull file | promos: FileNotFound: super-cofix: no PromoFull file |
| `politzer` | `ok` | 8 | 13430 | 1187 |  |
| `stop-market` | `ok` | 12 | 14351 | 2716 |  |
| `fresh-market` | `ok` | 47 | 8700 | 1343 |  |
| `salach-dabach` | `ok` | 12 | 12510 | 1772 |  |
| `super-yuda` | `ok` | 26 | 6397 | 381 |  |
| `yellow` | `ok` | 242 | 2133 | 658 |  |
| `good-pharm` | `ok` | 82 | 3377 | 340 |  |
| `super-bareket` | `ok` | 15 | 3356 | 591 |  |
| `king-store` | `ok` | 48 | 2341 | 295 |  |
| `maayan-2000` | `ok` | 38 | 2703 | 342 |  |
| `meshnat-yosef` | `ok` | 4 | 5495 | 203 |  |
| `shefa-birkat-hashem` | `ok` | 22 | 3679 | 531 |  |
| `shuk-hayir` | `ok` | 26 | 1819 | 0 |  |
| `super-sapir` | `ok` | 73 | 1146 | 75 |  |
| `zol-vebegadol` | `ok` | 35 | 4264 | 500 |  |
| `city-market` | `ok` | 28 | 4346 | 0 |  |
| `victory` | `geo-blocked` | 70 | 8720 | 4458 | reachable from Israeli IPs only (verified via proxy) |
| `mahsanei-hashuk` | `geo-blocked` | 71 | 12401 | 6046 | reachable from Israeli IPs only (verified via proxy) |
| `het-cohen` | `geo-blocked` | 5 | 8934 | 2426 | reachable from Israeli IPs only (verified via proxy) |
| `nativ-hahesed` | `down` | — | — | — | portal still unreachable (PortalError) |
