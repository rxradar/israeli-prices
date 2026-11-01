# Chain health

**Coverage: 31/32 chains implemented** — the full government roster bar Nativ HaHesed, whose portal has returned HTTP 500 since July 2026 (it stays registered and will be enabled when it returns).

**Last nightly check (2026-11-01T14:06:24+00:00): 28/32 reachable.** The check runs from a GitHub-hosted runner outside Israel and fetches every file type of every chain. Daily reachability fluctuates: chains sometimes publish empty or late files, and some small chains publish sporadically — that's the chains' portals, not the library. `geo-blocked` = the portal only answers Israeli IPs (verified through an Israeli proxy). `degraded` = some file types were missing/empty at check time.

| Chain | Status | Stores | Prices | Promos | Note |
|---|---|---|---|---|---|
| `shufersal` | `ok` | 418 | 6542 | 1 |  |
| `super-pharm` | `down` | — | — | — | stores: FileNotFound: super-pharm: no Stores file | prices: FileNotFound: super-pharm: no PriceFull file | promos: FileNotFound: super-pharm: no PromoFull file |
| `wolt` | `ok` | 34 | 0 | 145 |  |
| `carrefour` | `geo-blocked` | 147 | 11062 | 1655 | reachable from Israeli IPs only (verified via proxy) |
| `hatzi-hinam` | `down` | — | — | — | stores: PortalError: GET https://shop.hazi-hinam.co.il/Prices -> HTTP 403 | prices: PortalError: GET https://shop.hazi-hinam.co.il/Prices -> HTTP 403 | promos: PortalError: GET https://shop.hazi-hinam.co.il/Prices -> HTTP 403 |
| `rami-levy` | `ok` | 99 | 5213 | 1053 |  |
| `tiv-taam` | `ok` | 54 | 57 | 19 |  |
| `yochananof` | `ok` | 51 | 11749 | 2176 |  |
| `osher-ad` | `ok` | 24 | 6106 | 534 |  |
| `dor-alon` | `ok` | 157 | 3775 | 638 |  |
| `keshet-teamim` | `ok` | 28 | 14497 | 2337 |  |
| `super-cofix` | `degraded` | 34 | — | — | prices: FileNotFound: super-cofix: no PriceFull file | promos: FileNotFound: super-cofix: no PromoFull file |
| `politzer` | `ok` | 8 | 12234 | 752 |  |
| `stop-market` | `ok` | 11 | 14349 | 1811 |  |
| `fresh-market` | `ok` | 48 | 9191 | 1275 |  |
| `salach-dabach` | `ok` | 12 | 12367 | 1921 |  |
| `super-yuda` | `ok` | 26 | 4919 | 5 |  |
| `yellow` | `ok` | 242 | 1863 | 690 |  |
| `good-pharm` | `ok` | 83 | 3375 | 268 |  |
| `super-bareket` | `ok` | 15 | 4601 | 665 |  |
| `king-store` | `ok` | 48 | 2352 | 306 |  |
| `maayan-2000` | `ok` | 38 | 2768 | 206 |  |
| `meshnat-yosef` | `ok` | 4 | 5441 | 180 |  |
| `shefa-birkat-hashem` | `ok` | 22 | 3828 | 484 |  |
| `shuk-hayir` | `ok` | 26 | 1553 | 0 |  |
| `super-sapir` | `ok` | 130 | 2279 | 0 |  |
| `zol-vebegadol` | `ok` | 35 | 4259 | 368 |  |
| `city-market` | `ok` | 71 | 4298 | 0 |  |
| `victory` | `geo-blocked` | 70 | 9368 | 2312 | reachable from Israeli IPs only (verified via proxy) |
| `mahsanei-hashuk` | `geo-blocked` | 71 | 7874 | 3059 | reachable from Israeli IPs only (verified via proxy) |
| `het-cohen` | `geo-blocked` | 5 | 10719 | 3070 | reachable from Israeli IPs only (verified via proxy) |
| `nativ-hahesed` | `down` | — | — | — | portal still unreachable (PortalError) |
