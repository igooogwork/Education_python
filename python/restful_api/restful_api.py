# -*- coding: utf-8 -*-

# Создать RESTful API для управления задачами. 
# API должно обеспечивать следующие функции:
# 1)Создание новой задачи.
# 2)Получение списка задач.
# 3)Получение информации о конкретной задаче.
# 4)Обновление информации о задаче.
# 5)Удаление задачи.

from flask import Flask, request, jsonify

app = Flask(__name__)
tasks = []

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    new_task = {
        'id': len(tasks) + 1,
        'title': data['title'],
        'description': data['description'],
        'status': 'не выполнено'
    }
    tasks.append(new_task)
    return jsonify(new_task), 201

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

@app.route('/tasks/<int:task_id>', methods=['GET']) 
def get_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task is None:
        return jsonify({'error': 'Задача не найдена'}), 404
    return jsonify(task)

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task is None:
        return jsonify({'error': 'Задача не найдена'}), 404
    data = request.get_json()
    task['title'] = data['title']
    task['description'] = data['description']
    task['status'] = data['status']
    return jsonify(task)

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task is None:
        return jsonify({'error': 'Задача не найдена'}), 404
    tasks.remove(task)
    return jsonify({'message': 'Задача удалена'})

if __name__ == '__main__':
    app.run(debug=True)