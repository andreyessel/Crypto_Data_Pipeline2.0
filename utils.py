from sqlalchemy.orm import Session
from models import CryptoPrice

def get_top_performers(db: Session, days: int = 7):
    """
    Returns the top performing cryptocurrencies over the last N days
    by percentage price increase.
    """
    symbols = db.query(CryptoPrice.symbol).distinct().all()
    results = []
    for (sym,) in symbols:
        records = (
            db.query(CryptoPrice)
            .filter(CryptoPrice.symbol == sym)
            .order_by(CryptoPrice.date.desc())
            .limit(days)
            .all()
        )
        if len(records) >= 2:
            change = ((records[0].close - records[-1].close) / records[-1].close) * 100
            results.append({"symbol": sym, "change_percent": round(change, 2)})
    results.sort(key=lambda x: x["change_percent"], reverse=True)
    return results