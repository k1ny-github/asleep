import telebot

token = '7581408945:AAFSgjWGxW8RIXFhsx6pkwY6X_xAyLq27Ws'  
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])  
def start_join(message):
    bot.send_message(message.chat.id, text="Приветствую!")

bot.polling(none_stop=True)  
