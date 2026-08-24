"""List every branch of a chain, grouped by sub-chain."""

import israeli_prices as ilp

stores_file = ilp.get_stores("shufersal")

print(f"{stores_file.chain_name} — {len(stores_file.stores)} stores")
for store in stores_file.stores[:10]:
    print(f"  [{store.store_id}] {store.sub_chain_name or '-'} | {store.name} — {store.address}")
