from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, ContextTypes
from dotenv import load_dotenv
import os
# import requests
# import schedule
# import time
# from datetime import datetime

load_dotenv()

TOKEN = os.getenv('TOKEN')
BOT_USERNAME = os.getenv('BOT_USERNAME')
IS_DEVELOPMENT = bool(os.getenv('DEVELOPMENT'))
APP_URL = os.getenv('APP_URL_DEV') if IS_DEVELOPMENT else os.getenv('APP_URL_PROD')

CHAT_ID = ''

print(IS_DEVELOPMENT)
print(APP_URL)

startMessage: str = (
    "🎉 Welcome to CTB's MiniApp! 🎉\n\n"
    "Get ready for an exciting adventure under water! Tap on the screen to collect as many coins as you can. "
    "The more coins you collect, the better the prizes you can win! 🏆\n\n"
    "Press 'Start to play!' below to begin your quest for amazing prizes!"
)

async def startCommand(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print("sending start text")
    keyboard = [[InlineKeyboardButton("Start to play!", url=APP_URL)]]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(startMessage, reply_markup=reply_markup)



# def scheduled_task(context: ContextTypes.DEFAULT_TYPE):
#     url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
#     print(requests.get(url).json()) 
#     updates = requests.get(url).json()
#     CHAT_ID = updates["result"][0]["message"]["chat"]["id"]
#     print(CHAT_ID)

#     message = "Your lives have been updated!"
#     url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={message}"
#     try:
#         print(requests.get(url).json())
#     except Exception as e:
#         print(f"Failed to send message: {str(e)}")

#     print("Daily task completed at", datetime.now())


if __name__ == '__main__':
    load_dotenv()
    TOKEN = os.getenv('TOKEN')
    APP_URL = os.getenv('APP_URL_DEV') if bool(os.getenv('DEVELOPMENT')) else os.getenv('APP_URL_PROD')

    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler('start', startCommand))

    # Schedule daily task
    # schedule.every().day.at("13:35").do(scheduled_task)

    # Start bot polling
    print("Starting bot...")
    app.run_polling(poll_interval=3)
    # while True:
    #     schedule.run_pending()
    #     time.sleep(1)