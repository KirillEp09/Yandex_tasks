import datetime
import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase
from sqlalchemy_serializer import SerializerMixin


class Jobs(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'jobs'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    team_leader = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id"))
    creator = sqlalchemy.Column(sqlalchemy.Integer)
    job = sqlalchemy.Column(sqlalchemy.String)
    work_size = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    collaborators = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    start_date = sqlalchemy.Column(sqlalchemy.DateTime,
                                   default=datetime.datetime.now)
    finish_date = sqlalchemy.Column(sqlalchemy.DateTime)
    is_finished = sqlalchemy.Column(sqlalchemy.Boolean, default=False)
    user = orm.relationship('User')

