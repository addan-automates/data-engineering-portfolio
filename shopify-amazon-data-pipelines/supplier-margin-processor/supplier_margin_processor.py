with open("raw_supplier_data.csv", "r" , newline ='') as file:
     reader = file.DictReader("raw_supplier_data.csv")
     for row in reader:
        try:
          shopify_upload = float(row["wholesale_cost"] * (1.30)), int(row["warehouse_qty"]) 
          print(shopify_upload)
        except ValueError:
          print("The values are missing")
     print(row)

new_header = ["sku", "retail_price", "stock"]
with open("shopify_upload", "w", newline ='') as file:
   writer = file.dictwriter(file, fieldnames = new_header)
   cleaned_data = writer.write(new_header), writer.write(row)
   print(cleaned_data)
    

   




