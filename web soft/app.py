from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo

bot = Bot('6864089062:AAHfAt8eoqZYhV5q75eXdmOOM0Ua1Hk16-s')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Open web sote', web_app=WebAppInfo(url='https://www.youtube.com/')))
    await message.answer('Hi, my friend', reply_markup=markup)

executor.start_polling(dp)
