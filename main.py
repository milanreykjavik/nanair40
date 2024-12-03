from logic.Search import Search
from logic.employeeHandler import EmployeeHandler

x = Search()
r =x.searchEmployees()
#print(r[0])

y = EmployeeHandler()

print(y.addEmployee(r[0]))
