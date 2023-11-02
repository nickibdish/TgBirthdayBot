import telebot
import webbrowser

import schedule
import requests

from telebot import types

#if you need menu you must see second video dudar tgbot

bot = telebot.TeleBot('6568976463:AAG7UZSuZYkiJtsFBOCKKORuu3BztgElW1k')

@bot.message_handler(commands=['site','website'])
def site(message):
    webbrowser.open('https://ya.ru/')

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, f'Hello, {message.from_user.first_name} ')

#тут кнопки внизу строки
def start(message):
    markup = types.ReplyKeyboardMarkup()
    
    btn1 = types.KeyboardButton('btn1')
    markup.row(btn1)
    bot.send_message(message.chat.id,'hello',reply_markup=markup)


@bot.message_handler(commands=['help'])
def help(message): #<b></b> - жирным <em> - наклон
    bot.send_message(message.chat.id, '<b>print</b> /start <em>for</em> ...' , parse_mode='html')


@bot.message_handler()
def msg_from_user(message):
    if(message.text.lower() == 'привет'):
        bot.send_message(message.chat.id, 'и тебе привет')
    elif message.text.lower() == 'id':
        bot.reply_to(message,f'ID = {message.from_user.id}')

@bot.message_handler(content_types=['photo']) #any tipes
def get_photo(message):

    #add button inline тут кнопки к сообщению бота
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Перейти на сайт',url='https://ya.ru/')
    btn2 = types.InlineKeyboardButton('delete', callback_data='delete')
    markup.row(btn1,btn2) # расположение кнопок
    #markup.row(btn2)

    bot.reply_to(message, 'какое красивое фото!', reply_markup=markup)



#почитать про лямба функции, callback: True - разобраться
@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)


bot.polling(non_stop=True)                     
