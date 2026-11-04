# Chain health

**Coverage: 31/32 chains implemented** — the full government roster bar Nativ HaHesed, whose portal has returned HTTP 500 since July 2026 (it stays registered and will be enabled when it returns).

**Last nightly check (2026-11-04T15:12:09+00:00): 29/32 reachable.** The check runs from a GitHub-hosted runner outside Israel and fetches every file type of every chain. Daily reachability fluctuates: chains sometimes publish empty or late files, and some small chains publish sporadically — that's the chains' portals, not the library. `geo-blocked` = the portal only answers Israeli IPs (verified through an Israeli proxy). `degraded` = some file types were missing/empty at check time.

| Chain | Status | Stores | Prices | Promos | Note |
|---|---|---|---|---|---|
| `shufersal` | `ok` | 417 | 6551 | 1 |  |
| `super-pharm` | `geo-blocked` | 307 | 9122 | 834 | reachable from Israeli IPs only (verified via proxy) |
| `wolt` | `ok` | 37 | 0 | 0 |  |
| `carrefour` | `geo-blocked` | 147 | 11078 | 1672 | reachable from Israeli IPs only (verified via proxy) |
| `hatzi-hinam` | `down` | — | — | — | stores: PortalError: GET https://shop.hazi-hinam.co.il/Prices -> HTTP 403 | prices: PortalError: GET https://shop.hazi-hinam.co.il/Prices -> HTTP 403 | promos: PortalError: GET https://shop.hazi-hinam.co.il/Prices -> HTTP 403 |
| `rami-levy` | `ok` | 99 | 5259 | 1101 |  |
| `tiv-taam` | `ok` | 54 | 56 | 19 |  |
| `yochananof` | `ok` | 51 | 11775 | 1226 |  |
| `osher-ad` | `ok` | 24 | 6099 | 754 |  |
| `dor-alon` | `ok` | 157 | 3787 | 638 |  |
| `keshet-teamim` | `ok` | 28 | 8711 | 1534 |  |
| `super-cofix` | `degraded` | 34 | — | — | prices: FileNotFound: super-cofix: no PriceFull file | promos: FileNotFound: super-cofix: no PromoFull file |
| `politzer` | `ok` | 8 | 12245 | 922 |  |
| `stop-market` | `ok` | 11 | 17524 | 2784 |  |
| `fresh-market` | `ok` | 73 | 8306 | 743 |  |
| `salach-dabach` | `ok` | 12 | 12342 | 1955 |  |
| `super-yuda` | `ok` | 26 | 6676 | 415 |  |
| `yellow` | `ok` | 242 | 1871 | 683 |  |
| `good-pharm` | `ok` | 83 | 3335 | 285 |  |
| `super-bareket` | `ok` | 15 | 4665 | 705 |  |
| `king-store` | `ok` | 48 | 2342 | 258 |  |
| `maayan-2000` | `ok` | 38 | 2927 | 381 |  |
| `meshnat-yosef` | `ok` | 4 | 5457 | 204 |  |
| `shefa-birkat-hashem` | `ok` | 22 | 3648 | 545 |  |
| `shuk-hayir` | `ok` | 26 | 1772 | 0 |  |
| `super-sapir` | `ok` | 130 | 2322 | 1 |  |
| `zol-vebegadol` | `ok` | 35 | 4258 | 409 |  |
| `city-market` | `ok` | 70 | 4292 | 0 |  |
| `victory` | `geo-blocked` | 70 | 9939 | 3890 | reachable from Israeli IPs only (verified via proxy) |
| `mahsanei-hashuk` | `geo-blocked` | 71 | 12397 | 5284 | reachable from Israeli IPs only (verified via proxy) |
| `het-cohen` | `geo-blocked` | 5 | 7216 | 2806 | reachable from Israeli IPs only (verified via proxy) |
| `nativ-hahesed` | `down` | — | — | — | portal still unreachable (PortalError) |
