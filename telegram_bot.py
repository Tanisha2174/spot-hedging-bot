import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackContext, CallbackQueryHandler
from risk_engine import monitor_risk
from hedger import execute_hedge
from hedge_history import get_hedge_history
from dotenv import load_dotenv
from hedge_history import generate_pnl_chart

load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")

active_assets = {}

async def monitor(update: Update, context: CallbackContext):
    try:
        asset = context.args[0].upper()
        size = float(context.args[1])
        threshold = float(context.args[2])
        active_assets[asset] = (size, threshold)

        risk = monitor_risk(asset, size)
        button = InlineKeyboardMarkup([
            [InlineKeyboardButton("📉 Hedge Now", callback_data=f"hedge_{asset}")]
        ])
        await update.message.reply_text(
            f"📈 Risk Summary for {asset}:\nDelta: {risk['delta']:.2f}\nVaR: {risk['VaR']:.2f}\nVolatility: {risk['volatility_forecast']:.2f}",
            reply_markup=button
        )
    except:
        await update.message.reply_text("❌ Usage: /monitor_risk <asset> <position_size> <risk_threshold>")

async def auto_hedge(update: Update, context: CallbackContext):
    await update.message.reply_text("✅ Auto hedging strategy registered.")

async def hedge_status(update: Update, context: CallbackContext):
    asset = context.args[0].upper()
    size, threshold = active_assets.get(asset, (0, 0))
    risk = monitor_risk(asset, size)
    df = get_hedge_history()
    asset_df = df[df["asset"] == asset]
    cum_pnl = asset_df["pnl"].sum() if not asset_df.empty else 0
    await update.message.reply_text(
        f"📊 {asset} Hedge Status:\nDelta: {risk['delta']:.2f}\nVaR: {risk['VaR']:.2f}\n"
        f"Volatility: {risk['volatility_forecast']:.2f}\n📈 Cumulative PnL: ₹{cum_pnl:.2f}"
    )


async def pnl_chart(update: Update, context: CallbackContext):
    try:
        asset = context.args[0].upper()
        path = generate_pnl_chart(asset)
        if not path:
            await update.message.reply_text("No hedge history found.")
            return
        with open(path, 'rb') as chart:
            await update.message.reply_photo(photo=chart, caption=f"{asset} P&L Chart")
    except:
        await update.message.reply_text("❌ Usage: /pnl_chart <asset>")



async def hedge_now(update: Update, context: CallbackContext):
    asset = context.args[0].upper()
    size = float(context.args[1])
    msg = execute_hedge(asset, size)
    await update.message.reply_text(msg)

async def hedge_history(update: Update, context: CallbackContext):
    asset = context.args[0].upper()
    df = get_hedge_history()
    df = df[df["asset"] == asset]
    recent = df.tail(5)
    text = "\n".join([
       f"{r['timestamp']} | Δ: {r['delta']} | PnL: ₹{r['pnl']:.2f}"
    for _, r in recent.iterrows()
    ])
    total_pnl = df["pnl"].sum()
    await update.message.reply_text(f"📜 {asset} History:\n{text}\n\n📈 Total P&L: ₹{total_pnl:.2f}")


async def button_click(update: Update, context: CallbackContext):
    query = update.callback_query
    asset = query.data.replace("hedge_", "")
    size, _ = active_assets.get(asset, (0, 0))
    msg = execute_hedge(asset, size)
    await query.answer()
    await query.edit_message_text(text=msg)

def start_bot():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("monitor_risk", monitor))
    app.add_handler(CommandHandler("auto_hedge", auto_hedge))
    app.add_handler(CommandHandler("hedge_status", hedge_status))
    app.add_handler(CommandHandler("hedge_now", hedge_now))
    app.add_handler(CommandHandler("pnl_chart", pnl_chart))
    app.add_handler(CommandHandler("hedge_history", hedge_history))
    app.add_handler(CallbackQueryHandler(button_click))
    app.run_polling()

