from baseClasses.Employee import Employee
from dataControl.employeeController import EmployeeController

class Search:
    @staticmethod
    def searchEmployees(**kwargs) -> list[Employee] | None:
        employeesJson: list[str] = EmployeeController().readFile()

        employeesJson = [
            '{"id": 5, "kinnetala": "5678901234", "name": "Sven Jonsson", "phone": "+3545678901", "homePhone": "+3545432109", "address": "654 Pine Ave, Kopavogur", "email": "sven.jonsson@example.com", "country": 1}',
            '{"id": 6, "kinnetala": "6789012345", "name": "Hanna Thoroddsen", "phone": "+3546789012", "homePhone": "+3544321098", "address": "987 Cedar Blvd, Mosfellsbaer", "email": "hanna.thoroddsen@example.com", "country": 1}',
            '{"id": 7, "kinnetala": "7890123456", "name": "Bjorn Rognvaldsson", "phone": "+3547890123", "homePhone": "+3543210987", "address": "135 Maple Rd, Isafjordur", "email": "bjorn.rognvaldsson@example.com", "country": 1}'
        ]

        employees = Employee().normalize(employeesJson)

        employees = Employee().normalize(employeesJson)

        allowedKeys = ["a", "b", "c"]
        if not len(kwargs):
            return employees

        for key in kwargs.keys():
            if key not in allowedKeys:
                return None
