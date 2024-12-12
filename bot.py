from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

API_TOKEN = 7581408945:AAFSgjWGxW8RIXFhsx6pkwY6X_xAyLq27Ws
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привет! Я бот 'A-SLEEP', дам тебе основы правильного сна!")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
