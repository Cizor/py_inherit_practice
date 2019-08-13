"""ProductivitySystem class"""


class ProductivitySystem:
    """Class for Productivity"""
    @staticmethod
    def track(employees: list, hours: int):
        """Track work"""
        print('Tracking')
        for employee in employees:
            employee.work(hours)

    def __str__(self):
        """:returns name"""
        return self.__class__.__name__
