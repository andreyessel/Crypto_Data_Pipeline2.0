import requests
import pandas as pd
from sqlalchemy.orm import Session
from models import CryptoPrice
from database import get_db

def fetch_crypto_data(symbol="bitcoin", vs_currency="usd", days=30):
    """
    Fetch historical crypto prices from CoinGecko API.
    Returns a pandas DataFrame.
    """
    url = f"https://api.coingecko.com/api/v3/coins/{symbol}/market_chart"
    params = {"vs_currency": vs_currency, "days": days}
    response = requests.get(url, params=params)
    data = response.json()

    df = pd.DataFrame(data["prices"], columns=["timestamp", "price"])
    df["date"] = pd.to_datetime(df["timestamp"], unit="ms").dt.date
    df = df.groupby("date").agg(
        open=("price", "first"),
        high=("price", "max"),
        low=("price", "min"),
        close=("price", "last")
    ).reset_index()
    return df

def save_to_db(df: pd.DataFrame, symbol="BTC"):
    """
    Save processed crypto data to the database.
    """
    db: Session = next(get_db())
    for _, row in df.iterrows():
        crypto = CryptoPrice(
            symbol=symbol,
            date=row["date"],
            open=row["open"],
            high=row["high"],
            low=row["low"],
            close=row["close"],
            volume=0  # Placeholder for future enhancement
        )
        db.add(crypto)
    db.commit()