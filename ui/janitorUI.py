from ui.baseUI import BaseUI
from baseClasses.workOrder import WorkOrder  
from baseClasses.workReport import WorkReport
from logic.logicWrapper import Logic_Wrapper
from ui.searchUI import SearchUI
import os
quitOrBack = ['q', 'b']

class JanitorUI(SearchUI):
    def __init__(self, logicWrapper: Logic_Wrapper):
        self.logicWrapper = logicWrapper



    def workOrders(self):
        currentWorkOrders = self.logicWrapper.listWorkOrders(userID = 0, isCompleted = False) # get all work orders that an employee has not assigned himslef to.
        body = self.showWorkOrders(currentWorkOrders) # get the table of what should be printed out
        if not body: # if the body is empty that means there are no current work orders, if so we ask the user ot qquit or go back
            return self.takeInputAndPrintMenu(['[Q]uit', '[B]ack'], ("Work Orders", ['There are no current work orders!'], f'Choose a option'))
        
        workOrderIdList = [str(instance.id) for instance in currentWorkOrders] # Get all id's of the current work orders

        userOrderId = ''
        while userOrderId not in workOrderIdList: # while loop continues and keeps asking the user for a ID until the user enters a ID that isa available 
            userOrderId = self.takeInputAndPrintMenu('', ("Work Orders", body, 'Choose a ID to work on: '))
            if userOrderId.lower() in quitOrBack:
                return userOrderId

        employeeId = ''
        while not employeeId:
            lookUpkennitala = self.takeInputAndPrintMenu('', ("Work Orders", body, 'Enter a employee kennitala to asign the work order to: '))
            if lookUpkennitala.lower() in quitOrBack:
                return lookUpkennitala
            employeeId = self.logicWrapper.listEmployees(kennitala = lookUpkennitala)

        self.logicWrapper.editWorkOrder('id', int(userOrderId), userID = lookUpkennitala)

        currentWorkOrders = self.logicWrapper.listWorkOrders(userID = 0)
        newBody = self.showWorkOrders(currentWorkOrders)
        if newBody is None:
            return self.takeInputAndPrintMenu(['[Q]uit', '[B]ack'], ("Work Orders", [''], f'Employee {employeeId[0].name} has succesfully assigned himself to the work order\nChoose a option: '))

        return self.takeInputAndPrintMenu(['[Q]uit', '[B]ack'], ("Work Orders", newBody, f'Employee {employeeId[0].name} has succesfully assigned himself to the work order\nChoose a option: '))



    def addWorkReport(self):
        pass # work on this this week



