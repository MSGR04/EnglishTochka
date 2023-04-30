from data.englishword import Englishwords
from sqlalchemy.orm import Session
from data import db_session
from deep_translator import GoogleTranslator

db_session.global_init("db/english.db")
db_sess = db_session.create_session()


def database(db_session: Session):
    with open('ENRUS.TXT') as sf:
        sf = [i.replace('\n', '') for i in sf.readlines()]
        print(sf)

    while sf:
        slovo = sf.pop(0)
        translator = GoogleTranslator(source='auto', target='ru')
        rer = translator.translate(slovo)
        print(slovo)
        word = Englishwords(
            word=slovo,
            translate=rer,
        )
        db_session.add(word)
        db_session.commit()


database(db_sess)
