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

    def changeOneEntry(self, kennitala: str, **kwargs) -> bool:
        print(kennitala)
        print(kwargs.items())
        # do the search and change
        return True

    #def changeEntireEntry(self, kennitala: str, **kwargs) -> bool:
    #    return True


    def readFile(self) -> list[dict]:
        data = []
        with open(self.filePath, "r") as f:
            data = json.load(f)
        return data
