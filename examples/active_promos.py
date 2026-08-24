"""Show promotions currently active in one store."""

from datetime import datetime

import israeli_prices as ilp

promos = ilp.get_promos("shufersal", store_id="001")

now = datetime.now()
active = [
    p
    for p in promos.promotions
    if (p.start_time is None or p.start_time <= now)
    and (p.end_time is None or p.end_time >= now)
]
print(f"store {promos.store_id}: {len(active)} active promotions (of {len(promos.promotions)})")
for p in active[:5]:
    print(f"  [{p.promotion_id}] {p.description} — {len(p.items)} items, until {p.end_time:%Y-%m-%d}")
