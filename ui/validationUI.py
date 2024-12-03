class ValidationUI:
    @staticmethod
    def validateName(name):
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
        if len(phone) != 7:
            return False
        if not phone.isdigit():
            return False
        
        return True

    @staticmethod
    def validateEmail(email):
        for letter in email:
            if letter == "@":
                return True
        else:
            return False 
               
    @staticmethod
    def validateAddress(address):
        if address == "Reykjavík" or "Nuuk" or "Kulusuk" or "Tórshavn" or "Tingwall" or "Longyearbyen":
            return True
        else:
            return False
        
    @staticmethod
    def validateCountry(country):
        if country == "Iceland" or "Faeroe Islands" or "Greenland" or "Shetland Islands" or "Svalbard":
            return True
        else:
            return False