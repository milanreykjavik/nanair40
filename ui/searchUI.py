from ui.baseUI import BaseUI
from ui.validationUI import ValidationUI
from logic.logicWrapper import Logic_Wrapper
from baseClasses.workOrder import WorkOrder
from baseClasses.Employee import Employee
from baseClasses.Property import Property
from baseClasses.workReport import WorkReport
from baseClasses.Contractor import Contractor
validation = ValidationUI()
quitOrback = ['q', 'b', 'Q', 'B']




class SearchUI(BaseUI):
    def __init__(self, logicWrapper: Logic_Wrapper = None):
        self.logicWrapper = logicWrapper

    def employeeSearch(self) -> str:
        '''Prints menu with with options can choose form, user can either look up employee by kennitala or by location'''
        # the options the user can chose from
        options = ['Kennitala search', 'Location search']

        while True: # while loop continues until user picks either option
            # Print menu and ask the user to pick a option from options
            userOption = self.takeInputAndPrintMenu(options, ('Employee search', options, 'Choose a option: '))
            if userOption.lower() in quitOrback:
                return userOption.lower() # user either quits or goes back one page
            match userOption.lower():
                case 'k':
                    # if user chose to search for employee by kennitala then he is sent to that function
                    returnValue = self.showEmployeeID()
                case 'l':
                    employee_list = []
                    locations = self.logicWrapper.listLocations() # Get all locations by calling the logic layer
                    locationsList = [location.airport for location in locations] # get all locations into a list that will be printed out
                    prompt = 'Enter a location: ' # standard prompt
                    while not employee_list:
                        # ask the user for a location and printing all options, then checking if that location exists with logic layer
                        lookUpLocation = self.takeInputAndPrintMenuWithoutBrackets("", ('Employee search by location', locationsList, prompt)).capitalize()
                        if lookUpLocation in quitOrback:
                            return lookUpLocation.lower() # user quits ore goes back one page
                        employee_list = self.logicWrapper.listEmployees(location=lookUpLocation)  # logic layer returns nothing if location doesnt exist
                        prompt = 'Please choose a option from the given set of locations above\nPlease try again: ' # prompt changed to include a error message
                    returnValue = self.showEmployeesInfo(employee_list)
                    
            if returnValue == 'q':
                return 'q'

                    

    

    def showEmployeeID(self) -> str | bool:
        # use Search class there is Employee Search class there that can search by any param in this case kennitala
        employee = []
        prompt = 'Enter a kennitala: ' # standard prompt
        while not employee:
            # ask the user for a kennitala he wants to look up and print menu
            lookUpKennitala = self.getValidInput("look for employee",prompt, validation.validateKennitala)
            if lookUpKennitala.lower() in quitOrback:
                return lookUpKennitala.lower() # user quits or goes back one page
            # call logic layer to check if kennitala user enterd exists, if not the nothing is returned
            employee = self.logicWrapper.listEmployees(kennitala=lookUpKennitala)  
            prompt = 'This kennitala doesnt exist in the system\nPlease try again: ' # prompt changed to include a error message

        employee_list = [f'{key}: {value}' for key, value in list(employee[0].__dict__.items())[1:]] # create a list of all values to print out

        return self.takeInputAndPrintMenuWithoutBrackets(['[Q]uit', '[B]ack'], (f'List employees', employee_list, 'Choose a option: '))


    def showEmployeesInfo(self, employee_list: list[Employee]) -> str:
        '''Creates and prints a table of all employes that are passed into as argument'''
        if not employee_list: # if there are no employees in the list passed in then there is no table to be printed
            return self.takeInputAndPrintMenu(['[Q]uit', '[B]ack'], (f'List employees', '', 'No employees registered\nChoose a option: '))

        body = [] # body used to keep track of the values in the table
        headers = ['Name', 'Location', 'Phone number'] # headers in the table

        
        # calculate how each section of the table needs to be
        max_name_length = max(len(employee.name) for employee in employee_list)
        max_location_length = 12
        max_phone_length = 12


        # line is built with the max length variables
        line = '+' + '-' * (max_name_length + 2) + '+' + '-' * (max_location_length + 2) + '+' + '-' * (max_phone_length + 2) + '+'

        # header row 
        header_row = f"| {headers[0]:<{max_name_length}} | {headers[1]:<{max_location_length}} | {headers[2]:<{max_phone_length}} |"

        # first few lines of the table are created before the information is put into the table
        body.append(line)
        body.append(header_row)
        body.append(line)

        # looping through each instance and adding their values to the table
        for dict in employee_list:
            line_content = f"| {dict.name:<{max_name_length}} | {dict.location:<{max_location_length}} | {dict.phone:<{max_phone_length}} |"
            body.append(line_content)
            body.append(line)
    
    
        # prints the body that was created and user can either quit or back
        return self.takeInputAndPrintMenuWithoutBrackets(['[Q]uit', '[B]ack'], (f'List employees', body, 'Choose a option: '))
    



    def propertySearch(self) -> str:
        '''User can choose to search property by location or by property number'''
        
        # prints menu and asks user to either search property by location or property number
        userOption = self.takeInputAndPrintMenu( ['Location search', 'Property number search'], ('View property', ['Location search', 'Property number search'], "Choose a option: "))
        if userOption.lower() in quitOrback:
            return userOption.lower() # user quits or goes back one page
        
        match userOption.lower():
            case 'l':
                propertyList = []
                # get all location instances by calling logic layer to list them all
                locations = self.logicWrapper.listLocations()
                prompt = 'Pick a location from the given options: ' # standard prompt
                locationList = [location.airport for location in locations] # create a list of all destination to be printed out
                while not propertyList:
                    # ask the user for a location he wants to look up and print menu
                    lookUpLocation = self.takeInputAndPrintMenuWithoutBrackets('', ('Look up property by location', locationList, prompt)).capitalize()
                    if lookUpLocation.lower() in quitOrback:
                        return lookUpLocation.lower() # user quits or goes back one page
                    self.showPropertyInfo(self.logicWrapper.listProperties(location=lookUpLocation))
            case 'p':
                # user chooses to search for a property by property number
                returnValue = self.showropertyNumberSearch()
            
        if returnValue == 'q':
            return 'q'


    def showPropertyInfo(self, propertyList: list[Property], options: str = ['[Q]uit', '[B]ack'], prompt: str = 'Choose a option: ') -> str:
        if not propertyList: # if there are no instances passed into the function then the user can either quit or go back and no table is printed
            return self.takeInputAndPrintMenu(['[Q]uit', '[B]ack'], (f'List properties', '', 'No properties registered\nChoose a option: '))

        body = [] ## body keeps track of the table continents
        headers = ['Property ID', 'address', 'condition', 'Location'] # headers of out table


        try: # find the maximum length that each section of the table
            max_id_length = len('Property ID')
            max_address_length = max(len(employee.address) for employee in propertyList)
            max_address_length = max(len('address'), max_address_length)
            max_condition_length = 10
            max_location_length = 13
        except ValueError:
            return None


        # line if the table, size is determained by the max length variables
        line = '+' + '-' * (max_id_length + 2) + '+' + '-' * (max_address_length + 2) + '+' + '-' * (max_condition_length + 2) + '+' + '-' * (max_location_length + 2) + '+'

        # header row
        header_row = f"| {headers[0]:<{max_id_length}} | {headers[1]:<{max_address_length}} | {headers[2]:<{max_condition_length}} | {headers[3]:<{max_location_length}} |"

        # first few lines of the table made
        body.append(line)
        body.append(header_row)
        body.append(line)

        # loop though each and every isntance and putting their values in each row
        for dict in propertyList:
            line_content = f"| {dict.id:<{max_id_length}} | {dict.address:<{max_address_length}} | {dict.condition:<{max_condition_length}} | {dict.location:<{max_condition_length}}    |"
            body.append(line_content)
            body.append(line)

        # user can either quit or go back
        return self.takeInputAndPrintMenuWithoutBrackets(options, (f'List properties', body, prompt))
    

    def showropertyNumberSearch(self) -> str:
        '''User aksed for a property number where the system then prints out information about that property number, 'q' or 'b' is returned based on whether user quits or goes back'''
        property = []
        prompt = "Enter property number: " # defult prompt
        while not property:
            # ask the user for a location, print menu and validate the text
            lookUpLocation = self.getValidInput("look for property",prompt, validation.validateText)
            if lookUpLocation.lower() in quitOrback:
                return lookUpLocation.lower() # user either quits or goes one page back
            # send location to logic layer where its then checked whether this property num exists, if not nothing is returned
            property = self.logicWrapper.listProperties(id = lookUpLocation)  
            prompt = 'There is no property number assigned to the property you entered\nPlease try again: ' # updated prompt with error message
        propertyInstance = property[0] 
        # list created with each value, this list is used to print out the information in next menu
        valueList = [f'Property number: {propertyInstance.id}', f'Location: {propertyInstance.location}',f'Address: {propertyInstance.address}', f'Condition: {propertyInstance.condition}',
                     f'Facilities requiring maintenance: {propertyInstance.facilitiesMaintenance}', f'Room count: {len(propertyInstance.rooms)}', f'Facility count: {len(propertyInstance.facilities)}']
    
        # menu printed out and asked the user to either quit or go back
        return self.takeInputAndPrintMenuWithoutBrackets(['[Q]uit', '[B]ack'], ('look for property', valueList, 'Choose a option: '))




    def workOrderSearch(self) -> str:
        '''User asked for few options based on how he wants to search for a work order, 'q' or 'b' is returned based whether the user quits or goes back one page'''
        # options the user can choose from when the menu is printed
        options = ['ID search', 'Property number search', 'Kennitala search', 'Specific Date']

        # print the menu and make the user choose from the options available
        userOption = self.takeInputAndPrintMenu(options, ('Search work order', options, 'Choose a option: '))
        if userOption.lower() in quitOrback:
            return userOption.lower() # user either quits or goes one page back


        match userOption.lower():
            case 'i':
                # user chose to search by id
                workOrderID = None
                prompt = 'Choose a work order ID: ' # base prompt

                while not workOrderID:
                    # user asked for a work order id of the work report he would like to see information about
                    lookUpid = self.takeInputAndPrintMenuWithoutBrackets('', ('Search work order', ['Enter the ID of the work report you are looking for'], prompt, ''))
                    if lookUpid.lower() in quitOrback:
                        return lookUpid.lower() # user either quits or goes one page back
                    
                    # the id the user checked in is sent to logic layer where its checked if it exists, if it doesnt then none is returned
                    workOrders = self.logicWrapper.listWorkOrders(id = lookUpid)
                    workOrderID = self.showWorkOrders(workOrders)
                    prompt = 'No work order exists with that ID\nPlease try again:  ' # prompt changed, includes a error message now
                workOrders = self.logicWrapper.listWorkOrders(id = lookUpid)  
                body = self.showWorkOrders(workOrders) # showWorkorders is called, where a body(information about the work order) is returned
            case 'p':
                # user choose to search by property number
                propertiesWorkOrders = ''
                prompt = 'Enter a property number: ' # base prompt
                while not propertiesWorkOrders:
                    # ask the user for a property number and printing menu
                    lookUpPropertyNumber = self.takeInputAndPrintMenu([], ('Search Work orders','', prompt))

                    if lookUpPropertyNumber.lower() in quitOrback:
                        return lookUpPropertyNumber.lower() # user either quits or goes back one page
                    # checked with logic layer whether work orders exist for the property number user entered, 
                    workOrders = self.logicWrapper.listWorkOrders(propertyNumber = lookUpPropertyNumber)
                    propertiesWorkOrders = self.showWorkOrders(workOrders) # property work order return none if there is nothing to print
                    prompt = 'No work orders have been assinged to this property number\nEnter a property number: ' # prompt changed to include a error message
                workOrders = self.logicWrapper.listWorkOrders(propertyNumber = lookUpPropertyNumber)  
                body = self.showWorkOrders(workOrders)    # get a list of all workorders that will be printed

            case 'k':
                KennitalaWorkOrders = None
                prompt = 'Enter a kennitala: ' # base prompt
                while not KennitalaWorkOrders:
                    # ask the user for a kennitala to look up
                    lookUpKennitala = self.takeInputAndPrintMenu([], ('Search Work orders','', prompt))
                    if lookUpKennitala.lower() in quitOrback:
                        return lookUpKennitala.lower() # user quits or goes back one page
                    # cal logig layer to get every kennitala that matches the kennitala the user entered
                    KennitalaWorkOrders = self.logicWrapper.listWorkOrders(userID = lookUpKennitala)
                    body = self.showWorkOrders(KennitalaWorkOrders) # body gets created, this body will then be printed
                    prompt = 'No employee with this kennitala has assigned a work order\nEnter a kennitala: ' # new prompt with error message
            case 's':
                # ask the user for a specific data, and validate the date
                specificDate = self.getValidInput('Search work orders by a specific date', 'Enter a specifc date (DD.MM.YYYY)', validation.validate_date, {},  'Invalid date, please follow the given format\n')
                if specificDate.lower() in quitOrback:
                    return specificDate.lower() # user goes back or quits
                specificDateWorkOrders = self.logicWrapper.listByDateRangeWorkOrders(specificDate, None)
                body = self.showWorkOrders(specificDateWorkOrders) # get the body that will be printed out based on the date
               
        # if the body is none then there is nno body to print
        if body is None:
            return self.takeInputAndPrintMenuWithoutBrackets(['[Q]uit', '[B]ack'], ('Search work order', ['No work orders were found'], 'Choose a option: ' ,''))

        # menu printed with the body that was got above, user can  either quit or go one page back
        return self.takeInputAndPrintMenuWithoutBrackets(['[Q]uit', '[B]ack'], ('Search work order', body, 'Choose a option: ' ,''))
            
    
    def showWorkOrders(self, workOrders: list[WorkOrder]) -> str:
        '''returns a body of all work orders that where passed in as argument'''
        if not workOrders: # if there are no work orders to be printed then none is returned
            return None

        body = []
        now = []
        asap = []
        emergency = []
        for instance in workOrders: # looping through every current work order
            propertyForWorkOrder = self.logicWrapper.listProperties(id = instance.propertyNumber)
            txt = ''
            txt += f'WORK ORDER #{instance.id}, Location {propertyForWorkOrder[0].location}\n'
            txt += f'       Priority: {instance.priority}\n'
            txt += f'       Description: {instance.description}\n'
            txt += f'       Property Number: {instance.propertyNumber}\n'
            if int(instance.contractorID) > -1:
                contractor = self.logicWrapper.listContractors(id = instance.contractorID)
                txt += f'       Contractor: {contractor[0].name}\n'
            else:
                txt += f'       Contractor: No contractor is assigned to this work order\n'
            if int(instance.userID) != 0:
                Employee = self.logicWrapper.listEmployees(kennitala = instance.userID)
                txt += f'       Employee: {Employee[0].name}\n'
            txt += f'       Room/facility: {instance.roomFacilityId}\n'
            txt += f'       Status:{' Not completed' if not instance.isCompleted else ' Completed'}\n\n'

            if instance.priority.lower() == 'now': # add to the priority dict that matches the description
                now.append(txt)
            elif instance.priority.lower() == 'emergency': # add to the priority dict that matches the description
                emergency.append(txt)
            else:
                asap.append(txt)
        
        # the asap, now and emergency dict are then added to the body list in the order of this order
        # this is done ensure that the body is then printed with the work orders in a prioratized order
        body.extend(now) 
        body.extend(asap)
        body.extend(emergency)
 
        return body



    def workReportSearch(self) -> str:
        '''Ask the user to search for a work report, search by property, kennitala or by date range, 'b' or 'q' is either returned based on whethet the user quits or goes one page back'''
        # ask the user what he wants to search work reports by, either by property number, employee or date range
        userSelection = self.takeInputAndPrintMenu(['Property search', 'Employee search' , 'Date range search'], ('Search work reports', ['Property search', 'Employee search', 'Date range search'], 'Choose a option: '))
        
        if userSelection.lower() in quitOrback:
            return userSelection.lower() # user quits or goes one page back
        
        match userSelection.lower():
            case 'p':
                # user choose to search for work reports by property
                propertiesWorkReports = None
                prompt = 'Enter a property number: ' # base prompt
                while not propertiesWorkReports:
                    # Menu printed and user asked to enter a property number
                    lookUpPropertyNumber = self.takeInputAndPrintMenu([], ('Search Work reports','', prompt))

                    if lookUpPropertyNumber.lower() in quitOrback:
                        return lookUpPropertyNumber.lower() # user quits or goes one page back
                    # check whith logic wrapper whether a work report exists for the property number eneterd, if not then nothing is returned
                    workReports = self.logicWrapper.listWorkReports(propertyNumber = lookUpPropertyNumber)
                    propertiesWorkReports = self.showWorkReports(workReports) # None is returned if there are now work reports to show
                    prompt = 'No work reports have been assinged to this property number\nEnter a property number: ' # new prompt with additional error message
                # get the work report with the property number the user entered by calling the logic layer
                workOrders = self.logicWrapper.listWorkReports(propertyNumber = lookUpPropertyNumber)  
                body = self.showWorkReports(workOrders) # body that will be printed out gets created

            case 'e':
                # user chose to search bt kennitala/employee
                KennitalaWorkReports = None
                prompt = 'Enter a kennitala: '
                while not KennitalaWorkReports:
                    # user asked for a kennitala that he wants to search work reports for
                    lookUpKennitala = self.takeInputAndPrintMenu([], ('Search Work reports','', prompt))

                    if lookUpKennitala.lower() in quitOrback:
                        return lookUpKennitala.lower() # user either quits or goes back one page
                    
                    # get all work reports that have the kennitala the user entered assinged to them, if there are none then nothing is returned
                    KennitalaWorkReports = self.logicWrapper.listWorkReports(employeeID = lookUpKennitala)
                    body = self.showWorkReports(KennitalaWorkReports) # call the show work reports function that returns a body that will be printed
                    prompt = 'No employee with this kennitala has assigned a work report\nEnter a kennitala: ' # new prompt that includes a error message 
            case 'd':
            
                # ask the user for a starting date range, this date is validated
                startingDate = self.getValidInput('Search work reports', 'Choose a starting date(DD.MM.YYYY)', validation.validate_date, {}, 'Invalid date, please follow the given format\n')

                if startingDate.lower() in quitOrback:
                    return startingDate.lower() # user quits or goes one page back
                
                # ask the user fro a end date, this date is validated
                endDate = self.getValidInput('Search work reports', 'Choose a ending date(DD.MM.YYYY)', validation.validate_date, {}, 'Invalid date, please follow the given format\n')

                if endDate.lower() in quitOrback:
                    return endDate.lower() # user quits or goes one page back

                # call logic layer to lists all dates that match the date range
                workReports = self.logicWrapper.listByDateRange(start=startingDate, end=endDate)
                body = self.showWorkReports(workReports)

        if not body:
            return self.takeInputAndPrintMenuWithoutBrackets([], ('Search work reports', ['No work reports were found'], 'Choose a option: '))

        return self.takeInputAndPrintMenuWithoutBrackets([], ('Search work reports', body, 'Choose a option: '))

    def showWorkReports(self, workReports: list[WorkReport]) -> str:
        if not workReports:
            return None
        
        body = []
        for workreport in workReports:
            body.append(f'ID: {workreport.id}')
            body.append(f'Work order ID: {workreport.workOrderID}')
            body.append(f'description:  {workreport.description}')
            if int(workreport.contractorID) != -1:
                contractor = self.logicWrapper.listContractors(id = int(workreport.contractorID))
                body.append(f'Contractor:  {contractor[0].name}')
            else:
                body.append(f'Contractor: No contractor is assigned to this work report')
            employee = self.logicWrapper.listEmployees(kennitala = workreport.employeeID)
            body.append(f'Employee:  {employee[0].name}')
            body.append(f'Date: {workreport.date}')
            body.append(f'Total cost:  {workreport.cost}kr')
            body.append(f'Manager comment:  {workreport.comment if workreport.comment else 'No comment has been written'}\n\n')
        

        return body
            





    def showContractorsInfo(self, contractorsList: (list[Contractor]),options = 'choose a option: ', userOption = ['[Q]uit', '[B]ack']) -> str | bool:
        if not contractorsList:
            return self.takeInputAndPrintMenu(['[Q]uit', '[B]ack'], (f'List contractors', '', 'No contractors registered\nChoose a option: '))

        contractors = self.logicWrapper.listContractors()
        body = []

        # Initialize column names
        headers = ['Company name', 'Phone', 'Hours', 'Location', 'id']

        # Calculate the maximum width for each column
        max_name_length = max(len(contractor.name) for contractor in contractors)
        max_name_length = max(max_name_length, len('Company name'))

        max_phone_length = max(len(contractor.phone) for contractor in contractors)
        max_openingHours_length = max(len(contractor.openingHours) for contractor in contractors)
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
    
    

        return self.takeInputAndPrintMenuWithoutBrackets(userOption, (f'List contractors', body, options))
