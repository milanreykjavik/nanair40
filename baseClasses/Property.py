class Property:
    def __init__(self) -> None:
        self.id: int = 0
        self.country: int = -1
        self.address: str = ""
        self.condtion: int = -1 # 0 to 10 average calculation
        self.facilitiesL: list[str] = ["Hotubs", ]


    def addProperty(self, property: 'Property') -> bool:
        # call data layer here
        return True



