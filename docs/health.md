# Chain health

**Coverage: 31/32 chains implemented** — the full government roster bar Nativ HaHesed, whose portal has returned HTTP 500 since July 2026 (it stays registered and will be enabled when it returns).

**Last nightly check (2026-10-23T12:28:05+00:00): 28/32 reachable.** The check runs from a GitHub-hosted runner outside Israel and fetches every file type of every chain. Daily reachability fluctuates: chains sometimes publish empty or late files, and some small chains publish sporadically — that's the chains' portals, not the library. `geo-blocked` = the portal only answers Israeli IPs (verified through an Israeli proxy). `degraded` = some file types were missing/empty at check time.

| Chain | Status | Stores | Prices | Promos | Note |
|---|---|---|---|---|---|
| `shufersal` | `ok` | 417 | 6569 | 1 |  |
| `super-pharm` | `down` | — | — | — | stores: FileNotFound: super-pharm: no Stores file | prices: FileNotFound: super-pharm: no PriceFull file | promos: FileNotFound: super-pharm: no PromoFull file |
| `wolt` | `ok` | 34 | 5943 | 0 |  |
| `carrefour` | `geo-blocked` | 147 | 11090 | 1674 | reachable from Israeli IPs only (verified via proxy) |
| `hatzi-hinam` | `down` | — | — | — | stores: PortalError: GET https://shop.hazi-hinam.co.il/Prices -> HTTP 403 | prices: PortalError: GET https://shop.hazi-hinam.co.il/Prices -> HTTP 403 | promos: PortalError: GET https://shop.hazi-hinam.co.il/Prices -> HTTP 403 |
| `rami-levy` | `ok` | 99 | 5214 | 1078 |  |
| `tiv-taam` | `ok` | 54 | 125 | 41 |  |
| `yochananof` | `ok` | 51 | 11770 | 1340 |  |
| `osher-ad` | `ok` | 24 | 6260 | 718 |  |
| `dor-alon` | `ok` | 157 | 1490 | 325 |  |
| `keshet-teamim` | `ok` | 28 | 6347 | 1696 |  |
| `super-cofix` | `degraded` | 34 | — | — | prices: FileNotFound: super-cofix: no PriceFull file | promos: FileNotFound: super-cofix: no PromoFull file |
| `politzer` | `ok` | 8 | 13955 | 1197 |  |
| `stop-market` | `ok` | 11 | 10667 | 2738 |  |
| `fresh-market` | `ok` | 46 | 9181 | 1361 |  |
| `salach-dabach` | `ok` | 12 | 12411 | 1803 |  |
| `super-yuda` | `ok` | 26 | 6389 | 0 |  |
| `yellow` | `ok` | 242 | 1875 | 657 |  |
| `good-pharm` | `ok` | 83 | 3408 | 352 |  |
| `super-bareket` | `ok` | 15 | 4410 | 694 |  |
| `king-store` | `ok` | 48 | 2358 | 297 |  |
| `maayan-2000` | `ok` | 38 | 2775 | 370 |  |
| `meshnat-yosef` | `ok` | 4 | 5377 | 215 |  |
| `shefa-birkat-hashem` | `ok` | 22 | 3701 | 560 |  |
| `shuk-hayir` | `ok` | 26 | 1707 | 0 |  |
| `super-sapir` | `ok` | 130 | 2183 | 0 |  |
| `zol-vebegadol` | `ok` | 35 | 4283 | 490 |  |
| `city-market` | `ok` | 71 | 4278 | 0 |  |
| `victory` | `geo-blocked` | 70 | 8711 | 4365 | reachable from Israeli IPs only (verified via proxy) |
| `mahsanei-hashuk` | `geo-blocked` | 71 | 8789 | 3953 | reachable from Israeli IPs only (verified via proxy) |
| `het-cohen` | `geo-blocked` | 5 | 10716 | 2799 | reachable from Israeli IPs only (verified via proxy) |
| `nativ-hahesed` | `down` | — | — | — | portal still unreachable (PortalError) |
