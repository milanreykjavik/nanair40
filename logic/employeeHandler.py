from baseClasses.Employee import Employee
from dataControl.employeeController import EmployeeController
from typing import Any


class EmployeeHandler:
    def __init__(self) -> None:
        self.employeeControl = EmployeeController()
        self.employee = Employee()

    def addEmployee(self, employee: 'Employee') -> bool:
        return self.employeeControl.appendIntoFile(employee)


    def editEmployee(self, entry: str, entryValue: Any, **kwargs) -> bool:
        if not len(kwargs):
            return False
        if any(kwarg not in vars(self.employee) for kwarg in kwargs):
            return False
        return self.employeeControl.changeOneEntry(entry, entryValue, **kwargs)


    def listEmployes(self, **kwargs) -> list['Employee']:
        if any(kwarg not in vars(self.employee) for kwarg in kwargs):
            return []

        employees: list['Employee'] = self.employeeControl.readFile()
        if not len(kwargs):
            return employees

        for k, v in kwargs.items():
            # Top to bottom if we go bottom to top we get index out of range
            # Because things get deleted if they do not match the query before we loop through them if we go bottom to top
            for i in range(len(employees)-1, -1, -1):
                # hack around to check if result that might be int or float partialy contains our target number
                if str(v) not in str(employees[i].__dict__[k]):
                    del employees[i]


        return employees
