from baseClasses.Employee import Employee
from dataControl.employeeController import EmployeeController


class EmployeeHandler:
    def __init__(self):
        self.employeeControl = EmployeeController()
        self.employee = Employee()

    def addEmployee(self, employee: 'Employee') -> bool:
        employeeJson = self.employee.toJSON(employee)
        self.employeeControl.appendIntoFile(employeeJson)
        return True


    def editEmployee(self, targetKennitala: str, **kwargs) -> bool:
        if not len(kwargs):
            return False
        if any(kwarg not in vars(self.employee) for kwarg in kwargs):
            return False
        self.employeeControl.changeOneEntry(targetKennitala, **kwargs)
        return True


    def listEmployess(self, **kwargs) -> list[dict]:
        if any(kwarg not in vars(self.employee) for kwarg in kwargs):
            return []

        employees = self.employeeControl.readFile()
        if not len(kwargs):
            return employees

        for k, v in kwargs.items():
            # Top to bottom if we go bottom to top we get index out of range
            # Because things get deleted if they do not match the query before we loop through them if we go bottom to top
            for i in range(len(employees)-1, -1, -1):
                # hack around to check if result that might be int or float partialy contains our target number
                if str(v) not in str(employees[i][k]):
                    del employees[i]


        return employees
