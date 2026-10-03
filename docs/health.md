# Chain health

**Coverage: 31/32 chains implemented** — the full government roster bar Nativ HaHesed, whose portal has returned HTTP 500 since July 2026 (it stays registered and will be enabled when it returns).

**Last nightly check (2026-10-03T12:17:28+00:00): 30/32 reachable.** The check runs from a GitHub-hosted runner outside Israel and fetches every file type of every chain. Daily reachability fluctuates: chains sometimes publish empty or late files, and some small chains publish sporadically — that's the chains' portals, not the library. `geo-blocked` = the portal only answers Israeli IPs (verified through an Israeli proxy). `degraded` = some file types were missing/empty at check time.

| Chain | Status | Stores | Prices | Promos | Note |
|---|---|---|---|---|---|
| `shufersal` | `ok` | 417 | 6632 | 1 |  |
| `super-pharm` | `geo-blocked` | 307 | 8162 | 795 | reachable from Israeli IPs only (verified via proxy) |
| `wolt` | `ok` | 34 | 5036 | 723 |  |
| `carrefour` | `ok` | 147 | 11193 | 320 |  |
| `hatzi-hinam` | `geo-blocked` | 13 | 9779 | 755 | reachable from Israeli IPs only (verified via proxy) |
| `rami-levy` | `ok` | 99 | 5290 | 1137 |  |
| `tiv-taam` | `ok` | 54 | 135 | 47 |  |
| `yochananof` | `ok` | 51 | 11771 | 1718 |  |
| `osher-ad` | `ok` | 24 | 6518 | 896 |  |
| `dor-alon` | `ok` | 157 | 1823 | 362 |  |
| `keshet-teamim` | `ok` | 27 | 6434 | 1872 |  |
| `super-cofix` | `degraded` | 34 | — | — | prices: FileNotFound: super-cofix: no PriceFull file | promos: FileNotFound: super-cofix: no PromoFull file |
| `politzer` | `ok` | 8 | 10732 | 645 |  |
| `stop-market` | `ok` | 11 | 17459 | 4058 |  |
| `fresh-market` | `ok` | 47 | 8315 | 793 |  |
| `salach-dabach` | `ok` | 12 | 12642 | 2081 |  |
| `super-yuda` | `ok` | 26 | 4934 | 444 |  |
| `yellow` | `ok` | 242 | 1863 | 659 |  |
| `good-pharm` | `ok` | 82 | 3404 | 284 |  |
| `super-bareket` | `ok` | 14 | 6538 | 962 |  |
| `king-store` | `ok` | 29 | 2455 | 295 |  |
| `maayan-2000` | `ok` | 38 | 2700 | 440 |  |
| `meshnat-yosef` | `ok` | 4 | 5523 | 288 |  |
| `shefa-birkat-hashem` | `ok` | 22 | 3855 | 641 |  |
| `shuk-hayir` | `ok` | 26 | 1683 | 0 |  |
| `super-sapir` | `ok` | 72 | 1080 | 60 |  |
| `zol-vebegadol` | `ok` | 35 | 3778 | 1081 |  |
| `city-market` | `ok` | 28 | 4407 | 0 |  |
| `victory` | `geo-blocked` | 70 | 10053 | 5171 | reachable from Israeli IPs only (verified via proxy) |
| `mahsanei-hashuk` | `geo-blocked` | 71 | 12381 | 4281 | reachable from Israeli IPs only (verified via proxy) |
| `het-cohen` | `geo-blocked` | 5 | 8966 | 3384 | reachable from Israeli IPs only (verified via proxy) |
| `nativ-hahesed` | `down` | — | — | — | portal still unreachable (PortalError) |
