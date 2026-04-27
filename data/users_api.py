import flask
from . import db_session
from .users import User
from flask import jsonify, make_response, request

blueprint = flask.Blueprint(
    'users_api',
    __name__,
    template_folder='templates'
)


# Получение всех пользователей
@blueprint.route('/api/users')
def get_users():
    db_sess = db_session.create_session()
    users = db_sess.query(User).all()
    return jsonify(
        {
            'users':
                [item.to_dict(only=('id', 'name', 'surname'))
                 for item in users]
        }
    )


# Получение одного пользователя
@blueprint.route('/api/users/<int:id>', methods=['GET'])
def get_user(id):
    db_sess = db_session.create_session()
    users = db_sess.get(User, id)
    return jsonify(
        {
            'users': users.to_dict(only=(
                'id', 'name', 'surname'))
        }
    )


# Добавление пользователя
@blueprint.route('/api/users/<int:id>', methods=['POST'])
def create_user(id):
    if not request.json:
        return make_response(jsonify({'error': 'Empty request'}), 400)
    elif not all(key in request.json for key in
                 ['surname', 'name', 'age', 'position', 'speciality', 'address', 'email']):
        return make_response(jsonify({'error': 'Bad request'}), 400)
    db_sess = db_session.create_session()
    user = User(
        id=id,
        surname=request.json['surname'],
        name=request.json['name'],
        age=request.json['age'],
        position=request.json['position'],
        speciality=request.json['speciality'],
        address=request.json['address'],
        email=request.json['email']
    )
    db_sess.add(user)
    db_sess.commit()
    return jsonify({'surname': user.surname, 'name': user.name})


# Удаление пользователя
@blueprint.route('/api/users/<int:id>', methods=['DELETE'])
def delete_users(id):
    db_sess = db_session.create_session()
    users = db_sess.get(User, id)
    if not users:
        return make_response(jsonify({'error': 'Not found'}), 404)
    db_sess.delete(users)
    db_sess.commit()
    return jsonify({'success': 'OK'})


# Изменение пользователя
@blueprint.route('/api/users/<int:id>', methods=['PUT'])
def change_user(id):
    if not request.json:
        return make_response(jsonify({'error': 'Empty request'}), 400)
    elif not all(key in request.json for key in
                 ['surname', 'name', 'age', 'position', 'speciality', 'address', 'email']):
        return make_response(jsonify({'error': 'Bad request'}), 400)
    db_sess = db_session.create_session()
    user = db_sess.query(User).get(id)
    user.surname = request.json['surname']
    user.name = request.json['name']
    user.age = request.json['age']
    user.position = request.json['position']
    user.speciality = request.json['speciality']
    user.address = request.json['address']
    user.email = request.json['email']
    db_sess.commit()
    return jsonify({'success': 'OK'})
