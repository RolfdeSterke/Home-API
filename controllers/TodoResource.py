from flask_restful import Resource, request
from models.Todo import TodoModel
import json


class HiddenResource(Resource):

    def get(self):
        all_todos = TodoModel.find_all()
        all_in_json = [todo.to_json() for todo in all_todos]
        return {"todos": all_in_json}, 200


class TodosResource(Resource):

    def get(self):
        all_todos = TodoModel.find_all_non_hidden() or []
        all_in_json = [todo.to_json() for todo in all_todos]
        return {"todos": all_in_json}, 200

    def post(self):
        data = json.loads(request.data)
        if data['is_done']:
            is_done = 1
        else:
            is_done = 0
        if data['is_hidden']:
            is_hidden = 1
        else:
            is_hidden = 0
        todo = TodoModel(data['comment'], data['uri'], data['image_uri'], is_done, is_hidden)
        todo.save_to_db()
        return todo.to_json(), 201


class TodoResource(Resource):

    def get(self, todo_id):
        todo = TodoModel.find_by_id(todo_id)
        return todo.to_json()

    def post(self, todo_id):
        todo = TodoModel.find_by_id(todo_id)
        data = json.loads(request.data)
        if data['is_done']:
            is_done = 1
        else:
            is_done = 0
        if data['is_hidden']:
            is_hidden = 1
        else:
            is_hidden = 0
        todo.update(data['comment'], data['uri'], data['image_uri'], is_done, is_hidden)
        return todo.to_json(), 200

    def delete(self, todo_id):
        todo = TodoModel.find_by_id(todo_id)
        todo.delete_from_db()
        return "SUCCESSFUL DELETE", 200
