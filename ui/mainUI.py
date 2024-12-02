from propertiesUI import PropertiesUI
from baseUI import BaseUI
from employeeUI import EmployeeUI
from contractorsUI import ContractorsUI
from workUI import WorkUI

baseUI = BaseUI()
employeeUI = EmployeeUI()
contractorsIU = ContractorsUI()
propertiesUI = PropertiesUI()
workUI = WorkUI()




def ShowManagerMenu() -> None:
    while True:
        options = ['Manager menu', 'Properties menu', 'Work orders menu', 'Constructors']
        baseUI.printBaseMenu('Manager', options)

        input = userInput(options)

        if not input:
            print('Invalid Input')
            continue
        
        if input.lower() == 'e':
            employeeMenu()
        
        elif input.lower() == 'p':
            propertiesMenu()
        
        elif input.lower() == 'w':
            workOrderMenu()

        elif input.lower() == 'c':
            ContractorsUI()

        elif input.lower() == 'b':
            return False
        





def employeeMenu():
    while True:
        options = ['Add employee', 'Edit employee', 'List employees']
        baseUI.printBaseMenu('Employee menu', options, 'Choose a option') # Prints base menu

        input = userInput(options) #Gets the user input

        if not input: # If the user entered a options that is not available we ask again
            continue
            
        if input.lower() == 'a':
            employeeUI.addEmployee() # Go to the employeeUI class and add a new employee
            
        elif input.lower() == 'e':
            employeeUI.editEmployee() # Go to the employeeUI class and add edit a employee
            
        elif input.lower() == 'l':
            employeeUI.listEmployess() # Go to the employeeUI class and list all employees

        elif input.lower() == 'b':
            return False







def propertiesMenu():
    while True:
        baseUI.printBaseMenu('Properties menu', ['Add property', 'Edit property', 'List properties'], 'Choose a option')

        input = userInput(['Add employee', 'Edit employee', 'List employees'])

        if not input:
            print('Invalid Input')
            continue
                
        if input.lower() == 'a':
            propertiesUI.add_property()
                
        elif input.lower() == 'e':
            propertiesUI.edit_property()
                
        elif input.lower() == 'l':
            propertiesUI.list_properties()

        elif input.lower() == 'b':
            return False
    



    
def workOrderMenu():
    while True:
        options = ['Add work order', 'Completed work reports', 'Edit work orders']
        baseUI.printBaseMenu('Work order menu', options, 'Choose a option')

        input = userInput(options)

        if not input:
            print('Invalid Input')
            continue
                
        if input.lower() == 'a':
            workUI.add_work_order()
                
        elif input.lower() == 'c':
            workUI.edit_work_order()
                
        elif input.lower() == 'e':
            workUI.completed_work_order()

        elif input.lower() == 'b':
            return False

    

    




def ShowMaintenanceMenu():
    baseUI.printBaseMenu('Janitor menu', ['Work orders', 'Create work report'], 'Choose a option')



def ShowSearchMenu():
    baseUI.printBaseMenu('Janitor menu', ['Employee Search', 'Propertie'], 'Choose a option')








def userInput(options):
    try:
        input = baseUI.takeInput(options)
    except Exception as e:
        print('Invalid Input')
        return False


    return input


ShowManagerMenu()



