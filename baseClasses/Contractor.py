class Contractor:
    def __init__(self) -> None:
        self.id: int = 0
        self.name: str = ""
        self.phoneNumber: str = ""
        self.openingHours: str = "" # might change to date
        self.country: int = -1


    def addContractor(self, employee: 'Contractor') -> bool:
        # call data layer here
        return True
