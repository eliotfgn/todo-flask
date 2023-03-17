from flask import Blueprint, jsonify

from src.services.todo_service import TodoService

todo = Blueprint("todo", __name__, url_prefix="/api/v1/todos")


@todo.get("/")
def get_all():
    return jsonify(TodoService.get_all())


@todo.get("/<int:todo_id>")
def get_by_id(todo_id: int):
    return TodoService.get_by_id(todo_id)
