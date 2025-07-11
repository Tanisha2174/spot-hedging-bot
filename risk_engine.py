import random
from volatility_forecaster import forecast_volatility

def monitor_risk(asset, size):
    delta = random.uniform(-1, 1) * size
    VaR = abs(delta) * 0.1
    volatility_forecast = forecast_volatility(asset)
    return {
        "delta": delta,
        "VaR": VaR,
        "volatility_forecast": volatility_forecast
    }
