# Chain health

**Coverage: 31/32 chains implemented** — the full government roster bar Nativ HaHesed, whose portal has returned HTTP 500 since July 2026 (it stays registered and will be enabled when it returns).

**Last nightly check (2026-11-12T15:49:26+00:00): 30/32 reachable.** The check runs from a GitHub-hosted runner outside Israel and fetches every file type of every chain. Daily reachability fluctuates: chains sometimes publish empty or late files, and some small chains publish sporadically — that's the chains' portals, not the library. `geo-blocked` = the portal only answers Israeli IPs (verified through an Israeli proxy). `degraded` = some file types were missing/empty at check time.

| Chain | Status | Stores | Prices | Promos | Note |
|---|---|---|---|---|---|
| `shufersal` | `ok` | 417 | 6576 | 16 |  |
| `super-pharm` | `geo-blocked` | 307 | 8061 | 784 | reachable from Israeli IPs only (verified via proxy) |
| `wolt` | `ok` | 37 | 0 | 537 |  |
| `carrefour` | `geo-blocked` | 147 | 11105 | 1796 | reachable from Israeli IPs only (verified via proxy) |
| `hatzi-hinam` | `geo-blocked` | 13 | 601 | 864 | reachable from Israeli IPs only (verified via proxy) |
| `rami-levy` | `ok` | 99 | 5287 | 1079 |  |
| `tiv-taam` | `ok` | 54 | 52 | 17 |  |
| `yochananof` | `ok` | 51 | 11799 | 2800 |  |
| `osher-ad` | `ok` | 24 | 5988 | 810 |  |
| `dor-alon` | `ok` | 157 | 1493 | 333 |  |
| `keshet-teamim` | `ok` | 28 | 6505 | 1503 |  |
| `super-cofix` | `degraded` | 34 | — | — | prices: FileNotFound: super-cofix: no PriceFull file | promos: FileNotFound: super-cofix: no PromoFull file |
| `politzer` | `ok` | 8 | 15119 | 1157 |  |
| `stop-market` | `ok` | 11 | 15268 | 2805 |  |
| `fresh-market` | `ok` | 73 | 8302 | 786 |  |
| `salach-dabach` | `ok` | 12 | 12299 | 1982 |  |
| `super-yuda` | `ok` | 26 | 6462 | 415 |  |
| `yellow` | `ok` | 242 | 1013 | 733 |  |
| `good-pharm` | `ok` | 84 | 3317 | 336 |  |
| `super-bareket` | `ok` | 15 | 4740 | 713 |  |
| `king-store` | `ok` | 48 | 2347 | 267 |  |
| `maayan-2000` | `ok` | 38 | 3060 | 416 |  |
| `meshnat-yosef` | `ok` | 4 | 5522 | 230 |  |
| `shefa-birkat-hashem` | `ok` | 22 | 3660 | 545 |  |
| `shuk-hayir` | `ok` | 26 | 1636 | 0 |  |
| `super-sapir` | `ok` | 130 | 19 | 1 |  |
| `zol-vebegadol` | `ok` | 35 | 4281 | 493 |  |
| `city-market` | `ok` | 70 | 4310 | 0 |  |
| `victory` | `geo-blocked` | 70 | 8675 | 4310 | reachable from Israeli IPs only (verified via proxy) |
| `mahsanei-hashuk` | `geo-blocked` | 72 | 12486 | 6224 | reachable from Israeli IPs only (verified via proxy) |
| `het-cohen` | `geo-blocked` | 5 | 8935 | 2899 | reachable from Israeli IPs only (verified via proxy) |
| `nativ-hahesed` | `down` | — | — | — | portal still unreachable (PortalError) |
