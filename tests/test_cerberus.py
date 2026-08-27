from israeli_prices import FileType
from israeli_prices.chains.cerberus import make_cerberus_adapter


def test_listing_uses_filename_timestamp_instead_of_unsorted_portal_time(monkeypatch):
    adapter = make_cerberus_adapter("super-yuda")
    rows = [
        {
            "type": "file",
            "time": "z",
            "fname": "PriceFull7290058177776-999-202608220110.gz",
        },
        {
            "type": "file",
            "time": "y",
            "fname": "PriceFull7290058177776-001-216-20260827-011007.gz",
        },
        {
            "type": "file",
            "time": "x",
            "fname": "PriceFull7290058177776-001-211-20260827-093702.gz",
        },
    ]
    monkeypatch.setattr(adapter, "_list_dir", lambda folder, search="": rows)

    refs = list(adapter.iter_files(file_type=FileType.PRICE_FULL))

    assert [ref.store_id for ref in refs] == ["211", "216", "999"]
    assert [ref.published_at.strftime("%Y%m%d%H%M%S") for ref in refs] == [
        "20260827093702",
        "20260827011007",
        "20260822011000",
    ]
