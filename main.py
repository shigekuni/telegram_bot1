import telebot
import constans
import requests

bot = telebot.TeleBot(constans.token)
url = "https://www.cryptopia.co.nz/api/"

@bot.message_handler(commands=['help'])
def handle_text(message):
    bot.send_message(message.chat.id, """Мои""")

@bot.message_handler(commands=['BTC/USDT'])
def handle_text(message):
    data = requests.get("https://www.cryptopia.co.nz/api/GetMarket/BTC_USDT")
    data = data.json()
    data = data['Data']
    GetMarkets = "Label: "  + str(data["Label"]) + "\n" + "AskPrice: "  + str(data["AskPrice"]) + "\n" + "LastPrice: "  + str(data["LastPrice"]) + "\n" + "BidPrice: "  + str(data["BidPrice"]) + "\n" + "Low: "  + str(data["Low"]) + "\n" + "High: "  + str(data["High"]) + "\n"
    bot.send_message(message.chat.id, GetMarkets)

bot.polling(none_stop=True, interval=0)