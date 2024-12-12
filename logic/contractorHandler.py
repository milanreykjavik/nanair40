from baseClasses.Contractor import Contractor
from typing import Any
import logic.validator


class ContractorHandler:
    def __init__(self, dataWrapper=None) -> None:
        self.dataWrapper = dataWrapper
        self.contractor = Contractor()

    def addContractor(self, contractor: 'Contractor') -> bool:
        if not logic.validator.checkEntries(contractor.__dict__.values()):
            return False
        if not logic.validator.validatePhone(contractor.phone):
            return False
        if not logic.validator.validateOpeningHours(contractor.openingHours):
            return False
        return self.dataWrapper.contractorInsert(contractor)


    def editContractor(self, entry: str, entryValue: Any, **kwargs) -> bool:
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
        if any(kwarg not in vars(self.contractor) for kwarg in kwargs):
            return []

        contractors: list['Contractor'] = self.dataWrapper.contractorFetch()
        if not len(kwargs):
            return contractors

        for k, v in kwargs.items():
            # Top to bottom if we go bottom to top we get index out of range
            # Because things get deleted if they do not match the query before we loop through them if we go bottom to top
            for i in range(len(contractors)-1, -1, -1):
                # hack around to check if result that might be int or float partialy contains our target number
                if str(v) not in str(contractors[i].__dict__[k]):
                    del contractors[i]


        return contractors
