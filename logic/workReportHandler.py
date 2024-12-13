from baseClasses.workReport import WorkReport
from typing import Any
from datetime import datetime
import logic.validator

def is_date_in_range(check_date_str, start_date_str, end_date_str):
    check_date = datetime.strptime(check_date_str, "%d.%m.%Y")
    start_date = datetime.strptime(start_date_str, "%d.%m.%Y")
    end_date = datetime.strptime(end_date_str, "%d.%m.%Y")
    
    return start_date <= check_date <= end_date



class WorkReportHandler:
    def __init__(self, dataWrapper=None) -> None:
        """
        [>] Constructor for WorkReportHandler class
        Initialize with optional dataWrapper, and initialize WorkReport object
        """
        self.dataWrapper = dataWrapper
        self.workReport = WorkReport()

    def addWorkReport(self, work: 'WorkReport') -> bool:
        """
        [>] This function adds a new work report to the system
        It performs the following checks:
        - Verifies that the cost is a non-negative integer
        Returns true if the work report is successfully inserted, otherwise false
        """
        if type(work.cost) != int:
            return False
        if work.cost < 0:
            return False

        return self.dataWrapper.workReportInsert(work)

    def editWorkReport(self, entry: str, entryValue: Any, **kwargs) -> bool:
        """
        [>] This function is used to edit an existing work report's details
        It returns true or false based on the following conditions:
        - Verifies the entry and entryValue are valid
        - Ensures that the field to edit exists in the WorkReport class
        - Validates that cost, if being edited, is a non-negative integer
        """
        if not len(kwargs):
            return False
        if any(kwarg not in vars(self.workReport) for kwarg in kwargs):
            return False
        if not entry:
            return False
        if not entryValue:
            return False

        if entry == "cost":
            if type(entryValue) != int:
                return False
            if entryValue < 0:
                return False

        return self.dataWrapper.workReportChange(entry, entryValue, **kwargs)

    def listWorkReports(self, **kwargs) -> list['WorkReport']:
        """
        [>] This function lists all work reports or filters them based on given criteria
        Returns a list of work reports, optionally filtered by the provided kwargs
        kwargs: any field of WorkReport class to filter the list (e.g., "status", "date", "cost")
        """
        if any(kwarg not in vars(self.workReport) for kwarg in kwargs):
            return []

        workReports: list['WorkReport'] = self.dataWrapper.workReportFetch()
        if not len(kwargs):
            return workReports

        for k, v in kwargs.items():
            # Top to bottom if we go bottom to top we get index out of range
            # Because things get deleted if they do not match the query before we loop through them if we go bottom to top
            for i in range(len(workReports)-1, -1, -1):
                # hack around to check if result that might be int or float partially contains our target number
                if str(v) not in str(workReports[i].__dict__[k]):
                    del workReports[i]

        return workReports

    def currentWorkReportID(self) -> int:
        """
        [>] This function returns the next available work report ID
        It fetches the current list of work reports and returns the next ID as the highest existing ID + 1
        If no work reports exist, it returns 1
        """
        workReports: list['WorkReport'] = self.listWorkReports()
        if not len(workReports):
            return 1

        return workReports[-1].id + 1

    def listByDateRange(self, start: str, end: str, **kwargs) -> list[WorkReport]:
        """
        [>] This function lists work reports within a specified date range
        It filters work reports by their date and only includes those within the specified range (start to end)
        """
        if not start:
            return self.listWorkReports(date=end, **kwargs)
        if not end:
            return self.listWorkReports(date=start, **kwargs)

        workReports: list[WorkReport] = self.listWorkReports(**kwargs)
        final: list[WorkReport] = []
        for workReport in workReports:
            if not workReport.date:
                continue
            try:
                if is_date_in_range(workReport.date, start, end):
                    final.append(workReport)
            except:
                pass

        return final

