from baseClasses.Contractor import Contractor
from logic.logicWrapper import Logic_Wrapper
from ui.validationUI import ValidationUI
from ui.searchUI import SearchUI

validation = ValidationUI()

class ContractorsUI(SearchUI):
    def __init__(self, logicWrapper: Logic_Wrapper):
        self.logicWrapper = logicWrapper
    
    def showContractor(self):
        
        userInput = self.takeInputAndPrintMenu(['[A]dd contractor', '[E]dit contractor', '[L]ist contractors'], ('Contractor Menu', ['[A]dd contractor', '[E]dit contractor', '[L]ist contractors'], 'Choose a option'))

        match userInput.lower():
            case 'b':
                return False
            case 'q':
                return 'q'
            case 'l':
                return self.showContractorsInfo()
            case 'a':
                return self.addContractor()
            case 'e':
                return self.editContractor()
            
    def addContractor(self):
        contractorClass = Contractor()
        fields = [                                                                       # These are all of the keys, prompts, and values that we need to ask the user
            ('name', "Enter the name of the contractor: ", validation.validateName),
            ('phone', "Enter the phonenumer of the contractors : ", validation.validatePhone),
            ('openingHours', "Write the opening hours: ", validation.validateName),
            ('location', "Enter the location: ", validation.validateText),
        ]
        
        for key, prompt, validationFunc in fields: # This loops for all keys, prompts and functions the user needs to be askes
            value = self.getValidInput('Add contractor',prompt, validationFunc, contractorClass.__dict__)
            if value.lower() in ('q', 'b'): # If the user entered q or b, then we go back one page or quit
                match value.lower():
                    case 'q':
                        return 'q' # quit the whole program
                    case 'b':
                        return False # Go back one page
            contractorClass.__dict__[key] = value
        
        newContractor = Contractor(contractorClass.__dict__["id"], contractorClass.__dict__["name"], contractorClass.__dict__["phone"], contractorClass.__dict__["openingHours"], contractorClass.__dict__["location"])

        self.logicWrapper.addContractor(newContractor)

        return self.takeInputAndPrintMenu(['[Q]uit', '[B]ack'], ('Add Constractor', [f'{key}: {value}' for key, value in contractorClass.__dict__.items()], 'The Contractor has been succesfully created\nChoose a option: '))
        



    def editContractor():
        pass

        



    def getValidInput(self, name, prompt, validationFunc, user_dict: dict = {}) -> str:
        while True:
            self.printBaseMenu(name, [f'{key}: {value}' for key, value in user_dict.items()], prompt)
            user_input = input(' ')
        
            if validationFunc(user_input):
                return user_input
        