# Chain health

**Coverage: 31/32 chains implemented** — the full government roster bar Nativ HaHesed, whose portal has returned HTTP 500 since July 2026 (it stays registered and will be enabled when it returns).

**Last nightly check (2026-11-09T17:14:43+00:00): 30/32 reachable.** The check runs from a GitHub-hosted runner outside Israel and fetches every file type of every chain. Daily reachability fluctuates: chains sometimes publish empty or late files, and some small chains publish sporadically — that's the chains' portals, not the library. `geo-blocked` = the portal only answers Israeli IPs (verified through an Israeli proxy). `degraded` = some file types were missing/empty at check time.

| Chain | Status | Stores | Prices | Promos | Note |
|---|---|---|---|---|---|
| `shufersal` | `geo-blocked` | 417 | 6565 | 1 | reachable from Israeli IPs only (verified via proxy) |
| `super-pharm` | `geo-blocked` | 307 | 8071 | 541 | reachable from Israeli IPs only (verified via proxy) |
| `wolt` | `ok` | 37 | 0 | 632 |  |
| `carrefour` | `geo-blocked` | 147 | 11102 | 1713 | reachable from Israeli IPs only (verified via proxy) |
| `hatzi-hinam` | `geo-blocked` | 13 | 605 | 853 | reachable from Israeli IPs only (verified via proxy) |
| `rami-levy` | `ok` | 99 | 5287 | 1075 |  |
| `tiv-taam` | `ok` | 54 | 52 | 17 |  |
| `yochananof` | `ok` | 51 | 11782 | 1353 |  |
| `osher-ad` | `ok` | 24 | 6038 | 777 |  |
| `dor-alon` | `ok` | 157 | 1512 | 327 |  |
| `keshet-teamim` | `ok` | 28 | 4144 | 1522 |  |
| `super-cofix` | `degraded` | 34 | — | — | prices: FileNotFound: super-cofix: no PriceFull file | promos: FileNotFound: super-cofix: no PromoFull file |
| `politzer` | `ok` | 8 | 15099 | 1066 |  |
| `stop-market` | `ok` | 11 | 17564 | 2804 |  |
| `fresh-market` | `ok` | 73 | 8310 | 779 |  |
| `salach-dabach` | `ok` | 12 | 12340 | 1957 |  |
| `super-yuda` | `ok` | 26 | 6440 | 415 |  |
| `yellow` | `ok` | 242 | 1851 | 687 |  |
| `good-pharm` | `ok` | 84 | 3305 | 336 |  |
| `super-bareket` | `ok` | 15 | 4738 | 701 |  |
| `king-store` | `ok` | 48 | 2355 | 258 |  |
| `maayan-2000` | `ok` | 38 | 3061 | 410 |  |
| `meshnat-yosef` | `ok` | 4 | 5504 | 216 |  |
| `shefa-birkat-hashem` | `ok` | 22 | 3949 | 546 |  |
| `shuk-hayir` | `ok` | 26 | 1801 | 0 |  |
| `super-sapir` | `ok` | 130 | 14 | 1 |  |
| `zol-vebegadol` | `ok` | 35 | 4271 | 479 |  |
| `city-market` | `ok` | 70 | 3058 | 299 |  |
| `victory` | `geo-blocked` | 70 | 8663 | 4730 | reachable from Israeli IPs only (verified via proxy) |
| `mahsanei-hashuk` | `geo-blocked` | 71 | 12448 | 6086 | reachable from Israeli IPs only (verified via proxy) |
| `het-cohen` | `geo-blocked` | 5 | 7197 | 2873 | reachable from Israeli IPs only (verified via proxy) |
| `nativ-hahesed` | `down` | — | — | — | portal still unreachable (PortalError) |
