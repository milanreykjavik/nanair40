from baseClasses.Property import Property
from typing import Any
import logic.validator


class PropertyHandler:
    def __init__(self, dataWrapper=None) -> None:
        """
        [>] Constructor for PropertyHandler class
        Initialize with optional dataWrapper, and initialize Property object
        """
        self.dataWrapper = dataWrapper
        self.property = Property()

    def addProperty(self, property: 'Property') -> bool:
        """
        [>] This function adds a new property to the system
        It returns true or false based on several checks:
        - Verifies that no entry fields are empty or invalid
        - Ensures that the property ID does not already exist
        """
        if not logic.validator.checkEntries(property.__dict__.values()):
            return False
        if self.listProperties(id=property.id):
            return False

        return self.dataWrapper.propertyInsert(property)

    def editProperty(self, entry: str, entryValue: Any, **kwargs) -> bool:
        """
        [>] This function is used to edit an existing property's details
        It returns true or false based on the following conditions:
        - Verifies the entry and entryValue are valid
        - Ensures that the field to edit exists in the Property class
        - Validates that the property ID is a string and does not already exist
        """
        if not len(kwargs):
            return False
        if any(kwarg not in vars(self.property) for kwarg in kwargs):
            return False
        if not entry:
            return False
        if not entryValue:
            return False
        if entry == "id":
            if type(entryValue) != str:
                return False
            if not self.listProperties(id=entryValue):
                return False

        return self.dataWrapper.propertyChange(entry, entryValue, **kwargs)

    def listProperties(self, **kwargs) -> list['Property']:
        """
        [>] This function lists all properties or filters them based on given criteria
        Returns a list of properties, optionally filtered by the provided kwargs
        kwargs: any field of Property class to filter the list (e.g., "id", "location", "price")
        """
        if any(kwarg not in vars(self.property) for kwarg in kwargs):
            return []

        properties: list['Property'] = self.dataWrapper.propertyFetch()
        if not len(kwargs):
            return properties

        for k, v in kwargs.items():
            # Top to bottom if we go bottom to top we get index out of range
            # Because things get deleted if they do not match the query before we loop through them if we go bottom to top
            for i in range(len(properties)-1, -1, -1):
                # hack around to check if result that might be int or float partially contains our target number
                if str(v) != str(properties[i].__dict__[k]):  # exact match instead of partial
                    del properties[i]

        return properties

