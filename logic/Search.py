from baseClasses.Employee import Employee
from dataControl.employeeController import EmployeeController

class Search:
    @staticmethod
    def searchEmployees(**kwargs) -> list[Employee] | None:
        employeesJson = EmployeeController().readFile()

        employees = Employee().normalize(employeesJson)

        allowedKeys = ["a", "b", "c"]
        if not len(kwargs):
            return employees

        for key in kwargs.keys():
            if key not in allowedKeys:
                return None
