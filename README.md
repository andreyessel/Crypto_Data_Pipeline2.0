# Cryptocurrency Data Processing Pipeline2.0 
 
![Python](https://img.shields.io/badge/Python-3.11-blue) ![FastAPI](https://img.shields.io/badge/FastAPI-0.111.0-green) ![SQLite](https://img.shields.io/badge/Database-SQLite-orange) 
 
## Overview 
This project is a **data pipeline and REST API** for fetching, processing, storing, and analyzing cryptocurrency prices. 
It uses **FastAPI**, **SQLAlchemy**, and **Pandas**, with data fetched from the **CoinGecko API**. 
 
## Features 
- Fetch historical cryptocurrency prices (BTC, ETH, ADA, etc.) 
- Store prices in a database (SQLite by default) 
- Query data via REST API endpoints 
- Fetch latest N days of prices 
- Trigger manual updates from API 
- Analytics: top-performing assets over a period 
 
## Tech Stack 
- Python 3.x 
- FastAPI 
- SQLAlchemy (SQLite) 
- Pandas 
- Uvicorn (ASGI server) 
 
## Setup Instructions 
```bash 
git clone https://github.com/andreyessel/Crypto_Data_Pipeline2.0.git 
cd crypto_data_pipeline 
python -m venv venv 
venv\Scripts\activate 
pip install -r requirements.txt 
uvicorn main:app --reload 
``` 
 
## API Endpoints 
 
## Example Requests 
**Fetch all BTC prices** 
```bash 
curl -X GET "http://127.0.0.1:8000/prices/BTC" 
``` 
**Fetch last 7 days BTC prices** 
```bash 
curl -X GET "http://127.0.0.1:8000/prices/BTC/latest/7" 
``` 
**Trigger BTC update** 
```bash 
curl -X POST "http://127.0.0.1:8000/update/BTC" 
``` 
 
## Analytics Example 
**Top-performing assets over the last 7 days** 
```bash 
curl -X GET "http://127.0.0.1:8000/analytics/top_performers" 
``` 
 
## License 
MIT License 
