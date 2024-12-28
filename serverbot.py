import telebot
from telebot import types
from telebot.types import InputMediaPhoto, InputMediaVideo

bot = telebot.TeleBot('7976360176:AAHXzMkO-X61oWyjx5Oo8KTTxjlzjUwYNo8')

@bot.message_handler(commands=['start'])
def main(message):
    file = open('./hello.jpg', 'rb')
    bot.send_photo(message.chat.id, file )
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Подписаться на канал', url='https://t.me/+ZxJQqbvwoVxmODMy'))
    markup.add(types.InlineKeyboardButton('Инструкция по настройке', callback_data='instruction'))
    markup.add(types.InlineKeyboardButton('Отзывы. Осторожно, 18+ 😅', callback_data='otzivy'))

    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}. Если ты тут первый раз, то подпишись на наш канал, Влад тебя зарегистрирует и пришлет QR либо Файл для дальнейшей настройки входа на сервер. После, жми "Инструкция по настройке" 🤓 ', reply_markup=markup)

@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    if call.message:
        if call.data == 'instruction':
            file2 = open('./change.jpeg', 'rb')
            bot.send_photo(call.message.chat.id, file2)
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('iOS 📱', callback_data='ios'))
            markup.add(types.InlineKeyboardButton('Android 🤖', callback_data='android'))
            markup.add(types.InlineKeyboardButton('Windows 🖥', callback_data='pc'))
            markup.add(types.InlineKeyboardButton('MacOS 💻', callback_data='macos'))
            bot.send_message(call.message.chat.id, 'Выбери свою Платформу', reply_markup=markup)
        elif call.data == "otzivy":
            media = [
                InputMediaPhoto(open('otziv1.jpg', 'rb'), caption="Это первая фотография"),
                InputMediaPhoto(open('otziv2.jpg', 'rb'), caption="Это вторая фотография"),
                InputMediaPhoto(open('otziv3.jpg', 'rb'), caption="Это третья фотография"),
            ]
            bot.send_media_group(call.message.chat.id, media)
        elif call.data == "ios":
            media = [
                InputMediaPhoto(open('iphone1.jpg', 'rb'), caption="Это первая фотография"),
                InputMediaPhoto(open('iphone2.jpg', 'rb'), caption="Это вторая фотография"),
            ]
            bot.send_media_group(call.message.chat.id, media)

            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('БОНУС для Яблочных Рабов 😜', callback_data='bonus'))

            bot.send_message(call.message.chat.id,'Скачай --> Установи --> Нажми "Добавить Туннель" --> Отсканируй QR (имя можно любое) --> Наслаждайся 😎 ', reply_markup=markup)

        elif call.data == "bonus":
            with open('bonus1.mp4', 'rb') as video:
                bot.send_video(call.message.chat.id, video, width=384, height=848, supports_streaming=True)

        elif call.data == "android":
            media = [
                InputMediaPhoto(open('iphone1.jpg', 'rb'), caption="Это первая фотография"),
                InputMediaPhoto(open('iphone2.jpg', 'rb'), caption="Это вторая фотография"),
            ]
            bot.send_media_group(call.message.chat.id, media)

            bot.send_message(call.message.chat.id,'Скачай --> Установи --> Нажми "Добавить Туннель" --> Отсканируй QR (имя можно любое) --> Наслаждайся 😎 ')


        elif call.data == "pc":
            media = [
                InputMediaPhoto(open('pc1.jpg', 'rb'), caption="Это первая фотография"),
                InputMediaPhoto(open('pc2.jpg', 'rb'), caption="Это вторая фотография"),
                InputMediaPhoto(open('pc3.jpg', 'rb'), caption="Это третья фотография"),
                InputMediaPhoto(open('pc4.jpg', 'rb'), caption="Это третья фотография"),
            ]
            bot.send_media_group(call.message.chat.id, media)

            bot.send_message(call.message.chat.id, 'Скачай --> Установи --> Нажми "Добавить Туннель" --> Выбери файл, который прислал Влад (имя можно любое) --> Наслаждайся 😎 ')


        elif call.data == "macos":
            media = [
                InputMediaPhoto(open('pc1.jpg', 'rb'), caption="Это первая фотография"),
                InputMediaPhoto(open('pc2.jpg', 'rb'), caption="Это вторая фотография"),
                InputMediaPhoto(open('pc3.jpg', 'rb'), caption="Это третья фотография"),
                InputMediaPhoto(open('pc4.jpg', 'rb'), caption="Это третья фотография"),
            ]
            bot.send_media_group(call.message.chat.id, media)

            bot.send_message(call.message.chat.id,'Скачай --> Установи --> Нажми "Добавить Туннель" --> Выбери файл, который прислал Влад (имя можно любое) --> Наслаждайся 😎 ')


#@#bot.callback_query_handler(func=lambda call:True)
def callback(call):
    if call.message:
        if call.data == 'ios':
            iphone1 = open('./iphone1.jpg', 'rb')
            iphone2 = open('./iphone2.jpg', 'rb')
            iphone3 = open('./iphone3.jpg', 'rb')

            bot.send_photo(call.message.chat.id, iphone1)

            bot.send_message(call.message.chat.id, 'Скачай --> Установи --> Нажми "Добавить Туннель" --> Отсканируй QR (имя можно любое) --> Наслаждайся 😎 ')



bot.polling(non_stop=True)