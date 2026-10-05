# Chain health

**Coverage: 31/32 chains implemented** — the full government roster bar Nativ HaHesed, whose portal has returned HTTP 500 since July 2026 (it stays registered and will be enabled when it returns).

**Last nightly check (2026-10-05T15:38:13+00:00): 30/32 reachable.** The check runs from a GitHub-hosted runner outside Israel and fetches every file type of every chain. Daily reachability fluctuates: chains sometimes publish empty or late files, and some small chains publish sporadically — that's the chains' portals, not the library. `geo-blocked` = the portal only answers Israeli IPs (verified through an Israeli proxy). `degraded` = some file types were missing/empty at check time.

| Chain | Status | Stores | Prices | Promos | Note |
|---|---|---|---|---|---|
| `shufersal` | `ok` | 417 | 6616 | 1 |  |
| `super-pharm` | `geo-blocked` | 307 | 9072 | 800 | reachable from Israeli IPs only (verified via proxy) |
| `wolt` | `ok` | 34 | 5983 | 0 |  |
| `carrefour` | `ok` | 147 | 11174 | 1417 |  |
| `hatzi-hinam` | `geo-blocked` | 13 | 9813 | 546 | reachable from Israeli IPs only (verified via proxy) |
| `rami-levy` | `ok` | 99 | 5277 | 1039 |  |
| `tiv-taam` | `ok` | 54 | 135 | 46 |  |
| `yochananof` | `ok` | 51 | 11762 | 1040 |  |
| `osher-ad` | `ok` | 24 | 6498 | 565 |  |
| `dor-alon` | `ok` | 157 | 1713 | 313 |  |
| `keshet-teamim` | `ok` | 27 | 6328 | 1676 |  |
| `super-cofix` | `degraded` | 34 | — | — | prices: FileNotFound: super-cofix: no PriceFull file | promos: FileNotFound: super-cofix: no PromoFull file |
| `politzer` | `ok` | 8 | 13571 | 969 |  |
| `stop-market` | `ok` | 11 | 17478 | 2661 |  |
| `fresh-market` | `ok` | 47 | 4690 | 829 |  |
| `salach-dabach` | `ok` | 12 | 12632 | 1753 |  |
| `super-yuda` | `ok` | 26 | 6390 | 371 |  |
| `yellow` | `ok` | 242 | 855 | 683 |  |
| `good-pharm` | `ok` | 82 | 3389 | 289 |  |
| `super-bareket` | `ok` | 14 | 6547 | 821 |  |
| `king-store` | `ok` | 19 | 1114 | 295 |  |
| `maayan-2000` | `ok` | 38 | 2639 | 274 |  |
| `meshnat-yosef` | `ok` | 4 | 5519 | 171 |  |
| `shefa-birkat-hashem` | `ok` | 22 | 3639 | 428 |  |
| `shuk-hayir` | `ok` | 26 | 1681 | 0 |  |
| `super-sapir` | `ok` | 72 | 1078 | 63 |  |
| `zol-vebegadol` | `ok` | 35 | 3800 | 1118 |  |
| `city-market` | `ok` | 28 | 2907 | 180 |  |
| `victory` | `geo-blocked` | 70 | 8681 | 3872 | reachable from Israeli IPs only (verified via proxy) |
| `mahsanei-hashuk` | `geo-blocked` | 71 | 12413 | 4674 | reachable from Israeli IPs only (verified via proxy) |
| `het-cohen` | `geo-blocked` | 5 | 10704 | 2376 | reachable from Israeli IPs only (verified via proxy) |
| `nativ-hahesed` | `down` | — | — | — | portal still unreachable (PortalError) |
