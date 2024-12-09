class Location:
    def __init__(self, country: str = "", cities: str = [], airport: str = "", phone: str = "", openingHours: str = "", operationsManager: str = "") -> None:
        self.country: str = country
        self.cities: list = []
        self.airport: str = airport
        self.phone: str = phone
        self.openingHours: str = openingHours
        self.operationsManager: str = operationsManager

    def __repr__(self) -> str:
        return f"Location(country={self.country}, cities={self.cities}, airport={self.airport}, phone={self.phone}, openingHours={self.openingHours}, operationsManager={self.operationsManager})"


    def normalize(self, jsonData: list[dict]) -> list['Location']:
        locations: list['Location'] = []
        for data in jsonData:

            location: 'Location' = Location(**data)

            locations.append(location)

        return locations


    def toJSON(self, location: 'Location') -> str:
        return json.dumps(location.__dict__)



locations: dict = {'Iceland': ['Reykjavík'],
                   'Greenland': ['Nuuk', 'Kulusuk'],
                   'Faroe Islands': ['Tórshavn'],
                   'Shetland Islands': ['Tingwall'],
                   'Svalbard': ['Longyearbyen']
}
