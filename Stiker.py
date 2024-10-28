import schedule
import time
from telegram import Bot
from datetime import datetime

# Укажи токен своего бота
TOKEN = '7670754438:AAFfaDxJVj8CtHC6w9r7p-WQAVYzSi8I_tk'
bot = Bot(token=TOKEN)

# ID пользователя, которому будет отправляться стикер
USER_ID = '490436650'

# ID стикера для отправки
STICKER_ID = 'CAACAgIAAxkBAAIBiGcfUOICi0xHis3B450x_nRWJlDPAALKXgACC9XZSA5bfXUlU7icNgQ'

# Функция отправки стикера
def send_sticker():
    bot.send_sticker(chat_id=USER_ID, sticker=STICKER_ID)
    print("Стикер отправлен!")

# Проверка времени для разовой отправки сегодня
def check_once_today():
    now = datetime.now()
    if now.hour == 13 and now.minute == 15:
        send_sticker()
        print("Разовая отправка стикера завершена.")
        return schedule.CancelJob  # Останавливаем эту задачу после выполнения

# Настройка расписания для повторяющихся отправок
schedule.every().monday.at("10:50").do(send_sticker)
schedule.every().tuesday.at("10:50").do(send_sticker)
schedule.every().wednesday.at("10:50").do(send_sticker)
schedule.every().friday.at("10:50").do(send_sticker)

# Настройка разовой отправки на сегодня
schedule.every(1).minute.do(check_once_today)

# Запуск цикла для выполнения заданий по расписанию
while True:
    schedule.run_pending()
    time.sleep(1)  # проверяем задачи каждую секунду
