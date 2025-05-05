import requests
response = requests.get('https://cdn.india.deltaex.org/v2/products')
# Fetch products
def product_api():
    products = response.json()
    print(products)

def tickers_api():
    symbol = "BTCUSD"  # Example symbol
    response = requests.get("https://cdn.india.deltaex.org/v2/tickers" + f"/{symbol}")
    ticker_info = response.json()
    print(ticker_info)

def historical_data_api():
    params = {
        'resolution': "1m",
        'symbol': "BTCUSD",
        'start': "1712745270",
        'end': "1712746220"
    }
    response = requests.get("https://cdn.india.deltaex.org/v2/history/candles", params=params)
    historical_data = response.json()
    print(historical_data)

import hashlib
import hmac
import json
import time

api_key = 'your-api-key'
api_secret = 'your-api-secret'

# Create the signature
def generate_signature(method, endpoint, payload):
    timestamp = str(int(time.time()))
    signature_data = method + timestamp + endpoint + payload
    message = bytes(signature_data, 'utf-8')
    secret = bytes(api_secret, 'utf-8')
    hash = hmac.new(secret, message, hashlib.sha256)
    return hash.hexdigest(), timestamp
def orders():
    # Prepare the order data
    order_data = {
        'product_id': 27,  # Product ID for BTCUSD is 27
        'size': 1,
        'order_type': 'market_order',
        'side': 'buy'
    }
    
    body = json.dumps(order_data, separators=(',', ':'))
    method = 'POST'
    endpoint = '/v2/orders'
    signature, timestamp = generate_signature(method, endpoint, body)
    # Add the API key and signature to the request headers
    headers = {
        'api-key': api_key,
        'signature': signature,
        'timestamp': timestamp,
        'Content-Type': 'application/json'
    }
    response = requests.post('https://cdn.india.deltaex.org/v2/orders', headers=headers, data=body)
    order_response = response.json()
    print(order_response)

tickers_api()
