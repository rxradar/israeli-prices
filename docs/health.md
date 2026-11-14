# Chain health

**Coverage: 31/32 chains implemented** — the full government roster bar Nativ HaHesed, whose portal has returned HTTP 500 since July 2026 (it stays registered and will be enabled when it returns).

**Last nightly check (2026-11-14T13:58:30+00:00): 29/32 reachable.** The check runs from a GitHub-hosted runner outside Israel and fetches every file type of every chain. Daily reachability fluctuates: chains sometimes publish empty or late files, and some small chains publish sporadically — that's the chains' portals, not the library. `geo-blocked` = the portal only answers Israeli IPs (verified through an Israeli proxy). `degraded` = some file types were missing/empty at check time.

| Chain | Status | Stores | Prices | Promos | Note |
|---|---|---|---|---|---|
| `shufersal` | `ok` | 417 | 6571 | 16 |  |
| `super-pharm` | `down` | — | — | — | stores: FileNotFound: super-pharm: no Stores file | prices: FileNotFound: super-pharm: no PriceFull file | promos: FileNotFound: super-pharm: no PromoFull file |
| `wolt` | `ok` | 37 | 0 | 545 |  |
| `carrefour` | `geo-blocked` | 147 | 11108 | 1596 | reachable from Israeli IPs only (verified via proxy) |
| `hatzi-hinam` | `geo-blocked` | 13 | 9983 | 899 | reachable from Israeli IPs only (verified via proxy) |
| `rami-levy` | `ok` | 99 | 5300 | 1079 |  |
| `tiv-taam` | `ok` | 54 | 52 | 17 |  |
| `yochananof` | `ok` | 51 | 11816 | 1387 |  |
| `osher-ad` | `ok` | 24 | 5983 | 811 |  |
| `dor-alon` | `ok` | 157 | 1488 | 333 |  |
| `keshet-teamim` | `ok` | 28 | 6572 | 1503 |  |
| `super-cofix` | `degraded` | 34 | — | — | prices: FileNotFound: super-cofix: no PriceFull file | promos: FileNotFound: super-cofix: no PromoFull file |
| `politzer` | `ok` | 8 | 13738 | 1158 |  |
| `stop-market` | `ok` | 11 | 17562 | 2825 |  |
| `fresh-market` | `ok` | 73 | 9260 | 1517 |  |
| `salach-dabach` | `ok` | 12 | 12297 | 2001 |  |
| `super-yuda` | `ok` | 26 | 4923 | 414 |  |
| `yellow` | `ok` | 242 | 1805 | 733 |  |
| `good-pharm` | `ok` | 84 | 3349 | 338 |  |
| `super-bareket` | `ok` | 15 | 4804 | 719 |  |
| `king-store` | `ok` | 48 | 2374 | 271 |  |
| `maayan-2000` | `ok` | 38 | 3246 | 431 |  |
| `meshnat-yosef` | `ok` | 4 | 5577 | 233 |  |
| `shefa-birkat-hashem` | `ok` | 22 | 4029 | 566 |  |
| `shuk-hayir` | `ok` | 26 | 1887 | 0 |  |
| `super-sapir` | `ok` | 130 | 19 | 1 |  |
| `zol-vebegadol` | `ok` | 35 | 4284 | 495 |  |
| `city-market` | `ok` | 70 | 4287 | 0 |  |
| `victory` | `geo-blocked` | 70 | 8691 | 4259 | reachable from Israeli IPs only (verified via proxy) |
| `mahsanei-hashuk` | `geo-blocked` | 72 | 12463 | 6166 | reachable from Israeli IPs only (verified via proxy) |
| `het-cohen` | `geo-blocked` | 5 | 10808 | 2877 | reachable from Israeli IPs only (verified via proxy) |
| `nativ-hahesed` | `down` | — | — | — | portal still unreachable (PortalError) |
