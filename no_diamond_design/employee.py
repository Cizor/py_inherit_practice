""" Functions related to Employee and types"""

from no_diamond_design import payroll as pay
from no_diamond_design import productivity as product


class Employee:
    """ Functions related to Employee"""
    def __init__(self, eid: str, name: str):
        """ Sets employee name and id"""
        self.eid = eid
        self.name = name

    def __str__(self):
        """ :returns class name"""
        return self.__class__.__name__

    def __len__(self):
        """ :returns len"""
        return self.__len__()


class Manager(Employee, product.ManagerRole, pay.SalaryPolicy):
    """ Functions related to Manager"""
    def __init__(self, eid: str, name: str, weekly_salary: int):
        """ Sets Salary Policy and employee name and id"""
        pay.SalaryPolicy.__init__(self, weekly_salary)
        super().__init__(eid, name)

    def __str__(self):
        """ :returns class name"""
        return self.__class__.__name__

    def __len__(self):
        """ :returns len"""
        return self.__len__()


class Secretary(Employee, product.SecretaryRole, pay.HourlyPolicy):
    """ Functions related to Secretary"""
    def __init__(self, eid: str, name: str, hours_worked: int, hours_rate: int):
        """ Sets HourlyPolicy and employee name and id"""
        pay.HourlyPolicy.__init__(self, hours_worked, hours_rate)
        super().__init__(eid, name)

    def __str__(self):
        """ :returns class name"""
        return self.__class__.__name__

    def __len__(self):
        """ :returns len"""
        return self.__len__()


class SalesPerson(Employee, product.SalesPersonRole, pay.CommissionPolicy):
    """ Functions related to SalesPerson"""
    def __init__(self, eid: str, name: str, weekly_salary: int, commission: int):
        """ Sets CommissionSalary Policy and employee name and id"""
        pay.CommissionPolicy.__init__(self, weekly_salary, commission)
        super().__init__(eid, name)

    def __str__(self):
        """ :returns class name"""
        return self.__class__.__name__

    def __len__(self):
        """ :returns len"""
        return self.__len__()
