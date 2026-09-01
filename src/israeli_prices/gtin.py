"""GTIN helpers — the reliable way to line the same product up across chains.

Barcoded items carry a real GTIN/EAN barcode in ``item_code``, and that
barcode is identical at every chain — so it is the natural cross-chain
join key. The catch is cosmetic: the same product appears as a UPC-12 at
one chain, an EAN-13 at another, sometimes zero-padded. Canonicalizing to
GTIN-14 collapses those variants to one key.

``to_gtin14`` is strict on purpose: it returns a value only for a
structurally valid GTIN (right length + correct check digit), so a
chain-internal or weighted-item code — which has no shared meaning across
chains — resolves to ``None`` rather than a bogus join key. This mirrors
what the source data can and cannot promise; it invents nothing.

Note ``item_type`` is the *retailer's own* declaration (1 = barcoded,
0 = internal), and not every chain populates it. The GTIN derived here is
computed structurally from ``item_code``, so it is consistent everywhere.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .models import PriceFile, PriceItem

# GTIN-8, UPC-A (12), EAN-13 and GTIN-14 are the standard barcode lengths.
_GTIN_LENGTHS = frozenset({8, 12, 13, 14})


def check_digit(payload: str) -> int:
    """The GS1 mod-10 check digit for a numeric GTIN payload (all digits
    but the last). Weights alternate 3, 1 from the rightmost digit."""
    total = 0
    for i, ch in enumerate(reversed(payload)):
        total += int(ch) * (3 if i % 2 == 0 else 1)
    return (10 - total % 10) % 10


def is_valid_gtin(code: str | None) -> bool:
    """True if ``code`` is a structurally valid GTIN (a barcode length and
    a correct check digit)."""
    if not code:
        return False
    s = code.strip()
    if not s.isdigit() or len(s) not in _GTIN_LENGTHS:
        return False
    return check_digit(s[:-1]) == int(s[-1])


def to_gtin14(code: str | None) -> str | None:
    """Canonicalize a barcode to a 14-digit GTIN, or ``None`` if ``code``
    is not a structurally valid GTIN.

    Zero-pads GTIN-8 / UPC-12 / EAN-13 up to GTIN-14 so the same product
    shares one key across chains. Chain-internal and weighted-item codes
    (no valid barcode) return ``None`` — they have no cross-chain meaning.
    """
    if not is_valid_gtin(code):
        return None
    return code.strip().zfill(14)  # type: ignore[union-attr]  # is_valid_gtin guards None


def group_by_gtin(
    files: dict[str, PriceFile],
    min_sources: int = 1,
) -> dict[str, dict[str, PriceItem]]:
    """Line barcoded items up across price files by their canonical GTIN-14.

    ``files`` maps a label (e.g. a chain slug) to a :class:`PriceFile`.
    Returns ``{gtin14: {label: PriceItem}}`` for every barcoded product,
    so you can compare the same SKU across chains::

        sp = ilp.get_prices("super-pharm", "142")
        sh = ilp.get_prices("shufersal", "001")
        for gtin, byc in ilp.group_by_gtin({"super-pharm": sp, "shufersal": sh},
                                           min_sources=2).items():
            print(gtin, {c: it.price for c, it in byc.items()})

    ``min_sources`` keeps only GTINs present in at least that many files
    (use 2 for "products I can actually compare"). Loose/weighted items,
    which have no shared key, are skipped.
    """
    out: dict[str, dict[str, PriceItem]] = {}
    for label, pf in files.items():
        for item in pf.items:
            gtin = to_gtin14(item.item_code)
            if gtin is None:
                continue
            out.setdefault(gtin, {})[label] = item
    if min_sources > 1:
        out = {g: byc for g, byc in out.items() if len(byc) >= min_sources}
    return out
