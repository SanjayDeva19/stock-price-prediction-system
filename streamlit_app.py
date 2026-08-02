import streamlit as st
import pandas as pd
import requests
import plotly.express as px
import plotly.graph_objects as go

# ----------------------------------
# Page Configuration
# ----------------------------------
st.set_page_config(
    page_title="Stock Price Prediction System",
    page_icon="📈",
    layout="wide"
)

# ----------------------------------
# Title
# ----------------------------------
st.title("Stock Price Prediction and Investment Recommendation System")

# ----------------------------------
# Load Dataset
# ----------------------------------
from preprocessing import preprocess_data

df = pd.read_csv("stock_prediction_dataset.csv")

df = preprocess_data(df)
df["Date"] = pd.to_datetime(df["Date"])

# ----------------------------------
# Stock Selection
# ----------------------------------
stock = st.selectbox(
    "Select Stock",
    df["Stock"].unique()
)

stock_df = df[df["Stock"] == stock]

# ----------------------------------
# Candlestick Chart
# ----------------------------------
st.subheader(f"{stock} Candlestick Chart")

fig_candle = go.Figure()

fig_candle.add_trace(
    go.Candlestick(
        x=stock_df["Date"],
        open=stock_df["Open"],
        high=stock_df["High"],
        low=stock_df["Low"],
        close=stock_df["Close"],
        name=stock
    )
)

# SMA 20
fig_candle.add_trace(
    go.Scatter(
        x=stock_df["Date"],
        y=stock_df["SMA_20"],
        mode="lines",
        name="SMA 20"
    )
)

# EMA 20
fig_candle.add_trace(
    go.Scatter(
        x=stock_df["Date"],
        y=stock_df["EMA_20"],
        mode="lines",
        name="EMA 20"
    )
)

fig_candle.update_layout(
    title=f"{stock} Stock Price Movement",
    xaxis_title="Date",
    yaxis_title="Price (₹)",
    xaxis_rangeslider_visible=False,
    height=650
)

st.plotly_chart(fig_candle, use_container_width=True)

# ----------------------------------
# RSI Chart
# ----------------------------------
st.subheader("RSI Indicator")

fig_rsi = px.line(
    stock_df,
    x="Date",
    y="RSI",
    title=f"{stock} RSI"
)

st.plotly_chart(fig_rsi, use_container_width=True)

# ----------------------------------
# MACD Chart
# ----------------------------------
st.subheader("MACD Indicator")

fig_macd = px.line(
    stock_df,
    x="Date",
    y="MACD",
    title=f"{stock} MACD"
)

st.plotly_chart(fig_macd, use_container_width=True)

# ----------------------------------
# Risk Analysis
# ----------------------------------
st.subheader("Risk Analysis")

returns = stock_df["Close"].pct_change()
volatility = returns.std()

if volatility < 0.01:
    risk = "Low"
elif volatility < 0.02:
    risk = "Medium"
else:
    risk = "High"

st.metric(
    label="Risk Score",
    value=risk
)

# ----------------------------------
# Prediction Section
# ----------------------------------
st.subheader("Stock Prediction")

if st.button("Predict Next Day Price"):

    try:
        response = requests.get(
            f"http://127.0.0.1:8000/predict/{stock}"
        )

        result = response.json()

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Current Price",
                f"₹{result['current_price']:.2f}"
            )

        with col2:
            st.metric(
                "Predicted Price",
                f"₹{result['predicted_price']:.2f}"
            )

        with col3:
            st.metric(
                "Recommendation",
                result["signal"]
            )

        st.success(
            f"Risk Score: {result['risk_score']}"
        )

    except Exception as e:
        st.error(
            f"Unable to connect to FastAPI server.\n\nError: {e}"
        )

# ----------------------------------
# Latest Stock Information
# ----------------------------------
st.subheader("Latest Stock Information")

latest = stock_df.iloc[-1]

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Close Price",
        f"₹{latest['Close']:.2f}"
    )

with col2:
    st.metric(
        "RSI",
        f"{latest['RSI']:.2f}"
    )

with col3:
    st.metric(
        "MACD",
        f"{latest['MACD']:.2f}"
    )

with col4:
    st.metric(
        "Volume",
        f"{int(latest['Volume']):,}"
    )

# ----------------------------------
# Footer
# ----------------------------------
st.markdown("---")
st.caption(
    "Stock Price Prediction and Investment Recommendation System | FastAPI + Streamlit + XGBoost"
)