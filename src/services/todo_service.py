from datetime import timedelta

from src.database import db
from src.models.todo import Todo
from src.scheduler import scheduler


def remind(todo_id: int) -> None:
    print(f"Reminder for todo with id: {todo_id}.")


def remind_thirty_min_before(todo_id: int) -> None:
    print(f"It remains 30 to complete task with id: {todo_id}")


class TodoService:
    @staticmethod
    def create(todo: Todo) -> bool:
        try:
            db.session.add(todo)
            db.session.commit()
        except Exception as e:
            print(e)
            return False

        if todo.remind:
            remind_job_id = f"remind_for_{todo.id}"
            job = scheduler.add_job(id=remind_job_id, func=remind, trigger="date", args=[todo.id], run_date=todo.remind)
            print(job.id)

        if todo.deadline:
            job_id = f"remind_deadline_for_{todo.id}"
            remind_date = todo.deadline - timedelta(minutes=30)
            scheduler.add_job(id=job_id, func=remind_thirty_min_before, trigger="date", args=[todo.id],
                              run_date=remind_date)

        return True

    @staticmethod
    def get_all() -> list[dict[str, object]]:
        data = Todo.query.all()
        return [todo.to_json() for todo in data]

    @staticmethod
    def get_by_id(todo_id: int) -> dict[str, object]:
        todo = Todo.query.filter_by(id=todo_id).first()
        return todo.to_json()

    @staticmethod
    def update(todo_id: int, todo: Todo) -> bool:
        try:
            entity: Todo = Todo.query.filter_by(id=todo_id).first()
            entity.title = todo.title
            entity.description = todo.description
            entity.deadline = todo.deadline
            entity.remind = todo.remind
            db.session.commit()
        except Exception as e:
            print(e)
            return False

        """
        if todo.remind:
            job_id = f"remind_for_{entity.id}"
            scheduler.reschedule_job(job_id=job_id, trigger="date", run_date=todo.remind)

        if todo.deadline:
            job_id = f"remind_deadline_for_{entity.id}"
            remind_date = todo.deadline - timedelta(minutes=30)
            scheduler.reschedule_job(job_id=job_id, trigger="date",
                                     run_date=remind_date)
        """

        return True

    @staticmethod
    def delete(todo_id: int) -> bool:
        try:
            entity = Todo.query.filter_by(id=todo_id).first()
            if not entity:
                return False
            db.session.delete(entity)
            db.session.commit()
        except Exception as e:
            print(e)
            return False

        """
        scheduler.remove(f"remind_for_{todo_id}")
        scheduler.remove(f"remind_deadline_for_{todo_id}")
        """
        return True
