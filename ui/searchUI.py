from ui.baseUI import BaseUI
from employeeUI import EmployeeUI
employeeUI = EmployeeUI()

class SearchUI(BaseUI):
    def employeeSearch(self):
        isValid = False
        while not isValid:
            self.printBaseMenu('Seacrh employee',['[K]ennitala search', '[P]roperty number search'], 'Choose a option:  ')
            userOption, isValid = self.takeInput(['[K]ennitala search', '[P]roperty number search'])


            if userOption.lower() == 'k':
                employeeUI.showEmployee()



    def propertySearch():
        pass





    def workOrderSearch():
        pass

    def workReportSearch():
        pass

    def contractors():
        pass