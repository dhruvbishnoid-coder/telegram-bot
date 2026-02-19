import os
import telebot
import requests

TOKEN = os.getenv("TOKEN")  # Railway ya hosting me token set hona chahiye
bot = telebot.TeleBot(TOKEN)

CHANNEL_USERNAME = "@swiftxshort"  # Apna channel username

# 🔗 Short Link Function (No waiting)
def shorten_link(url):
    api_url = f"https://is.gd/create.php?format=simple&url={url}"
    response = requests.get(api_url)
    return response.text

# ✅ Check if user joined channel
def check_membership(user_id):
    try:
        member = bot.get_chat_member(CHANNEL_USERNAME, user_id)
        return member.status in ["member", "administrator", "creator"]
    except:
        return False

# 🚀 Start Command
@bot.message_handler(commands=['start'])
def start_message(message):
    text = (
        "🔗 Welcome to SwiftXShort 🚀\n\n"
        "Before using this bot, please complete the steps below:\n\n"
        "📌 Step 1: Follow on Instagram\n"
        "https://www.instagram.com/dhruvxbeniwal/\n\n"
        "📌 Step 2: Join our Telegram Channel\n"
        "https://t.me/swiftxshort\n\n"
        "✔ After completing both steps, send your link to get an instant short URL."
    )
    bot.reply_to(message, text)

# 🔗 Handle Links
@bot.message_handler(func=lambda message: True)
def send_short_link(message):
    user_id = message.from_user.id

    # Channel join check
    if not check_membership(user_id):
        bot.reply_to(
            message,
            "⚠ Please join our Telegram channel first 👇\n"
            "https://t.me/swiftxshort"
        )
        return

    long_url = message.text

    if long_url.startswith("http"):
        short_url = shorten_link(long_url)
        bot.reply_to(message, f"🔗 Short Link:\n{short_url}")
    else:
        bot.reply_to(message, "❌ Please send a valid link starting with http or https")

bot.polling()
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
