import json

class Employee:
    def __init__(self,kennitala: str = "", name: str = "", phone: str = "",
                 homePhone: str = "", address: str = "", email: str = "", country: int = -1) -> None:
        self.kennitala: str = kennitala
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
        return f"Employee(kennitala={self.kennitala}, name={self.name}, phone={self.phone}, homePhone={self.homePhone}, address={self.address}, email={self.email}, country={self.country})"


    def normalize(self, jsonStringList: list[str]) -> list['Employee']:
        employees: list['Employee'] = []
        for jsonString in jsonStringList:
            data = json.loads(jsonString)

            employee: 'Employee' = Employee(**data)

            employees.append(employee)

        return employees


    def toJSON(self, employee: 'Employee') -> str:
        return json.dumps(employee.__dict__)
