""" Functions related to payroll """


class PayrollSystem:
    """ Functions related to payroll system"""
    @staticmethod
    def calculate_payroll(employees: list):
        """ prints employee name and salary"""
        for employee in employees:
            print('Calculating payroll')
            print(f"{employee.name} salary is {employee.calculate_payroll()}")

    def __str__(self):
        """ :returns class name"""
        return self.__class__.__name__


class SalaryPolicy:
    """ Functions related to SalaryPolicy"""
    def __init__(self, weekly_salary: int):
        """ Sets weekly salary """
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        """ :returns weekly salary """
        return self.weekly_salary

    def __str__(self):
        """ :returns class name"""
        return self.__class__.__name__


class HourlyPolicy:
    """ Functions related to HourlyPolicy"""
    def __init__(self, hours_worked: int, hour_rate: int):
        """ Sets hours worked and rate"""
        self.hours_worked = hours_worked
        self.hour_rate = hour_rate

    def calculate_payroll(self):
        """ :returns salary"""
        return self.hours_worked * self.hour_rate

    def __str__(self):
        """ :returns class name"""
        return self.__class__.__name__


class CommissionPolicy(SalaryPolicy):
    """ Functions related to Commission Policy"""
    def __init__(self, weekly_salary: int, commission: int):
        """ Sets weekly salary and commission """
        super().__init__(weekly_salary)
        self.commission = commission

    def calculate_payroll(self):
        """ :returns salary"""
        return super().calculate_payroll() + self.commission

    def __str__(self):
        """ :returns class name"""
        return self.__class__.__name__
