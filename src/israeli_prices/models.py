"""Typed models for Israel's retail price-transparency data.

Field names follow the vocabulary of the government-mandated XML files
(ItemCode, ItemPrice, PromotionId...) translated to snake_case. Chains
publish several XML dialects; the parser normalizes all of them into
these models.
"""

from __future__ import annotations

from datetime import datetime
from decimal import Decimal
from enum import Enum

from pydantic import BaseModel, computed_field

from .gtin import to_gtin14


class _WithItemCode(BaseModel):
    """Base for barcode-carrying rows: keeps the raw ``item_code`` as
    published and adds a canonical cross-chain key derived from it.

    ``gtin`` is a computed field — it rides along in ``model_dump()`` /
    ``to_df()`` / JSON as a real column (the join key), while the source
    stays faithful 1:1 (``item_code`` is untouched). It derives the
    GTIN-14 structurally, so it is consistent across chains regardless of
    whether a chain populates the ``item_type`` field; ``None`` for
    internal/weighted codes. ``is_barcoded`` is the same signal as a bool.
    """

    item_code: str  # barcode (GTIN) or chain-internal code, as published

    @computed_field
    @property
    def gtin(self) -> str | None:
        """Canonical GTIN-14, or ``None`` if ``item_code`` is not a barcode."""
        return to_gtin14(self.item_code)

    @property
    def is_barcoded(self) -> bool:
        """True if ``item_code`` is a structurally valid GTIN barcode."""
        return self.gtin is not None


class FileType(str, Enum):
    """The five file categories mandated by the transparency regulation."""

    PRICE = "Price"  # incremental price updates
    PRICE_FULL = "PriceFull"  # full price snapshot for one store
    PROMO = "Promo"  # incremental promotion updates
    PROMO_FULL = "PromoFull"  # full promotion snapshot for one store
    STORES = "Stores"  # chain-wide store list


class ChainInfo(BaseModel):
    """A chain covered by the transparency law, as listed on gov.il."""

    slug: str
    name: str
    name_he: str | None = None
    chain_id: str | None = None  # GS1 prefix, e.g. "7290027600007"
    portal_url: str
    portal_family: str  # self-hosted | cerberus | bina | laib | webbase
    username: str | None = None  # portal login when required (public, per gov.il)
    sector: str = "supermarket"  # supermarket | pharmacy | convenience | delivery
    implemented: bool = False  # True when this library ships an adapter


class FileRef(BaseModel):
    """A downloadable file listed on a chain's transparency portal.

    ``url`` may be a signed link with a short expiry (e.g. Shufersal's
    Azure blob links) — download soon after listing.
    """

    chain: str  # chain slug
    name: str  # e.g. "PriceFull7290027600007-001-001-20260824-030000.gz"
    file_type: FileType
    url: str
    store_id: str | None = None
    published_at: datetime | None = None


class PriceItem(_WithItemCode):
    """One SKU row in a Price/PriceFull file."""

    item_type: int | None = None  # 1 = barcoded item, 0 = internal code
    name: str | None = None
    manufacturer: str | None = None
    manufacture_country: str | None = None
    manufacturer_description: str | None = None
    unit_qty: str | None = None  # unit label of `quantity` (Hebrew)
    quantity: Decimal | None = None
    unit_of_measure: str | None = None
    is_weighted: bool | None = None
    qty_in_package: Decimal | None = None
    price: Decimal | None = None
    unit_price: Decimal | None = None  # price per UnitOfMeasure
    allow_discount: bool | None = None
    status: int | None = None
    price_update_time: datetime | None = None
    last_sale_time: datetime | None = None  # not published by all chains


class PriceFile(BaseModel):
    """A parsed Price/PriceFull file (one store)."""

    chain_id: str | None = None
    sub_chain_id: str | None = None
    store_id: str | None = None
    bikoret_no: int | None = None
    items: list[PriceItem] = []

    def to_df(self):
        """Items as a pandas DataFrame (requires the `pandas` extra)."""
        import pandas as pd

        return pd.DataFrame([i.model_dump() for i in self.items])


class PromotionItem(_WithItemCode):
    """One SKU participating in a promotion.

    In the grouped dialect (Shufersal, Super-Pharm) reward fields sit on
    the item; in the flat dialect they sit on the promotion. Both levels
    are kept as published.
    """

    item_type: int | None = None
    is_gift_item: bool | None = None
    reward_type: int | None = None
    min_qty: Decimal | None = None
    max_qty: Decimal | None = None
    discount_rate: Decimal | None = None
    discounted_price: Decimal | None = None
    discounted_price_per_unit: Decimal | None = None  # DiscountedPricePerMida
    group_id: int | None = None
    min_purchase_amount: Decimal | None = None  # group-level in grouped dialect


class Promotion(BaseModel):
    """One promotion in a Promo/PromoFull file."""

    promotion_id: str
    description: str | None = None
    update_time: datetime | None = None
    start_time: datetime | None = None
    end_time: datetime | None = None
    allow_multiple_discounts: bool | None = None
    min_items_offered: Decimal | None = None
    club_id: str | None = None  # raw label, e.g. "0 - כלל הלקוחות"
    is_coupon: bool | None = None
    remarks: str | None = None
    additional_restrictions: str | None = None
    # flat-dialect reward fields (promotion-level)
    reward_type: int | None = None
    min_qty: Decimal | None = None
    discounted_price: Decimal | None = None
    discount_rate: Decimal | None = None
    min_purchase_amount: Decimal | None = None
    items: list[PromotionItem] = []


class PromoFile(BaseModel):
    """A parsed Promo/PromoFull file (one store)."""

    chain_id: str | None = None
    sub_chain_id: str | None = None
    store_id: str | None = None
    bikoret_no: int | None = None
    promotions: list[Promotion] = []

    def to_df(self):
        """One row per (promotion, item) as a pandas DataFrame."""
        import pandas as pd

        rows = []
        for p in self.promotions:
            base = p.model_dump(exclude={"items"})
            for it in p.items:
                rows.append({**base, **{f"item_{k}": v for k, v in it.model_dump().items()}})
        return pd.DataFrame(rows)


class Store(BaseModel):
    """One branch in a Stores file."""

    store_id: str
    name: str | None = None
    address: str | None = None
    city: str | None = None  # some chains publish a city code, not a name
    zip_code: str | None = None
    store_type: int | None = None
    bikoret_no: int | None = None
    sub_chain_id: str | None = None
    sub_chain_name: str | None = None


class StoresFile(BaseModel):
    """A parsed Stores file (chain-wide)."""

    chain_id: str | None = None
    chain_name: str | None = None
    last_updated: datetime | None = None
    stores: list[Store] = []

    def to_df(self):
        """Stores as a pandas DataFrame (requires the `pandas` extra)."""
        import pandas as pd

        return pd.DataFrame([s.model_dump() for s in self.stores])
