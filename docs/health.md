# Chain health

**Coverage: 31/32 chains implemented** — the full government roster bar Nativ HaHesed, whose portal has returned HTTP 500 since July 2026 (it stays registered and will be enabled when it returns).

**Last nightly check (2026-10-04T13:04:16+00:00): 30/32 reachable.** The check runs from a GitHub-hosted runner outside Israel and fetches every file type of every chain. Daily reachability fluctuates: chains sometimes publish empty or late files, and some small chains publish sporadically — that's the chains' portals, not the library. `geo-blocked` = the portal only answers Israeli IPs (verified through an Israeli proxy). `degraded` = some file types were missing/empty at check time.

| Chain | Status | Stores | Prices | Promos | Note |
|---|---|---|---|---|---|
| `shufersal` | `ok` | 417 | 6620 | 1 |  |
| `super-pharm` | `geo-blocked` | 307 | 7094 | 808 | reachable from Israeli IPs only (verified via proxy) |
| `wolt` | `ok` | 34 | 5124 | 654 |  |
| `carrefour` | `ok` | 147 | 11179 | 1417 |  |
| `hatzi-hinam` | `geo-blocked` | 13 | 607 | 716 | reachable from Israeli IPs only (verified via proxy) |
| `rami-levy` | `ok` | 99 | 5277 | 1030 |  |
| `tiv-taam` | `ok` | 54 | 135 | 46 |  |
| `yochananof` | `ok` | 51 | 11753 | 977 |  |
| `osher-ad` | `ok` | 24 | 6509 | 446 |  |
| `dor-alon` | `ok` | 157 | 4108 | 682 |  |
| `keshet-teamim` | `ok` | 27 | 6367 | 1668 |  |
| `super-cofix` | `degraded` | 34 | — | — | prices: FileNotFound: super-cofix: no PriceFull file | promos: FileNotFound: super-cofix: no PromoFull file |
| `politzer` | `ok` | 8 | 14477 | 863 |  |
| `stop-market` | `ok` | 11 | 17478 | 2074 |  |
| `fresh-market` | `ok` | 47 | 8298 | 577 |  |
| `salach-dabach` | `ok` | 12 | 15798 | 1732 |  |
| `super-yuda` | `ok` | 26 | 6395 | 303 |  |
| `yellow` | `ok` | 242 | 1896 | 632 |  |
| `good-pharm` | `ok` | 82 | 3407 | 283 |  |
| `super-bareket` | `ok` | 14 | 6549 | 687 |  |
| `king-store` | `ok` | 29 | 2453 | 296 |  |
| `maayan-2000` | `ok` | 38 | 2473 | 305 |  |
| `meshnat-yosef` | `ok` | 4 | 5523 | 138 |  |
| `shefa-birkat-hashem` | `ok` | 22 | 3694 | 435 |  |
| `shuk-hayir` | `ok` | 26 | 1546 | 0 |  |
| `super-sapir` | `ok` | 72 | 1085 | 67 |  |
| `zol-vebegadol` | `ok` | 35 | 3783 | 1089 |  |
| `city-market` | `ok` | 28 | 2911 | 224 |  |
| `victory` | `geo-blocked` | 70 | 8682 | 2440 | reachable from Israeli IPs only (verified via proxy) |
| `mahsanei-hashuk` | `geo-blocked` | 71 | 13334 | 4123 | reachable from Israeli IPs only (verified via proxy) |
| `het-cohen` | `geo-blocked` | 5 | 7155 | 3101 | reachable from Israeli IPs only (verified via proxy) |
| `nativ-hahesed` | `down` | — | — | — | portal still unreachable (PortalError) |
