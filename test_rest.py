from requests import get, post, delete
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
print(delete('http://localhost:5000/api/v2/users/999').json()) # не сущ id
print(get('http://localhost:5000/api/v2/users/999').json()) # не сущ id
print(post('http://localhost:5000/api/v2/users', json={
    'id': 2,
    'surname': 'Иванов',
    'name': 'Максим',
    'age': 20,
    'position': 'architector',
    'speciality': 'constructor',
    'address': 'Popova 66',
    'email': 'iva@iva'
}).json()) # добавление уже сущ пользователь