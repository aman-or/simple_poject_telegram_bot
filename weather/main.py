import telebot
import requests
import json

bot = telebot.TeleBot('')
API = ''


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Hi nice to see you, please write your country name:')


@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    if res.status_code == 200:
        data = json.loads(res.text)
        temp = data["main"]["temp"]
        wind = data["wind"]["speed"]
        bot.reply_to(message, f'Weather now: {temp}° C\n Wind now: {wind}')

        image = 'rain.png' if temp < 5.0 else 'sunAndCloud.png'
        file = open('weather/' + image, 'rb')
        bot.send_photo(message.chat.id, file)
    else:
        bot.reply_to(message, f'Weather wrote wrong')


bot.polling(non_stop=True)
