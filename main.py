import telebot
from telebot import types
from random import randint


token = "2128832499:AAGMuYyEYORERf-87cOeZXH1Uf9N9MxXKYo"

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("/help")
    bot.send_message(message.chat.id, 'Привет! Напиши /help для большей информации', reply_markup=keyboard)


@bot.message_handler(commands=['help'])
def start_message(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("hello", "ping", "/send", "/help")
    bot.send_message(message.chat.id, 'Список того, на что я способен:\n/start - первая команда пользователя, призвана сказать ему об /help\n/help - Вывод данного сообщения и добавление большинства команд в быстрый доступ\n/send - Добавление в быстрый доступ вариантов для отправки\n/cat - Фотография кота\n/dog - Фотография собаки\n\nТакже со мной можно поиграть в пинг-понг (ping)\nИли сказать привет(hello)', reply_markup=keyboard)


@bot.message_handler(commands=['send'])
def send(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("/cat", "/dog", "/help")
    bot.send_message(message.chat.id, 'What do you want I send you?', reply_markup=keyboard)


@bot.message_handler(commands=['cat'])
def cat(message):
    random_id = randint(0, 3)
    if random_id == 0:
        bot.send_photo(message.chat.id, "https://www.desktopbackground.org/download/1366x768/2010/10/09/92524_cute-kitten-cats-wallpapers-hd_1366x768_h.jpg")
    elif random_id == 1:
        bot.send_photo(message.chat.id, "https://image.winudf.com/v2/image/Y29tLmFuZHJvbW8uZGV2NDg2Mjc2LmFwcDQ0NzA4NV9zY3JlZW5zaG90c18wXzQzMzg3ZDBk/screen-0.jpg?fakeurl=1&type=.jpg")
    elif random_id == 2:
        bot.send_photo(message.chat.id, "https://i.pinimg.com/originals/3d/8b/31/3d8b3169f630d19ddc978f846a2ded96.jpg")
    elif random_id == 3:
        bot.send_photo(message.chat.id, "https://privately.ru/moda/uploads/posts/2020-05/privately.ru_krasivyj-kotik-861.jpg")


@bot.message_handler(commands=['dog'])
def dog(message):
    random_id = randint(0, 3)
    if random_id == 0:
        bot.send_photo(message.chat.id, "https://www.thesprucepets.com/thmb/wpN_ZunUaRQAc_WRdAQRxeTbyoc=/4231x2820/filters:fill(auto,1)/adorable-white-pomeranian-puppy-spitz-921029690-5c8be25d46e0fb000172effe.jpg")
    elif random_id == 1:
        bot.send_photo(message.chat.id, "https://avatars.mds.yandex.net/i?id=a5080b0d8eb370886ab751326997147d-3765082-images-thumbs&n=13")
    elif random_id == 2:
        bot.send_photo(message.chat.id, "https://avatars.mds.yandex.net/i?id=96f3aab45c00f6c8f2215f6657f4836f-3699999-images-thumbs&n=13")
    elif random_id == 3:
        bot.send_photo(message.chat.id, "https://storage.needpix.com/rsynced_images/puppy-1522280_1280.jpg")


@bot.message_handler(content_types=['text'])
def answer(message):
    if (message.text.lower() == "ping") or (message.text.lower() == "пинг"):
        bot.send_message(message.chat.id, 'pong')
    if (message.text.lower() == "pong") or (message.text.lower() == "понг"):
        bot.send_message(message.chat.id, 'no\nwrite ping')
    if (message.text.lower() == "hello") or (message.text.lower() == "привет"):
        bot.send_message(message.chat.id, 'Hi')


bot.polling(non_stop=True)

