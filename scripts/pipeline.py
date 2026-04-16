import requests
import sqlite3
from datetime import datetime

def fetch_crypto_data():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd"
    response = requests.get(url)
    return response.json()

def transform_data(raw_data):
    processed = []
    for coin, price in raw_data.items():
        processed.append({
            "coin": coin,
            "price_usd": price["usd"],
            "timestamp": datetime.now().isoformat()
        })
    return processed

def load_to_db(data):
    conn = sqlite3.connect('crypto_data.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS prices 
                      (coin TEXT, price_usd REAL, timestamp TEXT)''')
    
    for item in data:
        cursor.execute("INSERT INTO prices VALUES (?, ?, ?)", 
                       (item['coin'], item['price_usd'], item['timestamp']))
    
    conn.commit()
    conn.close()
    print(f"Successfully loaded {len(data)} records at {datetime.now()}")

if __name__ == "__main__":
    raw = fetch_crypto_data()
    clean = transform_data(raw)
    load_to_db(clean)