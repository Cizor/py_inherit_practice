class PayrollSystem:
    @staticmethod
    def calculate_payroll(employees: list):
        for employee in employees:
            print('Calculating payroll')
            print(f"{employee.name} salary is {employee.calculate_payroll()}" )


class SalaryPolicy:
    def __init__(self, weekly_salary: int):
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary


class HourlyPolicy:
    def __init__(self, hours_worked: int, hour_rate: int):
        self.hours_worked = hours_worked
        self.hour_rate = hour_rate

    def calculate_payroll(self):
        return self.hours_worked * self.hour_rate


class CommissionPolicy(SalaryPolicy):
    def __init__(self, weekly_salary: int, commission: int):
        super().__init__(weekly_salary)
        self.commission = commission

    def calculate_payroll(self):
        return super().calculate_payroll() + self.commission
