import json
import os
import tempfile
from typing import Any

from baseClasses.Contractor import Contractor
from dataControl.writer import atomicWrite


class ContractorController:
    def __init__(self):
        self.contractor = Contractor()
        self.filePath = "data/contractors.json"


    def appendIntoFile(self, data: 'Contractor') -> bool:
        try:
            with open(self.filePath, "r") as f:
                currentData = json.load(f)
        except:
            currentData = []
        try:
            dataJSON = self.contractor.toJSON(data)
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
            for contractor in currentData:
                if contractor.get(entry) == entryValue:
                    for key, value in kwargs.items():
                        if key in contractor:
                            contractor[key] = value
                    break
            else:
                return False

            atomicWrite(self.filePath, currentData)
            return True
        except:
            return False


    def readFile(self) -> list['Contractor']:
        try:
            data = []
            with open(self.filePath, "r") as f:
                data = json.load(f)
            return self.contractor.normalize(data)
        except:
            return []
