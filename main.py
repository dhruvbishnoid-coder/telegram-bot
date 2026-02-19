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
    bot.reply_to(
        message,
        "Welcome 😊\n\nFollow me on Instagram 👇\nhttps://www.instagram.com/dhruvxbeniwal/"
    )

@bot.message_handler(func=lambda message: True)
def send_short_link(message):
    long_url = message.text
    
    if long_url.startswith("http"):
        short_url = shorten_link(long_url)
        bot.reply_to(message, f"Short Link: {short_url}")
    else:
        bot.reply_to(message, "Please send a valid link starting with http or https")

bot.polling()
