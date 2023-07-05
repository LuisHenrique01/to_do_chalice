from datetime import date
from domain import SUCCESS_MESSAGE
from domain.domain import Task
from domain.exceptions import DadosInvalidosError, BaseException
from infrastructure.repositories import TaskRepository


class TaskService:

    def __init__(self) -> None:
        self.task_repository = TaskRepository()

    def list_tasks(self):
        tasks = self.task_repository.get_all_items()
        return [task.to_dict() for task in tasks]

    def create_task(self, task_data: dict):
        try:
            task = Task.from_dict(task_data)
            if self._validate_due_date(task):
                self.task_repository.save_item(task)
                return task.to_dict()
            raise DadosInvalidosError('Data inválida, due_date deve ser maior que a data atual.')
        except (DadosInvalidosError, BaseException) as e:
            return e.serializer

    def get_task(self, task_id: str):
        try:
            task = self.task_repository.get_item(task_id)
            return task.to_dict()
        except (DadosInvalidosError, BaseException) as e:
            return e.serializer

    def update_task(self, task_id: str, update_data: dict):
        try:
            task = self.task_repository.get_item(task_id)
            task.update_from_dict(update_data)
            if self._validate_due_date(task):
                self.task_repository.update_item(task_id, update_data)
                return task.to_dict()
            raise DadosInvalidosError('Data inválida, due_date deve ser maior que a data atual.')
        except (DadosInvalidosError, BaseException) as e:
            return e.serializer

    def delete_item(self, task_id: str):
        try:
            self.task_repository.delete_item(task_id)
            return SUCCESS_MESSAGE
        except (DadosInvalidosError, BaseException) as e:
            return e.serializer

    def _validate_due_date(self, task: Task) -> bool:
        return task.due_date >= date.today()
