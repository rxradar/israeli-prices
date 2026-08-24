"""Parse transparency XML files into typed models.

Chains publish several XML dialects: tag casing varies (ItemCode /
ITEMCODE / ItemNm), stores files root at <Root> or <Chain>, promotions
come grouped (Groups/Group/PromotionItems, used by Shufersal and
Super-Pharm) or flat (PromotionItems/Item). This module normalizes all
of them: tags are matched case-insensitively through alias tables and
every value is coerced leniently (empty string -> None).
"""

from __future__ import annotations

import gzip
import xml.etree.ElementTree as ET
from datetime import datetime
from decimal import Decimal, InvalidOperation
from pathlib import Path

from ..exceptions import ParseError
from ..models import (
    PriceFile,
    PriceItem,
    PromoFile,
    Promotion,
    PromotionItem,
    Store,
    StoresFile,
)

GZIP_MAGIC = b"\x1f\x8b"
ZIP_MAGIC = b"PK"


def to_text(data: bytes) -> str:
    """Decompress if compressed and decode, handling the quirks seen in
    the wild: gzip, ZIP served under a .gz name (some Bina portals),
    UTF-8 with/without BOM, UTF-16."""
    if data[:2] == GZIP_MAGIC:
        data = gzip.decompress(data)
    elif data[:2] == ZIP_MAGIC:
        import io
        import zipfile

        with zipfile.ZipFile(io.BytesIO(data)) as zf:
            data = zf.read(zf.namelist()[0])
    if data[:2] in (b"\xff\xfe", b"\xfe\xff"):
        return data.decode("utf-16")
    try:
        return data.decode("utf-8-sig")
    except UnicodeDecodeError:
        return data.decode("utf-8", errors="replace")


# ---------------------------------------------------------------------------
# lenient element access

def _fields(el: ET.Element) -> dict[str, str | None]:
    """Map an element's direct children to {lowercase tag: stripped text}."""
    out: dict[str, str | None] = {}
    for child in el:
        tag = child.tag.rsplit("}", 1)[-1].lower()  # drop any namespace
        text = child.text.strip() if child.text else None
        out[tag] = text or None
    return out


def _pick(fields: dict, *aliases: str) -> str | None:
    for a in aliases:
        if fields.get(a) is not None:
            return fields[a]
    return None


def _find(el: ET.Element, *names: str) -> ET.Element | None:
    """Case-insensitive direct-child lookup."""
    wanted = {n.lower() for n in names}
    for child in el:
        if child.tag.rsplit("}", 1)[-1].lower() in wanted:
            return child
    return None


# ---------------------------------------------------------------------------
# lenient scalar coercion

def _decimal(value: str | None) -> Decimal | None:
    if not value:
        return None
    try:
        return Decimal(value.replace(",", ""))
    except InvalidOperation:
        return None


def _int(value: str | None) -> int | None:
    if not value:
        return None
    try:
        return int(value)
    except ValueError:
        return None


def _bool(value: str | None) -> bool | None:
    if not value:
        return None
    if value in ("0", "1"):
        return value == "1"
    return None


_DT_FORMATS = (
    "%Y-%m-%dT%H:%M:%S.%f",
    "%Y-%m-%dT%H:%M:%S",
    "%Y-%m-%d %H:%M:%S",
    "%Y-%m-%d %H:%M",
    "%Y-%m-%d",
)


def _dt(value: str | None) -> datetime | None:
    if not value:
        return None
    for fmt in _DT_FORMATS:
        try:
            return datetime.strptime(value, fmt)
        except ValueError:
            continue
    return None


# ---------------------------------------------------------------------------
# file-level parsers

def parse(data: bytes | str | Path) -> PriceFile | PromoFile | StoresFile:
    """Parse a transparency file (gzipped or plain XML, bytes or path).

    The file kind is auto-detected from the XML structure.
    """
    if isinstance(data, (str, Path)):
        data = Path(data).read_bytes()
    text = to_text(data)
    try:
        root = ET.fromstring(text)
    except ET.ParseError as exc:
        raise ParseError(f"not valid XML: {exc}") from exc

    if _find(root, "Items") is not None:
        return _parse_prices(root)
    if _find(root, "Promotions") is not None:
        return _parse_promos(root)
    if _find(root, "SubChains", "Stores") is not None:
        return _parse_stores(root)
    raise ParseError(f"unrecognized transparency file (root <{root.tag}>)")


def _header(root: ET.Element) -> dict:
    f = _fields(root)
    return {
        "chain_id": _pick(f, "chainid"),
        "sub_chain_id": _pick(f, "subchainid"),
        "store_id": _pick(f, "storeid"),
        "bikoret_no": _int(_pick(f, "bikoretno")),
    }


def _parse_prices(root: ET.Element) -> PriceFile:
    items_el = _find(root, "Items")
    items = []
    for el in items_el:
        f = _fields(el)
        code = _pick(f, "itemcode")
        if code is None:
            continue
        items.append(
            PriceItem(
                item_code=code,
                item_type=_int(_pick(f, "itemtype")),
                name=_pick(f, "itemname", "itemnm"),
                manufacturer=_pick(f, "manufacturename", "manufacturername"),
                manufacture_country=_pick(f, "manufacturecountry", "manufacturercountry"),
                manufacturer_description=_pick(
                    f, "manufactureitemdescription", "manufactureritemdescription"
                ),
                unit_qty=_pick(f, "unitqty"),
                quantity=_decimal(_pick(f, "quantity")),
                unit_of_measure=_pick(f, "unitofmeasure"),
                is_weighted=_bool(_pick(f, "bisweighted", "isweighted", "blsweighted")),
                qty_in_package=_decimal(_pick(f, "qtyinpackage")),
                price=_decimal(_pick(f, "itemprice")),
                unit_price=_decimal(_pick(f, "unitofmeasureprice")),
                allow_discount=_bool(_pick(f, "allowdiscount")),
                status=_int(_pick(f, "itemstatus")),
                price_update_time=_dt(_pick(f, "priceupdatetime", "priceupdatedate")),
                last_sale_time=_dt(_pick(f, "lastsaledatetime", "lastsaledate")),
            )
        )
    return PriceFile(**_header(root), items=items)


