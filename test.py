from requests import get, post, delete

print(get('http://localhost:5000/api/jobs').json())  # Все работы
print(get('http://localhost:8080/api/jobs/1').json())  # 1 работа
print(get('http://localhost:8080/api/jobs/999').json())  # Неверное получение работы
print(get('http://localhost:8080/api/jobs/q').json())  # Неверное получение - строка
print(post('http://localhost:8080/api/jobs',  # Корректный запрос создания работы
           json={'job': 'Работа 2',
                 'team_leader': 1,
                 'work_size': 12,
                 'collaborators': '6, 8',
                 'id': 2,
                 'is_finished': False}).json())
print(post('http://localhost:8080/api/jobs',  # Не все обязательные поля указаны при создании
           json={'job': 'Работа 2',
                 'team_leader': 1,
                 'work_size': 12,
                 'collaborators': '6, 8',
                 'is_finished': False}).json())
print(post('http://localhost:8080/api/jobs', json={}).json())  # Пустой запрос
print(post('http://localhost:8080/api/jobs',  # Не тот тип данных указан при создании
           json={'job': 'Работа 2',
                 'team_leader': '1',
                 'work_size': '12',
                 'collaborators': '6, 8', 
                 'is_finished': 2}).json())
print(delete('http://localhost:8080/api/jobs/1'))  # Корректное удаление
print(delete('http://localhost:8080/api/jobs/91239'))  # Несуществующее id
print(delete('http://localhost:8080/api/jobs/91239')) # Неверное удаление - строка
