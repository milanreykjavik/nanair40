from logic.logicWrapper import Logic_Wrapper
from baseClasses.Work import WorkOrder
from ui.validationUI import ValidationUI
validation = ValidationUI()

class WorkUI:
    def __init__(self, logicWrapper: Logic_Wrapper):
        self.logicWrapper = logicWrapper



            
    def func(self):
            userClass = WorkOrder()
            fields = [
                ('description', "Enter the description of the work: ", validation.validateText),  # These are all of the keys, prompts, and values that we need to ask the user
                ('property Number', "Enter the property number: ", validation.validateText),
                ('contractors', "Enter a name of a contractor: ", validation.validateText),
                ('priority', "Enter your email: ", validation.validateText)
                ('date', 'Enter a date', validation.validateText)
            ]


            for key, prompt, validationFunc in fields: # This loops for all keys, prompts and functions the user needs to be askes
                value = self.getValidInput('Add work order', prompt, validationFunc, userClass.__dict__)
                if value.lower() in ('q', 'b'): # If the user entered q or b, then we go back one page or quit
                    match value.lower():
                        case 'q':
                            return 'q' # quit the whole program
                        case 'b':
                            return False # Go back one page
                userClass.__dict__[key] = value

                newWorkOrder = self.logicWrapper.addWorkOrder()






    def addWorkOrder():
        pass
        

    def editWorkOrder():
        pass

    def completedWorkOrder():
        pass





    def getValidInput(self, name, prompt, validationFunc, userDict: dict = {}) -> str:
        while True:
            self.printBaseMenu(name, [f'{key}: {value}' for key, value in userDict.items()], prompt)
            user_input = input(' ')
        
            if validationFunc(user_input):
                return user_input

