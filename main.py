import os
import telebot
import requests

TOKEN = os.getenv("TOKEN")
bot = telebot.TeleBot(TOKEN)

CHANNEL_USERNAME = "@swiftxshort"  # apna channel username

def shorten_link(url):
    api_url = f"https://is.gd/create.php?format=simple&url={url}"
    response = requests.get(api_url)
    return response.text

def is_user_joined(user_id):
    try:
        member = bot.get_chat_member(CHANNEL_USERNAME, user_id)
        return member.status in ["member", "administrator", "creator"]
    except:
        return False

@bot.message_handler(commands=['start'])
def start_message(message):
    if not is_user_joined(message.from_user.id):
        bot.reply_to(
            message,
            "⚠️ Pehle hamara Telegram channel join kare 👇\n"
            "https://t.me/swiftxshort\n\n"
            "Join karne ke baad fir se /start dabaye."
        )
        return

    bot.reply_to(
        message,
        "✅ Welcome 😊\n\nApna link bhejo, main turant short kar dunga 🚀"
    )

@bot.message_handler(func=lambda message: True)
def send_short_link(message):
    if not is_user_joined(message.from_user.id):
        bot.reply_to(
            message,
            "⚠️ Pehle hamara Telegram channel join kare 👇\n"
            "https://t.me/swiftxshort"
        )
        return

    long_url = message.text

    if long_url.startswith("http"):
        short_url = shorten_link(long_url)
        bot.reply_to(message, f"🔗 Short Link:\n{short_url}")
    else:
        bot.reply_to(message, "❌ Valid link bhejo (http ya https se start hona chahiye)")

bot.polling()
