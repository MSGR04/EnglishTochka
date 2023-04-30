import telebot
import keyboards
from randomword import randomword_1
from data.middle_table import Middle


def proverka(message, bot: telebot.TeleBot, db_sess, slovo):
    text = message.text
    translations_str = slovo[1]
    if text in translations_str:
        bot.send_message(message.chat.id, f'Вы правильно перевели слово')
        word = Middle(
            slovo=slovo[0],
            translate=slovo[1],
        )
        db_sess.add(word)
        db_sess.commit()
    else:
        bot.send_message(message.chat.id, f'Вы неправильно перевели слово')
        bot.send_message(message.chat.id, f'Правильный ответ: {translations_str}')
    middle_menu(message, bot, db_sess)


def middle_menu(message, bot: telebot.TeleBot, db_sess):
    bot.send_message(message.chat.id, 'Что делаем?',
                     reply_markup=keyboards.menu())

    @bot.callback_query_handler(func=lambda call: call.data == "add1")
    def new_word(call):
        random_word = randomword_1(db_sess)
        bot.send_message(call.message.chat.id, 'Переведите это слово')
        bot.send_message(call.message.chat.id, random_word[0])
        bot.register_next_step_handler(message, proverka, bot, db_sess, random_word)

    @bot.callback_query_handler(func=lambda call: call.data == "add2")
    def statistics(call):
        a = [f'({i.slovo}, {i.translate})' for i in db_sess.query(Middle).all()]
        bot.send_message(call.message.chat.id, str('  '.join(a)))
        middle_menu(message, bot, db_sess)
