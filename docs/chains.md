# Chain coverage

Every chain required to publish price-transparency files, per the
Ministry of Economy's official portal list (gov.il). Login usernames
are public — they are published on the same government page.

Status: `live` = adapter implemented and verified · `planned` = registered, adapter to come.

## Self-hosted portals (no auth)

| Chain | Slug | Sector | Portal | Status |
|---|---|---|---|---|
| Shufersal (incl. Be Pharm) | `shufersal` | supermarket | prices.shufersal.co.il | `live` |
| Super-Pharm | `super-pharm` | pharmacy | prices.super-pharm.co.il | `live` |
| Wolt Market | `wolt` | delivery | wm-gateway.wolt.com/isr-prices | `live` |
| Hatzi Hinam | `hatzi-hinam` | supermarket | shop.hazi-hinam.co.il/Prices | `live` |
| Carrefour Israel | `carrefour` | supermarket | prices.carrefour.co.il | `live` |

Wolt's feed covers only **Wolt Market**, its own dark-store venues
(~34 across the country) — the thousands of partner supermarkets,
pharmacies and restaurants selling on the Wolt platform are NOT in the
government feed. Its "stores" are virtual venues, and some publish
legitimately empty price files. Carrefour's portal lists the current
day only.

The Be Pharm drugstore chain publishes inside the Shufersal feed as
sub-chain 5 — filter the stores file on `sub_chain_id == "5"`, then
fetch those stores' price files.

## Cerberus shared portal (url.publishedprices.co.il, login form)

One adapter covers all 13. Usernames (and the three non-empty
passwords) are published on gov.il.

| Chain | Slug | Username | Status |
|---|---|---|---|
| Rami Levy | `rami-levy` | RamiLevi | `live` |
| Tiv Taam | `tiv-taam` | TivTaam | `live` |
| Yochananof | `yochananof` | yohananof | `live` |
| Osher Ad | `osher-ad` | osherad | `live` |
| Dor Alon | `dor-alon` | doralon | `live` |
| Keshet Teamim | `keshet-teamim` | Keshet | `live` |
| Super Cofix | `super-cofix` | SuperCofixApp | `live` |
| Politzer | `politzer` | politzer | `live` |
| Stop Market | `stop-market` | Stop_Market | `live` |
| Fresh Market | `fresh-market` | freshmarket | `live` |
| Salach Dabach | `salach-dabach` | SalachD | `live` |
| Super Yuda | `super-yuda` | yuda_ho | `live` |
| Yellow | `yellow` | Paz_bo | `live` |

Cerberus quirks handled by the adapter: CSRF login flow with ~30-minute
session expiry (automatic re-login), `NULL*` placeholder files skipped,
stray files from other chains filtered out by chain id, bare-.xml and
UTF-16 stores files, Super Yuda's `/Yuda` subfolder, legacy 12-digit
timestamps in file names.

## Bina portals ({prefix}.binaprojects.com, no auth)

One adapter covers all 10.

| Chain | Slug | Sector | Status |
|---|---|---|---|
| Good Pharm | `good-pharm` | pharmacy | `live` |
| Super Bareket | `super-bareket` | supermarket | `live` |
| King Store | `king-store` | supermarket | `live` |
| Maayan 2000 | `maayan-2000` | supermarket | `live` |
| Meshnat Yosef | `meshnat-yosef` | supermarket | `live` |
| Shefa Birkat Hashem | `shefa-birkat-hashem` | supermarket | `live` |
| Shuk Hayir | `shuk-hayir` | supermarket | `live` |
| Super Sapir | `super-sapir` | supermarket | `live` |
| Zol VeBegadol | `zol-vebegadol` | supermarket | `live` |
| City Market | `city-market` | supermarket | `live` |

Bina quirks handled by the adapter: JSON listing capped at 1000 rows
covering the current day, ZIP archives served under .gz names, mixed
legacy/standard file-name timestamps, uppercase .GZ extensions. Some
chains publish legitimately empty PromoFull files.

## Laib catalog (laibcatalog.co.il — the former matrixcatalog.co.il is defunct)

One adapter covers all 3, through the JSON API
(`/webapi/api/getfiles?edi=<chain_id>`).

| Chain | Slug | Status |
|---|---|---|
| Victory | `victory` | `live` |
| Mahsanei HaShuk | `mahsanei-hashuk` | `live` |
| Het Cohen | `het-cohen` | `live` |

## One-off endpoints

| Chain | Slug | Status |
|---|---|---|
| Nativ HaHesed | `nativ-hahesed` | `down` — portal answers HTTP 500 on every path (2026-08-24) |

Nativ HaHesed's portal (a bare-IP IIS host) has been returning HTTP 500
since at least July 2026; the chain — a ~90-branch haredi-sector
retailer — has essentially no other web presence, so there is no
alternative endpoint to fall back to. The chain stays registered and
will be enabled when the portal comes back.

## Geo-restriction

Observed from a non-Israeli runner (2026-08-24): **Super-Pharm** (serves
an empty listing), **Hatzi Hinam** (403) and the **laibcatalog** chains
(Victory, Mahsanei HaShuk, Het Cohen — connection dropped) only answer
Israeli IPs. From abroad, pass `HttpClient(proxy=...)` with Israeli
egress for those five; the other 26 chains work worldwide.

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
