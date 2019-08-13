from no_diamond_design.Employee import *
from no_diamond_design.payroll import PayrollSystem
from no_diamond_design.productivity import Productivity

'''
m = Manager("MID", "MNAME", 100)
s = SalesPerson("SALESID", "SALESNAME", 200, 500)
c = Secretary("SECID", "SECNAME", 12, 300)

employees = [m, s, c]
pr = Productivity()
pr.track(employees, 30)

pa = PayrollSystem()
pa.calculate_payroll(employees)
'''

manager = Manager("1", "Mary Poppins", 3000)
secretary = Secretary("2", 'John Smith', 1500, 21)
sales_guy = SalesPerson("3", 'Kevin Bacon', 1000, 250)
company_employees = [
    manager,
    secretary,
    sales_guy
]
pr = Productivity()
pr.track(company_employees, 40)
PayrollSystem.calculate_payroll(company_employees)
