import schedule
import time
import datetime

# Словарь с датами и именами
dates_and_names = {
    '2023-11-02': 'John',
    '2023-12-25': 'Alice',
    '2023-10-03': 'Bob'
}

def send_birthday_greetings():
    current_date = datetime.date.today()
    current_date_str = current_date.strftime('%Y-%m-%d')

    if current_date_str in dates_and_names:
        name = dates_and_names[current_date_str]
        print(f"Сегодня именинник: {name}")
        # Здесь можно добавить код для отправки поздравления (например, через Telegram бота)

# Создаем задачу, которая будет выполняться каждый день в полночь
schedule.every().day.at("11:33").do(send_birthday_greetings)

while True:
    schedule.run_pending()
    time.sleep(1)
