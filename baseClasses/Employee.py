import json

class Employee:
    def __init__(self, id: int = -1, kinnetala: str = "", name: str = "", phone: str = "",
                 homePhone: str = "", address: str = "", email: str = "", country: int = -1) -> None:
        self.id: int = id
        self.kinnetala: str = kinnetala
        self.name: str = name
        self.phone: str = phone
        self.homePhone: str = homePhone
        self.address: str = address
        self.email: str = email
        self.country: int = country


    def addEmployee(self, employee: 'Employee') -> bool:
        # call data layer here
        return True


    def __repr__(self) -> str:
        return f"Employee(id={self.id}, kinnetala={self.kinnetala}, name={self.name}, phone={self.phone}, homePhone={self.homePhone}, address={self.address}, email={self.email}, country={self.country})"


    def normalize(self, jsonStringList: list[str]) -> list['Employee']:
        employees: list['Employee'] = []
        for jsonString in jsonStringList:
            data = json.loads(jsonString)

            employee: 'Employee' = Employee(**data)

            employees.append(employee)

        return employees
