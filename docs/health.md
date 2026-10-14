# Chain health

**Coverage: 31/32 chains implemented** — the full government roster bar Nativ HaHesed, whose portal has returned HTTP 500 since July 2026 (it stays registered and will be enabled when it returns).

**Last nightly check (2026-10-14T12:41:58+00:00): 29/32 reachable.** The check runs from a GitHub-hosted runner outside Israel and fetches every file type of every chain. Daily reachability fluctuates: chains sometimes publish empty or late files, and some small chains publish sporadically — that's the chains' portals, not the library. `geo-blocked` = the portal only answers Israeli IPs (verified through an Israeli proxy). `degraded` = some file types were missing/empty at check time.

| Chain | Status | Stores | Prices | Promos | Note |
|---|---|---|---|---|---|
| `shufersal` | `geo-blocked` | 417 | 6582 | 1 | reachable from Israeli IPs only (verified via proxy) |
| `super-pharm` | `down` | — | — | — | stores: FileNotFound: super-pharm: no Stores file | prices: FileNotFound: super-pharm: no PriceFull file | promos: FileNotFound: super-pharm: no PromoFull file |
| `wolt` | `ok` | 34 | 0 | 454 |  |
| `carrefour` | `ok` | 147 | 11137 | 1582 |  |
| `hatzi-hinam` | `geo-blocked` | 13 | 608 | 558 | reachable from Israeli IPs only (verified via proxy) |
| `rami-levy` | `ok` | 99 | 5190 | 1074 |  |
| `tiv-taam` | `ok` | 54 | 125 | 40 |  |
| `yochananof` | `ok` | 51 | 11773 | 1308 |  |
| `osher-ad` | `ok` | 24 | 6401 | 715 |  |
| `dor-alon` | `ok` | 157 | 1981 | 316 |  |
| `keshet-teamim` | `ok` | 27 | 6369 | 1688 |  |
| `super-cofix` | `degraded` | 34 | — | — | prices: FileNotFound: super-cofix: no PriceFull file | promos: FileNotFound: super-cofix: no PromoFull file |
| `politzer` | `ok` | 8 | 13927 | 1187 |  |
| `stop-market` | `ok` | 12 | 17475 | 2707 |  |
| `fresh-market` | `ok` | 46 | 8276 | 696 |  |
| `salach-dabach` | `ok` | 12 | 12513 | 1782 |  |
| `super-yuda` | `ok` | 26 | 6400 | 381 |  |
| `yellow` | `ok` | 242 | 1875 | 710 |  |
| `good-pharm` | `ok` | 82 | 3366 | 343 |  |
| `super-bareket` | `ok` | 15 | 3530 | 605 |  |
| `king-store` | `ok` | 48 | 2345 | 294 |  |
| `maayan-2000` | `ok` | 38 | 2740 | 362 |  |
| `meshnat-yosef` | `ok` | 4 | 5480 | 204 |  |
| `shefa-birkat-hashem` | `ok` | 22 | 3583 | 529 |  |
| `shuk-hayir` | `ok` | 26 | 1852 | 0 |  |
| `super-sapir` | `ok` | 73 | 1137 | 78 |  |
| `zol-vebegadol` | `ok` | 35 | 4260 | 487 |  |
| `city-market` | `ok` | 28 | 4326 | 0 |  |
| `victory` | `geo-blocked` | 70 | 8722 | 4492 | reachable from Israeli IPs only (verified via proxy) |
| `mahsanei-hashuk` | `geo-blocked` | 71 | 12409 | 6093 | reachable from Israeli IPs only (verified via proxy) |
| `het-cohen` | `geo-blocked` | 5 | 8935 | 2733 | reachable from Israeli IPs only (verified via proxy) |
| `nativ-hahesed` | `down` | — | — | — | portal still unreachable (PortalError) |
