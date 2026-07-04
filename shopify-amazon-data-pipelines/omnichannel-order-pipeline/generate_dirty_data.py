import csv

dirty_data = [
    {"row_id": "1", "customer": "  ALEX SHAH !! ", "date_placed": "2026/06/15", "amount": "$120.50 USD"},
    {"row_id": "2", "customer": "fiona_geller__", "date_placed": "2026/06/17", "amount": "$45.00 USD"},
    {"row_id": "3", "customer": "CORRUPT_RECORD_##", "date_placed": "BAD_DATE", "amount": "ERROR"},
    {"row_id": "4", "customer": "   ZAIN MALIK ", "date_placed": "2026/06/14", "amount": "$350.00 USD"}
]

with open("dirty_orders.csv", mode="w", newline='') as f:
    writer = csv.DictWriter(f, fieldnames=["row_id", "customer", "date_placed", "amount"])
    writer.writeheader()
    writer.writerows(dirty_data)

print("✅ 'dirty_orders.csv' generated successfully!")