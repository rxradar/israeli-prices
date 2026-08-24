"""Parse tests on trimmed real-world fixtures (captured 2026-08-24)."""

from decimal import Decimal
from pathlib import Path

import pytest

from israeli_prices import PriceFile, PromoFile, StoresFile, parse

FIXTURES = Path(__file__).parent / "fixtures"


def load(name):
    return parse(FIXTURES / name)


def test_shufersal_pricefull():
    f = load("shufersal_pricefull.xml")
    assert isinstance(f, PriceFile)
    assert f.chain_id == "7290027600007"
    assert f.store_id == "001"
    assert f.bikoret_no == 9
    item = f.items[0]
    assert item.item_code == "10900302814"
    assert item.price == Decimal("10.00")
    assert item.name and any("֐" <= ch <= "ת" for ch in item.name)  # Hebrew intact
    assert item.price_update_time is not None


def test_superpharm_pricefull():
    f = load("superpharm_pricefull.xml")
    assert isinstance(f, PriceFile)
    assert f.chain_id == "7290172900007"
    assert f.store_id == "142"
    item = f.items[0]
    assert item.item_code == "3600523991556"
    assert item.price == Decimal("66.00")
    assert item.manufacture_country == "DE"
    assert item.unit_price == Decimal("94.28")


def test_superpharm_promofull_grouped_dialect():
    f = load("superpharm_promofull.xml")
    assert isinstance(f, PromoFile)
    assert f.store_id == "209"
    promo = f.promotions[0]
    assert promo.promotion_id == "0004719138"
    assert promo.start_time is not None and promo.end_time is not None
    item = promo.items[0]
    assert item.item_code == "3147758051216"
    assert item.reward_type == 3
    assert item.discounted_price == Decimal("65.00")
    assert item.group_id == 1


def test_shufersal_promofull_multi_group():
    f = load("shufersal_promofull.xml")
    assert isinstance(f, PromoFile)
    assert f.chain_id == "7290027600007"
    promo = f.promotions[0]
    assert promo.promotion_id == "4528444"
    assert promo.items
    # this promotion spans two groups (buy from group 1, gift from group 2)
    assert {i.group_id for i in promo.items} == {1, 2}
    assert promo.items[0].min_purchase_amount == Decimal("99.00")


def test_shufersal_stores():
    f = load("shufersal_stores.xml")
    assert isinstance(f, StoresFile)
    assert f.chain_id == "7290027600007"
    assert f.stores
    store = f.stores[0]
    assert store.sub_chain_id == "1"
    assert store.sub_chain_name == "שופרסל שלי"
    assert store.store_id


def test_superpharm_stores():
    f = load("superpharm_stores.xml")
    assert isinstance(f, StoresFile)
    assert f.chain_id == "7290172900007"
    assert f.stores[0].store_id == "096"
    assert f.stores[0].name == "סופר-פארם בן-גוריון"


def test_parse_rejects_garbage():
    from israeli_prices import ParseError

    with pytest.raises(ParseError):
        parse(b"not xml at all")
    with pytest.raises(ParseError):
        parse(b"<html><body>a portal error page</body></html>")
