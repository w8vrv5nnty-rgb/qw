import telebot
from config import token
from logic import high_rating
from logic import random_movie
from logic import old_movie
from logic import new_movie
from logic import drama_movie
from logic import action_movie


bot = telebot.TeleBot(token)


def senf_info(bot, message, row):
    info = f"""
Link:             {row[1]}
Title of movie:   {row[2]}
Year:             {row[3]}
Genres:           {row[4]}
Rating IMDB:      {row[5]}"""
    bot.send_message(message.chat.id, info)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'Привет, я бот, помогающий выбрать фильм')

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'Команды: /highRating - Фильм с высоким рейтигом /random - Фильм с любым рейтингом /old - Старый фильм /new - Новый фильм /drama - Фильм с жанром драма /action - Фильм с жанром экшен')

@bot.message_handler(commands=['highRating'])
def high_rated_movie(message):
    bot.send_message(message.chat.id,'Вот интересный фильм с высоким рейтингом:')
    import traceback
    try:
        row = high_rating()
        senf_info(bot, message, row)
    except Exception:
        traceback.print_exc()
        bot.send_message(message.chat.id, "Ошибка при получении фильма")

@bot.message_handler(commands=['random'])
def any_movie(message):
    bot.send_message(message.chat.id,'Вот интересный фильм:')
    import traceback
    try:
        row = random_movie()
        senf_info(bot, message, row)
    except Exception:
        traceback.print_exc()
        bot.send_message(message.chat.id, "Ошибка при получении фильма")

@bot.message_handler(commands=['old'])
def twenty_movie(message):
    bot.send_message(message.chat.id,'Вот интересный фильм снятый в 20 веке:')
    import traceback
    try:
        row = old_movie()
        senf_info(bot, message, row)
    except Exception:
        traceback.print_exc()
        bot.send_message(message.chat.id, "Ошибка при получении фильма")

@bot.message_handler(commands=['new'])
def twenty_one_movie(message):
    bot.send_message(message.chat.id,'Вот интересный фильм снятый в 21 веке:')
    import traceback
    try:
        row = new_movie()
        senf_info(bot, message, row)
    except Exception:
        traceback.print_exc()
        bot.send_message(message.chat.id, "Ошибка при получении фильма")

@bot.message_handler(commands=['drama'])
def sad_movie(message):
    bot.send_message(message.chat.id,'Вот интересный фильм в жанре драма:')
    import traceback
    try:
        row = drama_movie()
        senf_info(bot, message, row)
    except Exception:
        traceback.print_exc()
        bot.send_message(message.chat.id, "Ошибка при получении фильма") 

@bot.message_handler(commands=['action'])
def fight_movie(message):
    bot.send_message(message.chat.id,'Вот интересный фильм в жанре экшен:')
    import traceback
    try:
        row = action_movie()
        senf_info(bot, message, row)
    except Exception:
        traceback.print_exc()
        bot.send_message(message.chat.id, "Ошибка при получении фильма")                

bot.infinity_polling()