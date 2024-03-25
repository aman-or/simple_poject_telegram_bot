import telebot
import webbrowser

bot = telebot.TeleBot('6864089062:AAHfAt8eoqZYhV5q75eXdmOOM0Ua1Hk16-s')


# for links
@bot.message_handler(commands=['site', 'website'])
def site(message):
    webbrowser.open('https://www.youtube.com')


# for begining
@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id,
                     f'Hi {message.from_user.first_name} '
                     f'{message.from_user.last_name if message.from_user.last_name is not None else ""}')


# for messaage in from user
@bot.message_handler()
def info(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id,
                         f'Hi {message.from_user.first_name} '
                         f'{message.from_user.last_name if message.from_user.last_name is not None else ""}')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID: {message.from_user.id}')


bot.polling(non_stop=True)
