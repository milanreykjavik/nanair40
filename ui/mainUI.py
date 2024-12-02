from propertiesUI import PropertiesUI
from baseUI import BaseUI
from employeeUI import EmployeeUI
from contractorsUI import ContractorsUI
from workUI import WorkUI
from janitorUI import JanitorUI
from searchUI import SearchUI

baseUI = BaseUI()
employeeUI = EmployeeUI()
contractorsIU = ContractorsUI()
propertiesUI = PropertiesUI()
workUI = WorkUI()
janitorUI = JanitorUI()
searchUI = SearchUI()



def mainMenu() -> None:
    optionInput = ''
    while optionInput.lower() != 'q':
        baseUI.printMainMenu()
        options = ['Manager', 'Janitor', 'Search']

        optionInput = userInput(options)

        if not optionInput:
            optionInput = ''
            invalidInput()
            continue

        match optionInput.lower():  
            case 'm':  # Matching case for comparison
                ShowManagerMenu()
            case 'j':  # Matching case for comparison
                ShowMaintenanceMenu()
            case 's':  # Matching case for comparison
                ShowSearchMenu()




def ShowManagerMenu() -> None:
    optionInput = ''
    while optionInput.lower() != 'q':
        options = ['Employee menu', 'Properties menu', 'Work orders menu', 'Constructors']
        baseUI.printBaseMenu('Manager', options, 'Choose a option')

        optionInput = userInput(options)

        if not optionInput:
            optionInput = ''
            invalidInput()
            continue
        
        match optionInput.lower():  
            case 'e':  # Matching case for comparison
                employeeMenu()
            case 'p':  # Matching case for comparison
                propertiesMenu()
            case 'w':  # Matching case for comparison
                workOrderMenu()
            case 'c':  # Matching case for comparison
                contractorsIU()
            case 'b':  # Matching case for comparison
                return False




def employeeMenu() -> None:
    optionInput = ''
    while optionInput.lower() != 'q':
        options = ['Add employee', 'Edit employee', 'List employees']
        baseUI.printBaseMenu('Employee menu', options, 'Choose a option') # Prints base menu

        optionInput = userInput(options) #Gets the user input

        if not optionInput: # If the user entered a options that is not available we ask again
            optionInput = ''
            invalidInput()
            continue

        match optionInput.lower():
            case 'a':
                employeeUI.addEmployee() # Go to the employeeUI class and add a new employee
                
            case 'e':
                employeeUI.editEmployee() # Go to the employeeUI class and add edit a employee
                
            case 'l':
                employeeUI.listEmployess() # Go to the employeeUI class and list all employees

            case 'b':
                return False




def propertiesMenu() -> None:
    optionInput = ''
    while optionInput.lower() != 'q':
        options = ['Add property', 'Edit property', 'List properties']
        baseUI.printBaseMenu('Properties menu', options, 'Choose a option')

        optionInput = userInput(options)

        if not optionInput:
            optionInput = ''
            invalidInput()
            continue

        match optionInput.lower():
            case 'a':
                propertiesUI.addProperty()    
            case 'e':
                propertiesUI.editProperty()
            case 'l':
                propertiesUI.listProperties()
            case 'b':
                return False
        



    
def workOrderMenu() -> None:
    optionInput = ''
    while optionInput.lower() != 'q':
        options = ['Add work order', 'Completed work reports', 'Edit work orders']
        baseUI.printBaseMenu('Work order menu', options, 'Choose a option')

        optionInput = userInput(options)

        if not optionInput:
            optionInput = ''
            invalidInput()
            continue
                
        match optionInput.lower():
            case 'a':
                workUI.addWorkOrder()
            case 'c':
                workUI.editWorkOrder()
            case 'e':
                workUI.completedWorkOrder()
            case 'b':
                return False

    





def ShowMaintenanceMenu() -> None:
    optionInput = ''
    while optionInput.lower() != 'q':
        options = ['Work orders', 'Create work report']
        baseUI.printBaseMenu('Janitor menu', options, 'Choose a option')
        optionInput = userInput(options)

        if not optionInput:
            optionInput = ''
            invalidInput()
            continue

        match optionInput.lower():
            case 'w':
                janitorUI.workOrders()
            case 'c':
                janitorUI.workReports()
            case 'b':
                return False
                
                






def ShowSearchMenu() -> None:
    optionInput = ''
    while optionInput.lower() != 'q':
        options = ['Employee Search', 'Property search', 'Work order search', 'Report search', 'Contractors']
        baseUI.printBaseMenu('Search menu', options, 'Choose a option')
        optionInput = userInput(options)

        if not optionInput:
            optionInput = ''
            invalidInput()
            continue

        match optionInput.lower():
            case 'e':
                searchUI.employeeSearch()
            case 'p':
                searchUI.propertySearch()
            case 'w':
                searchUI.workOrderSearch()
            case 'r':
                searchUI.workReportSearch
            case 'c':
                searchUI.contractors()
            case 'b':
                return False











def userInput(options) -> str | bool:
    try:
        input = baseUI.takeInput(options)
    except Exception as e:
        print('Invalid Input')
        return False


    return input


def invalidInput() -> None:
    print('Try again')


mainMenu()



