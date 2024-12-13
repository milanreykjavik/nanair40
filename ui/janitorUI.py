from ui.baseUI import BaseUI
from baseClasses.workOrder import WorkOrder  
from baseClasses.workReport import WorkReport
from logic.logicWrapper import Logic_Wrapper
from ui.searchUI import SearchUI
from ui.validationUI import ValidationUI
from datetime import datetime
from baseClasses.workReport import WorkReport
import os

quitOrBack = ['q', 'b']
validation = ValidationUI()

class JanitorUI(SearchUI):
    def __init__(self, logicWrapper: Logic_Wrapper):
        self.logicWrapper = logicWrapper



    def workOrders(self) -> str:
        '''Work order is created by maintenance staff, either 'q' or 'b' is returned based on whether the user wants to quit or go back'''

        # check repeating work order function checks whether a work report has been created x many days for a reccuring work order
        # if that x days is more than what the work order should be reccuring for then that work order is reset and can be worked on again
        self.logicWrapper.checkRepeatingWorkOrders()

        # ask the user what he want sto fillet the work orders by, either all work orders, or filler by propertie
        filter = self.takeInputAndPrintMenu(['P', 'A'], ('Work orders', ['Property', 'All work orders'], 'Choose what you would like to filter by: '))
        if filter.lower() in quitOrBack:
            return filter.lower()
        
        match filter.lower():
            case 'p':
                property = []
                propertyList = self.logicWrapper.listProperties() # get a list of all properties , this will get printed out in menu
                prompt = 'Enter a property number you would like to see work orders from: ' # standard prompt
                while not property:
                    lookUpProperty = self.showPropertyInfo(propertyList, '', prompt) # prints out all properties and ask the user to choose
                    if lookUpProperty.lower() in quitOrBack:
                        return lookUpProperty.lower()
                    # call the logic wrapper and see if the propertie chosen by the user exists, if not then none is returned
                    property = self.logicWrapper.listProperties(id = lookUpProperty)
                    # change the prompt to a error message in case while loop resets
                    prompt = 'Please enter a property number from the options above\nEnter a property number you would like to see work orders from: '
                currentWorkOrders = self.logicWrapper.listWorkOrders(userID = 0, isCompleted = False, propertyNumber = lookUpProperty)
            case 'a':
                # if user chose to get all work orders then logic wrapper is called to get a list of all work orders
                currentWorkOrders = self.logicWrapper.listWorkOrders(userID = 0, isCompleted = False)





        # get all work orders that an employee has not assigned himslef to.
        body = self.showWorkOrders(currentWorkOrders) # get the table of what should be printed out
        if not body: # if the body is empty that means there are no current work orders, if so we ask the user ot qquit or go back
            return self.takeInputAndPrintMenu(['[Q]uit', '[B]ack'], ("Work Orders", ['There are no current work orders!'], f'Choose a option'))
        
        # work order id list created from all of the work orders logic layer sent
        workOrderIdList = [str(instance.id) for instance in currentWorkOrders] # Get all id's of the current work orders

        userOrderId = ''
        prompt = 'Here you can see all work orders prioratized\nChoose a ID to work on: ' # STANDARD prompt
        while userOrderId not in workOrderIdList: # while loop continues and keeps asking the user for a ID until the user enters a ID that isa available 
            userOrderId = self.takeInputAndPrintMenuWithoutBrackets('', ("Work Orders", body, prompt))
            if userOrderId.lower() in quitOrBack:
                return userOrderId.lower()
            prompt = 'Please choose a ID from the options above\nChoose a ID to work on: ' # changing prompt with error message

        employeeId = ''
        # ask the user what employee he wants to assing the work order to
        lookUpkennitala = self.takeInputAndPrintMenuWithoutBrackets('', ("Work Orders", body, 'Enter a employee kennitala to asign the work order to: '))
        while not employeeId: # while loop continues until user enters a valid kennitala
            if lookUpkennitala.lower() in quitOrBack: # user either quits or goes back
                return lookUpkennitala
            # check whith logic layer if a kennitala exists with the users kennitala, nothing is returned if a employee doesnt exist
            employeeId = self.logicWrapper.listEmployees(kennitala = lookUpkennitala)
            if not employeeId: # if there was nothing returned from logic then the user is asked again
                lookUpkennitala = self.takeInputAndPrintMenuWithoutBrackets('', ("Work Orders", body, 'No employee in the system has this kennitala\nEnter a employee kennitala to asign the work order to: '))

        # assign the employee kennitala to the work order
        self.logicWrapper.editWorkOrder(entry='id', entryValue=int(userOrderId), userID = lookUpkennitala)

        # get a updated list of current work orders to print to the menu screen
        currentWorkOrders = self.logicWrapper.listWorkOrders(userID = 0)
        newBody = self.showWorkOrders(currentWorkOrders) # updated menu screen
        if newBody is None:
            return self.takeInputAndPrintMenuWithoutBrackets(['Quit', 'Back'], ("Work Orders", [''], f'Employee {employeeId[0].name} has succesfully assigned himself to the work order\nChoose a option: '))

        # user is asked to either back or quit
        return self.takeInputAndPrintMenuWithoutBrackets(['Quit', 'Back'], ("Work Orders", newBody, f'Employee {employeeId[0].name} has succesfully assigned himself to the work order\nChoose a option: '))



    def addWorkReport(self) -> str:
        '''Lists all work orders that are not complete and have been signed to a employee, the user is asked for what work report he wants to work, user writes a work report on that work order and then returns'''
        # user asked what he would like to fillter the work orders he can make a report on by
        filter = self.takeInputAndPrintMenu(['P', 'A'], ('Work orders', ['Property', 'All work orders'], 'List work orders that you can create a report on\nChoose what you would like to filter by: '))
        if filter.lower() in quitOrBack: # if user chooses to quit or go back
            return filter.lower()
        match filter.lower():
            case 'p':
                property = []
                # if user choose to fillter by property, the logic layer is called to get a list of all properties in order to print options on screen
                propertyList = self.logicWrapper.listProperties()
                prompt = 'Enter a property number you would like to see work orders from: ' # standard prompt
                while not property:
                    # here the property instances are sprinted out and user can choose what property he wants to filter by
                    lookUpProperty = self.showPropertyInfo(propertyList, '', prompt)
                    if lookUpProperty.lower() in quitOrBack: # user either quits or go back
                        return lookUpProperty.lower()
                    # checked with logic layer if the property entered exists in system, if not the nothing is returned
                    property = self.logicWrapper.listProperties(id = lookUpProperty)
                    # updated prompt with error message
                    prompt = 'Please enter a property number from the options above\nEnter a property number you would like to see work orders from: '
                
                # get a list of instances of work orders that match the property number entered
                currentWorkOrders = self.logicWrapper.listWorkCurrentWorkOrders(isCompleted = False, propertyNumber = lookUpProperty, sentToManager = False)
            case 'a':
                # if user chose a then we get a list of every work order no matter the property
                currentWorkOrders = self.logicWrapper.listWorkCurrentWorkOrders(isCompleted = False, sentToManager = False)





        body = self.showWorkOrders(currentWorkOrders) # call the show work orders function and get a string of all work orders and theit info
        if not body:
            return self.takeInputAndPrintMenuWithoutBrackets(['q', 'b'], ("Create a work report", ['Currently there are no work orders to make a report on!'], 'Choose a option: ')).lower()
        # from the work order the logic layer brought a list is created of all work orders to print and make the user choose from
        availableWorkOrderIds = [str(instance.id) for instance in currentWorkOrders] 


        WorkOrderId = ''
        prompt = 'Choose a Work order to make a report on: ' # standard prompt
        # the user is asked for a work ID until her enters a id that is on of the ids that the logic layer gives
        while WorkOrderId not in availableWorkOrderIds: 
            # ask the user for an id until he enters an id in the list
            WorkOrderId =  self.takeInputAndPrintMenuWithoutBrackets('', ('Create a work report', body, prompt))
            if WorkOrderId.lower() in quitOrBack: # if user enters to quit or go back, we return that
                return WorkOrderId.lower()
            prompt = 'Please pick a work order ID from the options above\nChoose a Work order to make a report on: ' # updated prompt with error message
        
        workOrder = self.logicWrapper.listWorkOrders(id = WorkOrderId) # get all work orders listed to the id from logic layer
        # get the epmloyee that is assigned to the work order to print out on menu screen

        # get the current date to assing to the work report
        employee = self.logicWrapper.listEmployees(kennitala = workOrder[0].userID) 
        now = datetime.now()
        now = now.strftime("%d.%m.%Y")

        # create a dictionary that keeps track of all values to print out and user enters
        workReportDict = {'Work order id': WorkOrderId, 'Empbloyee': employee[0].name, 'date': now, 'Description': '', 'contractor': '---','cost': ''}

        # if the contractor ID is not -1, then this report has a contractor and we have to upadate what we print out on the screen
        if int(workOrder[0].contractorID) != -1:
            contractor = self.logicWrapper.listContractors(id = workOrder[0].contractorID)
            workReportDict['contractor'] = contractor[0].name

        # print the menu and ask the user for a dedscription for the work report
        workReportDict['Description'] = self.getValidInput('Create work report', 'Was the maintenance regular or unexpected, which property was worked on, and what was done?: ', validation.validateText, workReportDict)

        if workReportDict['Description'].lower() in quitOrBack: # user quits or goes back one page
            return workReportDict['Description'].lower()

        # ask the user for a total cost related to the work order
        workReportDict['cost'] = self.getValidInput('Create work report', 'Write the total cost for the work: ', validation.validateNumber, workReportDict, 'Please only enter a number in kr\n') 
        if workReportDict['cost'].lower() in quitOrBack:
            return workReportDict['cost'].lower()
        
        
    
        # create a work report instance that will be sent down to logic layer 
        WorkOrderId = int(WorkOrderId)
        workReportID: int = self.logicWrapper.currentWorkReportID()
        WorkReportInstance = WorkReport(workReportID, WorkOrderId, workReportDict['Description'], int(workOrder[0].contractorID), workOrder[0].userID, now, int(workReportDict['cost']), workOrder[0].propertyNumber)
        
        # add a kr sign to the end, so that it look better when printing out
        workReportDict['cost'] += 'Kr'
        self.logicWrapper.addWorkReport(WorkReportInstance)


        self.logicWrapper.editWorkOrder(entry='id', entryValue=workOrder[0].id, sentToManager = True)
        
        # create a list if strings that will be pirnted out in the body of next menu
        workReportList = [f'{key}: {value}' for key, value in workReportDict.items()]
        return self.takeInputAndPrintMenuWithoutBrackets(['[Q]uit', '[B]ack'], ("Work Orders", workReportList, f'Work report has been created succesfully!\nChoose a option'))


        

        


