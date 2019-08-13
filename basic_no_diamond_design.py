class Productivity:
    @staticmethod
    def track(employees: list, hours: int):
        print('Tracking')
        for employee in employees:
            result = employee.work(hours)
            print(f"{employee.name}{result}")
        print('')


class ManagerRole:
    @staticmethod
    def work(hours: int):
        return f"manages for {hours}"


class PayrollSystem:
    @staticmethod
    def calculate_payroll(employees: list):
        for employee in employees:
            print('Calculating payroll')
            print(f"{employee.name} salary is {employee.calculate_payroll()}")


class SalaryPolicy:
    def __init__(self, weekly_salary: int):
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary


class Employee:
    def __init__(self, eid: str, name: str):
        self.eid = eid
        self.name = name


class Manager(Employee, ManagerRole, SalaryPolicy):
    def __init__(self, eid: str, name: str, weekly_salary: int):
        SalaryPolicy.__init__(self, weekly_salary)
        super().__init__(eid, name)


if __name__ == '__main__':
    manager1 = Manager("1", "Mary Poppins", 3000)
    manager2 = Manager("2", "Luke Dave", 5000)
    company_employees = [
        manager1,
        manager2
    ]
    Productivity.track(company_employees, 40)
    PayrollSystem.calculate_payroll(company_employees)
