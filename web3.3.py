from flask import Flask
from data import db_session
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

def main():
    db_session.global_init("db/blogs.db")
    user = User()
    user.surname = "Scott"
    user.name = "Ridley"
    user.age = 21
    user.position = "captain"
    user.speciality = "research engineer"
    user.address = "module_1"
    user.email = "scott_chief@mars.org"
    db_sess = db_session.create_session()
    user1 = User()
    user1.surname = "Evans"
    user1.name = "Harry"
    user1.age = 22
    user1.position = "officer"
    user1.speciality = "civil engineer"
    user1.address = "module_1"
    user1.email = "user1@mars.org"
    user2 = User()
    user2.surname = "Aldridge"
    user2.name = "Joseph"
    user2.age = 23
    user2.position = "officer"
    user2.speciality = "surgeon"
    user2.address = "module_3"
    user2.email = "user2@mars.org"
    user3 = User()
    user3.surname = "Adamson"
    user3.name = "Samuel"
    user3.age = 24
    user3.position = "officer"
    user3.speciality = "physician"
    user3.address = "module_4"
    user3.email = "user3@mars.org"
    db_sess.add(user)
    db_sess.add(user1)
    db_sess.add(user2)
    db_sess.add(user3)
    db_sess.commit()
    #app.run()


if __name__ == '__main__':
    main()