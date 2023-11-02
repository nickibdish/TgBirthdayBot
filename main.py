import telebot
import schedule
import time

# Замените 'YOUR_BOT_TOKEN' на токен вашего бота
bot = telebot.TeleBot('6568976463:AAG7UZSuZYkiJtsFBOCKKORuu3BztgElW1k')

# Создаем словарь с днями рождения
birthdays = {
    '2023-11-02': 'user1',
    '2023-08-06': 'user2',
    # Добавьте сюда дни рождения в формате 'гггг-мм-дд': 'Имя пользователя'
}

# Функция для отправки сообщения с поздравлением
def send_birthday_greeting(chat_id, user_name):
    greeting = f'C днем рождения, {user_name}!'
    bot.send_message(chat_id, greeting)

# Функция, которая проверяет, есть ли день рождения сегодня
def check_birthdays():
    today = time.strftime('%Y-%m-%d')
    if today in birthdays:
        for chat_id, user_name in birthdays[today]:
            send_birthday_greeting(chat_id, user_name)

# Расписание для проверки дней рождения каждый день в полночь
schedule.every().day.at('12:00').do(check_birthdays)

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    print(chat_id)
    user_name = message.from_user.first_name  # Получаем имя пользователя
    bot.send_message(chat_id, f'Привет, {user_name}! я буду напоминать тебе, когда у твоих друзей день рождения!')


while True:
    schedule.run_pending()
    bot.polling(none_stop=True)
