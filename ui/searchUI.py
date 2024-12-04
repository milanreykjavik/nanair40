from ui.baseUI import BaseUI
from ui.employeeUI import EmployeeUI
from ui.validationUI import ValidationUI
employeeUI = EmployeeUI()
validation = ValidationUI()


class SearchUI(BaseUI):
    def employeeSearch(self):
        isValid = False
        while not isValid:
            self.printBaseMenu('Seacrh employee',['[K]ennitala search', '[P]roperty number search'], 'Choose a option:  ')
            userOption, isValid = self.takeInput(['[K]ennitala search', '[P]roperty number search'])


            if userOption.lower() == 'k':
                self.showEmployeeID()

            else:
                self.showEmployeesProperty()




    def showEmployeeID(self):
    
        # use Search class there is Employee Search class there that can search by any param in this case kennitala
        lookUpKennitala = self.getValidInput( 'View employee',"Look up employee by kennitala: ", validation.validateKennitala)

        match lookUpKennitala.lower():
            case 'q':
                return 'q'
            case 'b':
                return False

        # talk to wrapper with the kennitala entered 
        userInformation = ''
        return userInformation
    
    def showEmployeesProperty(self):
        lookUpProperty = self.getValidInput( 'View employees by property',"Look up employees by properties: ", validation.validateKennitala)

        match lookUpProperty.lower():
            case 'q':
                return 'q'
            case 'b':
                return False

        # talk to wrapper with property number entered and print all properties



        #new_employee = Employee(userDict['Kennitala'], userDict['Name'], userDict['Phone'], userDict['Homephone'], userDict['Country'], userDict['Email'], userDict['Address'])
    

    def propertySearch():
        pass


    def workOrderSearch():
        pass

    def workReportSearch():
        pass

    def contractors():
        pass


    def getValidInput(self, name, prompt, validationFunc, userDict: dict = {}) -> str:
        while True:
            self.printBaseMenu(name, [f'{key}: {value}' for key, value in userDict.items()], prompt)
            user_input = input(' ')
        
            if validationFunc(user_input):
                return user_input
        
