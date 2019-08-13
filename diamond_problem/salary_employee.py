"""Salary Employee class"""

from diamond_problem.employee import Employee


class SalaryEmployee(Employee):
    """Class of Salary Employee"""
    def __init__(self, eid: str, name: str, weekly_salary: int):
        """Sets employee id, nane and salary"""
        super().__init__(eid, name)
        self.weekly_salary = weekly_salary

    def calculate_payroll(self) -> int:
        """:returns salary"""
        return self.weekly_salary

    def __str__(self):
        """:returns name"""
        return self.__class__.__name__
