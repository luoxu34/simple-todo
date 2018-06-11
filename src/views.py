# -*- coding: utf-8 -*-

from flask import request, jsonify
from flask.views import MethodView
from models import ToDo


class ToDoView(MethodView):

    def get(self, todo_id=None):
        todos = ToDo.query
        if todo_id:
            todos = todos.filter(id=todo_id)
        todos = todos.all()
        
        data = [item.to_dict() for item in todos]
        return jsonify(data)
    
    def post(self):
        data = request.get_json()

        todo = ToDo()
        todo.title = data.get('title')
        todo.notes = data.get('notes')
        todo.deadline = data.get('deadline')
        todo.tag = data.get('tag')

        todo.save()

        return 'Succeed to add task.', 201

    def patch(self, todo_id):
        todo = ToDo.query.get(todo_id)
        if todo:
            data = request.get_json()
            todo.title = data.get('title') or todo.title
            todo.complete = data.get('complete') or todo.complete
            todo.notes = data.get('notes')
            todo.deadline = data.get('deadline')
            todo.tag = data.get('tag') or todo.tag
            todo.save()
            return jsonify(todo.to_dict())
        else:
            return 'nothing to update.', 200

    def delete(self, todo_id):
        todo = ToDo.query.get(todo_id)
        if todo:
            todo.delete()

        return 'Succeed to delete task.', 204
