import requests

BASE_URL = "https://gamma-api.polymarket.com"

def get_market(market_id):
    r = requests.get(f"{BASE_URL}/markets/{market_id}", timeout=10)
    r.raise_for_status()
    return r.json()
