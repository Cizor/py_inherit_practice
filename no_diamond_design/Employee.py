from no_diamond_design.payroll import *
from no_diamond_design.productivity import *


class Employee:
    def __init__(self, eid: str, name: str):
        self.eid = eid
        self.name = name


class Manager(Employee, ManagerRole, SalaryPolicy):
    def __init__(self, eid: str, name: str, weekly_salary: int):
        SalaryPolicy.__init__(self, weekly_salary)
        super().__init__(eid, name)


class Secretary(Employee, SecretaryRole, HourlyPolicy):
    def __init__(self, eid: str, name: str, hours_worked: int, hours_rate: int):
        HourlyPolicy.__init__(self, hours_worked, hours_rate)
        super().__init__(eid, name)


class SalesPerson(Employee, SalesPersonRole, CommissionPolicy):
    def __init__(self, eid: str, name: str, weekly_salary: int, commission: int):
        CommissionPolicy.__init__(self, weekly_salary, commission)
        super().__init__(eid, name)
