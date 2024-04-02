import json

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo

bot = Bot('6864089062:AAHfAt8eoqZYhV5q75eXdmOOM0Ua1Hk16-s')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Open web site', web_app=WebAppInfo(url='https://aman-or.github.io/page/')))
    await message.answer(f'Hi, {message.from_user.first_name}', reply_markup=markup)


@dp.message_handler(content_types=['web_app_data'])
async def web_app(message: types.Message):
    res = json.loads(message.web_app_data.data)
    await message.answer(f'Name: {res["name"]}.\n Email: {res["email"]}.\n Phone: {res["phone"]}')

executor.start_polling(dp)
