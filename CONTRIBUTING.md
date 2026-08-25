# Contributing

Thanks for helping! A few ground rules keep this library reliable.

## Dev setup

```bash
git clone https://github.com/rxradar/israeli-prices
cd israeli-prices
python3 -m venv .venv && .venv/bin/pip install -e ".[dev]"
.venv/bin/pytest -q && .venv/bin/ruff check .
```

## Fixtures first

Every parser change must be backed by a **real captured file**: fetch a
live file from the portal, trim it to a handful of records, drop it in
`tests/fixtures/` and assert on concrete values. No synthetic XML —
the portals' quirks (encodings, dialects, empty fields) are the whole
point of this library.

## One adapter per portal family

Chains sharing a portal engine share one adapter class parameterized by
a spec (see `chains/cerberus.py`, `chains/bina.py`, `chains/laib.py`).
Only genuinely one-off portals get their own module. If a chain
migrates portals, update its spec — don't fork the adapter.

## Principles

- Preserve what the source publishes: widen the models rather than
  truncate or reinterpret data. Empty/garbage values coerce to `None`,
  never to errors.
- Timestamps stay naive local-Israel time, as published.
- Be polite to the portals: no tight retry loops, no scraping beyond
  the transparency files.
- The nightly health check (`scripts/health_check.py`) is the source of
  truth for what works — run it locally if you touch an adapter.
