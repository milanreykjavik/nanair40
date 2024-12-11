from baseClasses.Employee import Employee
from logic.logicWrapper import Logic_Wrapper

lg = Logic_Wrapper()

emp = Employee("2707046969", "test", "1234567", "1234567", "test 12", "test@test.com", "Greenland")

x = lg.addEmployee(emp)
print(x)
