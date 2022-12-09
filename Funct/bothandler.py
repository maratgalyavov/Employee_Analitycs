# import telebot
# import pandas as pd
# import matplotlib.pyplot as plt
#
# bot = telebot.TeleBot("5822558054:AAE_sjhcVJaB8z3lv0OyNywa8Ug4eGkT3DA", parse_mode=None)
# button_line = telebot.types.InlineKeyboardButton('Line', callback_data='foo')
# button_bar = telebot.types.InlineKeyboardButton('Bar', callback_data='bar')
# keyboard = telebot.types.InlineKeyboardMarkup()
# keyboard.add(button_bar)
# keyboard.add(button_line)
#
#
# @bot.message_handler(commands=['start', 'help'])
# def send_welcome(message):
#     chat_id = message.chat.id
#     bot.reply_to(message, "Меня зовут Роман Б и я люблю хинкали")
#     bot.send_message(chat_id, text='What graph would you want to see?', reply_markup=keyboard)
#
#
# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
#     chat_id = message.chat.id
#     command = message
#     bot.send_photo(chat_id, photo=open("/Users/marat/PycharmProjects/Employee_Anal/Data/newplot.png", "rb"))
#     bot.reply_to(message, "А может ты " + message.text + "?")
#
#
# bot.infinity_polling()
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TELEGRAM_TOKEN = "5822558054:AAE_sjhcVJaB8z3lv0OyNywa8Ug4eGkT3DA"

bot = telebot.TeleBot(TELEGRAM_TOKEN)


def gen_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("Bar chart", callback_data="bar"),
               InlineKeyboardButton("Line chart", callback_data="line"),
               InlineKeyboardButton("Box chart", callback_data="box"),
               InlineKeyboardButton("Pie chart", callback_data="pie"))
    return markup


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    chat_id = call.message.chat.id
    if call.data == "bar":
        bot.send_photo(chat_id, photo=open("/Users/marat/PycharmProjects/Employee_Anal/Data/newplot.png", "rb"))
    elif call.data == "line":
        bot.send_photo(chat_id, photo=open("/Users/marat/PycharmProjects/Employee_Anal/Data/newplot-4.png", "rb"))
    elif call.data == "box":
        bot.send_photo(chat_id, photo=open("/Users/marat/PycharmProjects/Employee_Anal/Data/newplot-3.png", "rb"))
    elif call.data == "pie":
        bot.send_photo(chat_id, photo=open("/Users/marat/PycharmProjects/Employee_Anal/Data/newplot-2.png", "rb"))


@bot.message_handler(func=lambda message: True)
def message_handler(message):
    bot.send_message(message.chat.id, "Pick your poison", reply_markup=gen_markup())


bot.infinity_polling()
