from ui.baseUI import BaseUI
from ui.validationUI import ValidationUI
from logic.logicWrapper import Logic_Wrapper

validation = ValidationUI()
class PropertiesUI(BaseUI):
    def __init__(self, logicWrapper: Logic_Wrapper):
        self.logicWrapper = logicWrapper

    def addProperty(self):
        properties_dict = {
            'country': '',
            'location': '',
            'address':  '',
            'condition': '',
            "facilities requiring maintenance": '',
            'addition information': ''
        }

        fields = [
            ('country', "Enter the country of the property: ", validation.validateCountry),  # These are all of the keys, prompts, and values that we need to ask the user
            ('location', "Enter the location of the property: ", validation.validateLocation),
            ('address', "Enter the address of the property: : ", validation.validateAddress),
            ('condition', "Condition(Excellent, Good, Fair, Poor): ", validation.validateCondition),
            ('Facilities requiring maintenance', "Facilities requiring maintenance: ", validation.validateCountry),
            ('addition information', "Enter your address: ", validation.validateAddress),
        ]
        
        for key, prompt, validationFunc in fields: # This loops for all keys, prompts and functions the user needs to be askes
            value = self.getValidInput('Add property',prompt, validationFunc, properties_dict)
            if value.lower() in ('q', 'b'): # If the user entered q or b, then we go back one page or quit
                match value.lower():
                    case 'q':
                        return 'q' # quit the whole program
                    case 'b':
                        return False # Go back one page
            properties_dict[key] = value
        
        while True:
            self.printBaseMenu('Add property', [f'{key}: {value}' for key, value in properties_dict.items()], prompt, 'Choose an option: ') # if the user finished entering all the information needed then he gets to choose either to quit or go back
            optionInput = self.takeInput(['Back', 'Quit'])

            match optionInput.lower():
                case 'b':
                    return False
                case 'q':
                    return 'q'



        


    def showProperty():
        pass



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
        