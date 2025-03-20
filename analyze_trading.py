import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import ta  # Technical Analysis Library

# ✅ Your Flask API URLs
API_URL_STOCK = "https://ff58-135-134-196-134.ngrok-free.app/stock"
API_URL_OPTIONS = "https://ff58-135-134-196-134.ngrok-free.app/options"

# ✅ Fetch stock data
def get_stock_data():
    response = requests.get(API_URL_STOCK)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching stock data:", response.text)
        return None

# ✅ Fetch options data
def get_options_data():
    response = requests.get(API_URL_OPTIONS)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching options data:", response.text)
        return None

# ✅ Analyze Stock Price Movement
def analyze_stock(data):
    print("\n📊 Stock Data Analysis 📊")
    print(f"Symbol: {data['symbol']}")
    print(f"Last Price: ${data['last']:.2f}")
    print(f"Bid: ${data['bid']:.2f}, Ask: ${data['ask']:.2f}")

    # Simple Moving Averages
    prices = [data["last"], data["bid"], data["ask"]]
    sma = np.mean(prices)
    print(f"Simple Moving Average (SMA): ${sma:.2f}")

    # RSI Calculation (Example)
    rsi = np.random.randint(30, 70)  # Placeholder RSI (Replace with real data)
    print(f"Relative Strength Index (RSI): {rsi}")

    # Display price chart
    plt.figure(figsize=(6, 3))
    plt.bar(["Last Price", "Bid", "Ask"], prices, color=['blue', 'red', 'green'])
    plt.title(f"{data['symbol']} Price Analysis")
    plt.ylabel("Price ($)")
    plt.show()

# ✅ Analyze Options Chain
def analyze_options(data):
    print("\n📈 Options Chain Analysis 📈")

    # Convert to DataFrame
    df = pd.DataFrame
