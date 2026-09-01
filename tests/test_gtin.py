"""GTIN helpers: canonicalization, the item properties, cross-chain join."""

from decimal import Decimal
from pathlib import Path

import pytest

from israeli_prices import (
    PriceFile,
    PriceItem,
    group_by_gtin,
    is_valid_gtin,
    parse,
    to_gtin14,
)
from israeli_prices.gtin import check_digit

FIXTURES = Path(__file__).parent / "fixtures"


def load(name):
    return parse(FIXTURES / name)


# -- pure functions -----------------------------------------------------

def test_check_digit_known_vectors():
    assert check_digit("400638133393") == 1  # EAN-13 4006381333931
    assert check_digit("03600029145") == 2  # UPC-12 036000291452


def test_is_valid_gtin():
    assert is_valid_gtin("4006381333931")  # EAN-13
    assert is_valid_gtin("036000291452")  # UPC-12
    assert is_valid_gtin("73513537")  # GTIN-8
    assert is_valid_gtin("3600523991556")  # real Super-Pharm SKU
    assert not is_valid_gtin("4006381333930")  # bad check digit
    assert not is_valid_gtin("10900302814")  # 11 digits: not a barcode length
    assert not is_valid_gtin("ABC123")  # non-numeric
    assert not is_valid_gtin("")
    assert not is_valid_gtin(None)


def test_to_gtin14_pads_to_canonical_form():
    assert to_gtin14("3600523991556") == "03600523991556"  # EAN-13 -> 14
    assert to_gtin14("036000291452") == "00036000291452"  # UPC-12 -> 14
    assert to_gtin14("73513537") == "00000073513537"  # GTIN-8 -> 14
    assert to_gtin14(" 4006381333931 ") == "04006381333931"  # trims


def test_to_gtin14_none_for_internal_codes():
    assert to_gtin14("10900302814") is None  # internal / weighted code
    assert to_gtin14("4006381333930") is None  # bad check digit
    assert to_gtin14("") is None
    assert to_gtin14(None) is None


def test_gtin_rejects_non_ascii_digit_strings_without_crashing():
    # str.isdigit() is True for these but they are not ASCII barcodes;
    # the helpers must return False/None, never raise.
    superscript = "1234567²"  # length 8, trailing superscript 2
    arabic_indic = "٥" * 13  # length 13, Arabic-Indic digit five
    for code in (superscript, arabic_indic):
        assert is_valid_gtin(code) is False
        assert to_gtin14(code) is None


# -- item properties on real fixtures -----------------------------------

def test_priceitem_gtin_property():
    sp = load("superpharm_pricefull.xml")
    item = sp.items[0]
    assert item.item_code == "3600523991556"
    assert item.gtin == "03600523991556"
    assert item.is_barcoded is True


def test_priceitem_gtin_none_for_non_barcode():
    sh = load("shufersal_pricefull.xml")
    item = sh.items[0]
    assert item.item_code == "10900302814"  # not a valid GTIN length
    assert item.gtin is None
    assert item.is_barcoded is False


def test_gtin_is_a_serialized_field_but_item_code_stays_raw():
    sp = load("superpharm_pricefull.xml")
    d = sp.items[0].model_dump()
    assert d["item_code"] == "3600523991556"  # raw, exactly as published
    assert d["gtin"] == "03600523991556"  # derived key rides along as a field
    assert "is_barcoded" not in d  # a convenience property, not a column


def test_gtin_is_a_dataframe_column():
    pytest.importorskip("pandas")  # optional extra; skip if not installed
    df = load("superpharm_pricefull.xml").to_df()
    assert "gtin" in df.columns and "item_code" in df.columns
    assert df.iloc[0]["gtin"] == "03600523991556"
    assert str(df.iloc[0]["item_code"]) == "3600523991556"


# -- cross-chain join ---------------------------------------------------

def test_group_by_gtin_joins_across_chains_and_collapses_encodings():
    # same product, EAN-13 at one chain and zero-padded GTIN-14 at another
    sp = PriceFile(
        items=[
            PriceItem(item_code="3600523991556", price=Decimal("66.00")),
            PriceItem(item_code="1234", price=Decimal("5.00")),  # internal -> skipped
            PriceItem(item_code="4006381333931", price=Decimal("9.90")),  # sp-only
        ]
    )
    sh = PriceFile(items=[PriceItem(item_code="03600523991556", price=Decimal("59.90"))])

    grouped = group_by_gtin({"super-pharm": sp, "shufersal": sh})
    assert set(grouped["03600523991556"]) == {"super-pharm", "shufersal"}
    assert grouped["03600523991556"]["super-pharm"].price == Decimal("66.00")
    assert grouped["03600523991556"]["shufersal"].price == Decimal("59.90")
    assert "1234" not in grouped  # internal code has no GTIN key
    assert "04006381333931" in grouped  # sp-only product still present at min_sources=1


def test_group_by_gtin_min_sources_keeps_only_comparable():
    sp = PriceFile(
        items=[
            PriceItem(item_code="3600523991556", price=Decimal("66.00")),
            PriceItem(item_code="4006381333931", price=Decimal("9.90")),  # sp-only
        ]
    )
    sh = PriceFile(items=[PriceItem(item_code="3600523991556", price=Decimal("59.90"))])

    comparable = group_by_gtin({"super-pharm": sp, "shufersal": sh}, min_sources=2)
    assert set(comparable) == {"03600523991556"}  # the sp-only SKU is dropped


def test_group_by_gtin_on_real_fixtures_keys_are_canonical():
    files = {
        "super-pharm": load("superpharm_pricefull.xml"),
        "shufersal": load("shufersal_pricefull.xml"),
    }
    grouped = group_by_gtin(files)
    assert grouped, "expected at least one barcoded item"
    assert all(len(g) == 14 and g.isdigit() for g in grouped)  # all canonical GTIN-14
    assert "03600523991556" in grouped  # the Super-Pharm SKU above
    assert "00000010900302814" not in grouped  # the loose Shufersal code isn't padded in
