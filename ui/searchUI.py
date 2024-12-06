from ui.baseUI import BaseUI
from ui.validationUI import ValidationUI
from logic.logicWrapper import Logic_Wrapper
validation = ValidationUI()


class SearchUI(BaseUI):
    def __init__(self, logicWrapper: Logic_Wrapper):
        self.logicWrapper = logicWrapper

    def employeeSearch(self) -> str | bool:
        options = ['[K]ennitala search', '[L]ocation search']
        userOption = self.takeInputAndPrintMenu(options, ('Employee search', options, 'Choose a option'))


        if userOption.lower() == 'k':
            returnValue = self.showEmployeeID()
        else:
            returnValue = self.showEmployeesLocation()

        return returnValue




    def showEmployeeID(self) -> str | bool:
        # use Search class there is Employee Search class there that can search by any param in this case kennitala
        employee = []
        while not employee:
            lookUpKennitala = self.getValidInput("look for employee","Enter ID: ", validation.validateKennitala)
            match lookUpKennitala.lower():
                case 'q':
                    return 'q' # quit the whole program
                case 'b':
                    return False # Go back one page
    
            employee = self.logicWrapper.listEmployees(kennitala=lookUpKennitala)  # Call the wrapper that is




        employee_list = [f'{key}: {value}' for key, value in list(employee[0].__dict__.items())[1:]]

        return self.takeInputAndPrintMenu(['[Q]'], ('look for employee', employee_list, 'Choose a option: '))




    
    def showEmployeesLocation(self) -> str | bool:
        # use Search class there is Employee Search class there that can search by any param in this case kennitala
        employee_list = []
        while not employee_list:
            lookUpLocation = self.getValidInput("look for employee","Enter Location: ", validation.validateText)
            match lookUpLocation.lower():
                case 'q':
                    return 'q' # quit the whole program
                case 'b':
                    return False # Go back one page
    
            employee_list = self.logicWrapper.listEmployees(location=lookUpLocation)  

        body = []

        # Initialize column names
        headers = ['Name', 'Address', 'Phone number']

        # Calculate the maximum width for each column
        max_name_length = max(len(employee.name) for employee in employee_list)
        max_address_length = max(len(employee.address) for employee in employee_list)
        max_phone_length = max(len(employee.phone) for employee in employee_list)


        # Build the line separator based on the column widths
        line = '+' + '-' * (max_name_length + 2) + '+' + '-' * (max_address_length + 2) + '+' + '-' * (max_phone_length + 2) + '+'

        # Build the header row
        header_row = f"| {headers[0]:<{max_name_length}} | {headers[1]:<{max_address_length}} | {headers[2]:<{max_phone_length}}|"

        # Append the header and line to body
        body.append(line)
        body.append(header_row)
        body.append(line)

        # Build each employee row
        for dict in employee_list:
            line_content = f"| {dict.name:<{max_name_length}} | {dict.address:<{max_address_length}} | {dict.phone:<{max_phone_length}} |"
            body.append(line_content)
            body.append(line)
    
    

        return self.takeInputAndPrintMenu(['[Q]uit', '[B]ack'], (f'List employees for location {lookUpLocation}', body, 'Choose a option'))
    



    def propertySearch(self) -> str | bool:
                # use Search class there is Employee Search class there that can search by any param in this case kennitala
        userOption = self.takeInputAndPrintMenu( ['[L]ocation search', '[P]roperty number search'], ('View property', ['[L]ocation search', '[P]roperty number search'], "Choose a option: "))

        match userOption.lower():
            case 'q':
                return 'q'
            case 'b':
                return False
            case 'l':
                returnValue = self.showPropertyLocationSearch()
            case 'p':
                returnValue =self.showropertyNumberSearch()
            
        if returnValue == 'q':
            return 'q'



        # talk to wrapper with the kennitala entered THIS NEEDS TO GET SORTED :)


    def showPropertyLocationSearch(self) -> str | bool:

        # use Search class there is Employee Search class there that can search by any param in this case kennitala
        propertyList = []
        while not propertyList:
            lookUpLocation = self.getValidInput("look for property","Enter Location: ", validation.validateText)
            match lookUpLocation.lower():
                case 'q':
                    return 'q' # quit the whole program
                case 'b':
                    return False # Go back one page
    
            propertyList = self.logicWrapper.listProperties(location=lookUpLocation)  

        body = []

        # Initialize column names
        headers = ['Property ID', 'address', 'condition',]

        # Calculate the maximum width for each column
        max_id_length = len('Property ID')
        max_address_length = max(len(employee.address) for employee in propertyList)
        max_condition_length = 10


        # Build the line separator based on the column widths
        line = '+' + '-' * (max_id_length + 2) + '+' + '-' * (max_address_length + 2) + '+' + '-' * (max_condition_length + 2) + '+'

        # Build the header row
        header_row = f"| {headers[0]:<{max_id_length}} | {headers[1]:<{max_address_length}} | {headers[2]:<{max_condition_length}} |"

        # Append the header and line to body
        body.append(line)
        body.append(header_row)
        body.append(line)

        # Build each employee row
        for dict in propertyList:
            line_content = f"| {dict.id:<{max_id_length}} | {dict.address:<{max_address_length}} | {dict.condition:<{max_condition_length}} |"
            body.append(line_content)
            body.append(line)
    
    

        return self.takeInputAndPrintMenu(['[Q]uit', '[B]ack'], (f'List properties for location {lookUpLocation}', body, 'Choose a option'))
    





    def showropertyNumberSearch(self) -> str | bool:
        property = []
        while not property:
            lookUpLocation = self.getValidInput("look for property","Enter property number: ", validation.validateText)
            match lookUpLocation.lower():
                case 'q':
                    return 'q' # quit the whole program
                case 'b':
                    return False # Go back one page
    
            property = self.logicWrapper.listProperties(id = lookUpLocation)  

        propertyList = [f'{key}: {value}' for key, value in list(property[0].__dict__.items())]

        return self.takeInputAndPrintMenu(['[Q]'], ('look for property', propertyList, 'Choose a option: '))







    def workOrderSearch(self) -> str | bool:
        options = ['[I]D search', '[P]roperty number search', '[K]ennitala search']
        userOption = self.takeInputAndPrintMenu(options, ('Search work order', options, 'Choose a option:  '))
        work_orders = []

        match userOption.lower():
            case 'i':
                userId = self.takeInputAndPrintMenu([], ('Search Work orders','', 'Enter a work order ID: '))
                workOrdersInfo = self.logicWrapper.searchWorkOrders(workOrderId = userId)
            case 'p':
                propertyNumber = self.takeInputAndPrintMenu([], ('Search Work orders','', 'Enter a property Number: '))
                workOrdersInfo = self.logicWrapper.searchWorkOrders(properyNum = propertyNumber)
            case 'k':
                kennitala = self.takeInputAndPrintMenu([], ('Search Work orders','', 'Enter a kennital: '))
                workOrdersInfo = self.logicWrapper.searchWorkOrders(Kennitala = kennitala)
            
                

    def workReportSearch(self) -> str | bool:
        options = ['[I]D search', '[P]roperty number search', '[K]ennitala search']
        userOption = self.takeInputAndPrintMenu(options, ('Search work report', options, 'Choose a option:  '))
        work_orders = []

        match userOption.lower():
            case 'i':
                userId = self.takeInputAndPrintMenu([], ('Search Work reports','', 'Enter a work order ID: '))
                workOrdersInfo = self.logicWrapper.searchWorkReports(workOrderId = userId)
            case 'p':
                propertyNumber = self.takeInputAndPrintMenu([], ('Search Work reports','', 'Enter a property Number: '))
                workOrdersInfo = self.logicWrapper.searchWorkReports(properyNum = propertyNumber)
            case 'k':
                kennitala = self.takeInputAndPrintMenu([], ('Search Work reports','', 'Enter a kennital: '))
                workOrdersInfo = self.logicWrapper.searchWorkReports(Kennitala = kennitala)
    



  

    def workReportSearch(self) -> str | bool:
        pass

    def showContractorsInfo(self) -> str | bool:
        contractors = self.logicWrapper.listContractors()

        body = []

        # Initialize column names
        headers = ['Company name', 'Phone', 'Hours', 'Location', 'id']

        # Calculate the maximum width for each column
        max_name_length = max(len(contractor.name) for contractor in contractors)
        max_phone_length = 7
        max_openingHours_length = 5
        max_location_length = 12
        max_id_length = 5



        # Build the line separator based on the column widths
        line = '+' + '-' * (max_name_length + 2) + '+' + '-' * (max_phone_length + 2) + '+' + '-' * (max_openingHours_length + 2) + '+' + '-' * (max_location_length) + '+' + '-' * (max_id_length) + '--+'

        # Build the header row
        header_row = f"| {headers[0]:<{max_name_length}} | {headers[1]:<{max_phone_length}} | {headers[2]:<{max_openingHours_length}} | {headers[3]:<{max_location_length - 2}} | {headers[4]:<{max_id_length}} |"

        # Append the header and line to body
        body.append(line)
        body.append(header_row)
        body.append(line)

        # Build each employee row
        for instance in contractors:
            line_content = f"| {instance.name:<{max_name_length}} | {instance.phone:<{max_phone_length}} | {instance.openingHours:<{max_openingHours_length}} | {instance.location:<{max_location_length - 2}} | {instance.id:<{max_id_length}} |"
            body.append(line_content)
            body.append(line)
    
    

        return self.takeInputAndPrintMenu(['[Q]uit', '[B]ack'], (f'List contractors', body, 'Choose a option'))


 




    def getValidInput(self, name, prompt, validationFunc, userDict: dict = {}) -> str | bool:
        '''Validates the input based on the validation function given, prints baseMenu every time the user enters unvalid info. menu is based on the arguments given '''
        while True:
            self.printBaseMenu(name, [f'{key}: {value}' for key, value in userDict.items()], prompt)
            user_input = input(' ')
        
            if validationFunc(user_input):
                return user_input
