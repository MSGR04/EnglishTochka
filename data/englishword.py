import sqlalchemy
from data.db_session import SqlAlchemyBase


class Englishwords(SqlAlchemyBase):
    __tablename__ = 'englishwords'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    word = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    translate = sqlalchemy.Column(sqlalchemy.String, nullable=True)
