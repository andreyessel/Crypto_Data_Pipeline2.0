from database import Base, engine
from etl import fetch_crypto_data, save_to_db

# Create database tables
Base.metadata.create_all(bind=engine)

# Fetch last 30 days of Bitcoin prices
df = fetch_crypto_data(symbol="bitcoin", days=30)
save_to_db(df, symbol="BTC")

print("Crypto Data Pipeline executed successfully!")