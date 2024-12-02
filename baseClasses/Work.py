from typing import Type


class WorkReport:
    def __init__(self):
        self.id = 0
        self.description = ""
        self.date = "REPORT DATE"
        self.cost = 0
        self.comment = ""


class WorkOrder:
    def __init__(self):
        self.id = 0
        self.date = "ACTUAL DATE DATATYPE"
        self.description = "THis has to be done lalalala"
        self.propertyNumber = 0
        self.userID = 0
        self.priority = 0 # 0 1 2
        self.workReport = ""# class workReport
        self.contractorID = -1 # if it is -1 it is nobody if it is > -1 then it is an actual contrator
        self.isCompleted = False



    def addWorkOrder(self, employee: Type[WorkOrder]) -> bool:
        # call data layer here
        return True
