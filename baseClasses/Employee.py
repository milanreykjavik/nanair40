class Employee:
    def __init__(self) -> None:
        self.id: int = -1
        self.kinnetala: str = ""
        self.name: str = ""
        self.phone: str = ""
        self.honePhone: str = ""
        self.address: str = ""
        self.email: str = ""
        self.country: int = -1 # country will be list of countries as dict


    def addEmployee(self, employee: 'Employee') -> bool:
        # call data layer here
        return True
