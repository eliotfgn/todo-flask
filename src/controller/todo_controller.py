from datetime import datetime
from typing import Dict

from flask import Blueprint, jsonify, request, Response
from flask_cors import cross_origin

from src.models.todo import Todo
from src.services.todo_service import TodoService

todo = Blueprint("todo", __name__, url_prefix="/api/v1/todos")


@todo.get("/")
@cross_origin()
def get_all() -> Response:
    try:
        return jsonify(TodoService.get_all())
    except Exception as e:
        return jsonify({"message": e})


@todo.get("/<int:todo_id>")
def get_by_id(todo_id: int) -> Response:
    try:
        _todo = TodoService.get_by_id(todo_id)
        if _todo:
            return jsonify(_todo)
        else:
            return jsonify({"message": "Todo not found"}), 404
    except Exception as e:
        return jsonify({"message": e})


@todo.post("/")
def create() -> Response:
    try:
        data = request.json
        _todo = Todo(title=data["title"], description=data["description"])
        _todo.deadline = datetime.strptime(data["deadline"], "%Y-%m-%d %H:%M:%S")
        _todo.remind = datetime.strptime(data["remind"], "%Y-%m-%d %H:%M:%S")
        TodoService.create(_todo)
        return jsonify({"message": "Todo created."})
    except Exception as e:
        return jsonify({"message": e})


@todo.put("/<int:todo_id>")
def update(todo_id: int) -> Response:
    try:
        data = request.json
        _todo = Todo(title=data["title"], description=data["description"])
        _todo.deadline = datetime.strptime(data["deadline"], "%Y-%m-%d %H:%M:%S")
        _todo.remind = datetime.strptime(data["remind"], "%Y-%m-%d %H:%M:%S")
        TodoService.update(todo_id, _todo)
        return jsonify({"message": "Todo updated."})
    except Exception as e:
        return jsonify({"message": e})


@todo.delete("/<int:todo_id>")
def delete(todo_id: int) -> Response:
    try:
        TodoService.delete(todo_id)
        return jsonify({"message": "Todo deleted."})
    except Exception as e:
        return jsonify({"message": e})
