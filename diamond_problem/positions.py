"""Position classes"""

from diamond_problem.salary_employee import SalaryEmployee
from diamond_problem.commission_salary_employee import CommissionSalaryEmployee
from diamond_problem.hourly_employee import HourlyEmployee


class Manager(SalaryEmployee):
    """Manager class"""
    def work(self, hours: int):
        """print name, work and hours"""
        print(f'{self.name} manages for {hours}')


class Secretary(SalaryEmployee):
    """Secretary class"""
    def work(self, hours: int):
        """print name, work and hours"""
        print(f'{self.name} files for {hours}')


class SalesPerson(CommissionSalaryEmployee):
    """SalesPerson class"""
    def work(self, hours: int):
        """print name, work and hours"""
        print(f'{self.name} is on phone for {hours}')


class FactoryWorker(HourlyEmployee):
    """FactoryWorker class"""
    def work(self, hours: int):
        """print name, work and hours"""
        print(f'{self.name} manufactured for {hours}')


# Diving into multiple inheritance.
# Fixing Diamond problem by forcing HourlyEmployee payroll calculation
class TemporarySecretary(Secretary, HourlyEmployee):
    """TemporarySecretary class"""
    def __init__(self, eid, name, hours_worked, hours_rate):
        """Sets HourlyEmployee forcefully to avoid diamond problem"""
        HourlyEmployee.__init__(self, eid, name, hours_worked, hours_rate)

    def calculate_payroll(self) -> int:
        """:returns hourly employee salary"""
        return HourlyEmployee.calculate_payroll(self)
