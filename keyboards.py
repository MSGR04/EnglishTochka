from telebot import types


def func():
    call_back = types.InlineKeyboardMarkup()
    call_back.add(types.InlineKeyboardButton(text='Оценить свой уровень англиского', callback_data='add'))
    return call_back


def menu():
    call_back = types.InlineKeyboardMarkup()
    call_back.add(types.InlineKeyboardButton(text='Новое слово', callback_data='add1'))
    call_back.add(types.InlineKeyboardButton(text='Выученные слова', callback_data='add2'))
    return call_back