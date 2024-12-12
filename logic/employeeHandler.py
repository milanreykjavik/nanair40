from baseClasses.Employee import Employee
from typing import Any
import logic.validator


class EmployeeHandler:
    def __init__(self, dataWrapper=None) -> None:
        self.dataWrapper = dataWrapper
        self.employee = Employee()

    def addEmployee(self, employee: 'Employee') -> bool:
        # https://www.quora.com/What-is-maximum-and-minimum-length-of-any-mobile-number-across-the-world
        # logic layer checking, here the data is confirmed to be true from UI layer, if not false is returned
        if not logic.validator.checkEntries(employee.__dict__.values()):
            return False
        if not logic.validator.validateKennitala(employee.kennitala):
            return False
        if self.listEmployes(kennitala=employee.kennitala):
            return False
        if not logic.validator.validatePhone(employee.phone):
            return False
        if not logic.validator.validatePhone(employee.homePhone):
            return False
        if not logic.validator.validateEmail(employee.email):
            return False

        return self.dataWrapper.employeeInsert(employee)


    def editEmployee(self, entry: str, entryValue: Any, **kwargs) -> bool:
        if not len(kwargs):
            return False
        if any(kwarg not in vars(self.employee) for kwarg in kwargs):
            return False
        # https://www.quora.com/What-is-maximum-and-minimum-length-of-any-mobile-number-across-the-world
        if not entry:
            return False
        if not entryValue:
            return False
        if entry == "kennitala":
            if not logic.validator.validateKennitala(entryValue):
                return False
            if not self.listEmployes(kennitala=entryValue):
                return False
           

        if entry == "phone" or entry == "homePhone":
            if not logic.validator.validatePhone(entryValue):
                return False

        if entry == "email":
            if not logic.validator.validateEmail(entryValue):
                return False
                   
        return self.dataWrapper.employeeChange(entry, entryValue, **kwargs)


    def listEmployes(self, **kwargs) -> list['Employee']:
        if any(kwarg not in vars(self.employee) for kwarg in kwargs):
            return []

        employees: list['Employee'] = self.dataWrapper.employeeFetch()
        if not len(kwargs):
            return employees

        for k, v in kwargs.items():
            # Top to bottom if we go bottom to top we get index out of range
            # Because things get deleted if they do not match the query before we loop through them if we go bottom to top
            for i in range(len(employees)-1, -1, -1):
                # hack around to check if result that might be int or float partialy contains our target number
                if str(v) != str(employees[i].__dict__[k]): # used to be not in but we only want exact matches so
                    del employees[i]


        return employees
