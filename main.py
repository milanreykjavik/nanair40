from logic.employeeHandler import EmployeeHandler
from baseClasses.Work import WorkOrder, WorkReport
from logic.workHandler import WorkHandler
x = WorkHandler()

rep = WorkReport(1, "abc", "2024", 30, "abccc")
wo = WorkOrder(5, "2024", "testing", 2, 1, 1, [], 5, True)

print(x.addWork(wo))
