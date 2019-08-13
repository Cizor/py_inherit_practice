"""Payroll System class"""


class PayrollSystem:
    """Payroll System class and it's functions"""
    @staticmethod
    def calculate_payroll(employees: list):
        """Prints employee name, id and salary"""
        for employee in employees:
            print(f'Name: {employee.name}- ID: {employee.id}')
            print(f'Pay: {employee.calculate_payroll()}')

    def __str__(self):
        """:returns name"""
        return self.__class__.__name__
