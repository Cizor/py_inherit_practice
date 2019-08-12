from diamond_problem.Employee import Employee


class HourlyEmployee(Employee):
    def __init__(self, eid: str, name: str, hours_worked: int, hour_salary: int):
        super().__init__(eid, name)
        self.hours_worked = hours_worked
        self.hour_salary = hour_salary

    def calculate_payroll(self) -> int:
        return self.hour_salary * self.hours_worked
