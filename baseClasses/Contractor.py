import json

class Contractor:
    def __init__(self, id: int = 0, name: str = "", phone: str = "", openingHours: str = "", location: int = 0) -> None:
        self.id: int = id
        self.name: str = name
        self.phone: str = phone
        self.openingHours: str = openingHours # might change to dae
        self.location: int = location


    def __repr__(self) -> str:
        return f"Contractor(id={self.id}, name={self.name}, phone={self.phone}, openingHours={self.openingHours}, location={self.location})"


    def normalize(self, jsonData: list[str]) -> list['Contractor']:
        contractors: list['Contractor'] = []
        for data in jsonData:

            contractor: 'Contractor' = Contractor(**data)

            contractors.append(contractor)

        return contractors


    def toJSON(self, contractor: 'Contractor') -> str:
        return json.dumps(contractor.__dict__)
