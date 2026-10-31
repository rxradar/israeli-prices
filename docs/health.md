# Chain health

**Coverage: 31/32 chains implemented** — the full government roster bar Nativ HaHesed, whose portal has returned HTTP 500 since July 2026 (it stays registered and will be enabled when it returns).

**Last nightly check (2026-10-31T13:24:14+00:00): 28/32 reachable.** The check runs from a GitHub-hosted runner outside Israel and fetches every file type of every chain. Daily reachability fluctuates: chains sometimes publish empty or late files, and some small chains publish sporadically — that's the chains' portals, not the library. `geo-blocked` = the portal only answers Israeli IPs (verified through an Israeli proxy). `degraded` = some file types were missing/empty at check time.

| Chain | Status | Stores | Prices | Promos | Note |
|---|---|---|---|---|---|
| `shufersal` | `ok` | 418 | 6554 | 1 |  |
| `super-pharm` | `down` | — | — | — | stores: FileNotFound: super-pharm: no Stores file | prices: FileNotFound: super-pharm: no PriceFull file | promos: FileNotFound: super-pharm: no PromoFull file |
| `wolt` | `ok` | 37 | 0 | 564 |  |
| `carrefour` | `geo-blocked` | 147 | 11070 | 304 | reachable from Israeli IPs only (verified via proxy) |
| `hatzi-hinam` | `down` | — | — | — | stores: PortalError: GET https://shop.hazi-hinam.co.il/Prices -> HTTP 403 | prices: PortalError: GET https://shop.hazi-hinam.co.il/Prices -> HTTP 403 | promos: PortalError: GET https://shop.hazi-hinam.co.il/Prices -> HTTP 403 |
| `rami-levy` | `ok` | 99 | 5218 | 1078 |  |
| `tiv-taam` | `ok` | 54 | 74 | 24 |  |
| `yochananof` | `ok` | 51 | 11766 | 1348 |  |
| `osher-ad` | `ok` | 24 | 6127 | 738 |  |
| `dor-alon` | `ok` | 157 | 1704 | 325 |  |
| `keshet-teamim` | `ok` | 28 | 6467 | 1705 |  |
| `super-cofix` | `degraded` | 34 | — | — | prices: FileNotFound: super-cofix: no PriceFull file | promos: FileNotFound: super-cofix: no PromoFull file |
| `politzer` | `ok` | 8 | 10656 | 1174 |  |
| `stop-market` | `ok` | 11 | 17479 | 3591 |  |
| `fresh-market` | `ok` | 48 | 9205 | 1357 |  |
| `salach-dabach` | `ok` | 12 | 12364 | 1792 |  |
| `super-yuda` | `ok` | 26 | 6802 | 380 |  |
| `yellow` | `ok` | 242 | 1771 | 710 |  |
| `good-pharm` | `ok` | 83 | 3422 | 372 |  |
| `super-bareket` | `ok` | 15 | 4641 | 691 |  |
| `king-store` | `ok` | 48 | 2356 | 311 |  |
| `maayan-2000` | `ok` | 38 | 2977 | 390 |  |
| `meshnat-yosef` | `ok` | 4 | 5454 | 218 |  |
| `shefa-birkat-hashem` | `ok` | 22 | 3914 | 569 |  |
| `shuk-hayir` | `ok` | 26 | 1797 | 0 |  |
| `super-sapir` | `ok` | 130 | 2279 | 0 |  |
| `zol-vebegadol` | `ok` | 35 | 4259 | 486 |  |
| `city-market` | `ok` | 71 | 4269 | 0 |  |
| `victory` | `geo-blocked` | 70 | 8679 | 4387 | reachable from Israeli IPs only (verified via proxy) |
| `mahsanei-hashuk` | `geo-blocked` | 71 | 12342 | 5454 | reachable from Israeli IPs only (verified via proxy) |
| `het-cohen` | `geo-blocked` | 5 | 7214 | 2167 | reachable from Israeli IPs only (verified via proxy) |
| `nativ-hahesed` | `down` | — | — | — | portal still unreachable (PortalError) |
