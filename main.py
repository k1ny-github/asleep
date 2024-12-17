import telebot
from telebot import types
bot = telebot.TeleBot('7581408945:AAGVM1NtGhwVd6MGiRhpxeKLaqqThlhykEw')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("Погрузиться", url='https://t.me/safesleep_bot/asleep')
    markup.add(button1)
    bot.send_message(message.chat.id, "<b>Привет! Нажми на кнопку ниже, чтобы начать. Ты попадешь на веб-приложение про сон.</b> ", parse_mode='html'.format(message.from_user), reply_markup=markup)

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, 'Help information', parse_mode='html')



bot.polling(non_stop=True)