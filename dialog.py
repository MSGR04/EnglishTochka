import logging
import random
from beginer import menu
from middle import middle_menu
from profi import profi_menu
import keyboards
import startmessage
import telebot
from data.englishword import Englishwords
from sqlalchemy import select
from randomword import randomword_1

counter = 0
logger = logging.getLogger(__name__)


def start2(bot: telebot.TeleBot, message, db_sess):
    slova = []
    i = 0
    while i < 10:
        random_word = randomword_1(db_sess)
        if random_word in slova:
            continue
        else:
            slova.append(random_word)
            i += 1

    bot.send_message(message.chat.id, startmessage.HELLO_MESSAGE,
                     reply_markup=keyboards.func())

    @bot.callback_query_handler(func=lambda call: call.data == "add")
    def start_check(call):
        sended_counter = 1
        bot.send_message(call.message.chat.id, 'Переведите это слово')
        print(slova[0])
        bot.send_message(call.message.chat.id, slova[0][0])
        bot.register_next_step_handler(message, proverka, bot, db_sess, slova[0], sended_counter)

    @bot.message_handler(content_types=["text"])
    def proverka(message, bot: telebot.TeleBot, db_sess, slovo, sended_counter: int):
        global counter
        text = message.text
        translations_str = slovo[1]
        if text in translations_str:
            counter += 1
            bot.send_message(message.chat.id, f'Вы правильно перевели слово')
        else:
            bot.send_message(message.chat.id, f'Вы неправильно перевели слово')
            bot.send_message(message.chat.id, f'Правильный ответ: {translations_str}')

        if sended_counter < 10:
            bot.send_message(message.chat.id, 'Переведите это слово')
            bot.send_message(message.chat.id, slova[sended_counter][0])
            print(slova[sended_counter])
            sended_counter += 1
            bot.register_next_step_handler(message, proverka, bot, db_sess, slova[sended_counter - 1], sended_counter)
        else:
            if counter <= 4:
                bot.send_message(message.chat.id, f'Переведено слов: {counter}')
                bot.send_message(message.chat.id, f'Тебе стоит подучить некоторые слова. '
                                                  f'Твой уровень английского: Новичок')

                menu(message, bot, db_sess)
            elif counter > 4 and counter <= 8:
                bot.send_message(message.chat.id, f'Переведено слов: {counter}')
                bot.send_message(message.chat.id, f'А ты не плох. Твой уровень английского: Учился у бочки')
                middle_menu(message, bot, db_sess)
            elif counter >= 9:
                bot.send_message(message.chat.id, f'Переведено слов: {counter}')
                bot.send_message(message.chat.id, f'Ну ты машина. Твой уровень английского: Учил бочку')
                profi_menu(message, bot, db_sess)