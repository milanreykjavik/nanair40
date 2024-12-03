from propertiesUI import PropertiesUI
from baseUI import BaseUI
from employeeUI import EmployeeUI
from contractorsUI import ContractorsUI
from workUI import WorkUI
from janitorUI import JanitorUI
from searchUI import SearchUI

class mainUI(BaseUI):
    def __init__(self):
        self.baseUI = BaseUI()
        self.employeeUI = EmployeeUI()
        self.contractorsIU = ContractorsUI()
        self.propertiesUI = PropertiesUI()
        self.workUI = WorkUI()
        self.janitorUI = JanitorUI()
        self.searchUI = SearchUI()



    def mainMenu(self) -> None:
        optionInput = ''
        while optionInput.lower() != 'q':
            self.printMainMenu() 
            options = ['Manager', 'Janitor', 'Search'] # each option the user gets to pick from

            optionInput, isValid = self.userInput(options)
            if not isValid:
                continue

            match optionInput.lower():  
                case 'm':  
                    returnValue = self.ShowManagerMenu() 
                case 'j':  
                    returnValue = self.ShowMaintenanceMenu() 
                case 's':  
                    returnValue = self.ShowSearchMenu()
            
                case 'q':  # Matching case for comparison
                    return 'q'
                
            if returnValue == 'q': # if the user entered q then we go back until the program ends
               return 'q'





    def ShowManagerMenu(self) -> None:
        optionInput = ''
        while optionInput.lower() != 'q':
            options = ['Employee menu', 'Properties menu', 'Work orders menu', 'Constructors']
            self.printBaseMenu('Manager', options, 'Choose a option')


            optionInput, isValid = self.userInput(options)
            if not isValid:
                continue
            
            match optionInput.lower():  
                case 'e':  # Matching case for comparison
                    returnValue = self.employeeMenu()
                case 'p':  # Matching case for comparison
                    returnValue = self.propertiesMenu()
                case 'w':  # Matching case for comparison
                    returnValue = self.workOrderMenu()
                case 'c':  # Matching case for comparison
                    returnValue = self.contractorsIU()
                case 'b':  # Matching case for comparison
                    return False
                case 'q':  # Matching case for comparison
                    return 'q'
                
            if returnValue == 'q':
                return 'q'




    def employeeMenu(self) -> None:
        optionInput = ''
        while optionInput.lower() != 'q':
            options = ['Add employee', 'Edit employee', 'List employees']
            self.printBaseMenu('Employee menu', options, 'Choose a option') # Prints base menu

            optionInput, isValid = self.userInput(options)
            if not isValid:
                continue


            match optionInput.lower():
                case 'a':
                    returnValue = self.employeeUI.addEmployee() # Go to the employeeUI class and add a new employee
                    
                case 'e':
                    returnValue = self.employeeUI.editEmployee() # Go to the employeeUI class and add edit a employee
                    
                case 'l':
                    returnValue = self.employeeUI.listEmployess() # Go to the employeeUI class and list all employees

                case 'b':
                    return False
    
                case 'q':  # Matching case for comparison
                    return 'q'

            if returnValue == 'q': # if the user entered q then we go back until the program ends
                return 'q'







    def propertiesMenu(self) -> None:
        optionInput = ''
        while optionInput.lower() != 'q':
            options = ['Add property', 'Edit property', 'List properties']
            self.printBaseMenu('Properties menu', options, 'Choose a option')


            optionInput, isValid = self.userInput(options)
            if not isValid:
                continue

            match optionInput.lower():
                case 'a':
                    returnValue = self.propertiesUI.addProperty()    
                case 'e':
                    returnValue = self.propertiesUI.editProperty()
                case 'l':
                    returnValue = self.propertiesUI.listProperties()
                case 'b':
                    return False

                case 'q':  # Matching case for comparison
                    return 'q'


            if returnValue == 'q':
               return 'q'


           
    def workOrderMenu(self) -> None:
        optionInput = ''
        while optionInput.lower() != 'q':
            options = ['Add work order', 'Completed work reports', 'Edit work orders']
            self.printBaseMenu('Work order menu', options, 'Choose a option')

            optionInput, isValid = self.userInput(options)
            if not isValid:
                continue
                    
            match optionInput.lower():
                case 'a':
                    returnValue = self.workUI.addWorkOrder()
                case 'c':
                    returnValue = self.workUI.editWorkOrder()
                case 'e':
                    returnValue = self.workUI.completedWorkOrder()
                case 'b':
                    return False
                
                case 'q':  # Matching case for comparison
                    return 'q'


            if returnValue == 'q':
               return 'q'


        





    def ShowMaintenanceMenu(self) -> None:
        optionInput = ''
        while optionInput.lower() != 'q':
            options = ['Work orders', 'Create work report']
            self.printBaseMenu('Janitor menu', options, 'Choose a option')

            optionInput, isValid = self.userInput(options)
            if not isValid:
                continue

            match optionInput.lower():
                case 'w':
                    returnValue = self.janitorUI.workOrders()
                case 'c':
                    returnValue = self.janitorUI.workReports()
                case 'b':
                    return False

                case 'q':  # Matching case for comparison
                    return 'q'

            if returnValue == 'q':
               return 'q'


                    


    def ShowSearchMenu(self) -> None:
        optionInput = ''
        while optionInput.lower() != 'q':
            options = ['Employee Search', 'Property search', 'Work order search', 'Report search', 'Contractors']
            self.printBaseMenu('Search menu', options, 'Choose a option')

            optionInput, isValid = self.userInput(options)
            if not isValid:
                continue

            match optionInput.lower():
                case 'e':
                    returnValue = self.searchUI.employeeSearch()
                case 'p':
                    returnValue = self.searchUI.propertySearch()
                case 'w':
                    returnValue = self.searchUI.workOrderSearch()
                case 'r':
                    returnValue = self.searchUI.workReportSearch
                case 'c':
                    returnValue = self.searchUI.contractors()
                case 'b':
                    return False
                case 'q':  # Matching case for comparison
                    return 'q'

            if returnValue == 'q':
               return 'q'






    def userInput(self, options) -> tuple[str, bool]:
        try:
            input = self.baseUI.takeInput(options)
        except Exception as e:
            return '_', False

        return input, True



mainUI = mainUI()
mainUI.mainMenu()



