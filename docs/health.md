# Chain health

**Coverage: 31/32 chains implemented** — the full government roster bar Nativ HaHesed, whose portal has returned HTTP 500 since July 2026 (it stays registered and will be enabled when it returns).

**Last nightly check (2026-10-06T13:59:49+00:00): 30/32 reachable.** The check runs from a GitHub-hosted runner outside Israel and fetches every file type of every chain. Daily reachability fluctuates: chains sometimes publish empty or late files, and some small chains publish sporadically — that's the chains' portals, not the library. `geo-blocked` = the portal only answers Israeli IPs (verified through an Israeli proxy). `degraded` = some file types were missing/empty at check time.

| Chain | Status | Stores | Prices | Promos | Note |
|---|---|---|---|---|---|
| `shufersal` | `ok` | 417 | 6611 | 1 |  |
| `super-pharm` | `geo-blocked` | 307 | 9214 | 761 | reachable from Israeli IPs only (verified via proxy) |
| `wolt` | `ok` | 34 | 0 | 588 |  |
| `carrefour` | `ok` | 147 | 9344 | 1265 |  |
| `hatzi-hinam` | `geo-blocked` | 13 | 607 | 511 | reachable from Israeli IPs only (verified via proxy) |
| `rami-levy` | `ok` | 99 | 5272 | 1073 |  |
| `tiv-taam` | `ok` | 54 | 135 | 46 |  |
| `yochananof` | `ok` | 51 | 11763 | 1159 |  |
| `osher-ad` | `ok` | 24 | 6490 | 614 |  |
| `dor-alon` | `ok` | 157 | 4100 | 622 |  |
| `keshet-teamim` | `ok` | 27 | 6296 | 1731 |  |
| `super-cofix` | `degraded` | 34 | — | — | prices: FileNotFound: super-cofix: no PriceFull file | promos: FileNotFound: super-cofix: no PromoFull file |
| `politzer` | `ok` | 8 | 13434 | 1016 |  |
| `stop-market` | `ok` | 12 | 18373 | 2662 |  |
| `fresh-market` | `ok` | 47 | 8291 | 669 |  |
| `salach-dabach` | `ok` | 12 | 12626 | 1757 |  |
| `super-yuda` | `ok` | 26 | 6318 | 372 |  |
| `yellow` | `ok` | 242 | 809 | 669 |  |
| `good-pharm` | `ok` | 82 | 3376 | 290 |  |
| `super-bareket` | `ok` | 15 | 44 | 13 |  |
| `king-store` | `ok` | 48 | 2451 | 299 |  |
| `maayan-2000` | `ok` | 38 | 2685 | 281 |  |
| `meshnat-yosef` | `ok` | 4 | 5508 | 179 |  |
| `shefa-birkat-hashem` | `ok` | 22 | 3622 | 480 |  |
| `shuk-hayir` | `ok` | 26 | 1591 | 0 |  |
| `super-sapir` | `ok` | 72 | 1107 | 66 |  |
| `zol-vebegadol` | `ok` | 34 | 4246 | 492 |  |
| `city-market` | `ok` | 28 | 4364 | 0 |  |
| `victory` | `geo-blocked` | 70 | 8688 | 3812 | reachable from Israeli IPs only (verified via proxy) |
| `mahsanei-hashuk` | `geo-blocked` | 71 | 12409 | 4781 | reachable from Israeli IPs only (verified via proxy) |
| `het-cohen` | `geo-blocked` | 5 | 10696 | 2437 | reachable from Israeli IPs only (verified via proxy) |
| `nativ-hahesed` | `down` | — | — | — | portal still unreachable (PortalError) |
