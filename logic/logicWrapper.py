"""
fix to camelCase not python_case
"""

from logic.employeeHandler import EmployeeHandler
from baseClasses.Employee import Employee
from logic.PropertyHandler import PropertyHandler
from baseClasses.Property import Property
from logic.workOrderHandler import WorkOrderHandler
from logic.workReportHandler import WorkReportHandler
from baseClasses.workReport import WorkReport
from baseClasses.workOrder import WorkOrder
from logic.contractorHandler import ContractorHandler
from baseClasses.Contractor import Contractor
from logic.locationHandler import LocationHandler
from baseClasses.Location import Location
from typing import Any
from datetime import datetime
from dateutil.relativedelta import relativedelta

def time_diff_category(date1_str, date2_str):
    # Define the date format
    date_format = "%d.%m.%Y"
    
    # Parse the date strings into datetime objects
    date1 = datetime.strptime(date1_str, date_format)
    date2 = datetime.strptime(date2_str, date_format)
    
    # Calculate the absolute difference
    delta = relativedelta(date2, date1)
    
    # Check the difference and return appropriate category
    if delta.years > 0:
        return 4  # Year
    elif delta.months > 0:
        return 3  # Month
    elif delta.days > 7:
        return 2  # Week
    else:
        return 1  # Day

class Logic_Wrapper:
    def __init__(self) -> None:
        self.employeeHandler = EmployeeHandler()
        self.propertyHandler = PropertyHandler()
        self.workOrderHandler = WorkOrderHandler()
        self.workReportHandler = WorkReportHandler()
        self.contractorHandler = ContractorHandler()
        self.locationHandler = LocationHandler()
        self.currentContractors: list['Contractor'] = self.contractorHandler.listContractors()
        if len(self.currentContractors):
            self.currentContractorID: int = int(self.currentContractors[-1].id)
        else:
            self.currentContractorID = 0
        self.currentWorkOrders: list['WorkOrder'] = self.workOrderHandler.listWorkOrders()
        if len(self.currentWorkOrders):
            self.currentWorkOrderID: int = int(self.currentWorkOrders[-1].id)
        else:
            self.currentWorkOrderID = 0



    def addEmployee(self, employee: Employee) -> bool:
        return self.employeeHandler.addEmployee(employee)
    
    def editEmployee(self, entry: str, entryValue: Any, **kwargs) -> bool:
        return self.employeeHandler.editEmployee(entry, entryValue, **kwargs)
    
    def listEmployees(self, **kwargs) -> list['Employee']:
        return self.employeeHandler.listEmployes(**kwargs)

    def addProperty(self, property: Property) -> bool:
        return self.propertyHandler.addProperty(property)
    
    def listProperties(self, **kwargs) -> list['Property']:
        return self.propertyHandler.listProperties(**kwargs)
    
    def editProperty(self, entry: str, entryValue: Any, **kwargs) -> bool:
        return self.propertyHandler.editProperty(entry, entryValue, **kwargs)

    def addWorkOrder(self, work: 'WorkOrder') -> bool:
        return self.workOrderHandler.addWorkOrder(work)

    def editWorkOrder(self, entry: str, entryValue: Any, **kwargs) -> bool:
        return self.workOrderHandler.editWorkOrder(entry, entryValue, **kwargs)

    def listWorkOrders(self, **kwargs) -> list['WorkOrder']:
        return self.workOrderHandler.listWorkOrders(**kwargs)
    
    def listWorkCurrentWorkOrders(self, **kwargs) -> list['WorkOrder']:
        return self.workOrderHandler.listWorkCurrentOrders(**kwargs)
    
    def addWorkReport(self, workReport: 'WorkReport') -> bool:
        return self.workReportHandler.addWorkReport(workReport)
    def currentWorkReportID(self, workOrderID: int) -> int:
        return self.workReportHandler.currentWorkReportID(workOrderID)

    def listWorkOrders(self, **kwargs) -> list[WorkOrder]:

        return self.workOrderHandler.listWorkOrders(**kwargs)

    def addContractor(self, contractor: 'Contractor') -> bool:
        return self.contractorHandler.addContractor(contractor)

    def editContractor(self, entry: str, entryValue: Any, **kwargs) -> bool:
        return self.contractorHandler.editContractor(entry, entryValue, **kwargs)

    def listContractors(self, **kwargs) -> list['Contractor']:
        return self.contractorHandler.listContractors(**kwargs)
    
    def listLocations(self, **kwargs) -> list[Location]:
        return self.locationHandler.listLocations(**kwargs)

    def listRepeatingWorkOrders(self, **kwargs) -> list[WorkOrder]:
        repeatingList: list[WorkOrder] = self.workOrderHandler.listWorkOrders(repeating=True)

        currentDate = datetime.now()
        currentDate = currentDate.strftime("%d.%m.%Y")

        final = []
        for workOrder in repeatingList:
            if not len(workOrder.workReport):
                final.append(workOrder)
                continue
            tdif = time_diff_category(workOrder.workReport[-1].date, currentDate)
            if tdif >= workOrder.repeatInterval:
                final.append(workOrder)
        return final
            
