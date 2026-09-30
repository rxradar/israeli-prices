# Chain health

**Coverage: 31/32 chains implemented** — the full government roster bar Nativ HaHesed, whose portal has returned HTTP 500 since July 2026 (it stays registered and will be enabled when it returns).

**Last nightly check (2026-09-30T15:01:54+00:00): 30/32 reachable.** The check runs from a GitHub-hosted runner outside Israel and fetches every file type of every chain. Daily reachability fluctuates: chains sometimes publish empty or late files, and some small chains publish sporadically — that's the chains' portals, not the library. `geo-blocked` = the portal only answers Israeli IPs (verified through an Israeli proxy). `degraded` = some file types were missing/empty at check time.

| Chain | Status | Stores | Prices | Promos | Note |
|---|---|---|---|---|---|
| `shufersal` | `ok` | 417 | 6617 | 1 |  |
| `super-pharm` | `geo-blocked` | 307 | 9320 | 846 | reachable from Israeli IPs only (verified via proxy) |
| `wolt` | `ok` | 34 | 5951 | 816 |  |
| `carrefour` | `ok` | 147 | 11222 | 1572 |  |
| `hatzi-hinam` | `geo-blocked` | 13 | 608 | 719 | reachable from Israeli IPs only (verified via proxy) |
| `rami-levy` | `ok` | 99 | 5293 | 1108 |  |
| `tiv-taam` | `ok` | 54 | 134 | 47 |  |
| `yochananof` | `ok` | 51 | 11799 | 1718 |  |
| `osher-ad` | `ok` | 24 | 6543 | 909 |  |
| `dor-alon` | `ok` | 158 | 1711 | 358 |  |
| `keshet-teamim` | `ok` | 27 | 6352 | 1847 |  |
| `super-cofix` | `degraded` | 34 | — | — | prices: FileNotFound: super-cofix: no PriceFull file | promos: FileNotFound: super-cofix: no PromoFull file |
| `politzer` | `ok` | 8 | 15055 | 1455 |  |
| `stop-market` | `ok` | 11 | 17498 | 4047 |  |
| `fresh-market` | `ok` | 47 | 8310 | 801 |  |
| `salach-dabach` | `ok` | 12 | 12667 | 2128 |  |
| `super-yuda` | `ok` | 26 | 6393 | 445 |  |
| `yellow` | `ok` | 242 | 1102 | 672 |  |
| `good-pharm` | `ok` | 82 | 3379 | 371 |  |
| `super-bareket` | `ok` | 14 | 6580 | 1019 |  |
| `king-store` | `ok` | 29 | 2458 | 285 |  |
| `maayan-2000` | `ok` | 38 | 2530 | 422 |  |
| `meshnat-yosef` | `ok` | 4 | 5517 | 266 |  |
| `shefa-birkat-hashem` | `ok` | 22 | 3978 | 653 |  |
| `shuk-hayir` | `ok` | 26 | 1451 | 0 |  |
| `super-sapir` | `ok` | 72 | 1003 | 57 |  |
| `zol-vebegadol` | `ok` | 35 | 3826 | 1234 |  |
| `city-market` | `ok` | 28 | 2964 | 223 |  |
| `victory` | `geo-blocked` | 70 | 10058 | 5151 | reachable from Israeli IPs only (verified via proxy) |
| `mahsanei-hashuk` | `geo-blocked` | 71 | 12449 | 6931 | reachable from Israeli IPs only (verified via proxy) |
| `het-cohen` | `geo-blocked` | 5 | 10697 | 3195 | reachable from Israeli IPs only (verified via proxy) |
| `nativ-hahesed` | `down` | — | — | — | portal still unreachable (PortalError) |
