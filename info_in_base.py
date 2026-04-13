from data import db_session
from data.users import User
from data.jobs import Jobs
import datetime


def clear_base():
    db_sess = db_session.create_session()
    db_sess.query(User).delete()
    db_sess.query(Jobs).delete()
    db_sess.commit()


def add_people():
    db_sess = db_session.create_session()
    users = [
        User(name="Илон", surname="Маск", email="elon@mars.com", hashed_password="123", age=50,
             position="Командир базы", speciality="Космический инженер", address="Купол A-1"),
        User(name="Марк", surname="Уотни", email="mark@mars.com", hashed_password="123", age=42,
             position="Ботаник-агроном", speciality="Выращивание картофеля", address="Купол B-2"),
        User(name="Крис", surname="Хэдфилд", email="chris@mars.com", hashed_password="123", age=60,
             position="Главный инженер", speciality="Ремонт роверов", address="Купол C-3"),
        User(name="Валентина", surname="Терешкова", email="val@mars.com", hashed_password="123", age=80,
             position="Научный руководитель", speciality="Астробиология", address="Купол D-4"),
        User(name="Нил", surname="Армстронг", email="neil@mars.com", hashed_password="123", age=90,
             position="Старший инструктор", speciality="Выходы в открытый космос", address="Купол E-5"),
    ]
    for u in users:
        db_sess.add(u)
    db_sess.commit()


def add_jobs():
    db_sess = db_session.create_session()
    users = db_sess.query(User).all()
    user_dict = {u.id: u for u in users}
    leader_ids = list(user_dict.keys())[:5]

    jobs = [
        Jobs(
            team_leader=leader_ids[0],
            job="Постройка купола 'Olympus Mons'",
            work_size=120,
            collaborators=f"{leader_ids[1]}, {leader_ids[2]}",
            start_date=datetime.datetime(2026, 4, 1, 8, 0),
            finish_date=datetime.datetime(2026, 4, 15, 18, 0),
            is_finished=False
        ),
        Jobs(
            team_leader=leader_ids[1],
            job="Исследование кратера 'Victoria' на предмет водяного льда",
            work_size=48,
            collaborators=f"{leader_ids[0]}, {leader_ids[3]}",
            start_date=datetime.datetime(2026, 4, 2, 9, 0),
            finish_date=datetime.datetime(2026, 4, 5, 17, 0),
            is_finished=False
        ),
        Jobs(
            team_leader=leader_ids[2],
            job="Запуск ровера 'Curiosity 2.0' в долину Маринер",
            work_size=32,
            collaborators=f"{leader_ids[1]}, {leader_ids[4]}",
            start_date=datetime.datetime(2026, 4, 3, 10, 0),
            finish_date=datetime.datetime(2026, 4, 7, 14, 0),
            is_finished=True
        ),
        Jobs(
            team_leader=leader_ids[3],
            job="Создание системы жизнеобеспечения для купола 'Tharsis'",
            work_size=80,
            collaborators=f"{leader_ids[0]}, {leader_ids[2]}",
            start_date=datetime.datetime(2026, 4, 4, 7, 30),
            finish_date=datetime.datetime(2026, 4, 20, 20, 0),
            is_finished=False
        ),
        Jobs(
            team_leader=leader_ids[4],
            job="Сбор образцов грунта в районе 'Terra Sabaea'",
            work_size=24,
            collaborators=f"{leader_ids[3]}",
            start_date=datetime.datetime(2026, 4, 5, 12, 0),
            finish_date=datetime.datetime(2026, 4, 6, 12, 0),
            is_finished=False
        ),
        Jobs(
            team_leader=leader_ids[0],
            job="Калибровка метеорологической станции 'MARS-Weather'",
            work_size=16,
            collaborators=f"{leader_ids[2]}, {leader_ids[4]}",
            start_date=datetime.datetime(2026, 4, 6, 9, 0),
            finish_date=datetime.datetime(2026, 4, 8, 15, 0),
            is_finished=False
        ),
        Jobs(
            team_leader=leader_ids[2],
            job="Подготовка к пилотируемому полёту на Фобос",
            work_size=200,
            collaborators=f"{leader_ids[0]}, {leader_ids[1]}, {leader_ids[3]}",
            start_date=datetime.datetime(2026, 4, 7, 8, 0),
            finish_date=datetime.datetime(2026, 5, 1, 12, 0),
            is_finished=False
        ),
    ]
    for job in jobs:
        db_sess.add(job)
    db_sess.commit()
