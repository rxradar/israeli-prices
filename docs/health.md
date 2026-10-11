# Chain health

**Coverage: 31/32 chains implemented** — the full government roster bar Nativ HaHesed, whose portal has returned HTTP 500 since July 2026 (it stays registered and will be enabled when it returns).

**Last nightly check (2026-10-11T13:50:05+00:00): 30/32 reachable.** The check runs from a GitHub-hosted runner outside Israel and fetches every file type of every chain. Daily reachability fluctuates: chains sometimes publish empty or late files, and some small chains publish sporadically — that's the chains' portals, not the library. `geo-blocked` = the portal only answers Israeli IPs (verified through an Israeli proxy). `degraded` = some file types were missing/empty at check time.

| Chain | Status | Stores | Prices | Promos | Note |
|---|---|---|---|---|---|
| `shufersal` | `geo-blocked` | 417 | 6591 | 1 | reachable from Israeli IPs only (verified via proxy) |
| `super-pharm` | `geo-blocked` | 307 | 8799 | 753 | reachable from Israeli IPs only (verified via proxy) |
| `wolt` | `ok` | 34 | 5986 | 381 |  |
| `carrefour` | `ok` | 147 | 8753 | 1509 |  |
| `hatzi-hinam` | `geo-blocked` | 13 | 606 | 525 | reachable from Israeli IPs only (verified via proxy) |
| `rami-levy` | `ok` | 99 | 13860 | 2394 |  |
| `tiv-taam` | `ok` | 54 | 140 | 46 |  |
| `yochananof` | `ok` | 51 | 11767 | 1289 |  |
| `osher-ad` | `ok` | 24 | 6441 | 638 |  |
| `dor-alon` | `ok` | 157 | 4590 | 630 |  |
| `keshet-teamim` | `ok` | 27 | 6388 | 1687 |  |
| `super-cofix` | `degraded` | 34 | — | — | prices: FileNotFound: super-cofix: no PriceFull file | promos: FileNotFound: super-cofix: no PromoFull file |
| `politzer` | `ok` | 8 | 13916 | 1137 |  |
| `stop-market` | `ok` | 12 | 14359 | 2711 |  |
| `fresh-market` | `ok` | 47 | 8283 | 680 |  |
| `salach-dabach` | `ok` | 12 | 12533 | 1758 |  |
| `super-yuda` | `ok` | 26 | 5352 | 376 |  |
| `yellow` | `ok` | 242 | 1911 | 668 |  |
| `good-pharm` | `ok` | 82 | 3327 | 333 |  |
| `super-bareket` | `ok` | 15 | 2912 | 544 |  |
| `king-store` | `ok` | 48 | 2365 | 290 |  |
| `maayan-2000` | `ok` | 38 | 2660 | 324 |  |
| `meshnat-yosef` | `ok` | 4 | 5481 | 189 |  |
| `shefa-birkat-hashem` | `ok` | 22 | 3800 | 529 |  |
| `shuk-hayir` | `ok` | 26 | 1738 | 0 |  |
| `super-sapir` | `ok` | 73 | 1111 | 70 |  |
| `zol-vebegadol` | `ok` | 35 | 4258 | 481 |  |
| `city-market` | `ok` | 28 | 4344 | 0 |  |
| `victory` | `geo-blocked` | 70 | 8707 | 4577 | reachable from Israeli IPs only (verified via proxy) |
| `mahsanei-hashuk` | `geo-blocked` | 71 | 12371 | 5809 | reachable from Israeli IPs only (verified via proxy) |
| `het-cohen` | `geo-blocked` | 5 | 7164 | 1969 | reachable from Israeli IPs only (verified via proxy) |
| `nativ-hahesed` | `down` | — | — | — | portal still unreachable (PortalError) |
