from baseClasses.Contractor import Contractor
from logic.logicWrapper import Logic_Wrapper
from ui.validationUI import ValidationUI
from ui.searchUI import SearchUI

validation = ValidationUI()
# global variables that are used to keep track of error messages and validation functions
AVAILABLE_EDIT_OPTIONS_FUNCTIONS = {'name': validation.validateName, 'phone': validation.validatePhone, 'opening hours': validation.validateOpeningHours, 'location': validation.validateText}
ERROR_MESSAGES = {'name': 'Invalid name, Please enter only letters\n', 'phone': 'Phone number has to only include numbers and be of the length 7-15\n', 'opening hours': 'Opening hours must be in the format given in the brackets, for example 10-20 or 08-16\n', 'location': 'Please choose from the options above\n'}
quitOrBack = ['q', 'b']

class ContractorsUI(SearchUI):
    def __init__(self, logicWrapper: Logic_Wrapper):
        self.logicWrapper = logicWrapper
    
    def showContractor(self) -> str:
        '''Asks the user whether he wants to list all contractors, add contractors or edit contractors info'''
        # print mmenu and ask user what he would like to do
        userInput = self.takeInputAndPrintMenu(['Add contractor', 'Edit contractor', 'List contractors'], ('Contractor Menu', ['Add contractor', 'Edit contractor', 'List contractors'], 'Choose a option'))

        match userInput.lower(): # go into the function that matches the user input
            case 'l':
                return self.showContractors()
            case 'a':
                return self.addContractor()
            case 'e':
                return self.editContractor()
            
        return userInput # if the user didnt enter any of the available options then he either quits or goes back
            
    def addContractor(self):
        contractorClass = Contractor()
        fields = [    # These are all of the keys, prompts, and values that we need to ask the user
            ('name', "Enter the name of the contractor: ", validation.validateName, 'Invalid name, Please enter only letters\n'),
            ('phone', "Enter the phone number: ", validation.validatePhone, 'Phone number has to only include numbers and be of the length 7-15\n'),
            ('openingHours', "Write the opening hours(OPENING-CLOSING): ", validation.validateOpeningHours, 'Opening hours must be in the format given in the brackets, for example 10-20 or 08-16\n'),
        ]
        
        for key, prompt, validationFunc, errorMessage in fields: # This loops for all keys, prompts and functions the user needs to be askes
            value = self.getValidInput('Add contractor',prompt, validationFunc, contractorClass.__dict__, errorMessage)
            if value.lower() in quitOrBack: # If the user entered q or b, then we go back one page or quit
                return value.lower()
            # add the new value to the contractors class
            contractorClass.__dict__[key] = value

        location = None
        destinations = self.logicWrapper.listLocations() # call logic layer to get a list of all locations to print out in menu
        # print a menu with every single location option and asking the user for a location to pick from
        employeeLocation =  self.takeInputAndPrintMenuWithoutBrackets('', ('Add property', [destination.airport for destination in destinations], 'choose a location: ')).capitalize()
        while not location:
            if employeeLocation.lower() in quitOrBack:
                return employeeLocation.lower()
            # check whith logic layer if location the user entered exists, if it doesnt then logic layer returns none
            location = self.logicWrapper.listLocations(airport = employeeLocation)
            if not location:
                # if none was returned from logic layer then the user is asked again, and the menu is printed
                employeeLocation =  self.takeInputAndPrintMenuWithoutBrackets('', ('Add property', [destination.airport for destination in destinations], 'Please choose a location from the given options\nchoose a location: ')).capitalize()
        contractorClass.__dict__['location'] = employeeLocation



        
        # contractor isntance is created
        newContractor = Contractor(self.logicWrapper.currentContractorID, contractorClass.__dict__["name"], contractorClass.__dict__["phone"], contractorClass.__dict__["openingHours"], contractorClass.__dict__["location"])

        # contractor instance sent to the logic layer in order to create the employee
        self.logicWrapper.addContractor(newContractor)

        # Print a menu with all of the contractor information that was just created, the user can either quit or go back
        return self.takeInputAndPrintMenuWithoutBrackets(['[Q]uit', '[B]ack'], ('Add Constractor', [f'{key}: {value}' for key, value in newContractor.__dict__.items()], 'The Contractor has been succesfully created\nChoose a option: '))
        



    def editContractor(self) -> str:
        '''User is given options of contractors he can edit from, he chooses what value he wants to change and can enter a new value, either 'q' or 'b' is returned based on whether the user quits or goes back'''
        contractor = []
        while not contractor: # while loop keeps going until the user enters a contractor id that is available
            contractorList = self.logicWrapper.listContractors()
            #
            lookUpContractor = self.showContractorsInfo(contractorList, 'Enter contractor ID to edit: ', '')
            if lookUpContractor.lower() in quitOrBack:
                return lookUpContractor.lower()
            contractor = self.logicWrapper.listContractors(id=lookUpContractor)  # Call the wrapper and check if a employee exists with the kennitala the user entered

        # contractor dict is used to keep track of all values to print to the screen
        contractorDict = {'name': contractor[0].name, 'phone': contractor[0].phone, 'opening hours': contractor[0].openingHours, 'location': contractor[0].location}

        valueToChange = ''
        # user is asked for a value to change until he enters a value that is in the AVAILABLE_EDIT_OPTIONS_FUNCTIONS global variable
        while valueToChange.lower() not in AVAILABLE_EDIT_OPTIONS_FUNCTIONS: 
            # user asked for a value to change and the validation function is used to validate it
            valueToChange = self.getValidInput('Edit contractor', 'Enter the value of what you would like to change: ', validation.validateText, contractorDict)

            if valueToChange.lower() in quitOrBack: # if the user entered to quit or go back
                return valueToChange.lower()
            
        
        if valueToChange == 'location': # user chose to change location
            location = None
            destinations = self.logicWrapper.listLocations() # call logic layer to get a list of all locations to print out on the screen
            # ask the user for a locatino while printing the location options on the screen
            employeeLocation =  self.takeInputAndPrintMenuWithoutBrackets('', ('Add property', [destination.airport for destination in destinations], 'choose a location')).capitalize()
            while not location:
                if employeeLocation.lower() in quitOrBack: # user quits or goes back one page
                    return employeeLocation.lower()
                # check whith logic layer if the location entered is valid, none is returned if the location doesnt exist
                location = self.logicWrapper.listLocations(airport = employeeLocation)
                if not location:
                    # if no location was found then the user is asked again with a error message
                    employeeLocation =  self.takeInputAndPrintMenuWithoutBrackets('', ('Add property', [destination.airport for destination in destinations], 'Please choose a location from the given options\nchoose a location: ')).capitalize()
            contractorDict['location'] = employeeLocation
            newValue = employeeLocation
        else:
            # if the user did not choose to change location then he enters a new value and that value is validated in its validation func
            newValue = self.getValidInput('Edit contractor',  'Enter the new value: ', AVAILABLE_EDIT_OPTIONS_FUNCTIONS[valueToChange.lower()], contractorDict, ERROR_MESSAGES[valueToChange.lower()])
        
        if newValue.lower() in quitOrBack:
            return newValue.lower()

        # new value added to the dictionary that is keeping track of the contractors values
        contractorDict[valueToChange.lower()] = newValue

        # match what the user wants to change, the logic wrapper is called where he changes the value in the employee json file
        match valueToChange.lower(): 
            case 'name':
                self.logicWrapper.editContractor(entry= 'id', entryValue=int(lookUpContractor), name = newValue)
            case 'phone':
                self.logicWrapper.editContractor(entry='id', entryValue=int(lookUpContractor), phone = newValue)
            case 'opening hours':
                self.logicWrapper.editContractor(entry='id', entryValue=int(lookUpContractor), openingHours = newValue)
            case 'location':
                self.logicWrapper.editContractor(entry='id', entryValue=int(lookUpContractor), location = newValue)

        return self.takeInputAndPrintMenuWithoutBrackets(['[Q]uit', '[B]ack'], ('Edit contractors', [f'{key}: {value}' for key, value in list(contractorDict.items())], 'Employee information has been succesfuly updated!\nChoose a option: '))



        
    def showContractors(self) -> str:
        '''All contractors whithin the system are displayed in a table, either 'q' or 'b' is returned based on whether user quits or goes back'''
        contractorList = self.logicWrapper.listContractors()
        return self.showContractorsInfo(contractorList).lower()