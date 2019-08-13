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


class SecretaryRole:
    @staticmethod
    def work(hours: int):
        return f"files for {hours}"


class SalesPersonRole:
    @staticmethod
    def work(hours: int):
        return f"on phone for {hours}"