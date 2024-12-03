from logic.Search import Search
from logic.employeeHandler import EmployeeHandler

x = Search()
r =x.searchEmployees()
#print(r[0])

y = EmployeeHandler()

print(r[0])
print(y.addEmployee(r[0]))


from baseClasses.Work import WorkOrder, WorkReport

rep = WorkReport(1, "abc", "2024", 30, "abccc")

wo = WorkOrder(5, "2024", "testing", 2, 1, 1, rep, 5, True)

x = WorkOrder().toJSON(wo)

print(x)
