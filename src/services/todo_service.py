from src.database import db
from src.models.todo import Todo


class TodoService:
    @staticmethod
    def create(todo: Todo) -> bool:
        try:
            db.session.add(todo)
            db.session.commit()
        except Exception as e:
            print(e)
            return False
        return True

    @staticmethod
    def get_all() -> list[dict[str, object]]:
        data = Todo.query.all()
        return [todo.to_json() for todo in data]

    @staticmethod
    def get_by_id(todo_id: int) -> dict[str, object]:
        todo = Todo.query.filter_by(id=todo_id).first()
        return todo.to_json()
