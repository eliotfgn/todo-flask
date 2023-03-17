from datetime import datetime

from flask import Blueprint, jsonify, request

from src.models.todo import Todo
from src.services.todo_service import TodoService

todo = Blueprint("todo", __name__, url_prefix="/api/v1/todos")


@todo.get("/")
def get_all():
    return jsonify(TodoService.get_all())


@todo.get("/<int:todo_id>")
def get_by_id(todo_id: int):
    return TodoService.get_by_id(todo_id)


@todo.post("/")
def create():
    data = request.json
    _todo = Todo(title=data["title"], description=data["description"])
    _todo.deadline = datetime.strptime(data["deadline"], "%Y-%m-%d %H:%M:%S")
    _todo.remind = datetime.strptime(data["remind"], "%Y-%m-%d %H:%M:%S")
    TodoService.create(_todo)
    return jsonify({"message": "Todo created."})
