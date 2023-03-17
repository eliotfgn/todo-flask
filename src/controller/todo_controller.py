from flask import Blueprint

todo = Blueprint("todo", __name__, url_prefix="/api/v1/todos")
