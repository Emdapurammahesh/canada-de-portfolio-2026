import requests
import json
from datetime import datetime

def fetch_crypto_data():
    # 1. Define the API endpoint
    # We are asking for prices in USD and including 24h volume/change
    URL = "https://api.coingecko.com/api/v3/simple/price"
    PARAMS = {
        'ids': 'bitcoin,ethereum,solana',
        'vs_currencies': 'usd',
        'include_24hr_vol': 'true',
        'include_24hr_change': 'true'
    }

    try:
        print(f"[{datetime.now()}] Fetching data from CoinGecko...")
        response = requests.get(URL, params=PARAMS)
        
        # 2. Check if the request was successful
        response.raise_for_status() 
        
        data = response.json()

        # 3. Add Metadata (Crucial for Data Engineering!)
        # We record exactly when we pulled this data
        enriched_data = {
            "metadata": {
                "extracted_at": datetime.utcnow().isoformat(),
                "source": "CoinGecko"
            },
            "data": data
        }

        # 4. Save to a "Landing Zone" (Local JSON file)
        with open('raw_crypto_data.json', 'w') as f:
            json.dump(enriched_data, f, indent=4)
            
        print("✅ Extraction successful! Data saved to raw_crypto_data.json")

    except Exception as e:
        print(f"❌ Error during extraction: {e}")

if __name__ == "__main__":
    fetch_crypto_data()