# Chain health

**Coverage: 31/32 chains implemented** — the full government roster bar Nativ HaHesed, whose portal has returned HTTP 500 since July 2026 (it stays registered and will be enabled when it returns).

**Last nightly check (2026-11-26T17:35:06+00:00): 28/32 reachable.** The check runs from a GitHub-hosted runner outside Israel and fetches every file type of every chain. Daily reachability fluctuates: chains sometimes publish empty or late files, and some small chains publish sporadically — that's the chains' portals, not the library. `geo-blocked` = the portal only answers Israeli IPs (verified through an Israeli proxy). `degraded` = some file types were missing/empty at check time.

| Chain | Status | Stores | Prices | Promos | Note |
|---|---|---|---|---|---|
| `shufersal` | `ok` | 418 | 6522 | 22 |  |
| `super-pharm` | `down` | — | — | — | stores: FileNotFound: super-pharm: no Stores file | prices: FileNotFound: super-pharm: no PriceFull file | promos: FileNotFound: super-pharm: no PromoFull file |
| `wolt` | `ok` | 37 | 6119 | 710 |  |
| `carrefour` | `geo-blocked` | 147 | 12030 | 1722 | reachable from Israeli IPs only (verified via proxy) |
| `hatzi-hinam` | `down` | — | — | — | stores: PortalError: GET https://shop.hazi-hinam.co.il/Prices -> HTTP 403 | prices: PortalError: GET https://shop.hazi-hinam.co.il/Prices -> HTTP 403 | promos: PortalError: GET https://shop.hazi-hinam.co.il/Prices -> HTTP 403 |
| `rami-levy` | `ok` | 99 | 5316 | 1081 |  |
| `tiv-taam` | `ok` | 54 | 69 | 27 |  |
| `yochananof` | `ok` | 51 | 11878 | 2916 |  |
| `osher-ad` | `ok` | 24 | 5915 | 893 |  |
| `dor-alon` | `ok` | 157 | 1850 | 336 |  |
| `keshet-teamim` | `ok` | 28 | 14813 | 2406 |  |
| `super-cofix` | `degraded` | 34 | — | — | prices: FileNotFound: super-cofix: no PriceFull file | promos: FileNotFound: super-cofix: no PromoFull file |
| `politzer` | `ok` | 8 | 13832 | 1233 |  |
| `stop-market` | `ok` | 11 | 17592 | 3884 |  |
| `fresh-market` | `ok` | 73 | 9222 | 187 |  |
| `salach-dabach` | `ok` | 12 | 12295 | 2090 |  |
| `super-yuda` | `ok` | 26 | 6477 | 428 |  |
| `yellow` | `ok` | 242 | 1007 | 742 |  |
| `good-pharm` | `ok` | 85 | 3322 | 347 |  |
| `super-bareket` | `ok` | 15 | 4886 | 732 |  |
| `king-store` | `ok` | 48 | 2322 | 265 |  |
| `maayan-2000` | `ok` | 38 | 2882 | 428 |  |
| `meshnat-yosef` | `ok` | 4 | 5590 | 271 |  |
| `shefa-birkat-hashem` | `ok` | 22 | 3665 | 593 |  |
| `shuk-hayir` | `ok` | 26 | 1777 | 0 |  |
| `super-sapir` | `ok` | 130 | 28 | 1 |  |
| `zol-vebegadol` | `ok` | 35 | 4309 | 514 |  |
| `city-market` | `ok` | 70 | 4179 | 0 |  |
| `victory` | `geo-blocked` | 70 | 8748 | 4322 | reachable from Israeli IPs only (verified via proxy) |
| `mahsanei-hashuk` | `geo-blocked` | 72 | 12500 | 6631 | reachable from Israeli IPs only (verified via proxy) |
| `het-cohen` | `geo-blocked` | 5 | 8953 | 2644 | reachable from Israeli IPs only (verified via proxy) |
| `nativ-hahesed` | `down` | — | — | — | portal still unreachable (PortalError) |
