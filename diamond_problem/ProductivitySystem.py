class ProductivitySystem:
    @staticmethod
    def track(employees: list, hours: int):
        print('Tracking')
        for employee in employees:
            employee.work(hours)
