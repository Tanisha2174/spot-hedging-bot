# 🛡️ Spot Hedging Bot

A real-time risk analytics and Telegram-based hedging assistant for monitoring crypto exposure and making informed hedging decisions.

## 🚀 Features

- Real-time Delta, VaR, and volatility calculation
- Telegram bot for position monitoring and manual hedging
- P&L attribution and execution history
- Button-based hedge execution via Telegram
- **Bonus (Optional)**: Interactive charts and visual analytics

---

## ⚙️ Installation

```bash
git clone <your-repo-url>
cd spot_hedging_bot
python -m venv venv
source venv/Scripts/activate  # or venv/bin/activate for Mac/Linux
pip install -r requirements.txt
```

Create a `.env` file:
```ini
TELEGRAM_TOKEN=<your_telegram_bot_token>
```

> 📌 **Exchange API keys are not required yet** — current version simulates hedge logic.

## 💬 Telegram Bot Commands

| Command | Description |
|---------|-------------|
| `/monitor_risk BTC 2 0.1` | Start monitoring BTC with position size 2 and threshold 10% |
| `/auto_hedge delta 0.05` | Register a strategy (not yet fully automated) |
| `/hedge_now BTC 2` | Manually trigger hedge of size 2 for BTC |
| `/hedge_status BTC` | View delta, VaR, volatility, and cumulative P&L |
| `/hedge_history BTC` | Show latest 5 hedge entries with P&L |
| `/pnl_chart BTC` | Creates a P&L chart for BTC |

**Inline buttons:**
- 📉 **Hedge Now** → Trigger an immediate hedge

## 📊 Bonus Features (Optional)

- Matplotlib-based P&L and delta plots (if enabled)
- Cumulative and per-trade P&L reporting
- Risk summaries with volatility forecast
- Basic LSTM model included for volatility forecasting

## 🧠 Built With

- **Python, Pandas, NumPy** – Risk and hedge calculations
- **TensorFlow (LSTM)** – Volatility prediction
- **python-telegram-bot** – Bot interface and command handling
- **Matplotlib** – Chart generation
- *(No CCXT or exchange API integration yet)*

## 🧪 Quick Start

1. **Add .env file:**
   ```bash
   TELEGRAM_TOKEN=your_bot_token
   ```

2. **Create necessary folders and CSV file:**
   ```bash
   mkdir -p data
   echo "timestamp,asset,size,delta,volatility,pnl" > data/hedge_logs.csv
   ```

3. **Launch bot:**
   ```bash
   python main.py
   ```

4. **Interact in Telegram:**
   ```bash
   /monitor_risk BTC 1.0 0.05
   ```

## 📁 Project Structure

```
spot_hedging_bot/
│
├── main.py                         # Bot entrypoint
├── telegram_bot.py                 # Telegram handlers and UI
├── risk_engine.py                 # Risk calculation: delta, VaR, volatility
├── volatility_forecaster.py       # RNN volatility predictor
├── hedger.py                      # Hedge execution logic and logging
├── hedge_history.py               # Reads from hedge_logs.csv
├── analytics.py                   # (Optional) Plotting for risk/PnL visualization
├── utils.py                       # Helper functions (optional)
├── data/
│   └── hedge_logs.csv             # Log of hedge history
├── .env                           # Telegram token
└── requirements.txt               # Python dependencies

```

## 📈 Risk Metrics Used

- **Delta**: Position exposure to price changes
- **VaR (Value at Risk)**: Estimated loss with 95% confidence
- **Volatility Forecast**: Based on LSTM model (trained on past returns)
- **PnL Attribution**: Calculated per hedge and aggregated

## 🎯 Hedging Strategies Supported

- **Delta Hedging**: Based on threshold breach
- **Manual Hedging**: Via `/hedge_now` or button click

## 📢 Alerts & Reporting

- Real-time risk alerts if monitored risk breaches thresholds
- Execution confirmations with delta and volatility info
- PnL summaries with historical context

## 🧪 Testing

Basic manual testing steps:
- Use `/monitor_risk` with different assets and sizes
- Trigger hedges via `/hedge_now` or inline button
- View summaries via `/hedge_status` and `/hedge_history`

## 📄 License

This project is provided for educational purposes under the MIT License.

## ⚠️ Disclaimer

The bot simulates hedging logic. No live trading APIs are connected. Use for simulation and learning purposes only. Performance may differ in live markets.

---

**Made with 💻 by Tanisha Panesar** – *for real-time financial insight and risk awareness.*
