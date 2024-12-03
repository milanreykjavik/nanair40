from baseClasses.Employee import Employee
from dataControl.employeeController import EmployeeController


class EmployeeHandler:
    def __init__(self):
        self.employeeControl = EmployeeController()
        self.employee = Employee()

    # should be Employee type
    def addEmployee(self, employee: 'Employee') -> bool:
        employeeJson = self.employee.toJSON(employee)
        self.employeeControl.appendIntoFile(employeeJson)
        return True
