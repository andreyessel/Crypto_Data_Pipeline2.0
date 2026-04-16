# main.py
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import Base, engine, get_db
from models import CryptoPrice
from schemas import CryptoPriceSchema
from etl import fetch_crypto_data, save_to_db

# Create database tables
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI(title="Cryptocurrency Data Pipeline API")

# --------------------------
# API Endpoints
# --------------------------

# Fetch all records for a symbol
@app.get("/prices/{symbol}", response_model=List[CryptoPriceSchema])
def get_prices(symbol: str, db: Session = Depends(get_db)):
    records = db.query(CryptoPrice).filter(CryptoPrice.symbol == symbol.upper()).all()
    if not records:
        raise HTTPException(status_code=404, detail="No records found")
    return records

# Fetch latest N days for a symbol
@app.get("/prices/{symbol}/latest/{days}", response_model=List[CryptoPriceSchema])
def get_latest_prices(symbol: str, days: int, db: Session = Depends(get_db)):
    records = (
        db.query(CryptoPrice)
        .filter(CryptoPrice.symbol == symbol.upper())
        .order_by(CryptoPrice.date.desc())
        .limit(days)
        .all()
    )
    if not records:
        raise HTTPException(status_code=404, detail="No records found")
    return records

# Trigger manual update for a symbol from the API
@app.post("/update/{symbol}")
def update_prices(symbol: str, db: Session = Depends(get_db)):
    try:
        df = fetch_crypto_data(symbol=symbol.lower(), days=30)
        save_to_db(df, symbol=symbol.upper())
        return {"message": f"{symbol.upper()} prices updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Update failed: {e}")