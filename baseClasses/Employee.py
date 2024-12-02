from typing import Type


class Employee:
    def __init__(self) -> None:
        self.id = -1
        self.kinnetala = -1
        self.name = ""
        self.phone = ""
        self.honePhone = ""
        self.address = ""
        self.email = ""
        self.country = -1 # country will be list of countries as dict


    def addEmployee(self, employee: Type[Employee]) -> bool:
        # call data layer here
        return True
