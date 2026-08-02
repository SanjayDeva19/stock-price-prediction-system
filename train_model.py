import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score
from xgboost import XGBRegressor
import joblib

# Load dataset
from preprocessing import preprocess_data

df = pd.read_csv("stock_prediction_dataset.csv")

df = preprocess_data(df)

# Features
X = df[
    [
        "Open",
        "High",
        "Low",
        "Close",
        "Volume",
        "RSI",
        "MACD",
        "SMA_20",
        "EMA_20"
    ]
]

# Target
y = df["Next_Day_Close"]

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Model
model = XGBRegressor(
    n_estimators=100,
    learning_rate=0.1,
    max_depth=5,
    random_state=42
)

model.fit(X_train, y_train)

# Prediction
pred = model.predict(X_test)

# Evaluation
mae = mean_absolute_error(y_test, pred)
r2 = r2_score(y_test, pred)

print("MAE:", mae)
print("R2 Score:", r2)

# Save model
joblib.dump(model, "model.pkl")

print("Model Saved!")