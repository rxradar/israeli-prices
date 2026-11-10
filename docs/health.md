# Chain health

**Coverage: 31/32 chains implemented** — the full government roster bar Nativ HaHesed, whose portal has returned HTTP 500 since July 2026 (it stays registered and will be enabled when it returns).

**Last nightly check (2026-11-10T15:26:50+00:00): 30/32 reachable.** The check runs from a GitHub-hosted runner outside Israel and fetches every file type of every chain. Daily reachability fluctuates: chains sometimes publish empty or late files, and some small chains publish sporadically — that's the chains' portals, not the library. `geo-blocked` = the portal only answers Israeli IPs (verified through an Israeli proxy). `degraded` = some file types were missing/empty at check time.

| Chain | Status | Stores | Prices | Promos | Note |
|---|---|---|---|---|---|
| `shufersal` | `ok` | 417 | 6572 | 16 |  |
| `super-pharm` | `geo-blocked` | 307 | 8367 | 641 | reachable from Israeli IPs only (verified via proxy) |
| `wolt` | `ok` | 37 | 5814 | 0 |  |
| `carrefour` | `geo-blocked` | 147 | 11108 | 1780 | reachable from Israeli IPs only (verified via proxy) |
| `hatzi-hinam` | `geo-blocked` | 13 | 600 | 862 | reachable from Israeli IPs only (verified via proxy) |
| `rami-levy` | `ok` | 99 | 5296 | 1097 |  |
| `tiv-taam` | `ok` | 54 | 52 | 17 |  |
| `yochananof` | `ok` | 51 | 11781 | 1398 |  |
| `osher-ad` | `ok` | 24 | 6020 | 782 |  |
| `dor-alon` | `ok` | 157 | 5297 | 594 |  |
| `keshet-teamim` | `ok` | 28 | 6471 | 1496 |  |
| `super-cofix` | `degraded` | 34 | — | — | prices: FileNotFound: super-cofix: no PriceFull file | promos: FileNotFound: super-cofix: no PromoFull file |
| `politzer` | `ok` | 8 | 13978 | 1095 |  |
| `stop-market` | `ok` | 11 | 10741 | 2795 |  |
| `fresh-market` | `ok` | 73 | 9236 | 1510 |  |
| `salach-dabach` | `ok` | 12 | 12327 | 1965 |  |
| `super-yuda` | `ok` | 26 | 6450 | 415 |  |
| `yellow` | `ok` | 242 | 1397 | 683 |  |
| `good-pharm` | `ok` | 84 | 3300 | 336 |  |
| `super-bareket` | `ok` | 15 | 4746 | 701 |  |
| `king-store` | `ok` | 48 | 2347 | 259 |  |
| `maayan-2000` | `ok` | 38 | 3051 | 411 |  |
| `meshnat-yosef` | `ok` | 4 | 5510 | 219 |  |
| `shefa-birkat-hashem` | `ok` | 22 | 3932 | 568 |  |
| `shuk-hayir` | `ok` | 26 | 1661 | 0 |  |
| `super-sapir` | `ok` | 130 | 19 | 1 |  |
| `zol-vebegadol` | `ok` | 35 | 4272 | 500 |  |
| `city-market` | `ok` | 70 | 3061 | 301 |  |
| `victory` | `geo-blocked` | 70 | 10402 | 4356 | reachable from Israeli IPs only (verified via proxy) |
| `mahsanei-hashuk` | `geo-blocked` | 71 | 8513 | 4083 | reachable from Israeli IPs only (verified via proxy) |
| `het-cohen` | `geo-blocked` | 5 | 8931 | 2874 | reachable from Israeli IPs only (verified via proxy) |
| `nativ-hahesed` | `down` | — | — | — | portal still unreachable (PortalError) |
