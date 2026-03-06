import requests
import pandas as pd


def extract_data() -> pd.DataFrame:
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 20,
        "page": 1,
        "sparkline": False
    }

    response = requests.get(url, params=params, timeout=30)
    response.raise_for_status()

    data = response.json()
    df = pd.DataFrame(data)
    return df