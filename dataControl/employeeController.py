class EmployeeController:
    def __init__(self):
        self.filePath = "data/employees.json"

    def appendIntoFile(self, data) -> bool:
        with open(self.filePath, "a") as f:
            f.write(data+"\n")

        return True

    def changeOneEntry(self, kennitala: str, **kwargs) -> bool:
        # do the search and change
        return True

    def changeEntireEntry(self, kennitala: str, **kwargs) -> bool:
        return True


    def readFile(self) -> list[str]:
        data = []
        with open(self.filePath, "r") as f:
            for line in f:
                data.append(line.replace("\n", ""))

        return data