def _promo_item(el: ET.Element, group_id: int | None, min_purchase: Decimal | None) -> PromotionItem | None:
    f = _fields(el)
    code = _pick(f, "itemcode")
    if code is None:
        return None
    return PromotionItem(
        item_code=code,
        item_type=_int(_pick(f, "itemtype")),
        is_gift_item=_bool(_pick(f, "isgiftitem")),
        reward_type=_int(_pick(f, "rewardtype")),
        min_qty=_decimal(_pick(f, "minqty")),
        max_qty=_decimal(_pick(f, "maxqty")),
        discount_rate=_decimal(_pick(f, "discountrate")),
        discounted_price=_decimal(_pick(f, "discountedprice")),
        discounted_price_per_unit=_decimal(_pick(f, "discountedpricepermida")),
        group_id=group_id,
        min_purchase_amount=min_purchase,
    )


def _parse_promos(root: ET.Element) -> PromoFile:
    promos_el = _find(root, "Promotions")
    promotions = []
    for el in promos_el:
        f = _fields(el)
        promo_id = _pick(f, "promotionid")
        if promo_id is None:
            continue

        items: list[PromotionItem] = []
        groups_el = _find(el, "Groups")
        if groups_el is not None:
            # grouped dialect (Shufersal, Super-Pharm)
            for group_el in groups_el:
                gf = _fields(group_el)
                gid = _int(_pick(gf, "groupid"))
                min_purchase = _decimal(_pick(gf, "minpurchaseamount"))
                group_items = _find(group_el, "PromotionItems")
                if group_items is not None:
                    for item_el in group_items:
                        item = _promo_item(item_el, gid, min_purchase)
                        if item:
                            items.append(item)
        else:
            # flat dialect
            flat_items = _find(el, "PromotionItems")
            if flat_items is not None:
                for item_el in flat_items:
                    item = _promo_item(item_el, None, None)
                    if item:
                        items.append(item)

        promotions.append(
            Promotion(
                promotion_id=promo_id,
                description=_pick(f, "promotiondescription"),
                update_time=_dt(_pick(f, "promotionupdatetime", "promotionupdatedate")),
                start_time=_dt(_pick(f, "promotionstartdatetime", "promotionstartdate")),
                end_time=_dt(_pick(f, "promotionenddatetime", "promotionenddate")),
                allow_multiple_discounts=_bool(_pick(f, "allowmultiplediscounts")),
                min_items_offered=_decimal(_pick(f, "minnoofitemoffered", "minnoofitemofered")),
                club_id=_pick(f, "clubid"),
                is_coupon=_bool(_pick(f, "additionaliscoupon", "iscoupon")),
                remarks=_pick(f, "remarks"),
                additional_restrictions=_pick(f, "additionalrestrictions"),
                reward_type=_int(_pick(f, "rewardtype")),
                min_qty=_decimal(_pick(f, "minqty")),
                discounted_price=_decimal(_pick(f, "discountedprice")),
                discount_rate=_decimal(_pick(f, "discountrate")),
                min_purchase_amount=_decimal(_pick(f, "minpurchaseamount", "minpurchaseamnt")),
                items=items,
            )
        )
    return PromoFile(**_header(root), promotions=promotions)


def _parse_stores(root: ET.Element) -> StoresFile:
    f = _fields(root)
    last_date = _pick(f, "lastupdatedate")
    last_time = _pick(f, "lastupdatetime")
    last_updated = _dt(f"{last_date} {last_time}" if last_date and last_time else last_date)

    stores: list[Store] = []

    def collect(stores_el: ET.Element, sub_id: str | None, sub_name: str | None):
        for store_el in stores_el:
            sf = _fields(store_el)
            sid = _pick(sf, "storeid")
            if sid is None:
                continue
            stores.append(
                Store(
                    store_id=sid,
                    name=_pick(sf, "storename"),
                    address=_pick(sf, "address"),
                    city=_pick(sf, "city"),
                    zip_code=_pick(sf, "zipcode"),
                    store_type=_int(_pick(sf, "storetype")),
                    bikoret_no=_int(_pick(sf, "bikoretno")),
                    sub_chain_id=sub_id,
                    sub_chain_name=sub_name,
                )
            )

    sub_chains_el = _find(root, "SubChains")
    if sub_chains_el is not None:
        for sub_el in sub_chains_el:
            sub_f = _fields(sub_el)
            stores_el = _find(sub_el, "Stores")
            if stores_el is not None:
                collect(stores_el, _pick(sub_f, "subchainid"), _pick(sub_f, "subchainname"))
    else:
        stores_el = _find(root, "Stores")
        if stores_el is not None:
            collect(stores_el, None, None)

    return StoresFile(
        chain_id=_pick(f, "chainid"),
        chain_name=_pick(f, "chainname"),
        last_updated=last_updated,
        stores=stores,
    )
