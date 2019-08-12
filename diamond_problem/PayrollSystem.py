class PayrollSystem:
    @staticmethod
    def calculate_payroll(employees: list):
        for employee in employees:
            print(f'Name: {employee.name}- ID: {employee.id}')
            print(f'Pay: {employee.calculate_payroll()}')
