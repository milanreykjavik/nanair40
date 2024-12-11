from contractorController import ContractorController
from employeeController import EmployeeController
from locationController import LocationController
from propertyController import PropertyController
from workOrderController import WorkController
from workReportController import WorkReportController
from typing import Any


class DataWrapper:
    def __init__(self) -> None:
        self.employeeController = EmployeeController()
        self.propertyController = PropertyController()
        self.workOrderController = WorkController()
        self.workReportController = WorkReportController()
        self.contractorController = ContractorController()
        self.locationController = LocationController()


    def employeeInsert(self, data) -> bool:
        return self.employeeController.appendIntoFile(data)

    def employeeChange(self, entry: str, entryValue: Any, **kwargs):
        return self.employeeController.changeOneEntry(entry, entryValue, **kwargs)

    def employeeFetch(self):
        return self.employeeController.readFile()

    def propertyFetch():
        pass

    def propertyInsert():
        pass

    def propertyChange():
        pass

    def workOrderFetch():
        pass

    def workOrderInsert():
        pass

    def workOrderChange():
        pass

    def workReportInsert():
        pass

    def workReportChange():
        pass

    def workReportFetch():
        pass

    def contractorFetch():
        pass

    def contractorInsert():
        pass

    def contractorChange():
        pass

    def locationFetch():
        pass

    def locationInsert():
        pass

    def locationChange():
        pass
