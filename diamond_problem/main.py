"""Main Functions"""

from diamond_problem.payroll_system import PayrollSystem
from diamond_problem.positions import (
    Manager,
    Secretary,
    SalesPerson,
    FactoryWorker,
    TemporarySecretary
)
from diamond_problem.productivity_system import ProductivitySystem


def main_call():
    """Main logic"""
    man = Manager('MID', 'MNAME', 6000)
    sec = Secretary('SECID', 'SECNAME', 3000)
    salesp = SalesPerson('SALESNAME', 'SALESID', 4000, 1500)
    facwoeker = FactoryWorker('FACID', 'FACNAME', 78, 300)
    temp = TemporarySecretary('TEMPID', 'TEMPNAME', 4000, 30)

    employees = [man, sec, salesp, facwoeker, temp]

    prod_system = ProductivitySystem()
    prod_system.track(employees, 20)

    pay_system = PayrollSystem()
    pay_system.calculate_payroll(employees)


if __name__ == '__main__':
    main_call()
