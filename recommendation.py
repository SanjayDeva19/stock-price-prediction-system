def get_signal(current_price, predicted_price):

    if predicted_price > current_price * 1.02:
        return "BUY"

    elif predicted_price < current_price * 0.98:
        return "SELL"

    else:
        return "HOLD"