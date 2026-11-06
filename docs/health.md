# Chain health

**Coverage: 31/32 chains implemented** — the full government roster bar Nativ HaHesed, whose portal has returned HTTP 500 since July 2026 (it stays registered and will be enabled when it returns).

**Last nightly check (2026-11-06T14:49:32+00:00): 30/32 reachable.** The check runs from a GitHub-hosted runner outside Israel and fetches every file type of every chain. Daily reachability fluctuates: chains sometimes publish empty or late files, and some small chains publish sporadically — that's the chains' portals, not the library. `geo-blocked` = the portal only answers Israeli IPs (verified through an Israeli proxy). `degraded` = some file types were missing/empty at check time.

| Chain | Status | Stores | Prices | Promos | Note |
|---|---|---|---|---|---|
| `shufersal` | `ok` | 417 | 6572 | 1 |  |
| `super-pharm` | `geo-blocked` | 307 | 9571 | 605 | reachable from Israeli IPs only (verified via proxy) |
| `wolt` | `ok` | 37 | 5180 | 649 |  |
| `carrefour` | `geo-blocked` | 147 | 11094 | 1713 | reachable from Israeli IPs only (verified via proxy) |
| `hatzi-hinam` | `geo-blocked` | 13 | 608 | 827 | reachable from Israeli IPs only (verified via proxy) |
| `rami-levy` | `ok` | 99 | 5291 | 1078 |  |
| `tiv-taam` | `ok` | 54 | 52 | 17 |  |
| `yochananof` | `ok` | 51 | 11793 | 2682 |  |
| `osher-ad` | `ok` | 24 | 6064 | 751 |  |
| `dor-alon` | `ok` | 157 | 1792 | 326 |  |
| `keshet-teamim` | `ok` | 28 | 6420 | 1527 |  |
| `super-cofix` | `degraded` | 34 | — | — | prices: FileNotFound: super-cofix: no PriceFull file | promos: FileNotFound: super-cofix: no PromoFull file |
| `politzer` | `ok` | 8 | 15105 | 1045 |  |
| `stop-market` | `ok` | 11 | 14305 | 2779 |  |
| `fresh-market` | `ok` | 73 | 8305 | 764 |  |
| `salach-dabach` | `ok` | 12 | 12341 | 1961 |  |
| `super-yuda` | `ok` | 26 | 6417 | 416 |  |
| `yellow` | `ok` | 242 | 1887 | 685 |  |
| `good-pharm` | `ok` | 83 | 3314 | 286 |  |
| `super-bareket` | `ok` | 15 | 4688 | 718 |  |
| `king-store` | `ok` | 48 | 2335 | 252 |  |
| `maayan-2000` | `ok` | 38 | 2990 | 396 |  |
| `meshnat-yosef` | `ok` | 4 | 5493 | 211 |  |
| `shefa-birkat-hashem` | `ok` | 22 | 3915 | 565 |  |
| `shuk-hayir` | `ok` | 26 | 1834 | 0 |  |
| `super-sapir` | `ok` | 130 | 2330 | 1 |  |
| `zol-vebegadol` | `ok` | 35 | 4284 | 472 |  |
| `city-market` | `ok` | 70 | 4265 | 0 |  |
| `victory` | `geo-blocked` | 70 | 8648 | 4417 | reachable from Israeli IPs only (verified via proxy) |
| `mahsanei-hashuk` | `geo-blocked` | 71 | 12438 | 5452 | reachable from Israeli IPs only (verified via proxy) |
| `het-cohen` | `geo-blocked` | 5 | 8939 | 2559 | reachable from Israeli IPs only (verified via proxy) |
| `nativ-hahesed` | `down` | — | — | — | portal still unreachable (PortalError) |
