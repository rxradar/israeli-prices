# Chain health

**Coverage: 31/32 chains implemented** — the full government roster bar Nativ HaHesed, whose portal has returned HTTP 500 since July 2026 (it stays registered and will be enabled when it returns).

**Last nightly check (2026-10-17T11:27:19+00:00): 28/32 reachable.** The check runs from a GitHub-hosted runner outside Israel and fetches every file type of every chain. Daily reachability fluctuates: chains sometimes publish empty or late files, and some small chains publish sporadically — that's the chains' portals, not the library. `geo-blocked` = the portal only answers Israeli IPs (verified through an Israeli proxy). `degraded` = some file types were missing/empty at check time.

| Chain | Status | Stores | Prices | Promos | Note |
|---|---|---|---|---|---|
| `shufersal` | `ok` | 417 | 6581 | 1 |  |
| `super-pharm` | `down` | — | — | — | stores: FileNotFound: super-pharm: no Stores file | prices: FileNotFound: super-pharm: no PriceFull file | promos: FileNotFound: super-pharm: no PromoFull file |
| `wolt` | `ok` | 34 | 4 | 521 |  |
| `carrefour` | `ok` | 147 | 11135 | 1565 |  |
| `hatzi-hinam` | `down` | — | — | — | stores: PortalError: GET https://shop.hazi-hinam.co.il/Prices -> HTTP 403 | prices: PortalError: GET https://shop.hazi-hinam.co.il/Prices -> HTTP 403 | promos: PortalError: GET https://shop.hazi-hinam.co.il/Prices -> HTTP 403 |
| `rami-levy` | `ok` | 99 | 5222 | 1069 |  |
| `tiv-taam` | `ok` | 54 | 125 | 40 |  |
| `yochananof` | `ok` | 51 | 11775 | 1269 |  |
| `osher-ad` | `ok` | 24 | 6364 | 678 |  |
| `dor-alon` | `ok` | 158 | 1200 | 313 |  |
| `keshet-teamim` | `ok` | 28 | 6449 | 1695 |  |
| `super-cofix` | `degraded` | 34 | — | — | prices: FileNotFound: super-cofix: no PriceFull file | promos: FileNotFound: super-cofix: no PromoFull file |
| `politzer` | `ok` | 8 | 10693 | 1195 |  |
| `stop-market` | `ok` | 11 | 17468 | 2705 |  |
| `fresh-market` | `ok` | 46 | 8283 | 696 |  |
| `salach-dabach` | `ok` | 12 | 12482 | 1794 |  |
| `super-yuda` | `ok` | 26 | 4901 | 381 |  |
| `yellow` | `ok` | 242 | 1883 | 712 |  |
| `good-pharm` | `ok` | 82 | 3439 | 346 |  |
| `super-bareket` | `ok` | 15 | 3955 | 615 |  |
| `king-store` | `ok` | 48 | 2359 | 309 |  |
| `maayan-2000` | `ok` | 38 | 2946 | 371 |  |
| `meshnat-yosef` | `ok` | 4 | 5446 | 206 |  |
| `shefa-birkat-hashem` | `ok` | 22 | 3953 | 543 |  |
| `shuk-hayir` | `ok` | 26 | 2130 | 0 |  |
| `super-sapir` | `ok` | 73 | 1189 | 79 |  |
| `zol-vebegadol` | `ok` | 35 | 4285 | 487 |  |
| `city-market` | `ok` | 28 | 4315 | 0 |  |
| `victory` | `geo-blocked` | 70 | 8725 | 4481 | reachable from Israeli IPs only (verified via proxy) |
| `mahsanei-hashuk` | `geo-blocked` | 71 | 12354 | 5953 | reachable from Israeli IPs only (verified via proxy) |
| `het-cohen` | `geo-blocked` | 5 | 10697 | 2748 | reachable from Israeli IPs only (verified via proxy) |
| `nativ-hahesed` | `down` | — | — | — | portal still unreachable (PortalError) |
