# Chain health

**Coverage: 31/32 chains implemented** — the full government roster bar Nativ HaHesed, whose portal has returned HTTP 500 since July 2026 (it stays registered and will be enabled when it returns).

**Last nightly check (2026-10-01T14:17:12+00:00): 30/32 reachable.** The check runs from a GitHub-hosted runner outside Israel and fetches every file type of every chain. Daily reachability fluctuates: chains sometimes publish empty or late files, and some small chains publish sporadically — that's the chains' portals, not the library. `geo-blocked` = the portal only answers Israeli IPs (verified through an Israeli proxy). `degraded` = some file types were missing/empty at check time.

| Chain | Status | Stores | Prices | Promos | Note |
|---|---|---|---|---|---|
| `shufersal` | `ok` | 417 | 6626 | 1 |  |
| `super-pharm` | `geo-blocked` | 307 | 8040 | 759 | reachable from Israeli IPs only (verified via proxy) |
| `wolt` | `ok` | 34 | 5948 | 739 |  |
| `carrefour` | `ok` | 147 | 11199 | 1511 |  |
| `hatzi-hinam` | `geo-blocked` | 13 | 611 | 714 | reachable from Israeli IPs only (verified via proxy) |
| `rami-levy` | `ok` | 99 | 5296 | 1136 |  |
| `tiv-taam` | `ok` | 54 | 134 | 46 |  |
| `yochananof` | `ok` | 51 | 11807 | 1719 |  |
| `osher-ad` | `ok` | 24 | 6522 | 904 |  |
| `dor-alon` | `ok` | 157 | 1825 | 0 |  |
| `keshet-teamim` | `ok` | 27 | 6384 | 1847 |  |
| `super-cofix` | `degraded` | 34 | — | — | prices: FileNotFound: super-cofix: no PriceFull file | promos: FileNotFound: super-cofix: no PromoFull file |
| `politzer` | `ok` | 8 | 13404 | 1447 |  |
| `stop-market` | `ok` | 11 | 10673 | 4049 |  |
| `fresh-market` | `ok` | 47 | 9211 | 1565 |  |
| `salach-dabach` | `ok` | 12 | 12660 | 2086 |  |
| `super-yuda` | `ok` | 26 | 6389 | 444 |  |
| `yellow` | `ok` | 242 | 1362 | 662 |  |
| `good-pharm` | `ok` | 82 | 3373 | 279 |  |
| `super-bareket` | `ok` | 14 | 6492 | 1014 |  |
| `king-store` | `ok` | 29 | 2461 | 285 |  |
| `maayan-2000` | `ok` | 38 | 2495 | 427 |  |
| `meshnat-yosef` | `ok` | 4 | 5490 | 290 |  |
| `shefa-birkat-hashem` | `ok` | 22 | 3691 | 623 |  |
| `shuk-hayir` | `ok` | 26 | 1381 | 0 |  |
| `super-sapir` | `ok` | 72 | 1020 | 59 |  |
| `zol-vebegadol` | `ok` | 35 | 3759 | 1233 |  |
| `city-market` | `ok` | 28 | 4414 | 0 |  |
| `victory` | `geo-blocked` | 70 | 10053 | 5181 | reachable from Israeli IPs only (verified via proxy) |
| `mahsanei-hashuk` | `geo-blocked` | 71 | 12449 | 6840 | reachable from Israeli IPs only (verified via proxy) |
| `het-cohen` | `geo-blocked` | 5 | 7187 | 2473 | reachable from Israeli IPs only (verified via proxy) |
| `nativ-hahesed` | `down` | — | — | — | portal still unreachable (PortalError) |
