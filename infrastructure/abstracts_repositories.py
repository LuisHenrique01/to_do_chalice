from abc import ABC, abstractmethod
from typing import Any


class AbstractRepository(ABC):

    @abstractmethod
    def get_all_items(self):
        ...

    @abstractmethod
    def get_item(self, item_id: str):
        ...

    @abstractmethod
    def save_item(self, item: Any):
        ...

    @abstractmethod
    def update_item(self, item_id: str, update_data: dict):
        ...

    @abstractmethod
    def delete_item(self, item_id: str):
        ...

    @staticmethod
    def _generate_update_expression(update_data: dict) -> str:
        return 'SET ' + ', '.join((f'#{key} = :{key}' for key in update_data.keys()))

    @staticmethod
    def _generate_expression_attribute_values(update_data: dict) -> str:
        return {f':{key}': value for key, value in update_data.items()}

    @staticmethod
    def _generate_expression_attribute_names(update_data: dict) -> str:
        return {f'#{key}': key for key in update_data.keys()}
