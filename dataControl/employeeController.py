class EmployeeController:
    def __init__(self):
        self.filePath = "data/employees.json"

    def appendIntoFile(self, data) -> bool:
        with open(self.filePath, "a") as f:
            f.write(data)

        return True

    def changeOneEntry(self, change, **kwargs) -> bool:
        # do the search and change
        return True

    def changeEntireEntry(self, change, **kwargs) -> bool:
        return True


    def readFile(self) -> list[str]:
        data = []

        # parse obj

        return data
