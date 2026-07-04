import csv

# Run this script once to create your raw input CSV file!
data = [
    {"supplier_sku": "ECO-MUG-01", "wholesale_cost": "10.00", "warehouse_qty": "50"},
    {"supplier_sku": "SILVER-FLASK", "wholesale_cost": "20.00", "warehouse_qty": "15"},
    {"supplier_sku": "CHILL-COOLER", "wholesale_cost": "45.50", "warehouse_qty": "8"},
    {"supplier_sku": "BROKEN-ITEM", "wholesale_cost": "ERROR_PRICE", "warehouse_qty": "0"} # Messy data row!
]

with open("raw_supplier_data.csv", mode="w", newline='') as f:
    writer = csv.DictWriter(f, fieldnames=["supplier_sku", "wholesale_cost", "warehouse_qty"])
    writer.writeheader()
    writer.writerows(data)

print("✅ 'raw_supplier_data.csv' has been generated successfully!")