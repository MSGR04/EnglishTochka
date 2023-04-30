from data import db_session
from settings.config import BOT_TOKEN
import telebot
import dialog

# init
bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start'])
def start_hello(message):
    db_session.global_init("db/english.db")
    db_sess = db_session.create_session()
    dialog.start2(bot, message, db_sess)


bot.infinity_polling()
