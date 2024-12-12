import json
from typing import Any

from baseClasses.workOrder import WorkOrder
from dataControl.writer import atomicWrite


class WorkController:
    def __init__(self):
        self.workOrder = WorkOrder()
        self.filePath = "data/workOrders.json"


    def appendIntoFile(self, data: 'WorkOrder') -> bool:
        try:
            with open(self.filePath, "r") as f:
                currentData = json.load(f)
        except:
            currentData = []

        try:
            dataJSON = self.workOrder.toJSON(data)
            currentData.append(json.loads(dataJSON))

            atomicWrite(self.filePath, currentData)
            return True
        except:
            return False

    # We typehint any for value cuz some of them are str, some int, some bool
    def changeOneEntry(self, entry: str, entryValue: Any, **kwargs) -> bool:
        try:
            with open(self.filePath, "r") as f:
                currentData = json.load(f)
        except:
            currentData = []
        try:
            for workOrder in currentData:
                if workOrder.get(entry) == entryValue:
                    for key, value in kwargs.items():
                        if key in workOrder:
                            workOrder[key] = value
                    break
            else:
                return False

            atomicWrite(self.filePath, currentData)
            return True
        except:
            return False


    def readFile(self) -> list['WorkOrder']:
        try:
            data = []
            with open(self.filePath, "r") as f:
                data = json.load(f)
                return self.workOrder.normalize(data) 
        except Exception as e:
            return []
