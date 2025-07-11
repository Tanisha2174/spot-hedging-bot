import os
import pandas as pd
import random
from datetime import datetime

def execute_hedge(asset, size):
    delta = size * 0.9
    vol = round(random.uniform(0.1, 0.3), 2)
    price = round(random.uniform(100, 200), 2)
    pnl = round((price - 100) * size, 2)
    now = datetime.now().isoformat()

    # Check if file exists and has headers
    file_path = "data/hedge_logs.csv"
    if not os.path.exists(file_path) or os.stat(file_path).st_size == 0:
        df = pd.DataFrame(columns=["timestamp", "asset", "size", "delta", "volatility", "price", "pnl"])
    else:
        df = pd.read_csv(file_path)

    new_row = {
        "timestamp": now,
        "asset": asset,
        "size": size,
        "delta": delta,
        "volatility": vol,
        "price": price,
        "pnl": pnl
    }

    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    df.to_csv(file_path, index=False)

    return f"✅ Hedge executed for {asset}.\nSize: {size}, Δ: {delta:.2f}, Vol: {vol}, PnL: ₹{pnl}"
