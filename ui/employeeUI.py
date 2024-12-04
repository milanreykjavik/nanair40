from ui.baseUI import BaseUI
from ui.validationUI import ValidationUI
from baseClasses.Employee import Employee
from logic.logicWrapper import Logic_Wrapper
from ui.searchUI import SearchUI

validation = ValidationUI() 


class EmployeeUI(SearchUI):
    def __init__(self, logicWrapper: Logic_Wrapper):
        self.logicWrapper = logicWrapper

    def addEmployee(self): # use employee base class
        userClass = Employee()




        




        

        fields = [
            ('kennitala', "Enter a kennitala: ", validation.validateKennitala),  # These are all of the keys, prompts, and values that we need to ask the user
            ('name', "Enter your name: ", validation.validateName),
            ('phone', "Enter a phonenumber: ", validation.validatePhone),
            ('homePhone', "Enter a homephone: ", validation.validatePhone),
            ('address', "Enter a country: ", validation.validateCountry),
            ('email', "Enter your email: ", validation.validateEmail),
            ('location', "Enter your address: ", validation.validateAddress),
        ]

        for key, prompt, validationFunc in fields: # This loops for all keys, prompts and functions the user needs to be askes
            value = self.getValidInput('Add employee',prompt, validationFunc, userClass.__dict__)
            if value.lower() in ('q', 'b'): # If the user entered q or b, then we go back one page or quit
                match value.lower():
                    case 'q':
                        return 'q' # quit the whole program
                    case 'b':
                        return False # Go back one page
            userClass.__dict__[key] = value


        # Here a instance would get created in order to send to data layer
        new_employee = Employee(userClass.__dict__['kennitala'], userClass.__dict__['name'], userClass.__dict__['phone'], userClass.__dict__['homePhone'], userClass.__dict__['location'], userClass.__dict__['email'], userClass.__dict__['address'])

        self.logicWrapper.addEmployee(new_employee)

    
        return self.takeInputAndPrintMenu(['[Q]uit', '[B]ack'], ('Add employee', [f'{key}: {value}' for key, value in userClass.__dict__.items()], 'The employee has been succesfully created\nChoose a option: '))
    
    





    def showEmployee(self):
    
        # use Search class there is Employee Search class there that can search by any param in this case kennitala
        employeeInfo = self.showEmployeeID()


        # talk to wrapper with the kennitala entered 


        # Here a instance would get created in order to send to data layer
        new_employee = Employee(userDict['Kennitala'], userDict['Name'], userDict['Phone'], userDict['Homephone'], userDict['Country'], userDict['Email'], userDict['Address'])


        while True:
            self.printBaseMenu('Add employee', [f'{key}: {value}' for key, value in userClass.__dict__.items()], 'Choose an option: ') # if the user finished entering all the information needed then he gets to choose either to quit or go back
            optionInput, isValid = self.takeInput(['[B]ack', '[Q]uit'])

            if isValid:
                match optionInput.lower():
                    case 'b':
                        return False
                    case 'q':
                        return 'q'



    def showEmployee(self):
    
        # use Search class there is Employee Search class there that can search by any param in this case kennitala
        lookUpKennitala = self.getValidInput( 'View/edit employee',"Look up employee by kennitala: ", validation.validateKennitala)

        match lookUpKennitala.lower():
            case 'q':
                return 'q'
            case 'b':
                return False

        # talk to wrapper with the kennitala entered 


        # 
        #new_employee = Employee(userDict['Kennitala'], userDict['Name'], userDict['Phone'], userDict['Homephone'], userDict['Country'], userDict['Email'], userDict['Address'])
    




    def showEmployee(self):
    
        # use Search class there is Employee Search class there that can search by any param in this case kennitala
        lookUpKennitala = self.getValidInput( 'View/edit employee',"Look up employee by kennitala: ", validation.validateKennitala)

        match lookUpKennitala.lower():
            case 'q':
                return 'q'
            case 'b':
                return False

        # talk to wrapper with the kennitala entered 


    def editEmployee():
        pass
        



       
        
    def listEmployees(self):

        allEmployees = getEmployees()

        self.printBaseMenu('List employees', [f'{name}, {phone}, {location}' for name, phone, location in allEmployees ], 'Choose a option')
        pass
        



       
        
    def showEmployees(self):
        pass
        



    
       
            
    def showEmployees(self):
        employeesFile = self.logicWrapper.listEmployees()
        body = []

        # Initialize column names
        headers = ['Name', 'Address', 'Phone number']

        # Calculate the maximum width for each column
        max_name_length = max(len(employee['name']) for employee in employeesFile)
        max_address_length = max(len(employee['address']) for employee in employeesFile)
        max_phone_length = max(len(employee['phone']) for employee in employeesFile)


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
            line_content = f"| {dict['name']:<{max_name_length}} | {dict['address']:<{max_address_length}} | {dict['phone']:<{max_phone_length}} |"
            body.append(line_content)
            body.append(line)
        
        self.printBaseMenu('List employees', body, 'Choose a option')

    

        return self.takeInputAndPrintMenu(['[Q]uit', '[B]ack'], ('Add employee', [f'{key}: {value}' for key, value in userClass.__dict__.items()], 'The employee has been succesfully created\nChoose a option: '))
    



            




        

    def getValidInput(self, name, prompt, validationFunc, userDict: dict = {}) -> str:
        while True:
            self.printBaseMenu(name, [f'{key}: {value}' for key, value in userDict.items()], prompt)
            user_input = input(' ')
        
            if validationFunc(user_input):
                return user_input
