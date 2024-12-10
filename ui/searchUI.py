from ui.baseUI import BaseUI
from ui.validationUI import ValidationUI
from logic.logicWrapper import Logic_Wrapper
from baseClasses.workOrder import WorkOrder
from baseClasses.Employee import Employee
from baseClasses.Property import Property
validation = ValidationUI()
quitOrback = ['q', 'b']


class SearchUI(BaseUI):
    def __init__(self, logicWrapper: Logic_Wrapper = None):
        self.logicWrapper = logicWrapper

    def employeeSearch(self) -> str | bool:
        options = ['[K]ennitala search', '[L]ocation search']
        userOption = self.takeInputAndPrintMenu(options, ('Employee search', options, 'Choose a option'))


        if userOption.lower() == 'k':
            returnValue = self.showEmployeeID()
        else:
            employee_list = []
            lookUpLocation = self.getValidInput("look for employee","Enter Location: ", validation.validateText).capitalize()
            while not employee_list:
                if lookUpLocation.lower() in quitOrback:
                    return lookUpLocation.lower()
                employee_list = self.logicWrapper.listEmployees(location=lookUpLocation)  
                if not employee_list:
                    lookUpLocation = self.getValidInput("look for employee","The location you entered doesn't exist\nEnter Location: ", validation.validateText).capitalize()
            returnValue = self.showEmployeesInfo(employee_list)

        return returnValue

    def showEmployeeID(self) -> str | bool:
        # use Search class there is Employee Search class there that can search by any param in this case kennitala
        employee = []
        lookUpKennitala = self.getValidInput("look for employee","Enter ID: ", validation.validateKennitala)
        while not employee:
            if lookUpKennitala.lower() in quitOrback:
                return lookUpKennitala.lower()
            employee = self.logicWrapper.listEmployees(kennitala=lookUpKennitala)  # Call the wrapper that is
            if not employee:
                lookUpKennitala = self.getValidInput("look for employee","There is no employee assigned to that kennitala\nEnter ID: ", validation.validateKennitala)

        employee_list = [f'{key}: {value}' for key, value in list(employee[0].__dict__.items())[1:]]

        return self.takeInputAndPrintMenu(['[Q]'], ('look for employee', employee_list, 'Choose a option: '))

    def showEmployeesInfo(self, employee_list: list[Employee]) -> str:
        if not employee_list:
            return self.takeInputAndPrintMenu(['[Q]uit', '[B]ack'], (f'List employees', '', 'No employees registered to this location\nChoose a option: '))

        body = []

        # Initialize column names
        headers = ['Name', 'Location', 'Phone number']

        # Calculate the maximum width for each column

        max_name_length = max(len(employee.name) for employee in employee_list)
        max_location_length = 12
        max_phone_length = 12


        # Build the line separator based on the column widths
        line = '+' + '-' * (max_name_length + 2) + '+' + '-' * (max_location_length + 2) + '+' + '-' * (max_phone_length + 2) + '+'

        # Build the header row
        header_row = f"| {headers[0]:<{max_name_length}} | {headers[1]:<{max_location_length}} | {headers[2]:<{max_phone_length}} |"

        # Append the header and line to body
        body.append(line)
        body.append(header_row)
        body.append(line)

        # Build each employee row
        for dict in employee_list:
            line_content = f"| {dict.name:<{max_name_length}} | {dict.location:<{max_location_length}} | {dict.phone:<{max_phone_length}} |"
            body.append(line_content)
            body.append(line)
    
    

        return self.takeInputAndPrintMenu(['[Q]uit', '[B]ack'], (f'List employees', body, 'Choose a option: '))
    



    def propertySearch(self) -> str:
                # use Search class there is Employee Search class there that can search by any param in this case kennitala
        userOption = self.takeInputAndPrintMenu( ['[L]ocation search', '[P]roperty number search'], ('View property', ['[L]ocation search', '[P]roperty number search'], "Choose a option: "))
        if userOption.lower() in quitOrback:
            return userOption.lower()
        match userOption.lower():
            case 'l':
                propertyList = []
                while not propertyList:
                    lookUpLocation = self.getValidInput("look for property","Enter Location: ", validation.validateText)
                    match lookUpLocation.lower():
                        case 'q':
                            return 'q' # quit the whole program
                        case 'b':
                            return False # Go back one page
                    self.showPropertyInfo(self.logicWrapper.listProperties(location=lookUpLocation))
            case 'p':
                returnValue = self.showropertyNumberSearch()
            
        if returnValue == 'q':
            return 'q'


    def showPropertyInfo(self, propertyList: list[Property]) -> str:

        # use Search class there is Employee Search class there that can search by any param in this case kennitala

        body = []

        # Initialize column names
        headers = ['Property ID', 'address', 'condition', 'Location']

        # Calculate the maximum width for each column
        max_id_length = len('Property ID')
        max_address_length = max(len(employee.address) for employee in propertyList)
        max_condition_length = 10
        max_location_length = 13


        # Build the line separator based on the column widths
        line = '+' + '-' * (max_id_length + 2) + '+' + '-' * (max_address_length + 2) + '+' + '-' * (max_condition_length + 2) + '+' + '-' * (max_location_length + 2) + '+'

        # Build the header row
        header_row = f"| {headers[0]:<{max_id_length}} | {headers[1]:<{max_address_length}} | {headers[2]:<{max_condition_length}} | {headers[3]:<{max_location_length}} |"

        # Append the header and line to body
        body.append(line)
        body.append(header_row)
        body.append(line)

        # Build each employee row
        for dict in propertyList:
            line_content = f"| {dict.id:<{max_id_length}} | {dict.address:<{max_address_length}} | {dict.condition:<{max_condition_length}} | {dict.location:<{max_condition_length}}    |"
            body.append(line_content)
            body.append(line)


        return self.takeInputAndPrintMenu(['[Q]uit', '[B]ack'], (f'List properties', body, 'Choose a option'))
    

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

        propertyList = [f'{key}: {value}' for key, value in list(property[0].__dict__.items())[:-2]]

        return self.takeInputAndPrintMenu(['[Q]uit', '[B]ack'], ('look for property', propertyList, 'Choose a option: '))




    def workOrderSearch(self) -> str | bool:
        options = ['[I]D search', '[P]roperty number search', '[K]ennitala search']
        userOption = self.takeInputAndPrintMenu(options, ('Search work order', options, 'Choose a option:  '))
        work_orders = []

        match userOption.lower():
            case 'i':
                lookUpid = self.takeInputAndPrintMenu('', ('Search work order', ['Enter the ID of the work report you are looking for'], 'Choose a ID:  ', ''))
                workOrderID = None
                while not workOrderID:
                    workOrders = self.logicWrapper.listWorkOrders(id = lookUpid)
                    workOrderID = self.showWorkOrders(workOrders)
                    if workOrderID is None:
                        lookUpid = self.takeInputAndPrintMenu('', ('Search work order', ['No work orders exist for that ID!'], 'Choose a ID: ' ,''))
                return self.takeInputAndPrintMenu(['[Q]uit', '[B]ack'], ('Search work order', workOrderID, 'Choose a option: ' ,''))
            case 'p':
                lookUpPropertyNumber = self.takeInputAndPrintMenu([], ('Search Work orders','', 'Enter a property Number: '))
                propertiesWorkOrders = ''
                while not propertiesWorkOrders:
                    workOrders = self.logicWrapper.listWorkOrders(propertyNumber = lookUpPropertyNumber)
                    propertiesWorkOrders = self.showWorkOrders(workOrders)
                    if not propertiesWorkOrders:
                        lookUpPropertyNumber = self.takeInputAndPrintMenu([], ('Search Work orders',['No property with this ID'], 'Enter a property Number: '))
                return self.takeInputAndPrintMenu(['[Q]uit', '[B]ack'], ('Search work order', workOrderID, 'Choose a option: ' ,''))

                

            case 'k':
                kennitala = self.getValidInput('Search work orders', 'Enter a kennitala', validation.validateKennitala)
                workOrdersInfo = self.logicWrapper.listWorkOrders(employeeID = kennitala)
            
    
    def showWorkOrders(self, workOrders: list[WorkOrder]) -> str:

        if not workOrders:
            return None

        body = []
        for instance in workOrders: # looping through every current work order
            propertyForWorkOrder = self.logicWrapper.listProperties(id = instance.propertyNumber)
            
            body.append(f'WORK ORDER #{instance.id}, Location {propertyForWorkOrder[0].location}')
            body.append(f'Priority: {instance.priority}')
            body.append(f'Description: {instance.description}')
            body.append(f'Property Number: {instance.propertyNumber}')
            if int(instance.contractorID) > -1:
                contractor = self.logicWrapper.listContractors(id = instance.contractorID)
                body.append(f'Contractor: {contractor[0].name}')
            else:
                body.append(f'Contractor: No contractor is assigned to this work order')
            if int(instance.userID) != 0:
                Employee = self.logicWrapper.listEmployees(kennitala = instance.userID)
                body.append(f'Employee: {Employee[0].name}')
            body.append(f'Room/facility: {instance.roomFacilityId}')
            body.append(f'Status:{ 'Not completed' if not instance.isCompleted else ' Completed'}\n\n')

 
        return body





    def workReportSearch(self) -> str:
        pass











    def showContractorsInfo(self, options = 'choose a option', userOption = ['[Q]uit', '[B]ack']) -> str | bool:
        contractors = self.logicWrapper.listContractors()

        body = []

        # Initialize column names
        headers = ['Company name', 'Phone', 'Hours', 'Location', 'id']

        # Calculate the maximum width for each column
        max_name_length = max(len(contractor.name) for contractor in contractors)
        max_phone_length = 7
        max_openingHours_length = 5
        max_location_length = 14
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
    
    

        return self.takeInputAndPrintMenu(userOption, (f'List contractors', body, options))


 


