import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ✅ REPLACE with your Ngrok API URL
API_URL_STOCK = "https://8543-135-134-196-134.ngrok-free.app/stock"
API_URL_OPTIONS = "https://8543-135-134-196-134.ngrok-free.app/options"

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

# ✅ Analyze stock price movement
def analyze_stock(data):
    print("\n📊 Stock Data Analysis 📊")
    print(f"Symbol: {data['symbol']}")
    print(f"Last Price: ${data['last']:.2f}")
    print(f"Bid: ${data['bid']:.2f}, Ask: ${data['ask']:.2f}")
    
    # Simple Moving Averages
    prices = [data["last"], data["bid"], data["ask"]]
    sma = np.mean(prices)
    print(f"Simple Moving Average (SMA): ${sma:.2f}")

    # Display price chart
    plt.figure(figsize=(6, 3))
    plt.bar(["Last Price", "Bid", "Ask"], prices, color=['blue', 'red', 'green'])
    plt.title(f"{data['symbol']} Price Analysis")
    plt.ylabel("Price ($)")
    plt.show()

# ✅ Analyze options chain
def analyze_options(data):
    print("\n📈 Options Chain Analysis 📈")
    
    # Convert to DataFrame
    df = pd.DataFrame(data)
    df = df[df['option_type'] == 'call']  # Filter for Call options
    df = df.sort_values(by='strike')  # Sort by strike price

    print(df[["symbol", "strike", "last", "bid", "ask"]].head(10))  # Show top 10 strikes
    
    # Plot Option Prices
    plt.figure(figsize=(8, 4))
    plt.plot(df["strike"], df["last"], marker='o', label="Last Price")
    plt.plot(df["strike"], df["bid"], marker='x', label="Bid Price")
    plt.plot(df["strike"], df["ask"], marker='s', label="Ask Price")
    plt.xlabel("Strike Price")
    plt.ylabel("Option Price ($)")
    plt.title("Call Options Price vs. Strike Price")
    plt.legend()
    plt.show()

# ✅ Run the analysis
stock_data = get_stock_data()
if stock_data:
    analyze_stock(stock_data)

options_data = get_options_data()
if options_data:
    analyze_options(options_data)
