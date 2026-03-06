import pandas as pd


def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    columns = [
        "id",
        "symbol",
        "name",
        "current_price",
        "market_cap",
        "total_volume",
        "price_change_percentage_24h"
    ]

    df = df[columns].copy()

    df.rename(columns={
        "current_price": "price_usd",
        "market_cap": "market_cap_usd",
        "total_volume": "volume_usd_24h",
        "price_change_percentage_24h": "change_pct_24h"
    }, inplace=True)

    df["symbol"] = df["symbol"].str.upper()
    df["name"] = df["name"].str.strip()

    return df