import telebot
import config
from telebot import types


bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_1 = types.KeyboardButton('Регистрация нового волонтёра')
    item_2 = types.KeyboardButton('Просмотр коротких проектов')
    item_3 = types.KeyboardButton('Просмотр долгих проектов')

    markup.add(item_1, item_2,
               item_3
               )

    bot.send_message(message.chat.id,
                         "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный помочь тебе разобраться как тут всё устроено.".format(
                             message.from_user, bot.get_me()),
                         parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
            if message.text == 'Регистрация нового волонтёра':
                bot.send_message(message.chat.id, 'Введите ваше имя и возраст, пожалуйста:____.'
                                                  'После этого, выбирайте, пожалуйста, раздел с проектами.')
            elif message.text == 'Просмотр коротких проектов':
                bot.send_message(message.chat.id, 'Информацию о коротких проектах, которые есть на данный момент,'
                'можно посмотреть здесь:https://docs.google.com/document/d/1LmH3YlPP8qo6yrF-dI58g6p6chTqPKWH0UrDDaccM2Q/edit ')
            elif message.text == 'Просмотр долгих проектов':
                bot.send_message(message.chat.id, 'Информацию о коротких проектах, которые есть на данный момент,'
                'можно посмотреть здесь: https://docs.google.com/document/d/10Zntepf7AzpcyUmN-QomBEfUo_U0JcwBSEiwzlv2d54/edit')
            elif message.text.lower() == 'привет':
                bot.send_message(message.chat.id, 'Привет,нажми,пожалуйста, на кнопку меню справа в строке ввода сообщений.')
            else:
                bot.send_message(message.chat.id, 'Cпасибо,вы зарегистрированы!')

bot.polling(none_stop=True)



