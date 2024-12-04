import json

class EmployeeController:
    def __init__(self):
        self.filePath = "data/employees.json"

    def appendIntoFile(self, data) -> bool:
        with open(self.filePath) as f:
            currentData = json.load(f)

        currentData.append(json.loads(data))
        with open(self.filePath, "w") as f:
            json.dump(currentData, f, indent=4)




        return True

    def changeOneEntry(self, targetKennitala: str, **kwargs) -> bool:
        with open(self.filePath) as f:
            currentData = json.load(f)

        for employee in currentData:
            if employee.get('kennitala') == targetKennitala:
                for key, value in kwargs.items():
                    if key in employee:
                        employee[key] = value
                break
        else:
            return False

        with open(self.filePath, "w") as f:
            json.dump(currentData, f, indent=4)

        return True

    #def changeEntireEntry(self, kennitala: str, **kwargs) -> bool:
    #    return True


    def readFile(self) -> list[dict]:
        data = []
        with open(self.filePath, "r") as f:
            data = json.load(f)
        return data
