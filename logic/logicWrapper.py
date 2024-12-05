from logic.employeeHandler import EmployeeHandler
from logic.Search import Search
from baseClasses.Employee import Employee



class Logic_Wrapper:
    def __init__(self):
        self.employeeHandeler = EmployeeHandler()

    def addEmployee(self, employee: Employee) -> bool:
        return self.employeeHandeler.addEmployee(employee)
    
    def editEmployee(self, target_kennitala: str, **kwargs) -> bool:
        return self.employeeHandeler.editEmployee(target_kennitala, **kwargs)
    
    def listEmployees(self, **kwargs) -> list[dict]:
        return self.employeeHandeler.listEmployess(**kwargs)
    
    def searchEmployees(self, query: str) -> list[dict]:
        return self.employeeHandeler.listEmployess(query)
    
    def searchWorkOrders(self, **kwargs):
        pass

    def searchProperties(self, **kwargs):
        pass

    def searchWorkReports(self, **kwargs):
        pass
