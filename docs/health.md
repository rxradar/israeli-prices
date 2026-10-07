# Chain health

**Coverage: 31/32 chains implemented** — the full government roster bar Nativ HaHesed, whose portal has returned HTTP 500 since July 2026 (it stays registered and will be enabled when it returns).

**Last nightly check (2026-10-07T14:17:11+00:00): 30/32 reachable.** The check runs from a GitHub-hosted runner outside Israel and fetches every file type of every chain. Daily reachability fluctuates: chains sometimes publish empty or late files, and some small chains publish sporadically — that's the chains' portals, not the library. `geo-blocked` = the portal only answers Israeli IPs (verified through an Israeli proxy). `degraded` = some file types were missing/empty at check time.

| Chain | Status | Stores | Prices | Promos | Note |
|---|---|---|---|---|---|
| `shufersal` | `ok` | 417 | 6608 | 1 |  |
| `super-pharm` | `geo-blocked` | 307 | 9696 | 862 | reachable from Israeli IPs only (verified via proxy) |
| `wolt` | `ok` | 34 | 6120 | 453 |  |
| `carrefour` | `ok` | 147 | 11167 | 1466 |  |
| `hatzi-hinam` | `geo-blocked` | 13 | 609 | 523 | reachable from Israeli IPs only (verified via proxy) |
| `rami-levy` | `ok` | 99 | 5157 | 1052 |  |
| `tiv-taam` | `ok` | 54 | 135 | 46 |  |
| `yochananof` | `ok` | 51 | 11766 | 1207 |  |
| `osher-ad` | `ok` | 24 | 6485 | 624 |  |
| `dor-alon` | `ok` | 157 | 5307 | 967 |  |
| `keshet-teamim` | `ok` | 27 | 6312 | 1732 |  |
| `super-cofix` | `degraded` | 34 | — | — | prices: FileNotFound: super-cofix: no PriceFull file | promos: FileNotFound: super-cofix: no PromoFull file |
| `politzer` | `ok` | 8 | 15021 | 1054 |  |
| `stop-market` | `ok` | 12 | 16041 | 2671 |  |
| `fresh-market` | `ok` | 47 | 8301 | 678 |  |
| `salach-dabach` | `ok` | 12 | 12604 | 1758 |  |
| `super-yuda` | `ok` | 26 | 6402 | 378 |  |
| `yellow` | `ok` | 242 | 260 | 688 |  |
| `good-pharm` | `ok` | 82 | 3379 | 291 |  |
| `super-bareket` | `ok` | 15 | 1453 | 364 |  |
| `king-store` | `ok` | 48 | 2459 | 299 |  |
| `maayan-2000` | `ok` | 38 | 2727 | 295 |  |
| `meshnat-yosef` | `ok` | 4 | 5500 | 184 |  |
| `shefa-birkat-hashem` | `ok` | 22 | 3567 | 495 |  |
| `shuk-hayir` | `ok` | 26 | 1667 | 0 |  |
| `super-sapir` | `ok` | 72 | 1102 | 66 |  |
| `zol-vebegadol` | `ok` | 34 | 4249 | 480 |  |
| `city-market` | `ok` | 28 | 4346 | 0 |  |
| `victory` | `geo-blocked` | 70 | 8697 | 3771 | reachable from Israeli IPs only (verified via proxy) |
| `mahsanei-hashuk` | `geo-blocked` | 71 | 12411 | 4868 | reachable from Israeli IPs only (verified via proxy) |
| `het-cohen` | `geo-blocked` | 5 | 10698 | 2440 | reachable from Israeli IPs only (verified via proxy) |
| `nativ-hahesed` | `down` | — | — | — | portal still unreachable (PortalError) |
