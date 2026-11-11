# Chain health

**Coverage: 31/32 chains implemented** — the full government roster bar Nativ HaHesed, whose portal has returned HTTP 500 since July 2026 (it stays registered and will be enabled when it returns).

**Last nightly check (2026-11-11T14:57:40+00:00): 30/32 reachable.** The check runs from a GitHub-hosted runner outside Israel and fetches every file type of every chain. Daily reachability fluctuates: chains sometimes publish empty or late files, and some small chains publish sporadically — that's the chains' portals, not the library. `geo-blocked` = the portal only answers Israeli IPs (verified through an Israeli proxy). `degraded` = some file types were missing/empty at check time.

| Chain | Status | Stores | Prices | Promos | Note |
|---|---|---|---|---|---|
| `shufersal` | `ok` | 417 | 6572 | 16 |  |
| `super-pharm` | `geo-blocked` | 307 | 6511 | 787 | reachable from Israeli IPs only (verified via proxy) |
| `wolt` | `ok` | 37 | 0 | 0 |  |
| `carrefour` | `geo-blocked` | 147 | 11102 | 1774 | reachable from Israeli IPs only (verified via proxy) |
| `hatzi-hinam` | `geo-blocked` | 13 | 600 | 864 | reachable from Israeli IPs only (verified via proxy) |
| `rami-levy` | `ok` | 99 | 5287 | 1078 |  |
| `tiv-taam` | `ok` | 54 | 52 | 17 |  |
| `yochananof` | `ok` | 51 | 11789 | 1387 |  |
| `osher-ad` | `ok` | 24 | 6012 | 798 |  |
| `dor-alon` | `ok` | 157 | 4002 | 844 |  |
| `keshet-teamim` | `ok` | 28 | 6476 | 1501 |  |
| `super-cofix` | `degraded` | 34 | — | — | prices: FileNotFound: super-cofix: no PriceFull file | promos: FileNotFound: super-cofix: no PromoFull file |
| `politzer` | `ok` | 8 | 13706 | 1106 |  |
| `stop-market` | `ok` | 11 | 17590 | 2823 |  |
| `fresh-market` | `ok` | 73 | 9245 | 1509 |  |
| `salach-dabach` | `ok` | 12 | 12325 | 1978 |  |
| `super-yuda` | `ok` | 26 | 6451 | 416 |  |
| `yellow` | `ok` | 242 | 2180 | 746 |  |
| `good-pharm` | `ok` | 84 | 3302 | 332 |  |
| `super-bareket` | `ok` | 15 | 4756 | 706 |  |
| `king-store` | `ok` | 48 | 2360 | 261 |  |
| `maayan-2000` | `ok` | 38 | 3090 | 417 |  |
| `meshnat-yosef` | `ok` | 4 | 5526 | 229 |  |
| `shefa-birkat-hashem` | `ok` | 22 | 3822 | 558 |  |
| `shuk-hayir` | `ok` | 26 | 1716 | 0 |  |
| `super-sapir` | `ok` | 130 | 19 | 1 |  |
| `zol-vebegadol` | `ok` | 35 | 4277 | 489 |  |
| `city-market` | `ok` | 70 | 4303 | 0 |  |
| `victory` | `geo-blocked` | 70 | 8647 | 4250 | reachable from Israeli IPs only (verified via proxy) |
| `mahsanei-hashuk` | `geo-blocked` | 72 | 12464 | 6268 | reachable from Israeli IPs only (verified via proxy) |
| `het-cohen` | `geo-blocked` | 5 | 10774 | 2886 | reachable from Israeli IPs only (verified via proxy) |
| `nativ-hahesed` | `down` | — | — | — | portal still unreachable (PortalError) |
