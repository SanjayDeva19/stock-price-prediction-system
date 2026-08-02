# 📈 Stock Price Prediction and Investment Recommendation System

An end-to-end Machine Learning application that predicts the **next-day closing price** of stocks and provides **Buy, Hold, or Sell recommendations** along with **investment risk analysis**. The project leverages historical stock market data, technical indicators, and the XGBoost algorithm to assist investors in making informed decisions.

---

## 🚀 Features

- 📊 Historical stock data collection using Yahoo Finance
- 📈 Feature engineering with technical indicators:
  - RSI (Relative Strength Index)
  - MACD (Moving Average Convergence Divergence)
  - SMA (Simple Moving Average)
  - EMA (Exponential Moving Average)
- 🤖 Machine Learning model using XGBoost Regressor
- 🔮 Next-day stock price prediction
- 💹 Buy / Hold / Sell recommendation engine
- ⚠️ Risk assessment based on stock price volatility
- 🌐 REST API built with FastAPI
- 📊 Interactive dashboard developed using Streamlit
- 📉 Candlestick, RSI, and MACD visualizations

---

## 🛠️ Tech Stack

| Category | Technologies |
|----------|--------------|
| Programming Language | Python |
| Machine Learning | XGBoost, Scikit-learn |
| Backend | FastAPI |
| Frontend | Streamlit |
| Data Analysis | Pandas, NumPy |
| Visualization | Plotly |
| Data Source | Yahoo Finance (yfinance) |
| Technical Indicators | TA Library |
| Model Persistence | Joblib |
| Version Control | Git & GitHub |

---

## 📂 Project Structure

```text
Stock-Price-Prediction-System/
│
├── app.py                     # FastAPI backend
├── streamlit_app.py           # Streamlit frontend
├── train_model.py             # Model training script
├── predict.py                 # Prediction logic
├── recommendation.py          # Buy/Hold/Sell recommendation engine
├── preprocessing.py           # Data preprocessing
├── data_coll.py               # Data collection using Yahoo Finance
├── model.pkl                  # Trained XGBoost model
├── stock_prediction_dataset.csv
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Workflow

```
Yahoo Finance
      │
      ▼
Historical Data Collection
      │
      ▼
Feature Engineering
(RSI, MACD, SMA, EMA)
      │
      ▼
Data Preprocessing
      │
      ▼
XGBoost Model Training
      │
      ▼
Model Evaluation
      │
      ▼
FastAPI Prediction API
      │
      ▼
Recommendation Engine
      │
      ▼
Streamlit Dashboard
```

---

## 📷 Application Screenshots

### Dashboard

> Add your dashboard screenshot here.

```
screenshots/dashboard.png
```

---

### Prediction Result

> Add your prediction result screenshot here.

```
screenshots/prediction.png
```

---

## 📦 Installation

### Clone the repository

```bash
git clone https://github.com/SanjayDeva19/stock-price-prediction-system.git

cd stock-price-prediction-system
```

### Create a virtual environment

```bash
python -m venv .venv
```

### Activate the virtual environment

**Windows**

```bash
.venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Project

### Start FastAPI Server

```bash
uvicorn app:app --reload
```

Server runs at:

```
http://127.0.0.1:8000
```

---

### Launch Streamlit Dashboard

```bash
streamlit run streamlit_app.py
```

---

## 📊 Supported Stocks

- Reliance Industries
- HDFC Bank
- Tata Consultancy Services (TCS)

---

## 📈 Machine Learning Model

Algorithm used:

- **XGBoost Regressor**

Evaluation Metrics:

- Mean Absolute Error (MAE)
- R² Score

---

## 💡 Future Enhancements

- LSTM and GRU-based deep learning models
- Real-time stock data streaming
- News sentiment analysis
- Portfolio optimization
- Cloud deployment (AWS/Azure)
- Multi-stock comparison
- Explainable AI (SHAP/LIME)

---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

Feel free to fork the repository and submit a Pull Request.

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Sanjay Deva V**

- GitHub: https://github.com/SanjayDeva19
- LinkedIn: www.linkedin.com/in/sanjaydeva19

---

⭐ If you found this project useful, don't forget to **Star** the repository!
