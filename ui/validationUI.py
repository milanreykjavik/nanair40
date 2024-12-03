class ValidationUI:
    @staticmethod
    def validateName(name):
        name = input()
        if not name:
            return False
        if not name.isalpha():
            return False
        
        return True
    @staticmethod
    def validateKennitala(kennitala):
        if len(kennitala) != 10:
            return False
        if not kennitala.isdigit():
            return False
        
        return True
    @staticmethod
    def validatePhone(phone):
        pass
    
    @staticmethod
    def validateEmail(email):
        pass        