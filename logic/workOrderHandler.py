from baseClasses.workOrder import WorkOrder
from typing import Any
from datetime import datetime
from dateutil.relativedelta import relativedelta
import logic.validator

# replace dateutil with datetime

def is_date_in_range(check_date_str, start_date_str, end_date_str):
    check_date = datetime.strptime(check_date_str, "%d.%m.%Y")
    start_date = datetime.strptime(start_date_str, "%d.%m.%Y")
    end_date = datetime.strptime(end_date_str, "%d.%m.%Y")
    
    return start_date <= check_date <= end_date


def time_diff_category(date1_str, date2_str):
    # Define the date format
    date_format = "%d.%m.%Y"
    
    # Parse the date strings into datetime objects
    date1 = datetime.strptime(date1_str, date_format)
    date2 = datetime.strptime(date2_str, date_format)
    
    # Calculate the absolute difference
    delta = relativedelta(date2, date1)
    
    # Check the difference and return appropriate category
    if delta.years > 0:
        return 4  # Year
    elif delta.months > 0:
        return 3  # Month
    elif delta.days > 7:
        return 2  # Week
    else:
        return 1  # Day


class WorkOrderHandler:
    def __init__(self, dataWrapper=None) -> None:
        """
        [>] Constructor for WorkOrderHandler class
        Initialize with optional dataWrapper, and initialize WorkOrder object
        """
        self.dataWrapper = dataWrapper
        self.workOrder = WorkOrder()

    def addWorkOrder(self, workOrder: 'WorkOrder') -> bool:
        """
        [>] This function adds a new work order to the system
        It returns true if the work order is successfully inserted, otherwise false
        """
        return self.dataWrapper.workOrderInsert(workOrder)

    def editWorkOrder(self, entry: str, entryValue: Any, **kwargs) -> bool:
        """
        [>] This function is used to edit an existing work order's details
        It returns true or false based on the following conditions:
        - Verifies the entry and entryValue are valid
        - Ensures that the field to edit exists in the WorkOrder class
        """
        if not len(kwargs):
            return False
        if any(kwarg not in vars(self.workOrder) for kwarg in kwargs):
            return False
        if not entry:
            return False
        if not entryValue:
            return False
        return self.dataWrapper.workOrderChange(entry, entryValue, **kwargs)

    def listWorkOrders(self, **kwargs) -> list['WorkOrder']:
        """
        [>] This function lists all work orders or filters them based on given criteria
        Returns a list of work orders, optionally filtered by the provided kwargs
        kwargs: any field of WorkOrder class to filter the list (e.g., "status", "date", "userID")
        """
        if any(kwarg not in vars(self.workOrder) for kwarg in kwargs):
            return []

        workOrder: list['WorkOrder'] = self.dataWrapper.workOrderFetch()

        if not len(kwargs):
            return workOrder

        for k, v in kwargs.items():
            # Top to bottom if we go bottom to top we get index out of range
            # Because things get deleted if they do not match the query before we loop through them if we go bottom to top
            for i in range(len(workOrder)-1, -1, -1):
                # hack around to check if result that might be int or float partially contains our target number
                if str(v) != str(workOrder[i].__dict__[k]):
                    del workOrder[i]

        return workOrder

    def listWorkCurrentOrders(self, **kwargs) -> list['WorkOrder']:
        """
        [>] This function lists all current work orders (i.e., those assigned to users)
        Filters out work orders with userID equal to 0, indicating they are not assigned
        Returns a list of work orders that are currently assigned
        kwargs: filters to apply (e.g., "status", "date")
        """
        if any(kwarg not in vars(self.workOrder) for kwarg in kwargs):
            return []

        workOrder: list['WorkOrder'] = self.dataWrapper.workOrderFetch()
        if not len(kwargs):
            return workOrder

        for k, v in kwargs.items():
            for i in range(len(workOrder)-1, -1, -1):
                if str(v) != str(workOrder[i].__dict__[k]):
                    del workOrder[i]

        newWorkOrder = []
        for index, instance in enumerate(workOrder):
            if int(instance.userID) != 0:
                newWorkOrder.append(instance)

        return newWorkOrder

    def checkRepeatingWorkOrders(self, **kwargs) -> bool:
        """
        [>] This function checks for repeating work orders
        It compares the completion date of each repeating work order with the current date
        If the repeat interval is met, it resets the work order for a new cycle (sets it to incomplete and assigns it to no user)
        """
        repeatingList: list[WorkOrder] = self.listWorkOrders(repeating=True)

        currentDate = datetime.now()
        currentDate = currentDate.strftime("%d.%m.%Y")

        for workOrder in repeatingList:
            if not workOrder.date or not workOrder.isCompleted or not workOrder.dateCompleted:
                continue
            try:
                tdif = time_diff_category(workOrder.dateCompleted, currentDate)
            except:
                return False
            if tdif >= workOrder.repeatInterval:
                # Reset work order
                self.dataWrapper.workOrderChange("id", workOrder.id, isCompleted=False)
                self.dataWrapper.workOrderChange("id", workOrder.id, userID=0)
                self.dataWrapper.workOrderChange("id", workOrder.id, sentToManager=False)
        return True

    def listByDateRange(self, start: str, end: str, **kwargs) -> list[WorkOrder]:
        """
        [>] This function lists work orders within a specified date range
        It filters work orders by their date and only includes those within the specified range (start to end)
        """
        if not start:
            return self.listWorkOrders(date=end, **kwargs)
        if not end:
            return self.listWorkOrders(date=start, **kwargs)

        workOrders: list[WorkOrder] = self.listWorkOrders(**kwargs)
        final: list[WorkOrder] = []
        for workOrder in workOrders:
            if not workOrder.date:
                continue
            try:
                if is_date_in_range(workOrder.date, start, end):
                    final.append(workOrder)
            except:
                pass

        return final

