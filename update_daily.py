from etl import fetch_crypto_data, save_to_db

# List of symbols to update daily
symbols = ["BTC", "ETH", "ADA"]

for sym in symbols:
    df = fetch_crypto_data(symbol=sym.lower(), days=1)
    save_to_db(df, symbol=sym)
print("Daily update complete")