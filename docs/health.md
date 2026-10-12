# Chain health

**Coverage: 31/32 chains implemented** — the full government roster bar Nativ HaHesed, whose portal has returned HTTP 500 since July 2026 (it stays registered and will be enabled when it returns).

**Last nightly check (2026-10-12T16:33:32+00:00): 30/32 reachable.** The check runs from a GitHub-hosted runner outside Israel and fetches every file type of every chain. Daily reachability fluctuates: chains sometimes publish empty or late files, and some small chains publish sporadically — that's the chains' portals, not the library. `geo-blocked` = the portal only answers Israeli IPs (verified through an Israeli proxy). `degraded` = some file types were missing/empty at check time.

| Chain | Status | Stores | Prices | Promos | Note |
|---|---|---|---|---|---|
| `shufersal` | `ok` | 417 | 6596 | 1 |  |
| `super-pharm` | `geo-blocked` | 307 | 2489 | 736 | reachable from Israeli IPs only (verified via proxy) |
| `wolt` | `ok` | 34 | 5159 | 456 |  |
| `carrefour` | `ok` | 147 | 11161 | 1528 |  |
| `hatzi-hinam` | `geo-blocked` | 13 | 9824 | 592 | reachable from Israeli IPs only (verified via proxy) |
| `rami-levy` | `ok` | 99 | 5185 | 1048 |  |
| `tiv-taam` | `ok` | 54 | 140 | 42 |  |
| `yochananof` | `ok` | 51 | 11766 | 2594 |  |
| `osher-ad` | `ok` | 24 | 6427 | 643 |  |
| `dor-alon` | `ok` | 157 | 1936 | 318 |  |
| `keshet-teamim` | `ok` | 27 | 6326 | 1683 |  |
| `super-cofix` | `degraded` | 34 | — | — | prices: FileNotFound: super-cofix: no PriceFull file | promos: FileNotFound: super-cofix: no PromoFull file |
| `politzer` | `ok` | 8 | 13432 | 1159 |  |
| `stop-market` | `ok` | 12 | 17473 | 1787 |  |
| `fresh-market` | `ok` | 47 | 5700 | 887 |  |
| `salach-dabach` | `ok` | 12 | 12520 | 1759 |  |
| `super-yuda` | `ok` | 26 | 5692 | 380 |  |
| `yellow` | `ok` | 242 | 1747 | 717 |  |
| `good-pharm` | `ok` | 82 | 3373 | 338 |  |
| `super-bareket` | `ok` | 15 | 3168 | 561 |  |
| `king-store` | `ok` | 48 | 2351 | 294 |  |
| `maayan-2000` | `ok` | 38 | 2657 | 322 |  |
| `meshnat-yosef` | `ok` | 4 | 5503 | 192 |  |
| `shefa-birkat-hashem` | `ok` | 22 | 3763 | 515 |  |
| `shuk-hayir` | `ok` | 26 | 1872 | 0 |  |
| `super-sapir` | `ok` | 73 | 1148 | 71 |  |
| `zol-vebegadol` | `ok` | 35 | 4258 | 482 |  |
| `city-market` | `ok` | 28 | 4354 | 0 |  |
| `victory` | `geo-blocked` | 70 | 8723 | 4547 | reachable from Israeli IPs only (verified via proxy) |
| `mahsanei-hashuk` | `geo-blocked` | 71 | 12409 | 5862 | reachable from Israeli IPs only (verified via proxy) |
| `het-cohen` | `geo-blocked` | 5 | 8935 | 2426 | reachable from Israeli IPs only (verified via proxy) |
| `nativ-hahesed` | `down` | — | — | — | portal still unreachable (PortalError) |
