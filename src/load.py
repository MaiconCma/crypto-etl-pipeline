import os
import pandas as pd


def save_csv(df: pd.DataFrame, path: str) -> None:
    """
    Save a DataFrame to CSV.

    Args:
        df (pd.DataFrame): DataFrame to be saved.
        path (str): Output file path.
    """
    os.makedirs(os.path.dirname(path), exist_ok=True)
    df.to_csv(path, index=False)