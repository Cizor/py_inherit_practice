from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, eid: str, name: str):
        self.id = eid
        self.name = name

    @abstractmethod
    def calculate_payroll(self):
        pass
