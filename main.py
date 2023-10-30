import telebot
import webbrowser

bot = telebot.TeleBot('6568976463:AAG7UZSuZYkiJtsFBOCKKORuu3BztgElW1k')

@bot.message_handler(commands=['site','website'])
def site(message):
    webbrowser.open('https://ya.ru/')

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, f'Hello, {message.from_user.first_name} ')
    

@bot.message_handler(commands=['help'])
def help(message): #<b></b> - жирным <em> - наклон
    bot.send_message(message.chat.id, '<b>print</b> /start <em>for</em> ...' , parse_mode='html')


@bot.message_handler()
def msg_from_user(message):
    if(message.text.lower() == 'привет'):
        bot.send_message(message.chat.id, 'и тебе привет')
    elif message.text.lower() == 'id':
        bot.reply_to(message,f'ID = {message.from_user.id}')

bot.polling(non_stop=True)                     
