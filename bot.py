from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import random

# Replace 'YOUR_BOT_API_TOKEN' with your actual bot token
TOKEN = '7233069480:AAHOelvXM6ghBjtMDje68ANkIqXNCiZxG7o'

# In-memory storage for user data (use a database for production)
users = {}

def start(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_user.id
    if user_id not in users:
        users[user_id] = {"hamster": "basic", "points": 0}
    update.message.reply_text('Welcome to Hamster Kombat! Type /play to start.')

def play(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_user.id
    if user_id in users:
        points_earned = random.randint(1, 10)
        users[user_id]['points'] += points_earned
        update.message.reply_text(f'You earned {points_earned} points! Total points: {users[user_id]["points"]}')
    else:
        update.message.reply_text('Type /start first to initialize your hamster.')

def upgrade(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_user.id
    if user_id in users and users[user_id]['points'] >= 50:
        users[user_id]['hamster'] = 'upgraded'
        users[user_id]['points'] -= 50
        update.message.reply_text('Your hamster has been upgraded!')
    else:
        update.message.reply_text('Not enough points to upgrade or you need to start the game first.')

def main():
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("play", play))
    dispatcher.add_handler(CommandHandler("upgrade", upgrade))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
