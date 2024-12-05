from ui.propertiesUI import PropertiesUI
from ui.baseUI import BaseUI
from ui.employeeUI import EmployeeUI
from ui.contractorsUI import ContractorsUI
from ui.workUI import WorkUI
from ui.janitorUI import JanitorUI
from ui.searchUI import SearchUI
from logic.logicWrapper import Logic_Wrapper

class mainUI(BaseUI):
    def __init__(self):
        self.logicWrapper = Logic_Wrapper()
        self.baseUI = BaseUI()
        self.employeeUI = EmployeeUI(self.logicWrapper)
        self.contractorsIU = ContractorsUI(self.logicWrapper)
        self.propertiesUI = PropertiesUI(self.logicWrapper)
        self.workUI = WorkUI(self.logicWrapper)
        self.janitorUI = JanitorUI(self.logicWrapper)
        self.searchUI = SearchUI(self.logicWrapper)
    




    def mainMenu(self) -> str:
        optionInput = ''
        while optionInput.lower() != 'q':
            self.printMainMenu() 

            optionInput = input(' ')
 

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





    def ShowManagerMenu(self) -> str | bool:
        optionInput = ''
        while optionInput.lower() != 'q':
            options = ['[E]mployee menu', '[P]roperties menu', '[W]ork orders menu', '[C]onstructors']

            optionInput = self.takeInputAndPrintMenu(options, ('Manager', options, 'Choose a option: '))

            
            match optionInput.lower():  
                case 'e':  # Matching case for comparison
                    returnValue = self.employeeMenu()
                case 'p':  # Matching case for comparison
                    returnValue = self.propertiesMenu()
                case 'w':  # Matching case for comparison
                    returnValue = self.workOrderMenu()
                case 'c':  # Matching case for comparison
                    returnValue = self.contractorsUI.addContractor()
                case 'b':  # Matching case for comparison
                    return False
                case 'q':  # Matching case for comparison
                    return 'q'
                
            if returnValue == 'q':
                return 'q'




    def employeeMenu(self) -> str | bool:
        optionInput = ''
        while optionInput.lower() != 'q':
            options = ['[A]dd employee', '[E]dit employee', '[L]ist employees']

            optionInput = self.takeInputAndPrintMenu(options, ('Employee menu', ['[A]dd employee', '[E]dit employee', '[L]ist employees'], 'Choose a option'))



            match optionInput.lower():
                case 'a':
                    returnValue = self.employeeUI.addEmployee() # Go to the employeeUI class and add a new employee
                    
                case 'e':
                    returnValue = self.employeeUI.showEmployees() # Go to the employeeUI class and add edit a employee
                    
                case 'l':
                    returnValue = self.employeeUI.showEmployees() # Go to the employeeUI class and list all employees

                case 'b':
                    return False
    
                case 'q':  # Matching case for comparison
                    return 'q'

            if returnValue == 'q': # if the user entered q then we go back until the program ends
                return 'q'



    def propertiesMenu(self) -> str | bool:
        optionInput = ''
        while optionInput.lower() != 'q':
            options = ['[A]dd property', '[E]dit property', '[L]ist properties']


            optionInput = self.takeInputAndPrintMenu(options, ('Properties menu', options, 'Choose a option'))


            match optionInput.lower():
                case 'a':
                    returnValue = self.propertiesUI.addProperty()    
                case 'e':
                    returnValue = self.propertiesUI.editProperty()
                case 'l':
                    returnValue = self.propertiesUI.showProperty()
                case 'b':
                    return False

                case 'q':  # Matching case for comparison
                    return 'q'


            if returnValue == 'q':
               return 'q'


           
    def workOrderMenu(self) -> str | bool:
        optionInput = ''
        while optionInput.lower() != 'q':
            options = ['[A]dd work order', '[C]ompleted work reports', '[E]dit/view work orders']

            optionInput = self.takeInputAndPrintMenu(options, ('Work order menu', options, 'Choose a option'))

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


        





    def ShowMaintenanceMenu(self) -> str | bool:
        optionInput = ''
        while optionInput.lower() != 'q':
            options = ['[W]ork orders', '[C]reate work report']

            optionInput  = self.takeInputAndPrintMenu(options, ('Janitor Menu', options, 'Choose a option'))

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


                    


    def ShowSearchMenu(self) -> str | bool:
        optionInput = ''
        while optionInput.lower() != 'q':
            options = ['[E]mployee Search', '[P]roperty search', '[W]ork order search', '[R]eport search', '[C]ontractors']

            optionInput = self.takeInputAndPrintMenu(options, ('Search menu', options, 'Choose a option'))
 

            match optionInput.lower():
                case 'e':
                    returnValue = self.searchUI.employeeSearch()
                case 'p':
                    returnValue = self.searchUI.propertySearch()
                case 'w':
                    returnValue = self.searchUI.workOrderSearch()
                case 'r':
                    returnValue = self.searchUI.workReportSearch()
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

