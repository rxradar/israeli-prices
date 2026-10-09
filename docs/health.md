# Chain health

**Coverage: 31/32 chains implemented** — the full government roster bar Nativ HaHesed, whose portal has returned HTTP 500 since July 2026 (it stays registered and will be enabled when it returns).

**Last nightly check (2026-10-09T14:11:51+00:00): 30/32 reachable.** The check runs from a GitHub-hosted runner outside Israel and fetches every file type of every chain. Daily reachability fluctuates: chains sometimes publish empty or late files, and some small chains publish sporadically — that's the chains' portals, not the library. `geo-blocked` = the portal only answers Israeli IPs (verified through an Israeli proxy). `degraded` = some file types were missing/empty at check time.

| Chain | Status | Stores | Prices | Promos | Note |
|---|---|---|---|---|---|
| `shufersal` | `ok` | 417 | 6602 | 1 |  |
| `super-pharm` | `geo-blocked` | 307 | 9248 | 818 | reachable from Israeli IPs only (verified via proxy) |
| `wolt` | `ok` | 34 | 0 | 395 |  |
| `carrefour` | `ok` | 147 | 11168 | 1496 |  |
| `hatzi-hinam` | `geo-blocked` | 13 | 611 | 524 | reachable from Israeli IPs only (verified via proxy) |
| `rami-levy` | `ok` | 99 | 13861 | 2418 |  |
| `tiv-taam` | `ok` | 54 | 140 | 46 |  |
| `yochananof` | `ok` | 51 | 11792 | 1285 |  |
| `osher-ad` | `ok` | 24 | 6458 | 639 |  |
| `dor-alon` | `ok` | 157 | 1723 | 315 |  |
| `keshet-teamim` | `ok` | 27 | 6357 | 1687 |  |
| `super-cofix` | `degraded` | 34 | — | — | prices: FileNotFound: super-cofix: no PriceFull file | promos: FileNotFound: super-cofix: no PromoFull file |
| `politzer` | `ok` | 8 | 12190 | 1128 |  |
| `stop-market` | `ok` | 12 | 18060 | 2678 |  |
| `fresh-market` | `ok` | 47 | 8296 | 684 |  |
| `salach-dabach` | `ok` | 12 | 12556 | 1772 |  |
| `super-yuda` | `ok` | 26 | 6405 | 379 |  |
| `yellow` | `ok` | 242 | 817 | 669 |  |
| `good-pharm` | `ok` | 82 | 3346 | 284 |  |
| `super-bareket` | `ok` | 15 | 2610 | 526 |  |
| `king-store` | `ok` | 48 | 2412 | 289 |  |
| `maayan-2000` | `ok` | 38 | 2686 | 323 |  |
| `meshnat-yosef` | `ok` | 4 | 5498 | 188 |  |
| `shefa-birkat-hashem` | `ok` | 22 | 3764 | 528 |  |
| `shuk-hayir` | `ok` | 26 | 1825 | 0 |  |
| `super-sapir` | `ok` | 73 | 1115 | 70 |  |
| `zol-vebegadol` | `ok` | 35 | 4265 | 483 |  |
| `city-market` | `ok` | 28 | 4348 | 0 |  |
| `victory` | `geo-blocked` | 70 | 8715 | 4366 | reachable from Israeli IPs only (verified via proxy) |
| `mahsanei-hashuk` | `geo-blocked` | 71 | 12413 | 5395 | reachable from Israeli IPs only (verified via proxy) |
| `het-cohen` | `geo-blocked` | 5 | 8960 | 2663 | reachable from Israeli IPs only (verified via proxy) |
| `nativ-hahesed` | `down` | — | — | — | portal still unreachable (PortalError) |
