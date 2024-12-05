"""
fix to camelCase not python_case
"""

from logic.employeeHandler import EmployeeHandler
from baseClasses.Employee import Employee

class Logic_Wrapper:
    def __init__(self) -> None:
        self.employee_handler = EmployeeHandler()

    def addEmployee(self, employee: Employee) -> bool:
        return self.employee_handler.addEmployee(employee)
    
    def editEmployee(self, target_kennitala: str, **kwargs) -> bool:
        return self.employee_handler.editEmployee(target_kennitala, **kwargs)
    
    def listEmployees(self, **kwargs) -> list['Employee']:
        return self.employee_handler.listEmployes(**kwargs)
