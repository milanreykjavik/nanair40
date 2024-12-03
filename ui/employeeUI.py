from baseUI import BaseUI
from validationUI import ValidationUI


validation = ValidationUI() 

class EmployeeUI(BaseUI):
    def addEmployee(self):
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
            homephone = input("Enter a homephone: ")
            validhomephone = validation.validatePhone(homephone)

        validaddress = False
        while not validaddress:
            address = input("Enter youre address: ")
            validaddress = validation.validateAddress(address)

        validateemail = False
        while not validateemail:
            email = input("Enter youre email: ")
            validateemail = validation.validateEmail(email)

        validcountry = False
        while not validcountry:
            country = input("Enter a country: ")
            validcountry = validation.validateCountry(country)


    def editEmployee():
        pass


    def listEmployess():
        pass
