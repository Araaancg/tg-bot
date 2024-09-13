from flask import Flask, request, Response
from dotenv import load_dotenv
import os
import re
import requests
from flask_sslify import SSLify
import schedule
import time
from threading import Thread
import sqlite3

IS_DEVELOPMENT = bool(os.getenv('DEVELOPMENT'))

load_dotenv()

# adjust variables according to the enviroment
BOT_USERNAME = os.getenv('BOT_USERNAME_DEV') if IS_DEVELOPMENT else os.getenv('BOT_USERNAME_PROD')
INLINE_APP_URL = os.getenv('INLINE_APP_URL_DEV') if IS_DEVELOPMENT else os.getenv('INLINE_APP_URL_PROD')
MENU_APP_URL = os.getenv('MENU_APP_URL_DEV') if IS_DEVELOPMENT else os.getenv('MENU_APP_URL_PROD')
TOKEN = os.getenv('TOKEN_DEV') if IS_DEVELOPMENT else os.getenv('TOKEN_PROD')
WEBHOOK_URL = os.getenv('WEBHOOK_URL_DEV') if IS_DEVELOPMENT else os.getenv('WEBHOOK_URL_PROD')
BOT_URL = f"https://api.telegram.org/bot{TOKEN}"
API_URL = f"https://127.0.0.1:3001"

startMessage: str = (
    "🎉 Welcome to CTB's MiniApp! 🎉\n\n"
    "Get ready for an exciting adventure under water! Tap on the screen to collect as many coins as you can. "
    "The more coins you collect, the better the prizes you can win! 🏆\n\n"
    "Press 'Start to play!' below to begin your quest for amazing prizes!"
)
startMessage2: str = (
    "Welcome to CTB's MiniApp! \n\n"
    "Get ready for an exciting adventure under water! Tap on the screen to collect as many coins as you can. "
    "The more coins you collect, the better the prizes you can win! \n\n"
    "Press 'Start to play!' below to begin your quest for amazing prizes!"
)

app = Flask(__name__)
sslify = SSLify(app)

def parseMsg(message):
    chatId = message['message']['chat']['id']
    txt = message['message']['text']

    regexPatter = r'/[a-zA-Z]{2,7}'
    ticker = re.findall(regexPatter, txt)
    symbol = ticker[0][1:] if ticker else ''

    return chatId, symbol

def sendMessage(chatId, text, inline_keyboard={}):
    url = f'{BOT_URL}/sendMessage'
    payload = {'chat_id': chatId, 'text': text}
    if inline_keyboard:
        payload['reply_markup'] = inline_keyboard
    print('preparing request...')
    requests.post(url, json=payload)

def updateUserChatId(chatId, userId):
    url = f"{API_URL}/api/user?id={userId}"
    payload = {"chat_id": chatId}
    print(url, payload)
    requests.post(url, json=payload)
    return True

@app.route('/', methods=['POST', 'GET'])
def index() -> str:
    if request.method == "POST":
        msg = request.get_json()    
        chatId, symbol = parseMsg(msg)

        userId = msg['message']['from']['id']

        # print(chatId, symbol)

        if symbol == 'start':
            inline_keyboard = {
                "inline_keyboard": [[       
                    {"text": "Start to play!", "url": INLINE_APP_URL}
                ]]
            }
            print("sending message...")
            updateUserChatId(chatId, userId)
            sendMessage(chatId=chatId, text="jola", inline_keyboard=inline_keyboard)
            
            print("message sent")

        return Response('ok', status=200)
    return {'success': True}

if __name__ == '__main__':
    app.run(debug=True)