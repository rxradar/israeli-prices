# Chain health

**Coverage: 31/32 chains implemented** — the full government roster bar Nativ HaHesed, whose portal has returned HTTP 500 since July 2026 (it stays registered and will be enabled when it returns).

**Last nightly check (2026-11-13T15:09:52+00:00): 29/32 reachable.** The check runs from a GitHub-hosted runner outside Israel and fetches every file type of every chain. Daily reachability fluctuates: chains sometimes publish empty or late files, and some small chains publish sporadically — that's the chains' portals, not the library. `geo-blocked` = the portal only answers Israeli IPs (verified through an Israeli proxy). `degraded` = some file types were missing/empty at check time.

| Chain | Status | Stores | Prices | Promos | Note |
|---|---|---|---|---|---|
| `shufersal` | `ok` | 417 | 6578 | 16 |  |
| `super-pharm` | `down` | — | — | — | stores: FileNotFound: super-pharm: no Stores file | prices: FileNotFound: super-pharm: no PriceFull file | promos: FileNotFound: super-pharm: no PromoFull file |
| `wolt` | `ok` | 37 | 0 | 657 |  |
| `carrefour` | `geo-blocked` | 147 | 11109 | 1819 | reachable from Israeli IPs only (verified via proxy) |
| `hatzi-hinam` | `geo-blocked` | 13 | 599 | 864 | reachable from Israeli IPs only (verified via proxy) |
| `rami-levy` | `ok` | 99 | 5300 | 1079 |  |
| `tiv-taam` | `ok` | 54 | 52 | 17 |  |
| `yochananof` | `ok` | 51 | 11819 | 1399 |  |
| `osher-ad` | `ok` | 24 | 5983 | 816 |  |
| `dor-alon` | `ok` | 157 | 1504 | 335 |  |
| `keshet-teamim` | `ok` | 28 | 6538 | 1503 |  |
| `super-cofix` | `degraded` | 34 | — | — | prices: FileNotFound: super-cofix: no PriceFull file | promos: FileNotFound: super-cofix: no PromoFull file |
| `politzer` | `ok` | 8 | 15027 | 1158 |  |
| `stop-market` | `ok` | 11 | 18412 | 2825 |  |
| `fresh-market` | `ok` | 73 | 9251 | 1527 |  |
| `salach-dabach` | `ok` | 12 | 12292 | 1995 |  |
| `super-yuda` | `ok` | 26 | 6465 | 415 |  |
| `yellow` | `ok` | 242 | 1589 | 682 |  |
| `good-pharm` | `ok` | 84 | 3322 | 336 |  |
| `super-bareket` | `ok` | 15 | 4756 | 715 |  |
| `king-store` | `ok` | 48 | 2371 | 271 |  |
| `maayan-2000` | `ok` | 38 | 3097 | 426 |  |
| `meshnat-yosef` | `ok` | 4 | 5549 | 232 |  |
| `shefa-birkat-hashem` | `ok` | 22 | 3906 | 560 |  |
| `shuk-hayir` | `ok` | 26 | 1827 | 0 |  |
| `super-sapir` | `ok` | 130 | 19 | 1 |  |
| `zol-vebegadol` | `ok` | 35 | 4288 | 494 |  |
| `city-market` | `ok` | 70 | 4271 | 0 |  |
| `victory` | `geo-blocked` | 70 | 8697 | 4271 | reachable from Israeli IPs only (verified via proxy) |
| `mahsanei-hashuk` | `geo-blocked` | 72 | 12491 | 6275 | reachable from Israeli IPs only (verified via proxy) |
| `het-cohen` | `geo-blocked` | 5 | 8956 | 2902 | reachable from Israeli IPs only (verified via proxy) |
| `nativ-hahesed` | `down` | — | — | — | portal still unreachable (PortalError) |
