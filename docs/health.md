# Chain health

**Coverage: 31/32 chains implemented** — the full government roster bar Nativ HaHesed, whose portal has returned HTTP 500 since July 2026 (it stays registered and will be enabled when it returns).

**Last nightly check (2026-11-05T15:13:18+00:00): 29/32 reachable.** The check runs from a GitHub-hosted runner outside Israel and fetches every file type of every chain. Daily reachability fluctuates: chains sometimes publish empty or late files, and some small chains publish sporadically — that's the chains' portals, not the library. `geo-blocked` = the portal only answers Israeli IPs (verified through an Israeli proxy). `degraded` = some file types were missing/empty at check time.

| Chain | Status | Stores | Prices | Promos | Note |
|---|---|---|---|---|---|
| `shufersal` | `ok` | 417 | 6560 | 1 |  |
| `super-pharm` | `geo-blocked` | 307 | 12414 | 608 | reachable from Israeli IPs only (verified via proxy) |
| `wolt` | `ok` | 37 | 0 | 617 |  |
| `carrefour` | `geo-blocked` | 147 | 11088 | 1693 | reachable from Israeli IPs only (verified via proxy) |
| `hatzi-hinam` | `degraded` | 13 | — | 861 | prices: PortalError: GET https://shop.hazi-hinam.co.il/Prices -> HTTP 403 |
| `rami-levy` | `ok` | 99 | 5271 | 1079 |  |
| `tiv-taam` | `ok` | 54 | 52 | 17 |  |
| `yochananof` | `ok` | 51 | 11790 | 1313 |  |
| `osher-ad` | `ok` | 24 | 6097 | 751 |  |
| `dor-alon` | `ok` | 157 | 1826 | 331 |  |
| `keshet-teamim` | `ok` | 28 | 6372 | 1527 |  |
| `super-cofix` | `degraded` | 34 | — | — | prices: FileNotFound: super-cofix: no PriceFull file | promos: FileNotFound: super-cofix: no PromoFull file |
| `politzer` | `ok` | 8 | 15007 | 903 |  |
| `stop-market` | `ok` | 11 | 10698 | 2774 |  |
| `fresh-market` | `ok` | 73 | 9222 | 1488 |  |
| `salach-dabach` | `ok` | 12 | 12332 | 1961 |  |
| `super-yuda` | `ok` | 26 | 6425 | 416 |  |
| `yellow` | `ok` | 242 | 1572 | 680 |  |
| `good-pharm` | `ok` | 83 | 3317 | 285 |  |
| `super-bareket` | `ok` | 15 | 4685 | 707 |  |
| `king-store` | `ok` | 48 | 2336 | 250 |  |
| `maayan-2000` | `ok` | 38 | 2913 | 392 |  |
| `meshnat-yosef` | `ok` | 4 | 5455 | 205 |  |
| `shefa-birkat-hashem` | `ok` | 22 | 3663 | 541 |  |
| `shuk-hayir` | `ok` | 26 | 1518 | 0 |  |
| `super-sapir` | `ok` | 130 | 2333 | 1 |  |
| `zol-vebegadol` | `ok` | 35 | 4267 | 454 |  |
| `city-market` | `ok` | 70 | 4283 | 0 |  |
| `victory` | `geo-blocked` | 70 | 9048 | 4019 | reachable from Israeli IPs only (verified via proxy) |
| `mahsanei-hashuk` | `geo-blocked` | 71 | 12408 | 5363 | reachable from Israeli IPs only (verified via proxy) |
| `het-cohen` | `geo-blocked` | 5 | 7214 | 2829 | reachable from Israeli IPs only (verified via proxy) |
| `nativ-hahesed` | `down` | — | — | — | portal still unreachable (PortalError) |
