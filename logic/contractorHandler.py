from baseClasses.Contractor import Contractor
from typing import Any
import logic.validator


class ContractorHandler:
    def __init__(self, dataWrapper=None) -> None:
        """
        [>] Constructor for ContractorHandler class
        Initialize with optional dataWrapper, and initialize Contractor object
        """
        self.dataWrapper = dataWrapper
        self.contractor = Contractor()

    def addContractor(self, contractor: 'Contractor') -> bool:
        """
        [>] this function add news contractor into system
        it returns true or false and it can fail if some contractor entry is empty
        it can fail if phone number is not valid
        it can fail if opening hours aren't valid
        """
        if not logic.validator.checkEntries(contractor.__dict__.values()):
            return False
        if not logic.validator.validatePhone(contractor.phone):
            return False
        if not logic.validator.validateOpeningHours(contractor.openingHours):
            return False
        return self.dataWrapper.contractorInsert(contractor)

    def editContractor(self, entry: str, entryValue: Any, **kwargs) -> bool:
        """
        [>] This function is used to edit the existing contractor entry
        it returns true or false depending on if the entry was successfully changed
        entry: field to edit (e.g., "phone" or "openingHours")
        entryValue: new value for the field
        kwargs: additional parameters to verify and update contractor details
        """
        if not len(kwargs):
            return False
        if any(kwarg not in vars(self.contractor) for kwarg in kwargs):
            return False
        if not entry:
            return False
        if not entryValue:
            return False
        if entry == "phone":
            if not logic.validator.validatePhone(entryValue):
                return False
        if entry == "openingHours":
            if not logic.validator.validateOpeningHours(entryValue):
                return False
        return self.dataWrapper.contractorChange(entry, entryValue, **kwargs)

    def listContractors(self, **kwargs) -> list['Contractor']:
        """
        [>] This function is used to list all contractors or filter them based on certain criteria
        returns: a list of contractors, possibly filtered by given criteria (kwargs)
        kwargs: any field of Contractor class to filter the list (e.g., "name", "phone", etc.)
        """
        if any(kwarg not in vars(self.contractor) for kwarg in kwargs):
            return []

        contractors: list['Contractor'] = self.dataWrapper.contractorFetch()
        if not len(kwargs):
            return contractors

        for k, v in kwargs.items():
            # Top to bottom if we go bottom to top we get index out of range
            # Because things get deleted if they do not match the query before we loop through them if we go bottom to top
            for i in range(len(contractors)-1, -1, -1):
                # hack around to check if result that might be int or float partially contains our target number
                if str(v) not in str(contractors[i].__dict__[k]):
                    del contractors[i]

        return contractors

