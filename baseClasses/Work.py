import json

class WorkReport:
    def __init__(self, id: int = 0, description: str = "", date: str = "", cost: int = 0, comment: str = ""):
        self.id: int = id
        self.description: str = description
        self.date: str = date
        self.cost: int = cost
        self.comment: str = comment


    def __repr__(self) -> str:
        return f"WorkReport(id={self.id}, description={self.description}, date={self.date}, cost={self.cost}, comment={self.comment})"


    def normalize(self, jsonData: list[str]) -> list['WorkReport']:
        workreports: list['WorkReport'] = []
        for data in jsonData:
            workreport: 'WorkReport' = WorkReport(**data)

            workreports.append(workreport)

        return workreports


    def toJSON(self, workreport: 'WorkReport') -> str:
        return json.dumps(workreport.__dict__)


class WorkOrder:
    def __init__(self, id: int = 0, date: str = "", description: str = "", propertyNumber: int = 0, userID: int = 0, priority: int = 0, workReport: 'WorkReport' = WorkReport(), contractorID: int = 0, isCompleted: bool = False):
        self.id: int = id
        self.date: str = date
        self.description: str = description
        self.propertyNumber: int = propertyNumber
        self.userID: int = userID
        self.priority: int = priority # 0 1 2
        self.workReport: 'WorkReport' = workReport # class workReport
        self.contractorID: int = contractorID # if it is -1 it is nobody if it is > -1 then it is an actual contrator
        self.isCompleted: bool = isCompleted


    def __repr__(self) -> str:
        return f"WorkOrder(id={self.id}, date={self.date}, description={self.description}, propertyNumber={self.propertyNumber}, userID={self.userID}, priority={self.priority}, workReport={self.workReport}, contractorID={self.contractorID}, isCompleted={self.isCompleted})"


    def normalize(self, jsonData: list[str]) -> list['WorkOrder']:
        workorders: list['WorkOrder'] = []
        for data in jsonData:

            workorder: 'WorkOrder' = WorkOrder(**data)

            workorders.append(workorder)

        return workorders

    def toJSON(self, workorder: 'WorkOrder') -> str:
        workorderDict = workorder.__dict__.copy()
        workorderDict['workReport'] = json.loads(workorder.workReport.toJSON(workorder.workReport))

        return json.dumps(workorderDict)
