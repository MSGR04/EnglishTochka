from sqlalchemy import select
import random
from data.englishword import Englishwords


def randomword_1(db_sess):
    random_word = db_sess.scalar(
        select(Englishwords.word).where(Englishwords.id == random.randint(1, 2000)))
    translate = db_sess.scalar(select(Englishwords.translate).where(Englishwords.word == random_word))

    return random_word, translate
