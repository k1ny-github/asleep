import telebot

# Создаём объект бота
bot = telebot.TeleBot('TOKEN')

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start_handler(message):
    # Отправляем приветственное сообщение с именем пользователя
    bot.send_message(message.chat.id, f'Привет, это бот "A-SLEEP" твой информационный помощник по сну {message.from_user.first_name}!')

# Здесь можно добавить другие обработчики команд и сообщений

# Запускаем бота
bot.polling()
