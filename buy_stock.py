import alpaca_trade_api as tradeapi

API_KEY = 'PK3HK1FANI4LF632XXME'
API_SECRET = 'iITCsTwcC5xfwJWLHUsw1GcIAtuO6eLTypNOHffZ'
BASE_URL = 'https://paper-api.alpaca.markets'  # Use the paper trading URL

api = tradeapi.REST(API_KEY, API_SECRET, BASE_URL, api_version='v2')

def buy_stock(symbol, qty):
    api.submit_order(
        symbol=symbol,
        qty=qty,
        side='buy',
        type='market',
        time_in_force='gtc'
    )

if __name__ == '__main__':
    buy_stock('AAPL', 1)  # Example: Buy 1 share of Apple
