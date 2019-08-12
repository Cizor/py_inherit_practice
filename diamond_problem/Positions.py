from diamond_problem.SalaryEmployee import SalaryEmployee
from diamond_problem.CommissionSalaryEmployee import CommissionSalaryEmployee
from diamond_problem.HourlyEmployee import HourlyEmployee


class Manager(SalaryEmployee):
    def work(self, hours: int):
        print(f'{self.name} manages for {hours}')


class Secretary(SalaryEmployee):
    def work(self, hours: int):
        print(f'{self.name} files for {hours}')


class SalesPerson(CommissionSalaryEmployee):
    def work(self, hours: int):
        print(f'{self.name} is on phone for {hours}')


class FactoryWorker(HourlyEmployee):
    def work(self, hours: int):
        print(f'{self.name} manufactured for {hours}')


# Diving into multiple inheritance. Fixing Diamond problem by forcing HourlyEmployee payroll calculation
class TemporarySecretary(Secretary, HourlyEmployee):
    def __init__(self, eid, name, hours_worked, hours_rate):
        HourlyEmployee.__init__(self, eid, name, hours_worked, hours_rate)

    def calculate_payroll(self) -> int:
        return HourlyEmployee.calculate_payroll(self)

