from telebot import *
from config import token
from elements import delements, ptable, command, simpleformula
import json
import random
import time

current_tasks = {}
current_answers = {}
daily_elements = delements
periodic_table = ptable
bot = telebot.TeleBot(token)
subscribers = {}

@bot.message_handler(commands=['formula'])
def formula(message):
        bot.send_message(message.chat.id, simpleformula)


def send_daily_element(chat_id):
    bot.send_message(chat_id, random.choice(daily_elements))

@bot.message_handler(commands=['daily'])
def dailyelement(message):
    chat_id = message.chat.id
    subscribers[chat_id] = True
    subscriber = save_subscribers()
    bot.send_message(chat_id, "Вы подписаны на ежедневные сообщения! Вернитесь в 15:00 и заново пропишите команду.")
    bot.register_next_step_handler(message, lambda msg: send_daily_element(chat_id))

def read_subscribers():
    try:
        with open('subscribers.json', 'r') as file:
            subscribers = json.load(file)
    except FileNotFoundError:
        subscribers = {}
    return subscribers

def save_subscribers():
    with open('subscribers.json', 'w') as file:
        json.dump(subscribers, file)

subscriber = read_subscribers()

@bot.message_handler(commands=['commands'])
def commands(message):
    bot.send_message(message.chat.id, command)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет! Я бот химэкспресс, я твой личный помощник по химии.\n"
                                      "Пропиши /commands для подробной информации про команды")

@bot.message_handler(commands=['table'])
def table_command(message):
    bot.send_message(message.chat.id, "Введите номер элемента, его символ или название для получения информации.")

@bot.message_handler(func=lambda message: True)
def give_answer(message):
    chat_id = message.chat.id
    user_request = message.text

    if user_request.lower() == 'конец':
        bot.send_message(chat_id, "До новых встреч!")
        return

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

while True:
    current_time = time.strftime("%H:%M")

    if current_time == "15:00":
        for chat_id in subscribers.keys():
            send_daily_element(chat_id)
        time.sleep(60)



    bot.polling(non_stop=True)

