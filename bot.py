import telebot
import random
import time

# 🔑 Replace with your actual bot token
API_TOKEN = '8052955693:AAFiPuUaY_eBkJV7bn--zvGLT6t2w0XUos8'

bot = telebot.TeleBot(API_TOKEN)

# 🎉 List of random replies
fun_replies = [
    "I'm just a bot, but I'm learning fast! 😎",
    "Bolo bolo... kya kaam hai? 😁",
    "Mast din hai aaj! Tum kaise ho? 🌞",
    "Main hoon na! 💪",
    "Code chal raha hai, mood ban raha hai 😄"
]

# ✅ Start command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(
        message,
        "👋 Hello, *{}*! Welcome to my bot.\nType `hi`, `hello` or anything — I'm always listening 😄".format(message.from_user.first_name),
        parse_mode='Markdown'
    )

# 💬 Hi / Hello handler
@bot.message_handler(func=lambda msg: msg.text and msg.text.lower() in ["hi", "hello", "hey"])
def greet_user(message):
    bot.reply_to(message, "Hello 👋! How can I help you today?")

# 💬 How are you handler
@bot.message_handler(func=lambda msg: msg.text and "how are you" in msg.text.lower())
def how_are_you(message):
    bot.reply_to(message, "I'm doing great 🤖! What about you?")

# 💬 Any other text
@bot.message_handler(func=lambda msg: True)
def unknown_text(message):
    reply = random.choice(fun_replies)
    bot.reply_to(message, reply)

# 🔄 Keep the bot running even if it crashes once
if __name__ == "__main__":
    print("🤖 Bot is running...")
    while True:
        try:
            bot.infinity_polling()
        except Exception as e:
            print(f"⚠️ Bot crashed with error: {e}")
            time.sleep(15)  # Wait and retry
