import os
import pandas as pd


def save_raw_data(df: pd.DataFrame, path: str = "data/raw/crypto_raw.csv") -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    df.to_csv(path, index=False)


def save_processed_data(df: pd.DataFrame, path: str = "data/processed/crypto_processed.csv") -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    df.to_csv(path, index=False)