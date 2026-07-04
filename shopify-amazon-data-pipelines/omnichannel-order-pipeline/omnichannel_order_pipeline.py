import csv
from datetime import datetime

# Define file paths
RAW_DATA_PATH = "raw_omnichannel_orders.csv"
CLEAN_DATA_PATH = "clean_omnichannel_orders.csv"

def normalize_timestamp(raw_date):
    """
    Normalizes inconsistent date formats into ISO standard YYYY-MM-DD HH:MM:SS
    Handles Shopify format (YYYY-MM-DD) and Amazon FBA format (DD/MM/YYYY)
    """
    raw_date = raw_date.strip()
    try:
        # Check for Shopify format (e.g., 2026-06-25)
        if "-" in raw_date:
            parsed_date = datetime.strptime(raw_date, "%Y-%m-%d")
        # Check for Amazon format (e.g., 25/06/2026)
        elif "/" in raw_date:
            parsed_date = datetime.strptime(raw_date, "%d/%m/%Y")
        else:
            raise ValueError(f"Unknown date format: {raw_date}")
        
        return parsed_date.strftime("%Y-%m-%d %H:%M:%S")
    except Exception as e:
        # Fallback default for corrupt data
        return "1970-01-01 00:00:00"

def process_pipeline():
    print(" Starting Omnichannel Order Pipeline execution...")
    
    cleaned_records = []
    
    # 1. Read and Parse Raw Data
    try:
        with open(RAW_DATA_PATH, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            
            for row in reader:
                # 2. Extract and Normalize Data Fields
                order_id = row.get("order_id", "").strip()
                source = row.get("source", "UNKNOWN").strip().upper()
                
                # Normalize values
                raw_date = row.get("order_date", "")
                clean_date = normalize_timestamp(raw_date)
                
                try:
                    # Clear white spaces and convert currency fields safely
                    gross_sales = float(row.get("gross_sales", 0).replace("$", "").strip())
                except ValueError:
                    gross_sales = 0.0
                
                # 3. Structure into uniform business standard
                clean_record = {
                    "order_id": order_id,
                    "platform_source": source,
                    "normalized_timestamp": clean_date,
                    "gross_sales_usd": round(gross_sales, 2)
                }
                cleaned_records.append(clean_record)
                
    except FileNotFoundError:
        print(f"❌ Error: The file '{RAW_DATA_PATH}' was not found. Please create it first.")
        return

    # 4. Write Clean Data to Destination
    fieldnames = ["order_id", "platform_source", "normalized_timestamp", "gross_sales_usd"]
    
    with open(CLEAN_DATA_PATH, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(cleaned_records)
        
    print(f"✅ Success! Processed {len(cleaned_records)} records into '{CLEAN_DATA_PATH}'.")

if __name__ == "__main__":
    process_pipeline()