from employeeHandler import EmployeeHandler
from Search import Search
from baseClasses.Employee import Employee

class Logic_Wrapper:
    def __init__(self, employee_handler: EmployeeHandler, search: Search) -> None:
        self.employee_handler = employee_handler
        self.search = search

    def addEmployee(self, employee: Employee) -> bool:
        return self.employee_handler.addEmployee(employee)
    
    def editEmployee(self, target_kennitala: str, **kwargs) -> bool:
        return self.employee_handler.editEmployee(target_kennitala, **kwargs)
    
    def listEmployees(self, **kwargs) -> list['Employee']:
        return self.employee_handler.listEmployess(**kwargs)