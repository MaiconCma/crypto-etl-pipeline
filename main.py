from extract import extract_data
from transform import transform_data
from load import save_raw_data, save_processed_data


def main() -> None:
    raw_df = extract_data()
    save_raw_data(raw_df)

    processed_df = transform_data(raw_df)
    save_processed_data(processed_df)

    print("Pipeline executado com sucesso.")
    print(processed_df.head())


if __name__ == "__main__":
    main()