from telebot import *
from config import token
from gpt import GPT
import random
import time

current_tasks = {}
current_answers = {}
daily_elements = [
    "H - Водороду принадлежит звание самого горячего элемента. В звёздах, включая Солнце, происходят реакции синтеза водорода, выделяющие огромное количество энергии в форме света и тепла.",
    "He - Гелий — один из первых химических элементов, возникших после Большого Взрыва. Наша Вселенная практически на треть состоит из гелия."
]

# Словарь с элементами таблицы Менделеева
periodic_table = {
    1: {"symbol": "H", "name": "Водород", "mass": 1.008, "properties": "Газ, бесцветный, не имеет запаха.",
        "fact": "Самый распространённый элемент во Вселенной."},
    2: {"symbol": "He", "name": "Гелий", "mass": 4.0026, "properties": "Газ, инертный, бесцветный.",
        "fact": "Используется в воздушных шарах."},
    # Добавьте другие элементы по мере необходимости
}
bot = telebot.TeleBot(token)
gpt = GPT()

subscribers = {}


def send_daily_element(chat_id):
    bot.send_message(chat_id, random.choice(daily_elements))


@bot.message_handler(commands=['daily'])
def dailyelement(message):
    chat_id = message.chat.id
    subscribers[chat_id] = True
    bot.send_message(chat_id, "Вы подписаны на ежедневные сообщения! Вернитесь в 15:00 и заново пропишите команду.")
    bot.register_next_step_handler(message, lambda msg: send_daily_element(chat_id))

    while True:
        current_time = time.strftime("%H:%M")
        for chat_id in subscribers.keys():
            if current_time == "15:00":
                send_daily_element(chat_id)
            time.sleep(60)


@bot.message_handler(commands=['commands'])
def commands(message):
    bot.send_message(message.chat.id, "/start - Запусти или перезапусти бота\n"
                                      "/commands - Помощь по командам\n"
                                      "/bot - Запусти режим нейросети\n"
                                      "/table - Интерактивная таблица менделеева\n"
                                      "/daily - Запуск ежедневных интересных фактов про эл-ты химии")


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет! Я бот химэкспресс, я твой личный помощник по химии.\n"
                                      "Пропиши /commands для подробной информации про команды")


@bot.message_handler(commands=['bot'])
def start_gpt(message):
    bot.send_message(message.chat.id, "Запускаю нейросеть...")


@bot.message_handler(func=lambda message: True)
def give_answer(message):
    chat_id = message.chat.id
    user_request = message.text

    if user_request.lower() == 'конец':
        bot.send_message(chat_id, "До новых встреч!")
        return


@bot.message_handler(commands=['table'])
def table_command(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Введите номер элемента, его символ или название для получения информации.")

    # Обработка пользовательского ввода после команды /table
    @bot.message_handler(func=lambda msg: True)
    def handle_element_request(msg):
        user_request = msg.text

        # Проверка на ввод номера элемента
        if user_request.isdigit():
            element_number = int(user_request)
            element_info = periodic_table.get(element_number)
            if element_info:
                response = (f"Элемент: {element_info['name']}\n"
                            f"Символ: {element_info['symbol']}\n"
                            f"Атомная масса: {element_info['mass']}\n"
                            f"Свойства: {element_info['properties']}\n"
                            f"Интересный факт: {element_info['fact']}")
                bot.send_message(chat_id, response)
            else:
                bot.send_message(chat_id, "Элемент не найден. Попробуйте другой номер.")
            return

        for element in periodic_table.values():
            if element['symbol'].lower() == user_request.lower():
                response = (f"Элемент:{element['name']}\n"
                            f"Символ:{element['symbol']}\n"
                            f"Атомная масса{element['mass']}\n"
                            f"Свойства:{element['properties']}\n"
                            f"Интересный факт: {element['fact']}")
                bot.send_message(chat_id,response)
                return
        bot.send_message(chat_id, "Элемент не найден. Попробуйте другой символ или название.")

bot.polling(non_stop=True)
