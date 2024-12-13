from ui.propertiesUI import PropertiesUI
from ui.baseUI import BaseUI
from ui.employeeUI import EmployeeUI
from ui.contractorsUI import ContractorsUI
from ui.janitorUI import JanitorUI
from ui.searchUI import SearchUI
from logic.logicWrapper import Logic_Wrapper
from ui.managerWorkorderUI import ManagerWorkOrder

class MainUI(BaseUI):
    def __init__(self):
        self.logicWrapper = Logic_Wrapper()
        self.baseUI = BaseUI()
        self.employeeUI = EmployeeUI(self.logicWrapper)
        self.contractorsIU = ContractorsUI(self.logicWrapper)
        self.propertiesUI = PropertiesUI(self.logicWrapper)
        self.managerWorkOrderUI = ManagerWorkOrder(self.logicWrapper)
        self.janitorUI = JanitorUI(self.logicWrapper)
        self.searchUI = SearchUI(self.logicWrapper)

    def mainMenu(self) -> str:
        '''Prints out main menu and gives the user options to choose from'''
        optionInput = ''
        while optionInput.lower() != 'q':
            self.printMainMenu()  # main menu is printed with the options the user can choose from
            optionInput = input(' ') # user chooses what he wants to do 
 
            # match case the options the user can choose from
            match optionInput.lower():  
                case 'm':  
                    returnValue = self.ShowManagerMenu() 
                case 'j':  
                    returnValue = self.ShowMaintenanceMenu() 
                case 's':  
                    returnValue = self.ShowSearchMenu()
                case 'q':  
                    return 'q' # user quits
                case _:
                    continue # if user enters anything else he then entered a invalid value, while loop resets
                
            if returnValue == 'q': # if the user entered q then we go back until the program ends
               return 'q'


    def ShowManagerMenu(self) -> str | bool:
        '''Prints out manager menu and gives the user the options to go to employee, propertie, work order or contractor menu'''
        optionInput = ''
        while optionInput.lower() != 'q':
            options = ['Employee menu', 'Properties menu', 'Work orders menu', 'Contractors']
            # print the menu and ask the user to choose from the options given
            optionInput = self.takeInputAndPrintMenu(options, ('Manager', options, 'Choose a option: '))

            # matching the options given with the functions
            match optionInput.lower():
                case 'e':  
                    returnValue = self.employeeMenu()
                case 'p': 
                    returnValue = self.propertiesMenu()
                case 'w':  
                    returnValue = self.workOrderMenu()
                case 'c':  
                    returnValue = self.contractorsIU.showContractor()
                case 'b':  # user returns one page
                    return False
                case 'q':  # user quits the whole program
                    return 'q'
                
            if returnValue == 'q': # if q was returned from the last function the we continue returning q
                return 'q'


    def employeeMenu(self) -> str | bool:
        '''Employee menu is printed and user can choose from the given options, user cacn either go to the addEmployee, showEmployee/edit, or list all employess'''
        optionInput = ''
        while optionInput.lower() != 'q':
            options = ['Add employee', 'Edit employee', 'List employees']
            # print the menu and ask the user to choose from the options given
            optionInput = self.takeInputAndPrintMenu(options, ('Employee menu', ['Add employee', 'Edit employee', 'List employees'], 'Choose a option'))

            # matching the options given with the functions
            match optionInput.lower():
                case 'a':
                    returnValue = self.employeeUI.addEmployee() 
                    
                case 'e':
                    returnValue = self.employeeUI.showEmployee() 
                    
                case 'l':
                    returnValue = self.employeeUI.showEmployees() 

                case 'b': # user goes back one page
                    return False
    
                case 'q':  # user quits the program
                    return 'q'

            if returnValue == 'q':  # if q was returned from the last function the we continue returning q
                return 'q'



    def propertiesMenu(self) -> str:
        '''Property menu is printed and user can choose from the given options, use can either go to add new property, show/edit property or list all properties'''
        optionInput = ''
        while optionInput.lower() != 'q':
            options = ['Add property', 'Edit property', 'List properties']
            # print the menu and ask the user to choose from the options given
            optionInput = self.takeInputAndPrintMenu(options, ('Properties menu', options, 'Choose a option'))
            
            # matching the options given with the functions
            match optionInput.lower():
                case 'a':
                    returnValue = self.propertiesUI.addProperty()    
                case 'e':
                    returnValue = self.propertiesUI.showProperty()
                case 'l':
                    returnValue = self.propertiesUI.listProperties()
                case 'b': # user goes back one page
                    return False
                case 'q':  # user quits the program
                    return 'q'


            if returnValue == 'q': # if q was returned from the last function the we continue returning q
               return 'q'


           
    def workOrderMenu(self) -> str | bool:
        '''Work order menu is printed and user can choose menus from given options, uuser can either choose add new work order, edit work order or complete work reports'''
        optionInput = ''
        while optionInput.lower() != 'q':
            options = ['Add work order', 'Completed work reports', 'Edit/view work orders']
             # print the menu and ask the user to choose from the options given
            optionInput = self.takeInputAndPrintMenu(options, ('Work order menu', options, 'Choose a option'))

            # matching the options given with the functions
            match optionInput.lower():
                case 'a':
                    returnValue = self.managerWorkOrderUI.addNewWorkOrder()
                case 'e':
                    returnValue = self.managerWorkOrderUI.editWorkOrder()
                case 'c':
                    returnValue = self.managerWorkOrderUI.completedWorkOrder()
                case 'b':   # user goes back one page
                    return False
                case 'q':  # user quits the program
                    return 'q'


            if returnValue == 'q': # if q was returned from the last function the we continue returning q
               return 'q'



    def ShowMaintenanceMenu(self) -> str | bool:
        '''Maintenance menu is printed and user can choose from given options, user can either go to work orders section or add work report section'''
        optionInput = ''
        while optionInput.lower() != 'q':
            options = ['Work orders', 'Create work report']

            # print the menu and ask the user to choose from the options given
            optionInput  = self.takeInputAndPrintMenu(options, ('Janitor Menu', options, 'Choose a option'))

            # matching the options given with the functions
            match optionInput.lower():
                case 'w':
                    returnValue = self.janitorUI.workOrders()
                case 'c':
                    returnValue = self.janitorUI.addWorkReport()
                case 'b':   # user goes back one page
                    return False
                case 'q':  # user quits the program
                    return 'q'

            if returnValue == 'q': # if q was returned from the last function the we continue returning q
               return 'q'


            
    def ShowSearchMenu(self) -> str | bool:
        '''Search menu is printed am duser can choose from given options'''
        optionInput = ''
        while optionInput.lower() != 'q':
            options = ['Employee Search', 'Property search', 'Work order search', 'Report search', 'Contractors']

            # print the menu and ask the user to choose from the options given
            optionInput = self.takeInputAndPrintMenu(options, ('Search menu', options, 'Choose a option: '))
 
            # matching the options given with the functions
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
                    returnValue = self.contractorsIU.showContractors()
                case 'b':   # user goes back one page
                    return False
                case 'q':  # user quits the program
                    return 'q'

            if returnValue == 'q':  # if q was returned from the last function the we continue returning q
               return 'q'
