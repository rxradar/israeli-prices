# Chain health

**Coverage: 31/32 chains implemented** — the full government roster bar Nativ HaHesed, whose portal has returned HTTP 500 since July 2026 (it stays registered and will be enabled when it returns).

**Last nightly check (2026-10-08T14:25:19+00:00): 30/32 reachable.** The check runs from a GitHub-hosted runner outside Israel and fetches every file type of every chain. Daily reachability fluctuates: chains sometimes publish empty or late files, and some small chains publish sporadically — that's the chains' portals, not the library. `geo-blocked` = the portal only answers Israeli IPs (verified through an Israeli proxy). `degraded` = some file types were missing/empty at check time.

| Chain | Status | Stores | Prices | Promos | Note |
|---|---|---|---|---|---|
| `shufersal` | `ok` | 417 | 6613 | 1 |  |
| `super-pharm` | `geo-blocked` | 307 | 10317 | 649 | reachable from Israeli IPs only (verified via proxy) |
| `wolt` | `ok` | 34 | 0 | 0 |  |
| `carrefour` | `ok` | 147 | 11163 | 1495 |  |
| `hatzi-hinam` | `geo-blocked` | 13 | 610 | 525 | reachable from Israeli IPs only (verified via proxy) |
| `rami-levy` | `ok` | 99 | 13824 | 2308 |  |
| `tiv-taam` | `ok` | 54 | 135 | 46 |  |
| `yochananof` | `ok` | 51 | 11785 | 1272 |  |
| `osher-ad` | `ok` | 24 | 6467 | 635 |  |
| `dor-alon` | `ok` | 157 | 1134 | 314 |  |
| `keshet-teamim` | `ok` | 27 | 6346 | 1722 |  |
| `super-cofix` | `degraded` | 34 | — | — | prices: FileNotFound: super-cofix: no PriceFull file | promos: FileNotFound: super-cofix: no PromoFull file |
| `politzer` | `ok` | 8 | 13895 | 1077 |  |
| `stop-market` | `ok` | 12 | 15296 | 2678 |  |
| `fresh-market` | `ok` | 47 | 9199 | 1320 |  |
| `salach-dabach` | `ok` | 12 | 12584 | 1772 |  |
| `super-yuda` | `ok` | 26 | 6405 | 378 |  |
| `yellow` | `ok` | 242 | 1061 | 718 |  |
| `good-pharm` | `ok` | 82 | 3363 | 286 |  |
| `super-bareket` | `ok` | 15 | 2109 | 458 |  |
| `king-store` | `ok` | 48 | 2424 | 288 |  |
| `maayan-2000` | `ok` | 38 | 2689 | 298 |  |
| `meshnat-yosef` | `ok` | 4 | 5489 | 183 |  |
| `shefa-birkat-hashem` | `ok` | 22 | 3536 | 510 |  |
| `shuk-hayir` | `ok` | 26 | 1639 | 0 |  |
| `super-sapir` | `ok` | 73 | 1109 | 68 |  |
| `zol-vebegadol` | `ok` | 34 | 4258 | 481 |  |
| `city-market` | `ok` | 28 | 4373 | 0 |  |
| `victory` | `geo-blocked` | 70 | 8709 | 4235 | reachable from Israeli IPs only (verified via proxy) |
| `mahsanei-hashuk` | `geo-blocked` | 71 | 12416 | 5335 | reachable from Israeli IPs only (verified via proxy) |
| `het-cohen` | `geo-blocked` | 5 | 10701 | 2642 | reachable from Israeli IPs only (verified via proxy) |
| `nativ-hahesed` | `down` | — | — | — | portal still unreachable (PortalError) |
