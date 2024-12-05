from logic.employeeHandler import EmployeeHandler
from baseClasses.Employee import Employee
from dataControl.employeeController import EmployeeController

x = EmployeeHandler()
r = x.listEmployess()
print(r)


y = EmployeeController()
"""
for i in range(0, 10000):
    new_employee = Employee(
        kennitala="12345"+str(i),
        name="John Doe",
        phone="123-456-7890",
        homePhone="098-765-4321",
        address="123 Main Street",
        email="john.doe@example.com",
        location=101
    )
    print(i)
    employee_json = new_employee.toJSON(new_employee)

    y.appendIntoFile(employee_json)




exit()
"""
print(x.editEmployee(r[0].kennitala, kennitala="32"))
print(x.listEmployess(location=1))

"""
from baseClasses.Work import WorkOrder, WorkReport

rep = WorkReport(1, "abc", "2024", 30, "abccc")

wo = WorkOrder(5, "2024", "testing", 2, 1, 1, rep, 5, True)

x = WorkOrder().toJSON(wo)

print(x)
"""
