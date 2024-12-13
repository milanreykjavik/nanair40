from baseClasses.Location import Location
from typing import Any
import logic.validator


class LocationHandler:
    def __init__(self, dataWrapper=None) -> None:
        """
        [>] Constructor for LocationHandler class
        Initialize with optional dataWrapper, and initialize Location object
        """
        self.dataWrapper = dataWrapper
        self.location = Location()

    def addLocation(self, location: 'Location') -> bool:
        """
        [>] This function adds a new location to the system
        It returns true or false based on the following checks:
        - Verifies that no entry fields are empty or invalid
        """
        if not logic.validator.checkEntries(location.__dict__.values()):
            return False
        return self.dataWrapper.locationInsert(location)

    def editLocation(self, entry: str, entryValue: Any, **kwargs) -> bool:
        """
        [>] This function is used to edit an existing location's details
        It returns true or false based on the following conditions:
        - Verifies the entry and entryValue are valid
        - Ensures that the field to edit exists in the Location class
        """
        if not len(kwargs):
            return False
        if any(kwarg not in vars(self.location) for kwarg in kwargs):
            return False
        if not entry:
            return False
        if not entryValue:
            return False
        return self.dataWrapper.locationChange(entry, entryValue, **kwargs)

    def listLocations(self, **kwargs) -> list['Location']:
        """
        [>] This function lists all locations or filters them based on given criteria
        Returns a list of locations, optionally filtered by the provided kwargs
        kwargs: any field of Location class to filter the list (e.g., "name", "address")
        """
        if any(kwarg not in vars(self.location) for kwarg in kwargs):
            return []

        locations: list['Location'] = self.dataWrapper.locationFetch()
        if not len(kwargs):
            return locations

        for k, v in kwargs.items():
            # Top to bottom if we go bottom to top we get index out of range
            # Because things get deleted if they do not match the query before we loop through them if we go bottom to top
            for i in range(len(locations)-1, -1, -1):
                # hack around to check if result that might be int or float partially contains our target number
                if str(v) != str(locations[i].__dict__[k]):  # exact match instead of partial
                    del locations[i]

        return locations

