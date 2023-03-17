from datetime import datetime

from flask_sqlalchemy.model import Model
from sqlalchemy import Column, Integer, String, DateTime

from src.database import db


class Todo(Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    description = Column(String)
    deadline = Column(DateTime)
    remind = Column(DateTime)
    createdAt = Column(DateTime, default=datetime.now())
    updatedAt = Column(DateTime, onupdate=datetime.now())

    def to_json(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'deadline': self.deadline,
            'remind': self.remind,
            'createdAt': self.createdAt,
            'updatedAt': self.updatedAt
        }