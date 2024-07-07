from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, ContextTypes
from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv('TOKEN')
BOT_USERNAME = os.getenv('BOT_USERNAME')
IS_DEVELOPMENT = bool(os.getenv('DEVELOPMENT'))
APP_URL = os.getenv('APP_URL_DEV') if IS_DEVELOPMENT else os.getenv('APP_URL_PROD')

print(IS_DEVELOPMENT)
print(APP_URL)

startMessage: str = (
    "🎉 Welcome to CTB's MiniApp! 🎉\n\n"
    "Get ready for an exciting adventure! Tap on the screen to collect as many coins as you can. "
    "The more coins you collect, the better the prizes you can win! 🏆\n\n"
    "Press 'Start the Game!' below to begin your quest for amazing prizes!"
)

async def startCommand(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sends a message with three inline buttons attached."""
    keyboard = [[InlineKeyboardButton("Start the Game!", url=APP_URL)]]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(startMessage, reply_markup=reply_markup)

if __name__ == '__main__':
    print("Starting bot...")
    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler('start', startCommand))

    print("Start polling...")
    app.run_polling(poll_interval=3)