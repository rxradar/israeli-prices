# Chain health

**Coverage: 31/32 chains implemented** — the full government roster bar Nativ HaHesed, whose portal has returned HTTP 500 since July 2026 (it stays registered and will be enabled when it returns).

**Last nightly check (2026-10-22T12:49:34+00:00): 28/32 reachable.** The check runs from a GitHub-hosted runner outside Israel and fetches every file type of every chain. Daily reachability fluctuates: chains sometimes publish empty or late files, and some small chains publish sporadically — that's the chains' portals, not the library. `geo-blocked` = the portal only answers Israeli IPs (verified through an Israeli proxy). `degraded` = some file types were missing/empty at check time.

| Chain | Status | Stores | Prices | Promos | Note |
|---|---|---|---|---|---|
| `shufersal` | `ok` | 417 | 6566 | 1 |  |
| `super-pharm` | `down` | — | — | — | stores: FileNotFound: super-pharm: no Stores file | prices: FileNotFound: super-pharm: no PriceFull file | promos: FileNotFound: super-pharm: no PromoFull file |
| `wolt` | `ok` | 34 | 6010 | 518 |  |
| `carrefour` | `geo-blocked` | 147 | 11096 | 1664 | reachable from Israeli IPs only (verified via proxy) |
| `hatzi-hinam` | `down` | — | — | — | stores: PortalError: GET https://shop.hazi-hinam.co.il/Prices -> HTTP 403 | prices: PortalError: GET https://shop.hazi-hinam.co.il/Prices -> HTTP 403 | promos: PortalError: GET https://shop.hazi-hinam.co.il/Prices -> HTTP 403 |
| `rami-levy` | `ok` | 99 | 5205 | 1077 |  |
| `tiv-taam` | `ok` | 54 | 125 | 40 |  |
| `yochananof` | `ok` | 51 | 11759 | 2666 |  |
| `osher-ad` | `ok` | 24 | 6282 | 718 |  |
| `dor-alon` | `ok` | 157 | 3238 | 356 |  |
| `keshet-teamim` | `ok` | 28 | 6347 | 1696 |  |
| `super-cofix` | `degraded` | 34 | — | — | prices: FileNotFound: super-cofix: no PriceFull file | promos: FileNotFound: super-cofix: no PromoFull file |
| `politzer` | `ok` | 8 | 13571 | 1197 |  |
| `stop-market` | `ok` | 11 | 18366 | 2738 |  |
| `fresh-market` | `ok` | 46 | 9175 | 1361 |  |
| `salach-dabach` | `ok` | 12 | 12425 | 1799 |  |
| `super-yuda` | `ok` | 26 | 6391 | 0 |  |
| `yellow` | `ok` | 242 | 1892 | 709 |  |
| `good-pharm` | `ok` | 83 | 3403 | 351 |  |
| `super-bareket` | `ok` | 15 | 4307 | 675 |  |
| `king-store` | `ok` | 48 | 2338 | 296 |  |
| `maayan-2000` | `ok` | 38 | 2733 | 364 |  |
| `meshnat-yosef` | `ok` | 4 | 5358 | 214 |  |
| `shefa-birkat-hashem` | `ok` | 22 | 3489 | 543 |  |
| `shuk-hayir` | `ok` | 26 | 1531 | 0 |  |
| `super-sapir` | `ok` | 130 | 2163 | 0 |  |
| `zol-vebegadol` | `ok` | 35 | 4280 | 490 |  |
| `city-market` | `ok` | 71 | 4321 | 0 |  |
| `victory` | `geo-blocked` | 70 | 8710 | 4367 | reachable from Israeli IPs only (verified via proxy) |
| `mahsanei-hashuk` | `geo-blocked` | 71 | 12392 | 6003 | reachable from Israeli IPs only (verified via proxy) |
| `het-cohen` | `geo-blocked` | 5 | 10710 | 2792 | reachable from Israeli IPs only (verified via proxy) |
| `nativ-hahesed` | `down` | — | — | — | portal still unreachable (PortalError) |
