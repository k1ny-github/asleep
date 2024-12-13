import telebot

token = '7581408945:AAGVM1NtGhwVd6MGiRhpxeKLaqqThlhykEw'  
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])  
def start_join(message):
    bot.send_message(message.chat.id, text="")

bot.polling(none_stop=True)  
