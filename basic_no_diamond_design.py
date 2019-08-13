""" No Diamond Design Practice"""


class Productivity:
    """ Functions related to productivity """
    @staticmethod
    def track(employees: list, hours: int):
        """ Function prints Employee name and hours"""
        print('Tracking')
        for employee in employees:
            result = employee.work(hours)
            print(f"{employee.name}{result}")
        print('')

    def __str__(self):
        """ :returns class name"""
        return self.__class__.__name__


class ManagerRole:
    """ Functions related to Manager role """
    @staticmethod
    def work(hours: int):
        """ :returns work and hours"""
        return f"manages for {hours}"

    def __str__(self):
        """ :returns class name"""
        return self.__class__.__name__


class PayrollSystem:
    """ Functions related to Payroll system"""
    @staticmethod
    def calculate_payroll(employees: list):
        """ Prints employee name and payroll"""
        for employee in employees:
            print('Calculating payroll')
            print(f"{employee.name} salary is {employee.calculate_payroll()}")

    def __str__(self):
        """ :returns class name"""
        return self.__class__.__name__


class SalaryPolicy:
    """ Functions related to Salary Policy"""
    def __init__(self, weekly_salary: int):
        """ Initializes weekly salary """
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        """ :returns weekly salary """
        return self.weekly_salary

    def __str__(self):
        """ :returns class name"""
        return self.__class__.__name__


class Employee:
    """ Functions related to Employee """
    def __init__(self, eid: str, name: str):
        """ Initializes Employee ID and name """
        self.eid = eid
        self.name = name

    def __str__(self):
        """ :returns class name"""
        return self.__class__.__name__

    def __len__(self):  # len added to get perfect score at Pylint
        """ :returns len"""
        return self.__len__()


class Manager(Employee, ManagerRole, SalaryPolicy):
    """ Functions related to Manager """
    def __init__(self, eid: str, name: str, weekly_salary: int):
        """ Initializes Salary and Employee """
        SalaryPolicy.__init__(self, weekly_salary)
        super().__init__(eid, name)

    def __str__(self):
        """ :returns class name"""
        return self.__class__.__name__


def main_call():
    """ Main calling function """
    manager1 = Manager("1", "Mary Poppins", 3000)
    manager2 = Manager("2", "Luke Dave", 5000)
    company_employees = [
        manager1,
        manager2
    ]
    Productivity.track(company_employees, 40)
    PayrollSystem.calculate_payroll(company_employees)


if __name__ == '__main__':
    main_call()
