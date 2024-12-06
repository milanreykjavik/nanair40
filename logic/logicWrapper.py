"""
fix to camelCase not python_case
"""

from logic.employeeHandler import EmployeeHandler
from baseClasses.Employee import Employee
from logic.PropertyHandler import PropertyHandler
from baseClasses.Property import Property
from logic.workOrderHandler import WorkOrderHandler
from logic.workReportHandler import WorkReportHandler
from baseClasses.WorkReport import WorkReport
from baseClasses.WorkOrder import WorkOrder
from logic.contractorHandler import ContractorHandler
from baseClasses.Contractor import Contractor

class Logic_Wrapper:
    def __init__(self) -> None:
        self.employeeHandler = EmployeeHandler()
        self.propertyHandler = PropertyHandler()
        self.workOrderHandler = WorkOrderHandler()
        self.workReportHandler = WorkReportHandler()
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

    def addWorkOrder(self, workOrder: 'WorkOrder') -> bool:
        return self.workOrderHandler.addWorkOrder(workOrder)

    def editWorkOrder(self, workOrderID: str, **kwargs) -> bool:
        return self.workOrderHandler.editWorkOrder(workOrderID, **kwargs)

    def listWorkOrders(self, **kwargs) -> list['WorkOrder']:
        return self.workOrderHandler.listWorkOrders(**kwargs)
    
    def addWorkReport(self, workReport: 'WorkReport') -> bool:
        return self.workReportHandler.addWorkReport(workReport)

    def editWorkOrder(self, workReportID: str, **kwargs) -> bool:
        return self.workReportHandler.editWorkReport(workReportID, **kwargs)

    def listWorkOrders(self, **kwargs) -> list['WorkReport']:
        return self.workReportHandler.listWorkReports(**kwargs)

    def addContractor(self, contractor: 'Contractor') -> bool:
        return self.contractorHandler.addContractor(contractor)

    def editContractor(self, contractorID: str, **kwargs) -> bool:
        return self.contractorHandler.editContractor(contractorID, **kwargs)

    def listContractors(self, **kwargs) -> list['Contractor']:
        return self.contractorHandler.listContractors(**kwargs)