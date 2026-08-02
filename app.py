from fastapi import FastAPI
import pandas as pd
import joblib

app = FastAPI()

model = joblib.load("model.pkl")
df = pd.read_csv("stock_prediction_dataset.csv")


@app.get("/")
def home():
    return {"message": "Stock Prediction API"}


@app.get("/predict/{stock}")
def predict(stock: str):

    stock = stock.upper()

    stock_df = df[df["Stock"] == stock]

    if stock_df.empty:
        return {"error": "Stock not found"}

    latest = stock_df.iloc[-1]

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

    predicted_price = float(model.predict(features)[0])

    current_price = float(latest["Close"])

    if predicted_price > current_price * 1.02:
        signal = "BUY"
    elif predicted_price < current_price * 0.98:
        signal = "SELL"
    else:
        signal = "HOLD"

    returns = stock_df["Close"].pct_change()
    volatility = returns.std()

    if volatility < 0.01:
        risk = "Low"
    elif volatility < 0.02:
        risk = "Medium"
    else:
        risk = "High"

    return {
        "stock": stock,
        "current_price": current_price,
        "predicted_price": predicted_price,
        "signal": signal,
        "risk_score": risk
    }