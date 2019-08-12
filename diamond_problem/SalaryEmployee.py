from diamond_problem.Employee import Employee


class SalaryEmployee(Employee):
    def __init__(self, eid: str, name: str, weekly_salary: int):
        super().__init__(eid, name)
        self.weekly_salary = weekly_salary

    def calculate_payroll(self) -> int:
        return self.weekly_salary
