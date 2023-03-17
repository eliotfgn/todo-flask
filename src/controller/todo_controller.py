from datetime import datetime
from typing import Dict

from flask import Blueprint, jsonify, request, Response

from src.models.todo import Todo
from src.services.todo_service import TodoService

todo = Blueprint("todo", __name__, url_prefix="/api/v1/todos")


@todo.get("/")
def get_all() -> Response:
    return jsonify(TodoService.get_all())


@todo.get("/<int:todo_id>")
def get_by_id(todo_id: int) -> dict[str, object]:
    return TodoService.get_by_id(todo_id)


@todo.post("/")
def create() -> Response:
    data = request.json
    _todo = Todo(title=data["title"], description=data["description"])
    _todo.deadline = datetime.strptime(data["deadline"], "%Y-%m-%d %H:%M:%S")
    _todo.remind = datetime.strptime(data["remind"], "%Y-%m-%d %H:%M:%S")
    TodoService.create(_todo)
    return jsonify({"message": "Todo created."})


@todo.put("/<int:todo_id>")
def update(todo_id: int) -> Response:
    data = request.json
    _todo = Todo(title=data["title"], description=data["description"])
    _todo.deadline = datetime.strptime(data["deadline"], "%Y-%m-%d %H:%M:%S")
    _todo.remind = datetime.strptime(data["remind"], "%Y-%m-%d %H:%M:%S")
    TodoService.update(todo_id, _todo)
    return jsonify({"message": "Todo updated."})


@todo.delete("/<int:todo_id>")
def delete(todo_id: int) -> Response:
    TodoService.delete(todo_id)
    return jsonify({"message": "Todo deleted."})
