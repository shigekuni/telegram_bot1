import requests
import json

data = requests.get("https://www.cryptopia.co.nz/api/GetMarket/BTC_USDT")
data = data.json()
data = data['Data']
print(data)
print(data["AskPrice"])