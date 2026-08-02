import pandas as pd


def preprocess_data(df):

    # Remove missing values
    df.dropna(inplace=True)

    # Remove duplicate rows
    df.drop_duplicates(inplace=True)

    # Convert Date column
    df["Date"] = pd.to_datetime(df["Date"])

    # Sort by date
    df.sort_values("Date", inplace=True)

    return df