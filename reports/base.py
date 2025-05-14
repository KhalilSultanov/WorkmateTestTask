from abc import ABC, abstractmethod
from typing import List
from models.employee import Employee

class Report(ABC):
    @abstractmethod
    def generate(self, employees: List[Employee]) -> None:
        pass
