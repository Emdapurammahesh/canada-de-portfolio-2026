import extract_crypto
import load_to_sql
import time
from datetime import datetime

def start_automated_pipeline():
    print("🚀 Starting Live Crypto Tracker... (Press Ctrl+C to stop)")
    
    while True:
        print(f"\n--- Cycle Started: {datetime.now().strftime('%H:%M:%S')} ---")
        
        try:
            # Step 1: Get the data
            extract_crypto.fetch_crypto_data()
            
            # Step 2: Load the data
            load_to_sql.load_json_to_sql()
            
            print("✅ Cycle Complete. Sleeping for 30 seconds...")
            
        except Exception as e:
            print(f"⚠️ Pipeline halted due to error: {e}")
            break
            
        # Wait for 30 seconds before doing it again
        time.sleep(30)

if __name__ == "__main__":
    start_automated_pipeline()