from logic.logicWrapper import Logic_Wrapper
from baseClasses.Work import WorkOrder
from ui.validationUI import ValidationUI
validation = ValidationUI()

class WorkUI:
    def __init__(self, logicWrapper: Logic_Wrapper):
        self.logicWrapper = logicWrapper

        userClass = WorkOrder()

        

        fields = [
            ('Description', "Enter the description of the work: ", validation.validateText),  # These are all of the keys, prompts, and values that we need to ask the user
            ('property Number', "Enter the property number: ", validation.validateText),
            ('Contractors', "Enter a name of a contractor: ", validation.validateText),
            ('Priority', "Enter your email: ", validation.validateText)
        ]


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

