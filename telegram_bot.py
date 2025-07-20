import requests, json

BOT_TOKEN = "6183661771:AAGgHPZ-FDKnFQKZDf9n8DoGknpeIEj2b-A"
CHAT_ID = "5347483870"

def run():
    message = "[Warmwind AI] Telegram agent active."
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}
    requests.post(url, data=payload)
