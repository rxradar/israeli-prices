# Chain health

**Coverage: 31/32 chains implemented** — the full government roster bar Nativ HaHesed, whose portal has returned HTTP 500 since July 2026 (it stays registered and will be enabled when it returns).

**Last nightly check (2026-11-28T15:59:18+00:00): 28/32 reachable.** The check runs from a GitHub-hosted runner outside Israel and fetches every file type of every chain. Daily reachability fluctuates: chains sometimes publish empty or late files, and some small chains publish sporadically — that's the chains' portals, not the library. `geo-blocked` = the portal only answers Israeli IPs (verified through an Israeli proxy). `degraded` = some file types were missing/empty at check time.

| Chain | Status | Stores | Prices | Promos | Note |
|---|---|---|---|---|---|
| `shufersal` | `ok` | 418 | 6504 | 18 |  |
| `super-pharm` | `down` | — | — | — | stores: FileNotFound: super-pharm: no Stores file | prices: FileNotFound: super-pharm: no PriceFull file | promos: FileNotFound: super-pharm: no PromoFull file |
| `wolt` | `ok` | 37 | 0 | 0 |  |
| `carrefour` | `geo-blocked` | 147 | 11113 | 1693 | reachable from Israeli IPs only (verified via proxy) |
| `hatzi-hinam` | `down` | — | — | — | stores: PortalError: GET https://shop.hazi-hinam.co.il/Prices -> HTTP 403 | prices: PortalError: GET https://shop.hazi-hinam.co.il/Prices -> HTTP 403 | promos: PortalError: GET https://shop.hazi-hinam.co.il/Prices -> HTTP 403 |
| `rami-levy` | `ok` | 99 | 13098 | 2656 |  |
| `tiv-taam` | `ok` | 54 | 69 | 27 |  |
| `yochananof` | `ok` | 51 | 11852 | 1436 |  |
| `osher-ad` | `ok` | 24 | 5996 | 885 |  |
| `dor-alon` | `ok` | 157 | 1189 | 334 |  |
| `keshet-teamim` | `ok` | 28 | 6470 | 1524 |  |
| `super-cofix` | `degraded` | 34 | — | — | prices: FileNotFound: super-cofix: no PriceFull file | promos: FileNotFound: super-cofix: no PromoFull file |
| `politzer` | `ok` | 8 | 13921 | 1228 |  |
| `stop-market` | `ok` | 11 | 17579 | 3888 |  |
| `fresh-market` | `ok` | 73 | 9226 | 1768 |  |
| `salach-dabach` | `ok` | 12 | 12276 | 2090 |  |
| `super-yuda` | `ok` | 26 | 4895 | 427 |  |
| `yellow` | `ok` | 242 | 1140 | 712 |  |
| `good-pharm` | `ok` | 85 | 3369 | 356 |  |
| `super-bareket` | `ok` | 15 | 4971 | 356 |  |
| `king-store` | `ok` | 48 | 2309 | 269 |  |
| `maayan-2000` | `ok` | 38 | 3118 | 447 |  |
| `meshnat-yosef` | `ok` | 4 | 5627 | 276 |  |
| `shefa-birkat-hashem` | `ok` | 22 | 4010 | 625 |  |
| `shuk-hayir` | `ok` | 26 | 2024 | 0 |  |
| `super-sapir` | `ok` | 130 | 28 | 1 |  |
| `zol-vebegadol` | `ok` | 35 | 4306 | 513 |  |
| `city-market` | `ok` | 73 | 4112 | 0 |  |
| `victory` | `geo-blocked` | 70 | 8402 | 3693 | reachable from Israeli IPs only (verified via proxy) |
| `mahsanei-hashuk` | `geo-blocked` | 72 | 12484 | 5143 | reachable from Israeli IPs only (verified via proxy) |
| `het-cohen` | `geo-blocked` | 5 | 8978 | 2960 | reachable from Israeli IPs only (verified via proxy) |
| `nativ-hahesed` | `down` | — | — | — | portal still unreachable (PortalError) |
