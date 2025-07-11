import numpy as np
import tensorflow as tf
from keras.models import Sequential
from keras.layers import LSTM, Dense

def forecast_volatility(asset):
    model = Sequential([
        LSTM(10, input_shape=(10, 1)),
        Dense(1)
    ])
    x_dummy = np.random.rand(1, 10, 1)
    y_pred = model(x_dummy)
    return float(y_pred.numpy().flatten()[0])
