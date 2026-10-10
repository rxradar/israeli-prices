# Chain health

**Coverage: 31/32 chains implemented** — the full government roster bar Nativ HaHesed, whose portal has returned HTTP 500 since July 2026 (it stays registered and will be enabled when it returns).

**Last nightly check (2026-10-10T13:20:52+00:00): 30/32 reachable.** The check runs from a GitHub-hosted runner outside Israel and fetches every file type of every chain. Daily reachability fluctuates: chains sometimes publish empty or late files, and some small chains publish sporadically — that's the chains' portals, not the library. `geo-blocked` = the portal only answers Israeli IPs (verified through an Israeli proxy). `degraded` = some file types were missing/empty at check time.

| Chain | Status | Stores | Prices | Promos | Note |
|---|---|---|---|---|---|
| `shufersal` | `ok` | 417 | 6599 | 1 |  |
| `super-pharm` | `geo-blocked` | 307 | 10346 | 727 | reachable from Israeli IPs only (verified via proxy) |
| `wolt` | `ok` | 34 | 5884 | 486 |  |
| `carrefour` | `ok` | 147 | 11163 | 1490 |  |
| `hatzi-hinam` | `geo-blocked` | 13 | 9808 | 560 | reachable from Israeli IPs only (verified via proxy) |
| `rami-levy` | `ok` | 99 | 13873 | 2374 |  |
| `tiv-taam` | `ok` | 54 | 140 | 46 |  |
| `yochananof` | `ok` | 51 | 11783 | 2566 |  |
| `osher-ad` | `ok` | 24 | 6398 | 644 |  |
| `dor-alon` | `ok` | 157 | 1815 | 316 |  |
| `keshet-teamim` | `ok` | 27 | 6414 | 1687 |  |
| `super-cofix` | `degraded` | 34 | — | — | prices: FileNotFound: super-cofix: no PriceFull file | promos: FileNotFound: super-cofix: no PromoFull file |
| `politzer` | `ok` | 8 | 12212 | 1128 |  |
| `stop-market` | `ok` | 12 | 17462 | 2703 |  |
| `fresh-market` | `ok` | 47 | 9215 | 1321 |  |
| `salach-dabach` | `ok` | 12 | 12532 | 1771 |  |
| `super-yuda` | `ok` | 26 | 4905 | 378 |  |
| `yellow` | `ok` | 242 | 1054 | 718 |  |
| `good-pharm` | `ok` | 82 | 3376 | 285 |  |
| `super-bareket` | `ok` | 15 | 2912 | 545 |  |
| `king-store` | `ok` | 48 | 2392 | 290 |  |
| `maayan-2000` | `ok` | 38 | 2924 | 343 |  |
| `meshnat-yosef` | `ok` | 4 | 5521 | 189 |  |
| `shefa-birkat-hashem` | `ok` | 22 | 3921 | 541 |  |
| `shuk-hayir` | `ok` | 26 | 1964 | 0 |  |
| `super-sapir` | `ok` | 73 | 1112 | 69 |  |
| `zol-vebegadol` | `ok` | 35 | 4258 | 481 |  |
| `city-market` | `ok` | 28 | 4331 | 0 |  |
| `victory` | `geo-blocked` | 70 | 8709 | 4368 | reachable from Israeli IPs only (verified via proxy) |
| `mahsanei-hashuk` | `geo-blocked` | 71 | 8939 | 3974 | reachable from Israeli IPs only (verified via proxy) |
| `het-cohen` | `geo-blocked` | 5 | 7181 | 1974 | reachable from Israeli IPs only (verified via proxy) |
| `nativ-hahesed` | `down` | — | — | — | portal still unreachable (PortalError) |
