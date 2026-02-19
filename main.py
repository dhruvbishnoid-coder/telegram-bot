import os
import telebot
import requests

TOKEN = os.getenv("TOKEN")
bot = telebot.TeleBot(TOKEN)

def shorten_link(url):
    api_url = f"https://is.gd/create.php?format=simple&url={url}"
    response = requests.get(api_url)
    return response.text

@bot.message_handler(commands=['start'])
def start_message(message):
    text = """👋 Welcome to SwiftXShort 🚀

Is bot ko use karne ke liye pehle ye steps complete kare:

1️⃣ Instagram follow kare:
https://www.instagram.com/dhruvxbeniwal/

2️⃣ Telegram channel join kare:
https://t.me/swiftxshort

✅ Dono steps complete karne ke baad apna link bheje.
Main turant short karke dunga 🚀
"""
    bot.reply_to(message, text)

@bot.message_handler(func=lambda message: True)
def send_short_link(message):
    long_url = message.text
    
    if long_url.startswith("http"):
        short_url = shorten_link(long_url)
        bot.reply_to(message, f"🔗 Short Link:\n{short_url}")
    else:
        bot.reply_to(message, "⚠️ Please send a valid link starting with http or https")

bot.polling()
