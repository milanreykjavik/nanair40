class WorkReport:
    def __init__(self):
        self.id: int = -1
        self.description: str = ""
        self.date: str = ""
        self.cost: int = 0
        self.comment: str = ""


class WorkOrder:
    def __init__(self):
        self.id: int = -1
        self.date: str = ""
        self.description: str = ""
        self.propertyNumber: int = -1
        self.userID: int = -1
        self.priority: int = 0 # 0 1 2
        self.workReport: str = ""# class workReport
        self.contractorID: int = -1 # if it is -1 it is nobody if it is > -1 then it is an actual contrator
        self.isCompleted: bool = False



    def addWorkOrder(self, workOrder: 'WorkOrder') -> bool:
        # call data layer here
        return True
