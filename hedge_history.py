import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

def get_hedge_history():
    df = pd.read_csv("data/hedge_logs.csv")
    df["pnl"] = df["delta"] * (df["price"] - df["price"].shift(1).fillna(100))
    df["cum_pnl"] = df["pnl"].cumsum()
    return df

def generate_pnl_chart(asset):
    df = get_hedge_history()
    df = df[df["asset"] == asset]
    if df.empty:
        return None
    plt.figure(figsize=(10, 5))
    plt.plot(pd.to_datetime(df["timestamp"]), df["cum_pnl"], marker="o", label="Cumulative PnL")
    plt.title(f"Cumulative P&L - {asset}")
    plt.xlabel("Timestamp")
    plt.ylabel("₹ P&L")
    plt.grid(True)
    plt.legend()
    path = f"data/pnl_chart_{asset}.png"
    plt.tight_layout()
    plt.savefig(path)
    plt.close()
    return path
