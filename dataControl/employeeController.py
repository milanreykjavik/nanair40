import json
import os
import tempfile

def atomicWrite(fp, data):
    dirName = os.path.dirname(fp)
    with tempfile.NamedTemporaryFile("w", delete=False, dir=dirName) as tmpFile:
        json.dump(data, tmpFile, indent=4)
        tmpFileName = tmpFile.name
    os.replace(tmpFileName, fp)

class EmployeeController:
    def __init__(self):
        self.filePath = "data/employees.json"


    def appendIntoFile(self, data) -> bool:
        try:
            with open(self.filePath, "r") as f:
                currentData = json.load(f)

            currentData.append(json.loads(data))

            atomicWrite(self.filePath, currentData)
            return True
        except Exception as e:
            print(f"Error while appending to file: {e}")
            return False

    def changeOneEntry(self, targetKennitala: str, **kwargs) -> bool:
        try:
            with open(self.filePath, "r") as f:
                currentData = json.load(f)

            for employee in currentData:
                if employee.get('kennitala') == targetKennitala:
                    for key, value in kwargs.items():
                        if key in employee:
                            employee[key] = value
                    break
            else:
                return False

            atomicWrite(self.filePath, currentData)
            return True
        except Exception as e:
            print(f"Error while updating file: {e}")
            return False


    def readFile(self) -> list[dict]:
        data = []
        with open(self.filePath, "r") as f:
            data = json.load(f)
        return data
