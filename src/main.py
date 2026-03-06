from extract import extract_data
from transform import transform_data
from load import save_csv


RAW_PATH = "data/raw/crypto_raw.csv"
PROCESSED_PATH = "data/processed/crypto_processed.csv"


def main() -> None:
    try:
        raw_df = extract_data()
        save_csv(raw_df, RAW_PATH)

        processed_df = transform_data(raw_df)
        save_csv(processed_df, PROCESSED_PATH)

        print("Pipeline executed successfully.")
        print(processed_df.head())

    except Exception as error:
        print(f"Error while running pipeline: {error}")


if __name__ == "__main__":
    main()