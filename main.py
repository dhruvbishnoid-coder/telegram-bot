import os
import telebot
import requests

TOKEN = os.getenv("TOKEN")
bot = telebot.TeleBot(TOKEN)

CHANNEL_USERNAME = "@swiftxshort"   # Apna channel username

def is_user_joined(user_id):
    try:
        member = bot.get_chat_member(CHANNEL_USERNAME, user_id)
        if member.status in ["member", "creator", "administrator"]:
            return True
        else:
            return False
    except:
        return False

def shorten_link(url):
    api_url = f"https://tinyurl.com/api-create.php?url={url}"
    response = requests.get(api_url)
    return response.text

@bot.message_handler(commands=['start'])
def start_message(message):
    user_id = message.from_user.id
    
    if not is_user_joined(user_id):
        join_text = f"⚠️ Pehle hamara channel join kare 👇\n\nhttps://t.me/swiftxshort\n\nJoin karne ke baad /start dabaye."
        bot.reply_to(message, join_text)
        return
    
    bot.reply_to(message, "✅ Welcome!\n\nApna link bhejo, main short karke dunga 🚀")

@bot.message_handler(func=lambda message: True)
def send_short_link(message):
    user_id = message.from_user.id
    
    if not is_user_joined(user_id):
        join_text = f"⚠️ Pehle hamara channel join kare 👇\n\nhttps://t.me/swiftxshort\n\nJoin karne ke baad /start dabaye."
        bot.reply_to(message, join_text)
        return
    
    long_url = message.text
    short_url = shorten_link(long_url)
    bot.reply_to(message, f"🔗 Short Link:\n{short_url}")

bot.polling()
