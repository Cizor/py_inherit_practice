from diamond_problem.PayrollSystem import PayrollSystem
from diamond_problem.Positions import *
from diamond_problem.ProductivitySystem import ProductivitySystem
'''
s = SalaryEmployee('SID', 'SNAME', 500)
h = HourlyEmployee('HID', 'HNAME', 13, 400)
c = CommissionSalaryEmployee('CNAME', 'CID', 500, 700)

pr = PayrollSystem.calculate_payroll([s, h, c])
'''
m = Manager('MID', 'MNAME', 6000)
sec = Secretary('SECID', 'SECNAME', 3000)
salesp = SalesPerson('SALESNAME', 'SALESID', 4000, 1500)
facwoeker = FactoryWorker('FACID', 'FACNAME', 78, 300)
temp = TemporarySecretary('TEMPID', 'TEMPNAME', 4000, 30)

employees = [m, sec, salesp, facwoeker, temp]

prod_system = ProductivitySystem()
prod_system.track(employees, 20)

pay_system = PayrollSystem()
pay_system.calculate_payroll(employees)
