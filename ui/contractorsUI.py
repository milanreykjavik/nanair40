from baseClasses.Contractor import Contractor
from logic.logicWrapper import Logic_Wrapper
from ui.validationUI import ValidationUI
from ui.searchUI import SearchUI

validation = ValidationUI()

class ContractorsUI(SearchUI):
    def __init__(self, logicWrapper: Logic_Wrapper):
        self.logicWrapper = logicWrapper
    
    def addContractor(self):
        contractorClass = Contractor()

        fields = [
            ('id', "Enter a ID for the contractor: ", validation.validateID),  # These are all of the keys, prompts, and values that we need to ask the user
            ('name', "Enter the name of the contractor: ", validation.validateName),
            ('phone', "Enter the phonenumer of the contractors : ", validation.validatePhone),
            ('openingHours', "Write the opening hours: ", validation.validateName),
            ('location', "Enter the location: ", validation.validateLocation),
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
        


    def showContractor(self):
        contractorsFile = self.logicWrapper.listContractors()
        body = []

        # Initialize column names
        headers = ['ID', 'Name', 'Location']

        # Calculate the maximum width for each column
        max_ID_length = max((contractor.id) for contractor in contractorsFile)
        max_Name_length = max(len(contractor.name) for contractor in contractorsFile)
        max_Location_length = max((contractor.location) for contractor in contractorsFile)


        # Build the line separator based on the column widths
        line = '+' + '-' * (max_ID_length + 2) + '+' + '-' * (max_Name_length + 2) + '+' + '-' * (max_Location_length + 2) + '+'

        # Build the header row
        header_row = f"| {headers[0]:<{max_ID_length}} | {headers[1]:<{max_Name_length}} | {headers[2]:<{max_Location_length}}|"

        # Append the header and line to body
        body.append(line)
        body.append(header_row)
        body.append(line)

        # Build each employee row
        for dict in contractorsFile:
            line_content = f"| {dict.id:<{max_ID_length}} | {dict.name:<{max_Name_length}} | {dict.location:<{max_Location_length}} |"
            body.append(line_content)
            body.append(line)
        

    

        return self.takeInputAndPrintMenu(['[Q]uit', '[B]ack'], ('List Contractors', body, 'Choose a option'))


    def editContractor():
        pass
        



    def getValidInput(self, name, prompt, validationFunc, user_dict: dict = {}) -> str:
        while True:
            self.printBaseMenu(name, [f'{key}: {value}' for key, value in user_dict.items()], prompt)
            user_input = input(' ')
        
            if validationFunc(user_input):
                return user_input
        