import pandas as pd

DATA_PATH = "data/SMSSpamCollection"


def load_data():
    df = pd.read_csv(
        DATA_PATH,
        sep="\t",
        header=None,
        names=["label", "message"]
    )

    return df


def clean_data(df):
    df = df.dropna()
    df = df.drop_duplicates()

    return df


if __name__ == "__main__":
    data = load_data()
    data = clean_data(data)

    print("Dataset loaded successfully!")
    print(f"Total messages: {len(data)}")
    print("\nClass distribution:")
    print(data["label"].value_counts())
