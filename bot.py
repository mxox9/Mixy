import telebot
import random
import os

# Get token from environment variable
API_TOKEN = os.environ.get("BOT_TOKEN")

bot = telebot.TeleBot(API_TOKEN)

# 🎉 Random replies
fun_replies = [
    "I'm just a bot, but I'm learning fast! 😎",
    "Bolo bolo... kya kaam hai? 😁",
    "Mast din hai aaj! Tum kaise ho? 🌞",
    "Main hoon na! 💪",
    "Code chal raha hai, mood ban raha hai 😄"
]

# ✅ /start command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, f"👋 Hello, *{message.from_user.first_name}*! Welcome to my bot.\nType `hi`, `hello` or anything — I'm always listening 😄", parse_mode='Markdown')

# 💬 hi / hello handler
@bot.message_handler(func=lambda msg: msg.text.lower() in ["hi", "hello", "hey"])
def greet_user(message):
    bot.reply_to(message, "Hello 👋! How can I help you today?")

# 💬 how are you handler
@bot.message_handler(func=lambda msg: "how are you" in msg.text.lower())
def how_are_you(message):
    bot.reply_to(message, "I'm doing great 🤖! What about you?")

# 💬 any other message
@bot.message_handler(func=lambda msg: True)
def unknown_text(message):
    reply = random.choice(fun_replies)
    bot.reply_to(message, reply)

# 🔄 keep bot polling
bot.polling()
