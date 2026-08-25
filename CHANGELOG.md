# Changelog

## 0.1.0 — 2026-08-25

Initial release.

- 31 of the 32 chains on the government price-transparency roster,
  every one verified live end to end (the last one's portal is down).
- Five portal families: self-hosted (Shufersal, Super-Pharm, Wolt,
  Carrefour, Hatzi Hinam), Cerberus (13 chains), Bina (10 chains),
  Laib (3 chains), one-offs.
- Typed models (pydantic) for prices, promotions and stores; grouped
  and flat promotion dialects normalized; Decimal prices, Hebrew
  preserved.
- Handles the wild: UTF-16 and BOM'd files, ZIP archives under .gz
  names, expiring signed URLs, session expiry re-login, placeholder
  NULL files, legacy file-name timestamps.
- Nightly automated health check per chain, committed to docs/health.md.
- Optional pandas export (`.to_df()`), proxy support for the five
  geo-restricted portals.
