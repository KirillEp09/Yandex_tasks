from requests import get, post, delete, put

# Проверенные тесты
""" 
print(get('http://localhost:5000/api/jobs').json())  # Все работы
print(get('http://localhost:5000/api/jobs/1').json())  # 1 работа
print(get('http://localhost:5000/api/jobs/999').json())  # Неверное получение работы
print(get('http://localhost:5000/api/jobs/q').json())  # Неверное получение - строка
print(post('http://localhost:5000/api/jobs',  # Корректный запрос создания работы
           json={'job': 'Работа 2',
                 'team_leader': 1,
                 'work_size': 12,
                 'collaborators': '6, 8',
                 'id': 2,
                 'is_finished': False}).json())
print(post('http://localhost:5000/api/jobs',  # Не все обязательные поля указаны при создании
           json={'job': 'Работа 2',
                 'team_leader': 1,
                 'work_size': 12,
                 'collaborators': '6, 8',
                 'is_finished': False}).json())
print(post('http://localhost:5000/api/jobs', json={}).json())  # Пустой запрос
print(post('http://localhost:5000/api/jobs',  # Не тот тип данных указан при создании
           json={'job': 'Работа 2',
                 'team_leader': '1',
                 'work_size': '12',
                 'collaborators': '6, 8', 
                 'is_finished': 2}).json())
print(delete('http://localhost:5000/api/jobs/1'))  # Корректное удаление
print(delete('http://localhost:5000/api/jobs/91239'))  # Несуществующее id
print(delete('http://localhost:5000/api/jobs/91239')) # Неверное удаление - строка
"""
# Непроверенные тесты
print(delete('http://localhost:5000/api/jobs/1').json())
print(get('http://localhost:5000/api/jobs').json())
print(post('http://localhost:5000/api/jobs/1', json={'job': 'Работа до изменения',
                                                     'team_leader': 1,
                                                     'work_size': 12,
                                                     'collaborators': '6, 8',
                                                     'is_finished': False}).json())
print(put('http://localhost:5000/api/jobs/1', json={'job': 'Работа после изменения',
                                                     'team_leader': 2,
                                                     'work_size': 15,
                                                     'collaborators': '6, 7',
                                                     'is_finished': True}).json())
print(put('http://localhost:5000/api/jobs/999', json={'job': 'Работа после изменения', # указанной работы не существует
                                                     'team_leader': 2,
                                                     'work_size': 15,
                                                     'collaborators': '6, 7',
                                                     'is_finished': True}).json())
print(put('http://localhost:5000/api/jobs/1', json={'job': 'Работа после изменения', # переданы не все данные при изменении
                                                     'team_leader': 2,
                                                     'work_size': 15,
                                                     'collaborators': '6, 7',
                                                     'id': 1}).json())
print(get('http://localhost:5000/api/jobs').json())
