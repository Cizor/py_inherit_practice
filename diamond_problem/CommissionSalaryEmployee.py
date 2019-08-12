from diamond_problem.SalaryEmployee import SalaryEmployee


class CommissionSalaryEmployee(SalaryEmployee):
    def __init__(self, name: str, eid: str, weekly_salary: int, commission: int):
        super().__init__(eid, name, weekly_salary)
        self.commission = commission

    def calculate_payroll(self) -> int:
        return super().calculate_payroll() + self.commission
