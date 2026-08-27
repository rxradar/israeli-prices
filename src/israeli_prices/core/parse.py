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
import io
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


def _dt_pair(fields: dict, dt_alias: str, date_alias: str, hour_alias: str) -> datetime | None:
    """Timestamp from a single datetime field, or from the split
    date + hour fields used by the flat promotion dialect."""
    value = _pick(fields, dt_alias)
    if value:
        return _dt(value)
    date = _pick(fields, date_alias)
    if not date:
        return None
    hour = _pick(fields, hour_alias)
    if hour:
        combined = _dt(f"{date} {hour}")
        if combined:
            return combined
    return _dt(date)


# ---------------------------------------------------------------------------
# file-level parsers

def parse(data: bytes | str | Path) -> PriceFile | PromoFile | StoresFile:
    """Parse a transparency file (gzipped or plain XML, bytes or path).

    The file kind is auto-detected from the XML structure. Parsing is
    streamed element by element (each row is cleared once mapped) so a
    large PriceFull snapshot never materializes a full DOM in memory.
    """
    if isinstance(data, (str, Path)):
        data = Path(data).read_bytes()
    source = io.BytesIO(to_text(data).encode("utf-8"))
    try:
        return _stream_parse(source)
    except ET.ParseError as exc:
        raise ParseError(f"not valid XML: {exc}") from exc


def _local(tag: str) -> str:
    """Lowercased local name of a tag, dropping any XML namespace."""
    return tag.rsplit("}", 1)[-1].lower()


def _stream_parse(source: io.BytesIO) -> PriceFile | PromoFile | StoresFile:
    """Single streaming pass over the file.

    The top-level container (``<Items>`` / ``<Promotions>`` /
    ``<Stores>`` | ``<SubChains>``) selects the file kind; each price
    item, promotion or store is mapped on its closing tag and then
    cleared to bound memory. Sub-chain id and name are carried from the
    enclosing ``<SubChain>`` wrapper only, matching the DOM behaviour.
    """
    context = ET.iterparse(source, events=("start", "end"))
    root: ET.Element | None = None
    mode: str | None = None
    stack: list[str] = []
    price_items: list[PriceItem] = []
    promotions: list[Promotion] = []
    stores: list[Store] = []
    sub_id: str | None = None
    sub_name: str | None = None

    for event, elem in context:
        tag = _local(elem.tag)
        if event == "start":
            if root is None:
                root = elem
            stack.append(tag)
            if mode is None:
                if tag == "items":
                    mode = "prices"
                elif tag == "promotions":
                    mode = "promos"
                elif tag in ("stores", "subchains"):
                    mode = "stores"
            if tag == "subchain":
                sub_id = sub_name = None
            continue

        parent = stack[-2] if len(stack) >= 2 else None
        if mode == "prices" and tag == "item" and parent == "items":
            item = _price_item_from_el(elem)
            if item is not None:
                price_items.append(item)
            elem.clear()
        elif mode == "promos" and tag == "promotion":
            promo = _promotion_from_el(elem)
            if promo is not None:
                promotions.append(promo)
            elem.clear()
        elif mode == "stores":
            if tag == "subchainid" and parent == "subchain":
                sub_id = (elem.text or "").strip() or None
            elif tag == "subchainname" and parent == "subchain":
                sub_name = (elem.text or "").strip() or None
            elif tag == "store":
                store = _store_from_el(elem, sub_id, sub_name)
                if store is not None:
                    stores.append(store)
                elem.clear()
        stack.pop()

    if root is None or mode is None:
        root_tag = root.tag if root is not None else "?"
        raise ParseError(f"unrecognized transparency file (root <{root_tag}>)")

    if mode == "prices":
        return PriceFile(**_header(root), items=price_items)
    if mode == "promos":
        return PromoFile(**_header(root), promotions=promotions)
    f = _fields(root)
    last_date = _pick(f, "lastupdatedate")
    last_time = _pick(f, "lastupdatetime")
    last_updated = _dt(f"{last_date} {last_time}" if last_date and last_time else last_date)
    return StoresFile(
        chain_id=_pick(f, "chainid"),
        chain_name=_pick(f, "chainname"),
        last_updated=last_updated,
        stores=stores,
    )


def _header(root: ET.Element) -> dict:
    f = _fields(root)
    return {
        "chain_id": _pick(f, "chainid"),
        "sub_chain_id": _pick(f, "subchainid"),
        "store_id": _pick(f, "storeid"),
        "bikoret_no": _int(_pick(f, "bikoretno")),
    }


def _price_item_from_el(el: ET.Element) -> PriceItem | None:
    f = _fields(el)
    code = _pick(f, "itemcode")
    if code is None:
        return None
    return PriceItem(
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


def _promotion_from_el(el: ET.Element) -> Promotion | None:
    f = _fields(el)
    promo_id = _pick(f, "promotionid")
    if promo_id is None:
        return None

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

    return Promotion(
        promotion_id=promo_id,
        description=_pick(f, "promotiondescription"),
        update_time=_dt(_pick(f, "promotionupdatetime", "promotionupdatedate")),
        start_time=_dt_pair(
            f, "promotionstartdatetime", "promotionstartdate", "promotionstarthour"
        ),
        end_time=_dt_pair(
            f, "promotionenddatetime", "promotionenddate", "promotionendhour"
        ),
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


def _store_from_el(
    el: ET.Element, sub_id: str | None, sub_name: str | None
) -> Store | None:
    sf = _fields(el)
    sid = _pick(sf, "storeid")
    if sid is None:
        return None
    return Store(
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
