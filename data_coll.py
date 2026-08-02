import yfinance as yf
import pandas as pd
from ta.momentum import RSIIndicator
from ta.trend import MACD

stocks = {
    "RELIANCE": "RELIANCE.NS",
    "HDFCBANK": "HDFCBANK.NS",
    "TCS": "TCS.NS"
}

all_data = []

for stock_name, ticker in stocks.items():

    print(f"Downloading {stock_name}...")

    df = yf.download(
        ticker,
        start="2019-01-01",
        end="2025-06-01",
        auto_adjust=False,
        progress=False
    )

    # Fix MultiIndex columns from newer yfinance versions
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)

    df.reset_index(inplace=True)

    df["Stock"] = stock_name

    # Ensure Close is a Series
    close = df["Close"].squeeze()

    # Technical Indicators
    df["RSI"] = RSIIndicator(close=close, window=14).rsi()

    macd = MACD(close=close)
    df["MACD"] = macd.macd()

    df["SMA_20"] = close.rolling(window=20).mean()

    df["EMA_20"] = close.ewm(
        span=20,
        adjust=False
    ).mean()

    # Target Variable
    df["Next_Day_Close"] = close.shift(-1)

    all_data.append(df)

# Combine all stocks
final_df = pd.concat(
    all_data,
    ignore_index=True
)

# Remove rows with NaN values
final_df.dropna(inplace=True)

# Keep only required columns
final_df = final_df[
    [
        "Date",
        "Stock",
        "Open",
        "High",
        "Low",
        "Close",
        "Volume",
        "RSI",
        "MACD",
        "SMA_20",
        "EMA_20",
        "Next_Day_Close"
    ]
]

# Save Dataset
final_df.to_csv(
    "stock_prediction_dataset.csv",
    index=False
)

print("\nDataset Created Successfully!")
print("Shape:", final_df.shape)
print("\nFirst 5 Rows:")
print(final_df.head())

print("\nDataset saved as:")
print("stock_prediction_dataset.csv")