import sqlalchemy
from .db_session import SqlAlchemyBase
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy import orm


class Department(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'departaments'
    id = sqlalchemy.Column(sqlalchemy.Integer, autoincrement=True, primary_key=True)
    title = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    creator = sqlalchemy.Column(sqlalchemy.Integer)
    chief = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id"))
    members = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    email = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    user = orm.relationship('User')