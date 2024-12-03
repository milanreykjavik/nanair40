import json

class Property:
    def __init__(self, id: int = -1, country: int = -1, address: str = "", condition: int = -1, facilities: list[str] = []) -> None:
        self.id: int = id
        self.country: int = country
        self.address: str = address
        self.condition: int = condition # 0 to 10 average calculation
        self.facilities: list[str] = facilities


    def __repr__(self) -> str:
        return f"Property(id={self.id}, country={self.country}, address={self.address}, condition={self.condition}, facilities={self.facilities})"


    def normalize(self, jsonStringList: list[str]) -> list['Property']:
        properties: list['Property'] = []
        for jsonString in jsonStringList:
            data = json.loads(jsonString)

            property: 'Property' = Property(**data)

            properties.append(property)

        return properties


    def toJSON(self, property: 'Property') -> str:
        return json.dumps(property.__dict__)
