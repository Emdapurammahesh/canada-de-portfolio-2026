import json
import sqlite3
from datetime import datetime

def load_json_to_sql():
    # 1. Load the raw data from our JSON file
    with open('raw_crypto_data.json', 'r') as f:
        content = json.load(f)
    
    metadata = content['metadata']
    crypto_data = content['data']

    # 2. Connect to (or create) our SQLite Database
    # This creates a file named 'crypto_warehouse.db'
    conn = sqlite3.connect('crypto_warehouse.db')
    cursor = conn.cursor()

    # 3. Create the table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS prices (
            coin_id TEXT,
            price_usd REAL,
            vol_24h REAL,
            change_24h REAL,
            extracted_at TEXT
        )
    ''')

    # 4. Transform and Insert
    # We loop through the 'data' dictionary to flatten it
    for coin, stats in crypto_data.items():
        row = (
            coin, 
            stats['usd'], 
            stats['usd_24h_vol'], 
            stats['usd_24h_change'], 
            metadata['extracted_at']
        )
        
        cursor.execute('''
            INSERT INTO prices (coin_id, price_usd, vol_24h, change_24h, extracted_at)
            VALUES (?, ?, ?, ?, ?)
        ''', row)

    # 5. Commit and Close
    conn.commit()
    conn.close()
    print("✅ Data successfully flattened and loaded into 'crypto_warehouse.db'")

if __name__ == "__main__":
    load_json_to_sql()