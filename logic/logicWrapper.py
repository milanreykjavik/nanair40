"""
fix to camelCase not python_case
"""

from logic.employeeHandler import EmployeeHandler
from baseClasses.Employee import Employee
from logic.PropertyHandler import PropertyHandler
from baseClasses.Property import Property
from logic.workHandler import WorkHandler
from baseClasses.Work import WorkOrder, WorkReport
from logic.contractorHandler import ContractorHandler
from baseClasses.Contractor import Contractor

class Logic_Wrapper:
    def __init__(self) -> None:
        self.employeeHandler = EmployeeHandler()
        self.propertyHandler = PropertyHandler()
        self.workHandler = WorkHandler()
        self.contractorHandler = ContractorHandler()

    def addEmployee(self, employee: Employee) -> bool:
        return self.employeeHandler.addEmployee(employee)
    
    def editEmployee(self, employeeID: str, **kwargs) -> bool:
        return self.employeeHandler.editEmployee(employeeID, **kwargs)
    
    def listEmployees(self, **kwargs) -> list['Employee']:
        return self.employeeHandler.listEmployes(**kwargs)

    def addProperty(self, property: Property) -> bool:
        return self.propertyHandler.addProperty(property)
    
    def listProperties(self, **kwargs) -> list['Property']:
        return self.propertyHandler.listProperties(**kwargs)
    
    def editProperty(self, propertyID: str, **kwargs) -> bool:
        return self.propertyHandler.editProperty(propertyID, **kwargs)

    def addWork(self, work: 'WorkOrder') -> bool:
        return self.workHandler.addWork(work)

    def editWork(self, workID: str, **kwargs) -> bool:
        return self.workHandler.editWork(workID, **kwargs)

    def listWorkOrders(self, **kwargs) -> list['WorkOrder']:
        return self.workHandler.listWorkOrders(**kwargs)

    def addContractor(self, contractor: 'Contractor') -> bool:
        return self.contractorHandler.addContractor(contractor)

    def editContractor(self, contractorID: str, **kwargs) -> bool:
        return self.contractorHandler.editContractor(contractorID, **kwargs)

    def listContractors(self, **kwargs) -> list['Contractor']:
        return self.contractorHandler.listContractors(**kwargs)