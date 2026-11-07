# Chain health

**Coverage: 31/32 chains implemented** — the full government roster bar Nativ HaHesed, whose portal has returned HTTP 500 since July 2026 (it stays registered and will be enabled when it returns).

**Last nightly check (2026-11-07T13:46:20+00:00): 30/32 reachable.** The check runs from a GitHub-hosted runner outside Israel and fetches every file type of every chain. Daily reachability fluctuates: chains sometimes publish empty or late files, and some small chains publish sporadically — that's the chains' portals, not the library. `geo-blocked` = the portal only answers Israeli IPs (verified through an Israeli proxy). `degraded` = some file types were missing/empty at check time.

| Chain | Status | Stores | Prices | Promos | Note |
|---|---|---|---|---|---|
| `shufersal` | `ok` | 417 | 6567 | 1 |  |
| `super-pharm` | `geo-blocked` | 307 | 8350 | 763 | reachable from Israeli IPs only (verified via proxy) |
| `wolt` | `ok` | 37 | 5919 | 0 |  |
| `carrefour` | `geo-blocked` | 147 | 11094 | 1680 | reachable from Israeli IPs only (verified via proxy) |
| `hatzi-hinam` | `geo-blocked` | 13 | 605 | 827 | reachable from Israeli IPs only (verified via proxy) |
| `rami-levy` | `ok` | 99 | 13965 | 2394 |  |
| `tiv-taam` | `ok` | 54 | 52 | 17 |  |
| `yochananof` | `ok` | 51 | 11791 | 1338 |  |
| `osher-ad` | `ok` | 24 | 6064 | 743 |  |
| `dor-alon` | `ok` | 157 | 1492 | 325 |  |
| `keshet-teamim` | `ok` | 28 | 6491 | 1527 |  |
| `super-cofix` | `degraded` | 34 | — | — | prices: FileNotFound: super-cofix: no PriceFull file | promos: FileNotFound: super-cofix: no PromoFull file |
| `politzer` | `ok` | 8 | 15134 | 1014 |  |
| `stop-market` | `ok` | 11 | 17549 | 2800 |  |
| `fresh-market` | `ok` | 73 | 9244 | 1494 |  |
| `salach-dabach` | `ok` | 12 | 12355 | 1962 |  |
| `super-yuda` | `ok` | 26 | 4909 | 415 |  |
| `yellow` | `ok` | 242 | 1788 | 731 |  |
| `good-pharm` | `ok` | 84 | 3347 | 288 |  |
| `super-bareket` | `ok` | 15 | 4750 | 694 |  |
| `king-store` | `ok` | 48 | 2355 | 254 |  |
| `maayan-2000` | `ok` | 38 | 3175 | 417 |  |
| `meshnat-yosef` | `ok` | 4 | 5487 | 211 |  |
| `shefa-birkat-hashem` | `ok` | 22 | 4026 | 530 |  |
| `shuk-hayir` | `ok` | 26 | 1911 | 0 |  |
| `super-sapir` | `ok` | 130 | 4 | 1 |  |
| `zol-vebegadol` | `ok` | 35 | 4273 | 475 |  |
| `city-market` | `ok` | 70 | 4264 | 0 |  |
| `victory` | `geo-blocked` | 70 | 8649 | 4413 | reachable from Israeli IPs only (verified via proxy) |
| `mahsanei-hashuk` | `geo-blocked` | 71 | 12412 | 5374 | reachable from Israeli IPs only (verified via proxy) |
| `het-cohen` | `geo-blocked` | 5 | 10771 | 2863 | reachable from Israeli IPs only (verified via proxy) |
| `nativ-hahesed` | `down` | — | — | — | portal still unreachable (PortalError) |
