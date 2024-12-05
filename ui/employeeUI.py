from ui.baseUI import BaseUI
from ui.validationUI import ValidationUI
from baseClasses.Employee import Employee
from logic.logicWrapper import Logic_Wrapper
from ui.searchUI import SearchUI
validation = ValidationUI() 

AVAILABLE_EDIT_OPTIONS_FUNCTIONS = {'name': validation.validateName, 'phone:': validation.validatePhone, 'homephone': validation.validatePhone, 'address': validation.validateText , 'email':  validation.validateEmail, 'location': validation.validateText}

class EmployeeUI(SearchUI):
    def __init__(self, logicWrapper: Logic_Wrapper):
        self.logicWrapper = logicWrapper # initialize the logic wrapper

    def addEmployee(self): # use employee base class
        '''A new employee is created and sent to the json file that stores all employees'''
        userClass = Employee()

        fields = [
            ('kennitala', "Enter a kennitala: ", validation.validateKennitala),  # These are all of the keys, prompts, and values that we need to ask the user
            ('name', "Enter your name: ", validation.validateName),
            ('phone', "Enter a phonenumber: ", validation.validatePhone),
            ('homePhone', "Enter a homephone: ", validation.validatePhone),
            ('address', "Enter a country: ", validation.validateText),
            ('email', "Enter your email: ", validation.validateEmail),
            ('location', "Enter your address: ", validation.validateText),
        ]

        for key, prompt, validationFunc in fields: # This loops for all keys, prompts and functions the user needs to be askes
            value = self.getValidInput('Add employee',prompt, validationFunc, userClass.__dict__)
            if value.lower() in ('q', 'b'): # If the user entered q or b, then we go back one page or quit
                match value.lower():
                    case 'q':
                        return 'q' # quit the whole program
                    case 'b':
                        return False # Go back one page
            userClass.__dict__[key] = value # add the key value pair to the instance


        # Here a instance would get created in order to send to data layer
        new_employee = Employee(userClass.__dict__['kennitala'], userClass.__dict__['name'], userClass.__dict__['phone'], userClass.__dict__['homePhone'], userClass.__dict__['location'], userClass.__dict__['email'], userClass.__dict__['address'])

        self.logicWrapper.addEmployee(new_employee) # ask the logic wrapper to create the new employee the user entered

        # User can then only choose from two options either quit or back
        return self.takeInputAndPrintMenu(['[Q]uit', '[B]ack'], ('Add employee', [f'{key}: {value}' for key, value in userClass.__dict__.items()], 'The employee has been succesfully created\nChoose a option: ')) #



    def showEmployee(self):
        employee = []
        while not employee: # whilee loop keeps going until the wrapper sends a instance to the list
            lookUpKennitala = self.getValidInput("look for employee","Enter ID: ", validation.validateKennitala) # asks the user for a kennital until he enters a valid kennitala, or presses back/quit
            match lookUpKennitala.lower():
                case 'q':
                    return 'q' # quit the whole program
                case 'b':
                    return False # Go back one page
    
            employee = self.logicWrapper.listEmployees(kennitala=lookUpKennitala)  # Call the wrapper and check if a employee exists with the kennitala the user entered

        employee_list = [f'{key}: {value}' for key, value in list(employee[0].__dict__.items())[1:]] # create a list of key, value pairs from the employee the user asked for, we skip the first iteration that is kennitala

        userInput = ''

        while userInput not in AVAILABLE_EDIT_OPTIONS_FUNCTIONS: # here we allow the user to choose what he wants to change, the option he enters needs to be in the global dictionary that stores all options and their validation funcition
            self.printBaseMenu('look for employee', employee_list, 'Enter the number of what you would like to change: ')
            userInput = input(' ').lower()
            match lookUpKennitala.lower():
                case 'q':
                    return 'q' # quit the whole program
                case 'b':
                    return False # Go back one page
                
        newValue = self.getValidInput('look for employee',  'Enter the new value: ', AVAILABLE_EDIT_OPTIONS_FUNCTIONS[userInput], employee[0].__dict__)

        self.logicWrapper.editEmployee(lookUpKennitala, userInput, newValue) #needs to be implemented,....





            
            

            
    def showEmployees(self):
        employeesFile = self.logicWrapper.listEmployees()
        body = []

        # Initialize column names
        headers = ['Name', 'Address', 'Phone number']

        # Calculate the maximum width for each column
        max_name_length = max(len(employee.name) for employee in employeesFile)
        max_address_length = max(len(employee.address) for employee in employeesFile)
        max_phone_length = max(len(employee.phone) for employee in employeesFile)


        # Build the line separator based on the column widths
        line = '+' + '-' * (max_name_length + 2) + '+' + '-' * (max_address_length + 2) + '+' + '-' * (max_phone_length + 2) + '+'

        # Build the header row
        header_row = f"| {headers[0]:<{max_name_length}} | {headers[1]:<{max_address_length}} | {headers[2]:<{max_phone_length}}|"

        # Append the header and line to body
        body.append(line)
        body.append(header_row)
        body.append(line)

        # Build each employee row
        for dict in employeesFile:
            line_content = f"| {dict.name:<{max_name_length}} | {dict.address:<{max_address_length}} | {dict.phone:<{max_phone_length}} |"
            body.append(line_content)
            body.append(line)
    
    

        return self.takeInputAndPrintMenu(['[Q]uit', '[B]ack'], ('List employees', body, 'Choose a option'))
    

            

 
    

    



            




        

    def getValidInput(self, name, prompt, validationFunc, userDict: dict = {}) -> str:
        while True:
            self.printBaseMenu(name, [f'{key}: {value}' for key, value in userDict.items()], prompt)
            user_input = input(' ')
        
            if validationFunc(user_input):
                return user_input
