import os
from flask import Flask, request
from telebot import types
import telebot

TOKEN = '5262735741:AAHL1PTf8GnPWXCFlgNp1Dngrei-RynBzB4'

bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)

@bot.message_handler(content_types=['text'])
def commands(message):
    if message.text == '/start':
        stik = open('Илон и шампусико.webp', 'rb')
        bot.send_sticker(message.chat.id, stik)
        bot.send_message(message.chat.id, 'Привет, я хотя уже и не тестовый бот но всё ещё нахожусь в разработке так что если будут какие-то баги то их наверное скоро исправит мой разраб, но лучше напиши (@HiikiToSS)\n Введи \" /commands\" чтобы увидеть список доступных команд')
    

@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200
@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://hikkibotik.herokuapp.com/' + TOKEN)
    return "!", 200
if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
