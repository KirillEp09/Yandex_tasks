from requests import get, post, delete

"""
# Правильные тесты
print(delete('http://localhost:5000/api/v2/users/2').json())
print(post('http://localhost:5000/api/v2/users', json={
    'id': 2,
    'surname': 'Иванов',
    'name': 'Максим',
    'age': 20,
    'position': 'architector',
    'speciality': 'constructor',
    'address': 'Popova 66',
    'email': 'iva@iva'
}).json())
print(get('http://localhost:5000/api/v2/users').json())
print(get('http://localhost:5000/api/v2/users/2').json())
# Неправильные тесты
print(delete('http://localhost:5000/api/v2/users/999').json())  # не сущ id
print(get('http://localhost:5000/api/v2/users/999').json())  # не сущ id
print(post('http://localhost:5000/api/v2/users', json={
    'id': 2,
    'surname': 'Иванов',
    'name': 'Максим',
    'age': 20,
    'position': 'architector',
    'speciality': 'constructor',
    'address': 'Popova 66',
    'email': 'iva@iva'
}).json())  # добавление уже сущ пользователь
"""
# Правильные тесты
print(delete('http://localhost:5000/api/v2/jobs/1').json()) # Для очищения бд
print(post('http://localhost:5000/api/v2/jobs', json={
    'job': 'Работа1',
    'team_leader': 1,
    'work_size': 12,
    'collaborators': '6, 7',
    'is_finished': False,
}).json())
print(get('http://localhost:5000/api/v2/jobs/1').json())
print(delete('http://localhost:5000/api/v2/jobs/1').json())
print(get('http://localhost:5000/api/v2/jobs').json())
# Неправильные тесты
print(get('http://localhost:5000/api/v2/jobs/999').json()) # Не сущ id
print(post('http://localhost:5000/api/v2/jobs', json={
    'job': 'Работа1',
    'team_leader': 1,
    'work_size': 12,
    'collaborators': '6, 7',
}).json()) # Не все обязательные полья указаны при создании