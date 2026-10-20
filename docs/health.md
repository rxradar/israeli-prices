# Chain health

**Coverage: 31/32 chains implemented** — the full government roster bar Nativ HaHesed, whose portal has returned HTTP 500 since July 2026 (it stays registered and will be enabled when it returns).

**Last nightly check (2026-10-20T12:34:55+00:00): 28/32 reachable.** The check runs from a GitHub-hosted runner outside Israel and fetches every file type of every chain. Daily reachability fluctuates: chains sometimes publish empty or late files, and some small chains publish sporadically — that's the chains' portals, not the library. `geo-blocked` = the portal only answers Israeli IPs (verified through an Israeli proxy). `degraded` = some file types were missing/empty at check time.

| Chain | Status | Stores | Prices | Promos | Note |
|---|---|---|---|---|---|
| `shufersal` | `ok` | 417 | 6572 | 1 |  |
| `super-pharm` | `down` | — | — | — | stores: FileNotFound: super-pharm: no Stores file | prices: FileNotFound: super-pharm: no PriceFull file | promos: FileNotFound: super-pharm: no PromoFull file |
| `wolt` | `ok` | 34 | 5838 | 0 |  |
| `carrefour` | `ok` | 147 | 10312 | 1535 |  |
| `hatzi-hinam` | `down` | — | — | — | stores: PortalError: GET https://shop.hazi-hinam.co.il/Prices -> HTTP 403 | prices: PortalError: GET https://shop.hazi-hinam.co.il/Prices -> HTTP 403 | promos: PortalError: GET https://shop.hazi-hinam.co.il/Prices -> HTTP 403 |
| `rami-levy` | `ok` | 99 | 5205 | 1093 |  |
| `tiv-taam` | `ok` | 54 | 125 | 40 |  |
| `yochananof` | `ok` | 51 | 11763 | 1354 |  |
| `osher-ad` | `ok` | 24 | 6308 | 695 |  |
| `dor-alon` | `ok` | 158 | 7495 | 946 |  |
| `keshet-teamim` | `ok` | 28 | 6356 | 1694 |  |
| `super-cofix` | `degraded` | 34 | — | — | prices: FileNotFound: super-cofix: no PriceFull file | promos: FileNotFound: super-cofix: no PromoFull file |
| `politzer` | `ok` | 8 | 12176 | 1195 |  |
| `stop-market` | `ok` | 11 | 10677 | 2721 |  |
| `fresh-market` | `ok` | 46 | 8236 | 698 |  |
| `salach-dabach` | `ok` | 12 | 12450 | 1793 |  |
| `super-yuda` | `ok` | 26 | 6412 | 381 |  |
| `yellow` | `ok` | 242 | 1874 | 710 |  |
| `good-pharm` | `ok` | 83 | 3401 | 354 |  |
| `super-bareket` | `ok` | 15 | 4159 | 665 |  |
| `king-store` | `ok` | 48 | 2341 | 302 |  |
| `maayan-2000` | `ok` | 38 | 2723 | 359 |  |
| `meshnat-yosef` | `ok` | 4 | 5391 | 209 |  |
| `shefa-birkat-hashem` | `ok` | 22 | 3736 | 557 |  |
| `shuk-hayir` | `ok` | 26 | 1620 | 0 |  |
| `super-sapir` | `ok` | 130 | 1205 | 0 |  |
| `zol-vebegadol` | `ok` | 35 | 4282 | 502 |  |
| `city-market` | `ok` | 71 | 4338 | 0 |  |
| `victory` | `geo-blocked` | 70 | 8712 | 4452 | reachable from Israeli IPs only (verified via proxy) |
| `mahsanei-hashuk` | `geo-blocked` | 71 | 12395 | 6082 | reachable from Israeli IPs only (verified via proxy) |
| `het-cohen` | `geo-blocked` | 5 | 8941 | 2471 | reachable from Israeli IPs only (verified via proxy) |
| `nativ-hahesed` | `down` | — | — | — | portal still unreachable (PortalError) |
