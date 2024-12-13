from baseClasses.Employee import Employee
from typing import Any
import logic.validator

class EmployeeHandler:
    def __init__(self, dataWrapper=None) -> None:
        """
        [>] Constructor for EmployeeHandler class
        Initialize with optional dataWrapper, and initialize Employee object
        """
        self.dataWrapper = dataWrapper
        self.employee = Employee()

    def addEmployee(self, employee: 'Employee') -> bool:
        """
        [>] This function adds a new employee to the system
        It returns true or false based on several checks:
        - Checks if any fields are empty or invalid
        - Validates the employee's kennitala
        - Ensures there are no duplicate employees with the same kennitala
        - Validates phone, home phone, and email
        - Checks that the employee's name does not exceed 40 characters
        """
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
        if len(employee.name) > 40:
            return False

        return self.dataWrapper.employeeInsert(employee)

    def editEmployee(self, entry: str, entryValue: Any, **kwargs) -> bool:
        """
        [>] This function is used to edit an existing employee's details
        It returns true or false based on the following conditions:
        - Verifies the entry and entryValue are valid
        - Checks for valid kennitala, name length, phone number, and email
        - Ensures that the employee's kennitala is not already taken
        """
        if not len(kwargs):
            return False
        if any(kwarg not in vars(self.employee) for kwarg in kwargs):
            return False
        if not entry:
            return False
        if not entryValue:
            return False
        if entry == "kennitala":
            if not logic.validator.validateKennitala(entryValue):
                return False
            if not self.listEmployes(kennitala=entryValue):
                return False
        if entry == "name":
            if len(entryValue) > 40:
                return False
        if entry == "phone" or entry == "homePhone":
            if not logic.validator.validatePhone(entryValue):
                return False
        if entry == "email":
            if not logic.validator.validateEmail(entryValue):
                return False
        return self.dataWrapper.employeeChange(entry, entryValue, **kwargs)

    def listEmployes(self, **kwargs) -> list['Employee']:
        """
        [>] This function lists all employees or filters them based on given criteria
        Returns a list of employees, optionally filtered by the provided kwargs
        kwargs: any field of Employee class to filter the list (e.g., "kennitala", "name", "phone")
        """
        if any(kwarg not in vars(self.employee) for kwarg in kwargs):
            return []

        employees: list['Employee'] = self.dataWrapper.employeeFetch()
        if not len(kwargs):
            return employees

        for k, v in kwargs.items():
            # Top to bottom if we go bottom to top we get index out of range
            # Because things get deleted if they do not match the query before we loop through them if we go bottom to top
            for i in range(len(employees)-1, -1, -1):
                # hack around to check if result that might be int or float partially contains our target number
                if str(v) != str(employees[i].__dict__[k]):  # exact match instead of partial
                    del employees[i]

        return employees

