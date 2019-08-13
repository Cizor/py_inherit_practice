""" Main function call """

from no_diamond_design.employee import (Manager, Secretary, SalesPerson)
from no_diamond_design.payroll import PayrollSystem
from no_diamond_design.productivity import Productivity


def main_call():
    """ Main logic to function call"""
    manager = Manager("1", "Mary Poppins", 3000)
    secretary = Secretary("2", 'John Smith', 1500, 21)
    sales_guy = SalesPerson("3", 'Kevin Bacon', 1000, 250)
    company_employees = [
        manager,
        secretary,
        sales_guy
    ]
    Productivity.track(company_employees, 40)
    PayrollSystem.calculate_payroll(company_employees)


if __name__ == '__main__':
    main_call()
