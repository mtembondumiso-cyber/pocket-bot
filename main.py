import os, time, requests, yfinance as yf
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def send(msg):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": CHAT_ID, "text": msg, "parse_mode":"Markdown"})

pairs = ["EUR/USD", "GBP/USD", "USD/JPY", "AUD/USD", "USD/CAD", "EUR/JPY"]
tickers = ["EURUSD=X", "GBPUSD=X", "JPY=X", "AUDUSD=X", "USDCAD=X", "EURJPY=X"]

send("🚀 *POCKET BOT LIVE FOREVER* Demo + Real Signals ON!")

while True:
    for name, ticker in zip(pairs, tickers):
        try:
            data = yf.download(ticker, period="1d", interval="1m", progress=False)
            if len(data) < 2: continue
            last = float(data['Close'].iloc[-1])
            prev = float(data['Close'].iloc[-2])
            sig = "🔼 CALL (BUY)" if last > prev else "🔽 PUT (SELL)"
            msg = f"📊 *POCKET SIGNAL*\nPair: {name}\nPrice: {last:.5f}\nSignal: {sig}\n⏰ 1 Min Expiry"
            send(msg)
        except: pass
        time.sleep(15)
    time.sleep(60)
