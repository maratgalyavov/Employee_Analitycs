import telebot
import pandas as pd
import matplotlib.pyplot as plt

bot = telebot.TeleBot("5822558054:AAE_sjhcVJaB8z3lv0OyNywa8Ug4eGkT3DA", parse_mode=None)

df = pd.read_csv("Data/HR Employee Attrition.csv")


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Меня зовут Роман Б и я люблю хинкали")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "А может ты "+message.text+"?")


bot.infinity_polling()
