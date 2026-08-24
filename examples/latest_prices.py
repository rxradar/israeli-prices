"""Fetch the latest full price snapshot for one store and show the
cheapest and most expensive items."""

import israeli_prices as ilp

prices = ilp.get_prices("super-pharm", store_id="142")

priced = sorted((i for i in prices.items if i.price), key=lambda i: i.price)
print(f"store {prices.store_id}: {len(prices.items)} items")
for item in priced[:3] + priced[-3:]:
    print(f"  {item.price:>8} ILS  {item.name}")
