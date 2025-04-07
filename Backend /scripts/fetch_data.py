import requests
import json
import time
from scripts.store_data import save_to_db  # Import save function

# NSE URL for fetching live stock data
NSE_URL = "https://www.nseindia.com/api/quote-equity?symbol={}"

# Headers to mimic a browser request
HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br"
}

# List of NIFTY 50 stock symbols
NIFTY50_SYMBOLS = ["RELIANCE", "TCS", "INFY", "HDFCBANK", "ICICIBANK"]

def fetch_nse_stock_price(symbol):
    url = NSE_URL.format(symbol)
    try:
        response = requests.get(url, headers=HEADERS, timeout=5)
        response.raise_for_status()
        data = response.json()
        last_price = data["priceInfo"]["lastPrice"]
        print(f"{symbol} Live Price: {last_price}")
        return last_price
    except Exception as e:
        print(f"Error fetching {symbol}: {e}")
        return None

def fetch_all_nifty50():
    stock_prices = {}
    for symbol in NIFTY50_SYMBOLS:
        price = fetch_nse_stock_price(symbol)
        if price:
            stock_prices[symbol] = price
            save_to_db(symbol, price)  # Save to MySQL
    return stock_prices

# Fetch and store stock data every second
if __name__ == "__main__":
    while True:
        fetch_all_nifty50()
        time.sleep(1)
