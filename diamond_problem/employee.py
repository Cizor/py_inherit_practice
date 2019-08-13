""" Employee class"""

from abc import ABC, abstractmethod


class Employee(ABC):
    """Employee abstract class"""
    def __init__(self, eid: str, name: str):
        """ sets id and name"""
        self.eid = eid
        self.name = name

    @abstractmethod
    def calculate_payroll(self):
        """Abstract method for calculate payroll"""

    def __str__(self):
        """:returns name"""
        return self.__class__.__name__
