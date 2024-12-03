from baseUI import BaseUI
baseUI = BaseUI()


validation = ValidationUI() 

class EmployeeUI(BaseUI):
    def addEmployee(self):
        user_dict = {
            'Kennitala': '',
            'Name': '',
            'Phone': '',
            'Homephone': '',
            'Country': '',
            'Email': '',
            'Address': ''
        }

        fields = [
            ('Kennitala', "Enter a kennitala: ", validation.validateKennitala),  # These are all of the keys, prompts, and values that we need to ask the user
            ('Name', "Enter your name: ", validation.validateName),
            ('Phone', "Enter a phonenumber: ", validation.validatePhone),
            ('Homephone', "Enter a homephone: ", validation.validatePhone),
            ('Country', "Enter a country: ", validation.validateCountry),
            ('Email', "Enter your email: ", validation.validateEmail),
            ('Address', "Enter your address: ", validation.validateAddress),
        ]

        for key, prompt, validationFunc in fields: # This loops for all keys, prompts and functions the user needs to be askes
            value = self.getValidInput('Add employee',prompt, validationFunc, user_dict)
            if value.lower() in ('q', 'b'): # If the user entered q or b, then we go back one page or quit
                match value.lower():
                    case 'q':
                        return 'q' # quit the whole program
                    case 'b':
                        return False # Go back one page
            user_dict[key] = value


        # Here a instance would get created in order to send to data layer


        while True:
            self.printBaseMenu('Add employee', [f'{key}: {value}' for key, value in user_dict.items()], 'Choose an option: ') # if the user finished entering all the information needed then he gets to choose either to quit or go back
            optionInput = self.takeInput(['Back', 'Quit'])

            match optionInput.lower():
                case 'b':
                    return False
                case 'q':
                    return 'q'



    def editEmployee(self):
    
        lookUpKennitala = self.getValidInput( 'View/edit employee',"Look up employee by kennitala: ", validation.validateKennitala)

        match lookUpKennitala.lower():
            case 'q':
                return 'q'
            case 'b':
                return False

        # talk to wrapper with the kennitala entered
        



       
        
    def listEmployess(self):
        pass
        # Here we need to call showEmployees in the wrapper to get all of the employees in the system


        

    def getValidInput(self, name, prompt, validationFunc, user_dict: dict = {}) -> str:
        while True:
            self.printBaseMenu(name, [f'{key}: {value}' for key, value in user_dict.items()], prompt)
            user_input = input(' ')
        
            if validationFunc(user_input):
                return user_input
        



