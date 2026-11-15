# Chain health

**Coverage: 31/32 chains implemented** — the full government roster bar Nativ HaHesed, whose portal has returned HTTP 500 since July 2026 (it stays registered and will be enabled when it returns).

**Last nightly check (2026-11-15T14:33:37+00:00): 29/32 reachable.** The check runs from a GitHub-hosted runner outside Israel and fetches every file type of every chain. Daily reachability fluctuates: chains sometimes publish empty or late files, and some small chains publish sporadically — that's the chains' portals, not the library. `geo-blocked` = the portal only answers Israeli IPs (verified through an Israeli proxy). `degraded` = some file types were missing/empty at check time.

| Chain | Status | Stores | Prices | Promos | Note |
|---|---|---|---|---|---|
| `shufersal` | `ok` | 417 | 6565 | 18 |  |
| `super-pharm` | `down` | — | — | — | stores: FileNotFound: super-pharm: no Stores file | prices: FileNotFound: super-pharm: no PriceFull file | promos: FileNotFound: super-pharm: no PromoFull file |
| `wolt` | `ok` | 37 | 6060 | 209 |  |
| `carrefour` | `geo-blocked` | 147 | 11102 | 1604 | reachable from Israeli IPs only (verified via proxy) |
| `hatzi-hinam` | `geo-blocked` | 13 | 9993 | 868 | reachable from Israeli IPs only (verified via proxy) |
| `rami-levy` | `ok` | 99 | 5301 | 1081 |  |
| `tiv-taam` | `ok` | 54 | 52 | 17 |  |
| `yochananof` | `ok` | 51 | 11798 | 1375 |  |
| `osher-ad` | `ok` | 24 | 5975 | 824 |  |
| `dor-alon` | `ok` | 157 | 1498 | 334 |  |
| `keshet-teamim` | `ok` | 28 | 6423 | 1503 |  |
| `super-cofix` | `degraded` | 34 | — | — | prices: FileNotFound: super-cofix: no PriceFull file | promos: FileNotFound: super-cofix: no PromoFull file |
| `politzer` | `ok` | 8 | 14563 | 1158 |  |
| `stop-market` | `ok` | 11 | 17579 | 2824 |  |
| `fresh-market` | `ok` | 73 | 8308 | 788 |  |
| `salach-dabach` | `ok` | 12 | 12301 | 2028 |  |
| `super-yuda` | `ok` | 26 | 6463 | 417 |  |
| `yellow` | `ok` | 242 | 1825 | 687 |  |
| `good-pharm` | `ok` | 84 | 3306 | 331 |  |
| `super-bareket` | `ok` | 15 | 4739 | 713 |  |
| `king-store` | `ok` | 48 | 2381 | 271 |  |
| `maayan-2000` | `ok` | 38 | 3024 | 398 |  |
| `meshnat-yosef` | `ok` | 4 | 5550 | 232 |  |
| `shefa-birkat-hashem` | `ok` | 22 | 3915 | 548 |  |
| `shuk-hayir` | `ok` | 26 | 1690 | 0 |  |
| `super-sapir` | `ok` | 130 | 19 | 1 |  |
| `zol-vebegadol` | `ok` | 35 | 4284 | 498 |  |
| `city-market` | `ok` | 70 | 4301 | 0 |  |
| `victory` | `geo-blocked` | 70 | 8687 | 4435 | reachable from Israeli IPs only (verified via proxy) |
| `mahsanei-hashuk` | `geo-blocked` | 72 | 2990 | 1677 | reachable from Israeli IPs only (verified via proxy) |
| `het-cohen` | `geo-blocked` | 5 | 8930 | 2871 | reachable from Israeli IPs only (verified via proxy) |
| `nativ-hahesed` | `down` | — | — | — | portal still unreachable (PortalError) |
