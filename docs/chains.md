# Chain coverage

Every chain required to publish price-transparency files, per the
Ministry of Economy's official portal list (gov.il). Login usernames
are public — they are published on the same government page.

Status: ✅ adapter implemented · 🔜 registered, adapter planned.

## Self-hosted portals (no auth)

| Chain | Slug | Sector | Portal | Status |
|---|---|---|---|---|
| Shufersal (incl. Be Pharm) | `shufersal` | supermarket | prices.shufersal.co.il | ✅ |
| Super-Pharm | `super-pharm` | pharmacy | prices.super-pharm.co.il | ✅ |
| Wolt Market | `wolt` | delivery | wm-gateway.wolt.com/isr-prices | 🔜 |
| Hatzi Hinam | `hatzi-hinam` | supermarket | shop.hazi-hinam.co.il/Prices | 🔜 |
| Carrefour Israel | `carrefour` | supermarket | prices.carrefour.co.il | 🔜 |

The Be Pharm drugstore chain publishes inside the Shufersal feed as
sub-chain 5 — filter the stores file on `sub_chain_id == "5"`, then
fetch those stores' price files.

## Cerberus shared portal (url.retail.publishedprices.co.il, login form)

One adapter will unlock all of these; usernames per gov.il.

| Chain | Slug | Username | Status |
|---|---|---|---|
| Rami Levy | `rami-levy` | RamiLevi | 🔜 |
| Tiv Taam | `tiv-taam` | TivTaam | 🔜 |
| Yochananof | `yochananof` | yohananof | 🔜 |
| Osher Ad | `osher-ad` | osherad | 🔜 |
| Dor Alon | `dor-alon` | doralon | 🔜 |
| Keshet Teamim | `keshet-teamim` | Keshet | 🔜 |
| Super Cofix | `super-cofix` | SuperCofixApp | 🔜 |
| Politzer | `politzer` | politzer | 🔜 |
| Stop Market | `stop-market` | Stop_Market | 🔜 |
| Fresh Market | `fresh-market` | freshmarket | 🔜 |
| Salach Dabach | `salach-dabach` | SalachD | 🔜 |
| Super Yuda | `super-yuda` | yuda_ho | 🔜 |
| Yellow | `yellow` | Paz_bo | 🔜 |

## Bina portals ({prefix}.binaprojects.com, no auth)

| Chain | Slug | Sector | Status |
|---|---|---|---|
| Good Pharm | `good-pharm` | pharmacy | 🔜 |
| Super Bareket | `super-bareket` | supermarket | 🔜 |
| King Store | `king-store` | supermarket | 🔜 |
| Maayan 2000 | `maayan-2000` | supermarket | 🔜 |
| Meshnat Yosef | `meshnat-yosef` | supermarket | 🔜 |
| Shefa Birkat Hashem | `shefa-birkat-hashem` | supermarket | 🔜 |
| Shuk Hayir | `shuk-hayir` | supermarket | 🔜 |
| Super Sapir | `super-sapir` | supermarket | 🔜 |
| Zol VeBegadol | `zol-vebegadol` | supermarket | 🔜 |
| City Market | `city-market` | supermarket | 🔜 |

## Laib catalog (laibcatalog.co.il — the former matrixcatalog.co.il is defunct)

| Chain | Slug | Status |
|---|---|---|
| Victory | `victory` | 🔜 |
| Mahsanei HaShuk | `mahsanei-hashuk` | 🔜 |
| Het Cohen | `het-cohen` | 🔜 |

## One-off endpoints

| Chain | Slug | Status |
|---|---|---|
| Nativ HaHesed | `nativ-hahesed` | 🔜 |

## File types

Every chain publishes five categories, gzipped XML. Cadence is set by
the regulation itself:

| Type | Content | Legal cadence |
|---|---|---|
| `PriceFull` | full price snapshot, per store | daily, by store opening time |
| `Price` | incremental price updates, per store | within 1 hour of a register price change |
| `PromoFull` | full promotions snapshot, per store | daily, by store opening time |
| `Promo` | incremental promotion updates, per store | within 1 hour |
| `Stores` | chain-wide branch list | within 1 day of any change |

Files must stay available for 3 months, free and without registration.

File names follow `<Type><chain_id>-<subchain>-<store>-<YYYYMMDD>-<HHMMSS>.gz`
with minor per-chain variations, all handled by `israeli_prices.chains.base.parse_filename`.
