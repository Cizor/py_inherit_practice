"""CommissionSalaryEmployee class"""

from diamond_problem.salary_employee import SalaryEmployee


class CommissionSalaryEmployee(SalaryEmployee):
    """Class for CommisionSalaryEmployee"""
    def __init__(self, name: str, eid: str, weekly_salary: int, commission: int):
        """ set commission, employee id and name, weekly salary"""
        super().__init__(eid, name, weekly_salary)
        self.commission = commission

    def calculate_payroll(self) -> int:
        """:returns salary"""
        return super().calculate_payroll() + self.commission

    def __str__(self):
        """:returns name"""
        return self.__class__.__name__
