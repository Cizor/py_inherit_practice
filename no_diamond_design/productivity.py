""" Functions related to Productivity """


class Productivity:
    """ Functions related to productivity """
    @staticmethod
    def track(employees: list, hours: int):
        """ Prints Employee name and hours"""
        print('Tracking')
        for employee in employees:
            result = employee.work(hours)
            print(f"{employee.name}{result}")
        print('')

    def __str__(self):
        """ :returns class name"""
        return self.__class__.__name__


class ManagerRole:
    """ Functions related to ManagerRole"""
    @staticmethod
    def work(hours: int):
        """ :returns work and hours"""
        return f"manages for {hours}"

    def __str__(self):
        """ :returns class name"""
        return self.__class__.__name__


class SecretaryRole:
    """ Functions related to Secretary Role"""
    @staticmethod
    def work(hours: int):
        """ :returns work and hours"""
        return f"files for {hours}"

    def __str__(self):
        """ :returns class name"""
        return self.__class__.__name__


class SalesPersonRole:
    """ Functions related to SalesPersonRole"""
    @staticmethod
    def work(hours: int):
        """ :returns work and hours"""
        return f"on phone for {hours}"

    def __str__(self):
        """ :returns class name"""
        return self.__class__.__name__
