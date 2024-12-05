from ui.baseUI import BaseUI
from ui.validationUI import ValidationUI
from baseClasses.Property import Property
from logic.logicWrapper import Logic_Wrapper
from ui.searchUI import SearchUI

validation = ValidationUI()


class PropertiesUI(SearchUI):
    def __init__(self, logicWrapper: Logic_Wrapper):
        self.logicWrapper = logicWrapper
    
    def addProperty(self):
        propertyClass = Property()

        fields = [
            ('id', "Enter a ID for the property: ", validation.validateCountry),  # These are all of the keys, prompts, and values that we need to ask the user
            ('location', "Enter the location of the property: ", validation.validateLocation),
            ('address', "Enter the address of the property: : ", validation.validateAddress),
            ('condition', "Condition(Excellent, Good, Fair, Poor): ", validation.validateCondition),
            ('facilities', "Facilities requiring maintenance: ", validation.validateCountry),
        ]
        
        for key, prompt, validationFunc in fields: # This loops for all keys, prompts and functions the user needs to be askes
            value = self.getValidInput('Add property',prompt, validationFunc, propertyClass.__dict__)
            if value.lower() in ('q', 'b'): # If the user entered q or b, then we go back one page or quit
                match value.lower():
                    case 'q':
                        return 'q' # quit the whole program
                    case 'b':
                        return False # Go back one page
            propertyClass.__dict__[key] = value
        
        newProperty = Property(propertyClass.__dict__["id"], propertyClass.__dict__["location"], propertyClass.__dict__["address"], propertyClass.__dict__["condition"], propertyClass.__dict__["facilities"])

        self.logicWrapper.addProperty(newProperty)

        return self.takeInputAndPrintMenu(['[Q]uit', '[B]ack'], ('Add Property', [f'{key}: {value}' for key, value in propertyClass.__dict__.items()], 'The Property has been succesfully created\nChoose a option: '))
        


    def editProperty():
        pass

    def listProperties():
        pass



    def getValidInput(self, name, prompt, validationFunc, user_dict: dict = {}) -> str:
        while True:
            self.printBaseMenu(name, [f'{key}: {value}' for key, value in user_dict.items()], prompt)
            user_input = input(' ')
        
            if validationFunc(user_input):
                return user_input
        