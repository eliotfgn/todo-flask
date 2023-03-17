from flask import Flask
from flask_migrate import Migrate

from src.controller.todo_controller import todo
from src.database import db
from src.config import Config

app: Flask = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

migrate = Migrate(app, db)

app.register_blueprint(todo)

if __name__ == '__main__':
    app.run()
