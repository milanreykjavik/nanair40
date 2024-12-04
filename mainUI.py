from ui.propertiesUI import PropertiesUI
from ui.baseUI import BaseUI
from ui.employeeUI import EmployeeUI
from ui.contractorsUI import ContractorsUI
from ui.workUI import WorkUI
from ui.janitorUI import JanitorUI
from ui.searchUI import SearchUI

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
            options = ['[M]anager', '[J]anitor', '[S]earch'] # each option the user gets to pick from

            optionInput, isValid = self.takeInput(options)
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
            options = ['[E]mployee menu', '[P]roperties menu', '[W]ork orders menu', '[C]onstructors']
            self.printBaseMenu('Manager', options, 'Choose a option: ')


            optionInput, isValid = self.takeInput(options)
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
            options = ['[A]dd employee', '[E]dit employee', '[L]ist employees']
            self.printBaseMenu('Employee menu', options, 'Choose a option: ') # Prints base menu

            optionInput, isValid = self.takeInput(options)
            if not isValid:
                continue


            match optionInput.lower():
                case 'a':
                    returnValue = self.employeeUI.addEmployee() # Go to the employeeUI class and add a new employee
                    
                case 'e':
                    returnValue = self.employeeUI.showEmployee() # Go to the employeeUI class and add edit a employee
                    
                case 'l':
                    returnValue = self.employeeUI.showEmployees() # Go to the employeeUI class and list all employees

                case 'b':
                    return False
    
                case 'q':  # Matching case for comparison
                    return 'q'

            if returnValue == 'q': # if the user entered q then we go back until the program ends
                return 'q'







    def propertiesMenu(self) -> None:
        optionInput = ''
        while optionInput.lower() != 'q':
            options = ['[A]dd property', '[E]dit property', '[L]ist properties']
            self.printBaseMenu('Properties menu', options, 'Choose a option')


            optionInput, isValid = self.takeInput(options)
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
            options = ['[A]dd work order', '[C]ompleted work reports', '[E]dit/view work orders']
            self.printBaseMenu('Work order menu', options, 'Choose a option')

            optionInput, isValid = self.takeInput(options)
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
            options = ['[W]ork orders', '[C]reate work report']
            self.printBaseMenu('Janitor menu', options, 'Choose a option')

            optionInput, isValid = self.takeInput(options)
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
            options = ['[E]mployee Search', '[P]roperty search', '[W]ork order search', '[R]eport search', '[C]ontractors']
            self.printBaseMenu('Search menu', options, 'Choose a option')

            optionInput, isValid = self.takeInput(options)
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






mainUI = mainUI()
mainUI.mainMenu()



