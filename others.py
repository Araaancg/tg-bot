# https://www.youtube.com/watch?v=OgPQB-G3EPw
# https://www.youtube.com/watch?v=XiBA5LRQFLM
# https://www.youtube.com/watch?v=OgPQB-G3EPw

# def sendDailyMessage():
#     # Fetch the list of chat IDs from your database or a stored list
#     chat_ids = getChatIds()
#     for chat_id in chat_ids:
#         sendMessage(chat_id, "Good morning! Have a great day! ☀️")

# def setMenuButton():
#     url = f'{BOT_URL}/setChatMenuButton'
#     payload = {
#         'menu_button': {
#             'type': 'web_app',
#             'text': '🕹️ Play',
#             'web_app': {
#                 'url': MENU_APP_URL
#             }
#         }
#     }
#     requests.post(url, json=payload)