Создание задачи (POST):

POST http://127.0.0.1:5000/tasks
Content-Type: application/json
{
    "title": "Завершить проект",
    "description": "Завершить разработку API"
}


Получение списка задач (GET):

GET http://127.0.0.1:5000/tasks


Получение информации о задаче (GET):

GET http://127.0.0.1:5000/tasks/1


Обновление задачи (PUT):

PUT http://127.0.0.1:5000/tasks/1
Content-Type: application/json
{
    "title": "Завершить проект",
    "description": "Завершить разработку API",
    "status": "выполнено"
}


Удаление задачи (DELETE):

DELETE http://127.0.0.1:5000/tasks/1