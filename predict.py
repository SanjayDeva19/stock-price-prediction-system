import pandas as pd
import joblib

model = joblib.load("model.pkl")

df = pd.read_csv("stock_prediction_dataset.csv")

latest = df.iloc[-1]

features = [[
    latest["Open"],
    latest["High"],
    latest["Low"],
    latest["Close"],
    latest["Volume"],
    latest["RSI"],
    latest["MACD"],
    latest["SMA_20"],
    latest["EMA_20"]
]]

prediction = model.predict(features)[0]

print("Current Price:", latest["Close"])
print("Predicted Next Day Price:", prediction)