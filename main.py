import os
import telebot
import requests

TOKEN = os.getenv("TOKEN")
bot = telebot.TeleBot(TOKEN)

def shorten_link(url):
    api_url = f"http://tinyurl.com/api-create.php?url={url}"
    response = requests.get(api_url)
    return response.text

@bot.message_handler(func=lambda message: True)
def send_short_link(message):
    long_url = message.text
    short_url = shorten_link(long_url)
    bot.reply_to(message, f"Short Link: {short_url}")

bot.polling()
