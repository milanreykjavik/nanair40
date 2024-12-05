from baseClasses.Work import WorkOrder, WorkReport
from dataControl.workController import WorkController
from typing import Any


class WorkHandler:

    def __init__(self) -> None:
        self.workControl = WorkController()
        self.work = WorkOrder()

    def addWork(self, work: 'WorkOrder') -> bool:
        return self.workControl.appendIntoFile(work)


    def editWork(self, entry: str, entryValue: Any, **kwargs) -> bool:
        if not len(kwargs):
            return False
        if any(kwarg not in vars(self.work) for kwarg in kwargs):
            return False
        self.workControl.changeOneEntry(entry, entryValue, **kwargs)
        return True


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
