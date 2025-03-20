from flask import Flask, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)  # Enable external access

# ✅ REPLACE WITH YOUR API KEY
API_KEY = "oCs9mC2usDSZRAJslhDJA4BbrBPl"
SYMBOL = "QQQ"  # Change symbol if needed
EXPIRATION_DATE = "2025-03-20"  # Adjust as needed

# ✅ API Endpoints
STOCK_URL = f"https://api.tradier.com/v1/markets/quotes?symbols={SYMBOL}&includeExtendedHours=true"
OPTIONS_URL = f"https://api.tradier.com/v1/markets/options/chains?symbol={SYMBOL}&expiration={EXPIRATION_DATE}"

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Accept": "application/json"
}

@app.route('/stock', methods=['GET'])
def get_stock():
    """Fetch real-time stock price."""
    response = requests.get(STOCK_URL, headers=HEADERS)
    if response.status_code == 200:
        return jsonify(response.json()["quotes"]["quote"])
    else:
        return jsonify({"error": "Failed to fetch stock data"}), 500

@app.route('/options', methods=['GET'])
def get_options():
    """Fetch real-time options chain."""
    response = requests.get(OPTIONS_URL, headers=HEADERS)
    if response.status_code == 200:
        return jsonify(response.json()["options"]["option"])
    else:
        return jsonify({"error": "Failed to fetch options data"}), 500

@app.route('/')
def home():
    return jsonify({"message": "Welcome to your real-time market data API!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
