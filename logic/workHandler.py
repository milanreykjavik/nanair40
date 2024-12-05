from baseClasses.Work import WorkOrder, WorkReport
from dataControl.workController import WorkController
from typing import Any


class WorkHandler:
    def __init__(self) -> None:
        self.workControl = WorkController()
        self.work = WorkOrder()

    def addWork(self, work: 'WorkOrder') -> bool:
        return self.workControl.appendIntoFile(work)


    """
    def editWork(self, entry: str, entryValue: Any, workReportIndex: int = 0, **kwargs) -> bool:
        if not len(kwargs):
            return False
        if any(kwarg not in vars(self.work) for kwarg in kwargs):
            return False

        workOrders = self.workControl.readFile()
        for workOrder in workOrders:
            if getattr(workOrder, entry) == entryValue:
                if workReportIndex > 0 and workReportIndex < len(workOrder.workReports):
                    workReport = workOrder.workReports[workReportIndex]
                    for key, value in kwargs.items():
                        if key in vars(workReport):
                            setattr(workReport, key, value)
                        else:
                            return False
                else:
                    for key, value in kwargs.items():
                        if key in vars(workOrder):
                            setattr(workOrder, key, value)
                        else:
                            return False
                return self.workControl.editWork(workOrders, 'workReport',)
        return False
    """

    def editWork(self, entry: str, entryValue: Any, **kwargs) -> bool:
        if not len(kwargs):
            return False
        if any(kwarg not in vars(self.work) for kwarg in kwargs):
            return False
        
        return self.workControl.changeOneEntry(entry, entryValue, **kwargs)


    def listWorkOrders(self, **kwargs) -> list['WorkOrder']:
        if any(kwarg not in vars(self.work) for kwarg in kwargs):
            return []

        workOrders: list['WorkOrder'] = self.workControl.readFile()
        if not len(kwargs):
            return workOrders

        for k, v in kwargs.items():
            # Top to bottom if we go bottom to top we get index out of range
            # Because things get deleted if they do not match the query before we loop through them if we go bottom to top
            for i in range(len(workOrders)-1, -1, -1):
                # hack around to check if result that might be int or float partialy contains our target number
                if str(v) not in str(workOrders[i].__dict__[k]):
                    del workOrders[i]

    # LIST WORK REPORTS MAYBE


        return workOrders
