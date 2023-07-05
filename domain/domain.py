from datetime import date
from uuid import uuid4, UUID

from domain.exceptions import DadosInvalidosError
from domain.abstracts_domains import AbstractDomain

class Task(AbstractDomain):

    def __init__(self, description: str, name: str, due_date: date, id: UUID = None) -> None:
        self.name = name
        self.description = description
        self.due_date = due_date
        self.id = id

    @classmethod
    def from_dict(cls, data: dict):
        try:
            return cls(name=data['name'],
                       description=data['description'],
                       due_date=date.fromisoformat(data['due_date']),
                       id=UUID(data['id']) if data.get('id') else uuid4())
        except (KeyError, ValueError):
            raise DadosInvalidosError()

    def to_dict(self):
        return {
            "id": str(self.id),
            "name": self.name,
            "description": self.description,
            "due_date": str(self.due_date)
        }

    def update_from_dict(self, update_data: dict):
        if new_description := update_data.get('description'):
            self.description = new_description
        if new_due_date := update_data.get('due_date'):
            self.due_date = new_due_date
        if new_name := update_data.get('name'):
            self.name = new_name
