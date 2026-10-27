# Chain health

**Coverage: 31/32 chains implemented** — the full government roster bar Nativ HaHesed, whose portal has returned HTTP 500 since July 2026 (it stays registered and will be enabled when it returns).

**Last nightly check (2026-10-27T13:01:37+00:00): 28/32 reachable.** The check runs from a GitHub-hosted runner outside Israel and fetches every file type of every chain. Daily reachability fluctuates: chains sometimes publish empty or late files, and some small chains publish sporadically — that's the chains' portals, not the library. `geo-blocked` = the portal only answers Israeli IPs (verified through an Israeli proxy). `degraded` = some file types were missing/empty at check time.

| Chain | Status | Stores | Prices | Promos | Note |
|---|---|---|---|---|---|
| `shufersal` | `ok` | 418 | 6567 | 1 |  |
| `super-pharm` | `down` | — | — | — | stores: FileNotFound: super-pharm: no Stores file | prices: FileNotFound: super-pharm: no PriceFull file | promos: FileNotFound: super-pharm: no PromoFull file |
| `wolt` | `ok` | 34 | 5977 | 0 |  |
| `carrefour` | `geo-blocked` | 147 | 11075 | 1701 | reachable from Israeli IPs only (verified via proxy) |
| `hatzi-hinam` | `down` | — | — | — | stores: PortalError: GET https://shop.hazi-hinam.co.il/Prices -> HTTP 403 | prices: PortalError: GET https://shop.hazi-hinam.co.il/Prices -> HTTP 403 | promos: PortalError: GET https://shop.hazi-hinam.co.il/Prices -> HTTP 403 |
| `rami-levy` | `ok` | 99 | 5215 | 1106 |  |
| `tiv-taam` | `ok` | 54 | 125 | 41 |  |
| `yochananof` | `ok` | 51 | 11761 | 2782 |  |
| `osher-ad` | `ok` | 24 | 6201 | 731 |  |
| `dor-alon` | `ok` | 157 | 3235 | 357 |  |
| `keshet-teamim` | `ok` | 28 | 6347 | 1695 |  |
| `super-cofix` | `degraded` | 34 | — | — | prices: FileNotFound: super-cofix: no PriceFull file | promos: FileNotFound: super-cofix: no PromoFull file |
| `politzer` | `ok` | 8 | 15081 | 1202 |  |
| `stop-market` | `ok` | 11 | 18361 | 2737 |  |
| `fresh-market` | `ok` | 46 | 8250 | 706 |  |
| `salach-dabach` | `ok` | 12 | 12385 | 1792 |  |
| `super-yuda` | `ok` | 26 | 6392 | 380 |  |
| `yellow` | `ok` | 242 | 1605 | 685 |  |
| `good-pharm` | `ok` | 83 | 3362 | 347 |  |
| `super-bareket` | `ok` | 15 | 4541 | 685 |  |
| `king-store` | `ok` | 48 | 2344 | 299 |  |
| `maayan-2000` | `ok` | 38 | 2730 | 380 |  |
| `meshnat-yosef` | `ok` | 4 | 5412 | 214 |  |
| `shefa-birkat-hashem` | `ok` | 22 | 3803 | 587 |  |
| `shuk-hayir` | `ok` | 26 | 1660 | 0 |  |
| `super-sapir` | `ok` | 130 | 2232 | 0 |  |
| `zol-vebegadol` | `ok` | 35 | 4278 | 503 |  |
| `city-market` | `ok` | 71 | 4317 | 0 |  |
| `victory` | `geo-blocked` | 70 | 9989 | 4530 | reachable from Israeli IPs only (verified via proxy) |
| `mahsanei-hashuk` | `geo-blocked` | 71 | 12372 | 6132 | reachable from Israeli IPs only (verified via proxy) |
| `het-cohen` | `geo-blocked` | 5 | 7193 | 2873 | reachable from Israeli IPs only (verified via proxy) |
| `nativ-hahesed` | `down` | — | — | — | portal still unreachable (PortalError) |
