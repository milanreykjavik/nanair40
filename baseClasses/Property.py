import json

class Property:
    def __init__(self, id: int = 0, location: int = 0, address: str = "", condition: int = 0, facilities: list[str] = []) -> None:
        self.id: int = id
        self.location: int = location
        self.address: str = address
        self.size: int = condition # 0 to 10 average calculation
        self.roomCount: list[int] = roomId
        facilatiesId: dict = facilatiesId

    def __repr__(self) -> str:
        return f"Property(id={self.id}, location={self.location}, address={self.address}, condition={self.condition}, facilities={self.facilities})"


    def normalize(self, jsonData: list[str]) -> list['Property']:
        properties: list['Property'] = []
        for data in jsonData:

            property: 'Property' = Property(**data)

            properties.append(property)

        return properties


    def toJSON(self, property: 'Property') -> str:
        return json.dumps(property.__dict__)
