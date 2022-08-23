import telebot
from telebot import types

bot = telebot.TeleBot('<TOKEN>')


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id,
                     f'Здравствуйте, {message.from_user.first_name} {message.from_user.last_name}. Для просмотра '
                     f'доступных команд используйте /help. Для просмотра проектов напишите "Покажи проекты"')


@bot.message_handler(commands=['help'])
def info(message):
    bot.send_message(message.chat.id, f'/start - запуск бота.\n/help - показать доступные команды.\nНапишите "Покажи '
                                      f'проекты" для просмотра проектов')


@bot.message_handler(content_types='text')
def projects(message):
    if message.text == 'Покажи проекты':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        gitbtn = types.KeyboardButton('GitHub')
        websitebtn = types.KeyboardButton('Мой сайт')
        markup.add(gitbtn, websitebtn)
        bot.send_message(message.chat.id, "Выберите интересующие проекты на клавиатуре.",
                         reply_markup=markup,)
    elif message.text == "GitHub":
        bot.send_message(message.chat.id, "Вот мой GitHub: https://github.com/JustAnUserMax",
                         reply_markup=types.ReplyKeyboardRemove())
    elif message.text == "Мой сайт":
        bot.send_message(message.chat.id, "Вот мой сайт: https://",
                         reply_markup=types.ReplyKeyboardRemove())


bot.polling(none_stop=True)
