from baseUI import BaseUI
from validationUI import ValidationUI


validation = ValidationUI() 

class EmployeeUI(BaseUI):
    def addEmployee():
        validkennitala = False
        while not validkennitala:
            kennitala = input("Enter youre kennitala: ")
            validkennitala = validation.validateKennitala(kennitala)

        validname = False
        while not validname:
            name = input("Enter youre name: ")
            validname = validation.validateName(name)
        
        validphone = False
        while not validphone:
            phone = input("Enter a phonenumber: ")
            validphone = validation.validatePhone(phone)
        
        validhomephone = False
        while not validhomephone:
            phone = input("Enter a homephone: ")
            validphone = validation.validatePhone(validhomephone)
        
            #address = input("Enter youre address: ")
            #email = input("Enter youre email: ")
            #country = input("Enter a country: ")


    def editEmployee():
        pass


    def listEmployess():
        pass
