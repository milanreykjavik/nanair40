from baseClasses.Property import Property
from logic.logicWrapper import Logic_Wrapper
from ui.searchUI import SearchUI
from ui.validationUI import ValidationUI


validation = ValidationUI()


class PropertiesUI(SearchUI):
    def __init__(self, logicWrapper: Logic_Wrapper):
        self.logicWrapper = logicWrapper
    
    def addProperty(self):
        propertyClass = Property()

        fields = [
            ('id', "Enter a a property numner: ", validation.validateText),  # These are all of the keys, prompts, and values that we need to ask the user
            ('location', "Enter the location of the property: ", validation.validateText),
            ('Size', 'Enter the size of the property')
            ('address', "Enter the address of the property: : ", validation.validateText),
            ('condition', "Condition(Excellent, Good, Fair, Poor): ", validation.validateCondition),
            ('Room ID range', 'How many): ', validation.validatePhone)
            ('facilities', "Facilities requiring maintenance: ", validation.validateText),
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
        


    def showProperty(self):
        propertiesFile = self.logicWrapper.listProperties()
        body = []

        # Initialize column names
        headers = ['ID', 'Location', 'Address', 'Condition']

        # Calculate the maximum width for each column
        max_ID_length = max(len(property.id) for property in propertiesFile)
        max_Location_length = 12
        max_address_length = max(len(property.address) for property in propertiesFile)
        max_Condition_length = 12


        # Build the line separator based on the column widths
        line = '+' + '-' * (max_ID_length + 2) + '+' + '-' * (max_Location_length + 2) + '+' + '-' * (max_address_length + 2) + '+' + '-' * (max_Condition_length + 2) + '+'

        # Build the header row
        header_row = f"| {headers[0]:<{max_ID_length}} | {headers[1]:<{max_Location_length}} | {headers[2]:<{max_address_length}} | {headers[3]:<{max_Condition_length}} |"

        # Append the header and line to body
        body.append(line)
        body.append(header_row)
        body.append(line)

        # Build each employee row
        for dict in propertiesFile:
            line_content = f"| {dict.id:<{max_ID_length}} | {dict.location:<{max_Location_length}} | {dict.address:<{max_address_length}} | {dict.condition:<{max_Condition_length}} |"
            body.append(line_content)
            body.append(line)
        

    

        return self.takeInputAndPrintMenu(['[Q]uit', '[B]ack'], ('List Properties', body, 'Choose a option'))


 
    def listProperties():
        pass



    def getValidInput(self, name, prompt, validationFunc, user_dict: dict = {}) -> str:
        while True:
            self.printBaseMenu(name, [f'{key}: {value}' for key, value in user_dict.items()], prompt)
            user_input = input(' ')
        
            if validationFunc(user_input):
                return user_input
        