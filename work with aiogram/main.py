from aiogram import Bot, Dispatcher, executor, types

bot = Bot('6864089062:AAHfAt8eoqZYhV5q75eXdmOOM0Ua1Hk16-s')
dp = Dispatcher(bot)


@dp.message_handler(content_types=['photo'])  # commands=['start'] content_types=['photo anf etc.']
async def start(message: types.Message):
    await message.reply('Hello')


@dp.message_handler(commands=['inline'])
async def info(message: types.Message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Site', url='https://www.youtube.com/'))
    markup.add(types.InlineKeyboardButton('Hello', callback_data='hello'))
    await message.reply('Hello', reply_markup=markup)


@dp.callback_query_handler()
async def callback(call):
    await call.message.answer(call.data)


@dp.message_handler(commands=['reply'])
async def reply(message: types.Message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.add(types.KeyboardButton('Site'))
    markup.add(types.KeyboardButton('Website'))
    await message.answer('Hello', reply_markup=markup)

executor.start_polling(dp)
