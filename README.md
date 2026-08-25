# israeli-prices

[![tests](https://github.com/rxradar/israeli-prices/actions/workflows/tests.yml/badge.svg)](https://github.com/rxradar/israeli-prices/actions/workflows/tests.yml)
[![chains live](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Frxradar%2Fisraeli-prices%2Fmain%2Fdocs%2Fhealth-badge.json)](docs/health.md)
[![PyPI](https://img.shields.io/pypi/v/israeli-prices)](https://pypi.org/project/israeli-prices/)
[![license: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

Typed Python client for Israel's retail **price-transparency data**.

Israeli law requires large retailers — supermarkets and drugstore chains alike —
to publish their full price, promotion and store lists several times a day.
The data is public, but it is scattered across ~30 chain portals with
different auth schemes, file listings and XML dialects.

`israeli-prices` turns all of that into one clean API:

```python
import israeli_prices as ilp

ilp.list_chains()                              # every chain covered by the law
stores = ilp.get_stores("super-pharm")         # -> StoresFile (typed)
prices = ilp.get_prices("shufersal", store_id="001")   # -> PriceFile
promos = ilp.get_promos("super-pharm", store_id="209") # -> PromoFile

prices.items[0].price        # Decimal("10.00")
prices.to_df()               # optional pandas export
```

- **Fetch + parse, end to end** — one `pip install`, portal quirks handled per
  chain, gzip + XML dialects normalized into [pydantic](https://docs.pydantic.dev)
  models. No raw file juggling.
- **Prices, promotions AND stores** — including grouped promotion structures
  (groups, reward types, club restrictions), not just price rows.
- **Pharmacy coverage first-class** — Super-Pharm today, Good Pharm and the
  Be Pharm sub-chain on the roadmap, alongside every supermarket chain.
- **MIT licensed** — free for any use, commercial included.

## Status

**31 of the 32 chains on the government roster are implemented**, every
one verified live end to end (the last one's portal is down — it is
registered and will be enabled when it comes back):

- **Self-hosted portals**: Shufersal (incl. the Be Pharm sub-chain),
  Super-Pharm, Wolt Market, Carrefour, Hatzi Hinam.
- **Cerberus shared portal** (one adapter, 13 chains): Rami Levy,
  Tiv Taam, Yochananof, Osher Ad, Dor Alon, Keshet Teamim, Super Cofix,
  Politzer, Stop Market, Fresh Market, Salach Dabach, Super Yuda,
  Yellow.
- **Bina portals** (one adapter, 10 chains): Good Pharm, Super Bareket,
  King Store, Maayan 2000, Meshnat Yosef, Shefa Birkat Hashem,
  Shuk Hayir, Super Sapir, Zol VeBegadol, City Market.
- **Laib catalog** (one adapter, 3 chains): Victory, Mahsanei HaShuk,
  Het Cohen.

See [docs/chains.md](docs/chains.md) for the full coverage matrix and
per-portal quirks.

## Install

```bash
pip install israeli-prices
```

Requires Python ≥ 3.10. Optional extra: `israeli-prices[pandas]` for
`.to_df()`.

## Lower-level API

```python
from israeli_prices import FileType, list_files, download, parse

refs = list_files("shufersal", file_type=FileType.PROMO_FULL, limit=5)
payload = download(refs[0])          # raw gzipped XML, as published
promo_file = parse(payload)          # auto-detects the file kind
```

Some portals sign their download URLs with a short expiry (Shufersal) —
download right after listing. Some portals are geo-restricted to Israeli
IPs; pass a proxy via `HttpClient(proxy=...)` if you fetch from abroad.

## Data notes

- Timestamps are naive local Israel time, as published.
- Prices are `Decimal`, in ILS (`ItemPrice` from the source files).
- `item_code` is usually a GTIN/barcode but chains also publish internal
  codes (`item_type` distinguishes them).
- Hebrew text is preserved as published; encodings (UTF-8 BOM, UTF-16)
  are handled transparently.
- Freshness: chains publish incremental `Price`/`Promo` files throughout
  the day and daily `PriceFull`/`PromoFull` snapshots per store.
- Scope: the law covers each retailer's own sales only — e.g. Wolt's
  feed contains Wolt Market (its dark stores), not the partner
  retailers on the Wolt platform. Per-chain caveats live in
  [docs/chains.md](docs/chains.md).

## License

MIT © RxRadar Inc. — the data itself is published by the chains under
Israel's price-transparency regulation and remains theirs; this library
just fetches and parses it. Be a good citizen: cache locally and keep
request rates reasonable.
