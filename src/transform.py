import pandas as pd


def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Select, rename and clean relevant columns from the raw DataFrame.

    Args:
        df (pd.DataFrame): Raw DataFrame.

    Returns:
        pd.DataFrame: Transformed DataFrame.
    """
    columns = [
        "id",
        "symbol",
        "name",
        "current_price",
        "market_cap",
        "total_volume",
        "price_change_percentage_24h",
    ]

    transformed_df = df[columns].copy()

    transformed_df.rename(
        columns={
            "current_price": "price_usd",
            "market_cap": "market_cap_usd",
            "total_volume": "volume_usd_24h",
            "price_change_percentage_24h": "change_pct_24h",
        },
        inplace=True,
    )

    transformed_df["symbol"] = transformed_df["symbol"].str.upper()
    transformed_df["name"] = transformed_df["name"].str.strip()

    return transformed_df