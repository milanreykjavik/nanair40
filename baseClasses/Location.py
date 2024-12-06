class location:
    def __init__(self, id: int = 0, location: int = 0, address: str = "", condition: int = 0, facilities: list[str] = []) -> None:
        self.id: int = id
        self.location: int = location
        self.condition: int = condition # 0 to 10 average calculation
        self.facilities: list[str] = facilities











locations: dict = {'Iceland': ['Reykjavík'],
                   'Greenland': ['Nuuk', 'Kulusuk'],
                   'Faroe Islands': ['Tórshavn'],
                   'Shetland Islands': ['Tingwall'],
                   'Svalbard': ['Longyearbyen']
}
