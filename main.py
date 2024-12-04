from logic.employeeHandler import EmployeeHandler

x = EmployeeHandler()
r =x.listEmployess()

print(x.editEmployee(r[0].kennitala, kennitala="32"))
print(x.listEmployess(location=1))

"""
from baseClasses.Work import WorkOrder, WorkReport

rep = WorkReport(1, "abc", "2024", 30, "abccc")

wo = WorkOrder(5, "2024", "testing", 2, 1, 1, rep, 5, True)

x = WorkOrder().toJSON(wo)

print(x)
"""
