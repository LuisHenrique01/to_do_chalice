from abc import ABC, abstractmethod
from typing import Any


class AbstractDomain(ABC):

    @classmethod
    @abstractmethod
    def from_dict(cls, data: dict):
        ...

    @abstractmethod
    def to_dict(self):
        ...
