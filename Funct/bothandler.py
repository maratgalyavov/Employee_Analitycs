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

TELEGRAM_TOKEN = "5822558054:AAH74WueVh3EbBD_uqHr4M3X7Pgzaogw-h4"

bot = telebot.TeleBot(TELEGRAM_TOKEN)


def gen_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("Bar chart of job satisfaction", callback_data="bar"),
               InlineKeyboardButton("Line chart of uneployment around the world", callback_data="line"),
               InlineKeyboardButton("Scatter plot of wages based on age", callback_data="scatter"),
               InlineKeyboardButton("Pie chart of job satisfaction", callback_data="pie"))
    return markup


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    chat_id = call.message.chat.id
    if call.data == "bar":
        bot.send_message(chat_id,
                         "I assume that monthly income has a healthy effect on job satisfaction. Charts you see below are a great disproof for my hypothesis, as they show that income has a very subtle effect on one's level of satisfaction")
        bot.send_photo(chat_id, photo=open("/Users/marat/PycharmProjects/Employee_Anal/Data/newplot-2.png", "rb"))
        bot.send_message(chat_id, "What would you like to see", reply_markup=gen_markup())
    elif call.data == "line":
        bot.send_message(chat_id,
                         "Level of unemployment generally reflects what is happening with the world economy. line chart below depicts unemployment percentage in europe, us and average among all countries. all three trends follow the same pattern, proving the point that level of uneployment is a great metric for analyzing worldwide economical situation")
        bot.send_photo(chat_id, photo=open("/Users/marat/PycharmProjects/Employee_Anal/Data/newplot.png", "rb"))
        bot.send_message(chat_id, "What would you like to see", reply_markup=gen_markup())
    elif call.data == "scatter":
        bot.send_message(chat_id,
                         " I want to prove that most people get paid above their minimum threshold and this gap is not dependant on one's age")
        bot.send_photo(chat_id, photo=open("/Users/marat/PycharmProjects/Employee_Anal/Data/newplot-3.png", "rb"))
        bot.send_message(chat_id, "What would you like to see", reply_markup=gen_markup())
    elif call.data == "pe":
        bot.send_message(chat_id,
                         "On the pie chart below, i represented different percentages of job satisfaction based on salary")
        bot.send_photo(chat_id, photo=open("/Users/marat/PycharmProjects/Employee_Anal/Data/newplot-4.png", "rb"))
        bot.send_message(chat_id, "What would you like to see", reply_markup=gen_markup())


@bot.message_handler(commands=["help","start"])
def message_handler(message):
    bot.send_message(message.chat.id, "What chart would you like to see?", reply_markup=gen_markup())

bot.infinity_polling()
