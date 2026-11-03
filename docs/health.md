# Chain health

**Coverage: 31/32 chains implemented** — the full government roster bar Nativ HaHesed, whose portal has returned HTTP 500 since July 2026 (it stays registered and will be enabled when it returns).

**Last nightly check (2026-11-03T14:53:13+00:00): 28/32 reachable.** The check runs from a GitHub-hosted runner outside Israel and fetches every file type of every chain. Daily reachability fluctuates: chains sometimes publish empty or late files, and some small chains publish sporadically — that's the chains' portals, not the library. `geo-blocked` = the portal only answers Israeli IPs (verified through an Israeli proxy). `degraded` = some file types were missing/empty at check time.

| Chain | Status | Stores | Prices | Promos | Note |
|---|---|---|---|---|---|
| `shufersal` | `ok` | 417 | 6550 | 1 |  |
| `super-pharm` | `down` | — | — | — | stores: FileNotFound: super-pharm: no Stores file | prices: FileNotFound: super-pharm: no PriceFull file | promos: FileNotFound: super-pharm: no PromoFull file |
| `wolt` | `ok` | 37 | 0 | 506 |  |
| `carrefour` | `geo-blocked` | 147 | 11066 | 1694 | reachable from Israeli IPs only (verified via proxy) |
| `hatzi-hinam` | `down` | — | — | — | stores: PortalError: GET https://shop.hazi-hinam.co.il/Prices -> HTTP 403 | prices: PortalError: GET https://shop.hazi-hinam.co.il/Prices -> HTTP 403 | promos: PortalError: GET https://shop.hazi-hinam.co.il/Prices -> HTTP 403 |
| `rami-levy` | `ok` | 99 | 5234 | 1123 |  |
| `tiv-taam` | `ok` | 54 | 56 | 19 |  |
| `yochananof` | `ok` | 51 | 11768 | 1196 |  |
| `osher-ad` | `ok` | 24 | 6105 | 757 |  |
| `dor-alon` | `ok` | 157 | 1071 | 304 |  |
| `keshet-teamim` | `ok` | 28 | 6368 | 1518 |  |
| `super-cofix` | `degraded` | 34 | — | — | prices: FileNotFound: super-cofix: no PriceFull file | promos: FileNotFound: super-cofix: no PromoFull file |
| `politzer` | `ok` | 8 | 15097 | 786 |  |
| `stop-market` | `ok` | 11 | 17520 | 2765 |  |
| `fresh-market` | `ok` | 48 | 8294 | 733 |  |
| `salach-dabach` | `ok` | 12 | 12356 | 1947 |  |
| `super-yuda` | `ok` | 26 | 6422 | 416 |  |
| `yellow` | `ok` | 242 | 1780 | 694 |  |
| `good-pharm` | `ok` | 83 | 3351 | 284 |  |
| `super-bareket` | `ok` | 15 | 4631 | 706 |  |
| `king-store` | `ok` | 48 | 2342 | 256 |  |
| `maayan-2000` | `ok` | 38 | 2906 | 355 |  |
| `meshnat-yosef` | `ok` | 4 | 5452 | 203 |  |
| `shefa-birkat-hashem` | `ok` | 22 | 3575 | 524 |  |
| `shuk-hayir` | `ok` | 26 | 1756 | 0 |  |
| `super-sapir` | `ok` | 132 | 2321 | 0 |  |
| `zol-vebegadol` | `ok` | 35 | 4261 | 421 |  |
| `city-market` | `ok` | 70 | 4294 | 0 |  |
| `victory` | `geo-blocked` | 70 | 7934 | 3106 | reachable from Israeli IPs only (verified via proxy) |
| `mahsanei-hashuk` | `geo-blocked` | 71 | 12366 | 5066 | reachable from Israeli IPs only (verified via proxy) |
| `het-cohen` | `geo-blocked` | 5 | 10753 | 2442 | reachable from Israeli IPs only (verified via proxy) |
| `nativ-hahesed` | `down` | — | — | — | portal still unreachable (PortalError) |
