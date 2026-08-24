from datetime import datetime

from israeli_prices.chains.base import parse_filename, same_store
from israeli_prices.models import FileType


def test_pricefull_with_subchain_store_and_time():
    ft, store, published = parse_filename(
        "PriceFull7290027600007-001-001-20260824-030000.gz"
    )
    assert ft == FileType.PRICE_FULL
    assert store == "001"
    assert published == datetime(2026, 8, 24, 3, 0, 0)


def test_price_prefix_not_confused_with_pricefull():
    ft, store, _ = parse_filename("Price7290172900007-000-142-20260824-164011.gz")
    assert ft == FileType.PRICE
    assert store == "142"


def test_stores_file_has_no_store_id():
    ft, store, published = parse_filename("Stores7290172900007-000-20260824-070016.gz")
    assert ft == FileType.STORES
    assert store is None
    assert published == datetime(2026, 8, 24, 7, 0, 16)


def test_stores_file_with_non_time_suffix():
    # Shufersal stores files end with a 3-digit sequence, not HHMMSS
    ft, store, published = parse_filename("Stores7290027600007-000-20260824-021.gz")
    assert ft == FileType.STORES
    assert store is None
    assert published == datetime(2026, 8, 24)


def test_same_store_is_lenient_about_zero_padding():
    assert same_store("001", "1")
    assert same_store("142", "142")
    assert not same_store("001", "2")
    assert not same_store(None, "1")
