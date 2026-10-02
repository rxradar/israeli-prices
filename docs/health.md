# Chain health

**Coverage: 31/32 chains implemented** — the full government roster bar Nativ HaHesed, whose portal has returned HTTP 500 since July 2026 (it stays registered and will be enabled when it returns).

**Last nightly check (2026-10-02T13:39:15+00:00): 30/32 reachable.** The check runs from a GitHub-hosted runner outside Israel and fetches every file type of every chain. Daily reachability fluctuates: chains sometimes publish empty or late files, and some small chains publish sporadically — that's the chains' portals, not the library. `geo-blocked` = the portal only answers Israeli IPs (verified through an Israeli proxy). `degraded` = some file types were missing/empty at check time.

| Chain | Status | Stores | Prices | Promos | Note |
|---|---|---|---|---|---|
| `shufersal` | `ok` | 417 | 6632 | 1 |  |
| `super-pharm` | `geo-blocked` | 307 | 9965 | 801 | reachable from Israeli IPs only (verified via proxy) |
| `wolt` | `ok` | 34 | 5961 | 713 |  |
| `carrefour` | `ok` | 147 | 11195 | 1520 |  |
| `hatzi-hinam` | `geo-blocked` | 13 | 610 | 714 | reachable from Israeli IPs only (verified via proxy) |
| `rami-levy` | `ok` | 99 | 5290 | 1136 |  |
| `tiv-taam` | `ok` | 54 | 135 | 47 |  |
| `yochananof` | `ok` | 51 | 11799 | 1720 |  |
| `osher-ad` | `ok` | 24 | 6520 | 903 |  |
| `dor-alon` | `ok` | 157 | 1202 | 0 |  |
| `keshet-teamim` | `ok` | 27 | 6408 | 1872 |  |
| `super-cofix` | `degraded` | 34 | — | — | prices: FileNotFound: super-cofix: no PriceFull file | promos: FileNotFound: super-cofix: no PromoFull file |
| `politzer` | `ok` | 8 | 10715 | 1444 |  |
| `stop-market` | `ok` | 11 | 10676 | 4057 |  |
| `fresh-market` | `ok` | 47 | 8313 | 797 |  |
| `salach-dabach` | `ok` | 12 | 12647 | 2080 |  |
| `super-yuda` | `ok` | 26 | 6381 | 444 |  |
| `yellow` | `ok` | 242 | 1855 | 659 |  |
| `good-pharm` | `ok` | 82 | 3378 | 283 |  |
| `super-bareket` | `ok` | 14 | 6476 | 1024 |  |
| `king-store` | `ok` | 29 | 2460 | 292 |  |
| `maayan-2000` | `ok` | 38 | 2532 | 413 |  |
| `meshnat-yosef` | `ok` | 4 | 5499 | 289 |  |
| `shefa-birkat-hashem` | `ok` | 22 | 3721 | 628 |  |
| `shuk-hayir` | `ok` | 26 | 1583 | 0 |  |
| `super-sapir` | `ok` | 72 | 1064 | 59 |  |
| `zol-vebegadol` | `ok` | 35 | 3757 | 1233 |  |
| `city-market` | `ok` | 28 | 4395 | 0 |  |
| `victory` | `geo-blocked` | 70 | 10056 | 5183 | reachable from Israeli IPs only (verified via proxy) |
| `mahsanei-hashuk` | `geo-blocked` | 71 | 12431 | 6808 | reachable from Israeli IPs only (verified via proxy) |
| `het-cohen` | `geo-blocked` | 5 | 8973 | 2947 | reachable from Israeli IPs only (verified via proxy) |
| `nativ-hahesed` | `down` | — | — | — | portal still unreachable (PortalError) |
