"""Hourly Employee class"""

from diamond_problem.employee import Employee


class HourlyEmployee(Employee):
    """Class for HourlyEmployee"""
    def __init__(self, eid: str, name: str, hours_worked: int, hour_salary: int):
        """Set hours worked and hour rate. Also employee id and name"""
        super().__init__(eid, name)
        self.hours_worked = hours_worked
        self.hour_salary = hour_salary

    def calculate_payroll(self) -> int:
        """:returns salary"""
        return self.hour_salary * self.hours_worked
