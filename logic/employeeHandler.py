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


    def editEmployee(self, targetKennitala: str, **kwargs) -> bool:
        if any(kwarg not in vars(self.employee) for kwarg in kwargs):
            return False
        self.employeeControl.changeOneEntry(targetKennitala, **kwargs)
        return True


    def listEmployess(self, employee: 'Employee', **kwargs) -> bool:
        return True
