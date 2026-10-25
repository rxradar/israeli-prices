# Chain health

**Coverage: 31/32 chains implemented** — the full government roster bar Nativ HaHesed, whose portal has returned HTTP 500 since July 2026 (it stays registered and will be enabled when it returns).

**Last nightly check (2026-10-25T12:23:19+00:00): 28/32 reachable.** The check runs from a GitHub-hosted runner outside Israel and fetches every file type of every chain. Daily reachability fluctuates: chains sometimes publish empty or late files, and some small chains publish sporadically — that's the chains' portals, not the library. `geo-blocked` = the portal only answers Israeli IPs (verified through an Israeli proxy). `degraded` = some file types were missing/empty at check time.

| Chain | Status | Stores | Prices | Promos | Note |
|---|---|---|---|---|---|
| `shufersal` | `ok` | 416 | 6562 | 1 |  |
| `super-pharm` | `down` | — | — | — | stores: FileNotFound: super-pharm: no Stores file | prices: FileNotFound: super-pharm: no PriceFull file | promos: FileNotFound: super-pharm: no PromoFull file |
| `wolt` | `ok` | 34 | 5185 | 472 |  |
| `carrefour` | `geo-blocked` | 147 | 11090 | 1664 | reachable from Israeli IPs only (verified via proxy) |
| `hatzi-hinam` | `down` | — | — | — | stores: PortalError: GET https://shop.hazi-hinam.co.il/Prices -> HTTP 403 | prices: PortalError: GET https://shop.hazi-hinam.co.il/Prices -> HTTP 403 | promos: PortalError: GET https://shop.hazi-hinam.co.il/Prices -> HTTP 403 |
| `rami-levy` | `ok` | 99 | 5207 | 1078 |  |
| `tiv-taam` | `ok` | 54 | 125 | 41 |  |
| `yochananof` | `ok` | 51 | 11743 | 1332 |  |
| `osher-ad` | `ok` | 24 | 6244 | 717 |  |
| `dor-alon` | `ok` | 157 | 5336 | 638 |  |
| `keshet-teamim` | `ok` | 28 | 6347 | 1696 |  |
| `super-cofix` | `degraded` | 34 | — | — | prices: FileNotFound: super-cofix: no PriceFull file | promos: FileNotFound: super-cofix: no PromoFull file |
| `politzer` | `ok` | 8 | 13974 | 1204 |  |
| `stop-market` | `ok` | 11 | 18268 | 2737 |  |
| `fresh-market` | `ok` | 46 | 7902 | 1350 |  |
| `salach-dabach` | `ok` | 12 | 16794 | 1771 |  |
| `super-yuda` | `ok` | 26 | 6392 | 0 |  |
| `yellow` | `ok` | 242 | 1784 | 655 |  |
| `good-pharm` | `ok` | 83 | 3398 | 353 |  |
| `super-bareket` | `ok` | 15 | 4475 | 672 |  |
| `king-store` | `ok` | 48 | 2353 | 296 |  |
| `maayan-2000` | `ok` | 38 | 2728 | 369 |  |
| `meshnat-yosef` | `ok` | 4 | 5389 | 213 |  |
| `shefa-birkat-hashem` | `ok` | 22 | 3769 | 563 |  |
| `shuk-hayir` | `ok` | 26 | 1673 | 0 |  |
| `super-sapir` | `ok` | 130 | 2189 | 0 |  |
| `zol-vebegadol` | `ok` | 35 | 4282 | 489 |  |
| `city-market` | `ok` | 71 | 4323 | 0 |  |
| `victory` | `geo-blocked` | 70 | 10611 | 4218 | reachable from Israeli IPs only (verified via proxy) |
| `mahsanei-hashuk` | `geo-blocked` | 71 | 12325 | 6001 | reachable from Israeli IPs only (verified via proxy) |
| `het-cohen` | `geo-blocked` | 5 | 10693 | 2773 | reachable from Israeli IPs only (verified via proxy) |
| `nativ-hahesed` | `down` | — | — | — | portal still unreachable (PortalError) |
