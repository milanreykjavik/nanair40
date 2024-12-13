from datetime import datetime
import re
# validation UI is used to call static method functions that do simple validation


class ValidationUI:
    @staticmethod
    def validateName(name) -> str | bool:
        """Checks if the name is valid, includes only letters and is not empty, if [b]ack or [q]uit were entered we return the letter"""
        if name.lower() in ('q', 'b'):
            return name

        if not name:
            return False
        
        if not all(c.isalpha() or c == ' ' for c in name): # check id everything is either a letter or space
            return False
        
        if len(name) > 30: # name cant be longer than 30 letters for the table printing
            return False

        
        return True
    

    @staticmethod
    def validateKennitala(kennitala) -> str | bool:
        # Returns the original letter if 'q' or 'b', otherwise checks via regex that dd, mm, yy are valid and total length = 10
        return kennitala if kennitala.lower() in ('q','b') else bool(re.match(r'^(0[1-9]|[12]\d|3[0-1])(0[1-9]|1[0-2])\d{6}$', kennitala))

    
    @staticmethod
    def validatePhone(phone) -> str | bool:
        """Checks if the phone number is valid, includes only numbers and has len = 7, if [b]ack or [q]uit were entered we return the letter"""
        if phone.lower() in ('q', 'b'):
            return phone
        if not 6 < len(phone) < 16:
            return False
        if not phone.isdigit():
            return False
        
        return True

    @staticmethod
    def validateEmail(email) -> str | bool:
        ''''"""Checks if the email is valid, has a @ sign and is a valid email address, if [b]ack or [q]uit were entered we return the letter"""'''
        if email.lower() in ('q', 'b'):
            return email
        
        emailPattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        if re.fullmatch(emailPattern, email):
            return True
        return False


    @staticmethod
    def validateCondition(condition) -> str | bool:
        '''checks if a condition is in a available set of condition options'''
        if condition.lower() in ('q', 'b'):
            return condition
        
        if condition.lower() in ("excellent", "good", "fair", "poor"):
            return True
        return False
        

    @staticmethod
    def validateFacilitiesRequiringMaintenance(facilitiesRequiringMaintenance):
        if facilitiesRequiringMaintenance.lower() in ('q', 'b'):
            return facilitiesRequiringMaintenance
        
        return True
    

    @staticmethod
    def validateText(text) -> str | bool:
        '''Checks if str sent is empty, if so false is returned'''
        if text.lower() in ('q', 'b'):
            return text
        
        if not text:
            return False
        
        return True
    
    @staticmethod
    def validateNumber(num) -> str | bool:
        '''Checks if str sent in isnt all digits and whether it is less than 1'''
        if num.lower() in ('q', 'b'):
            return num
        if num.isdigit():
            if int(num) > 0:
                return True
        return False
    
    @staticmethod
    def validatePriority(priority) -> str | bool:
        '''Checks if string is in avaiable set of priorities'''
        if priority.lower() in ('q', 'b'):
            return priority
        if priority.lower() in ('now', 'emergency', 'as soon as possible'):
            return True
        return False
    

    @staticmethod
    def validate_date(dateString) -> str | bool:
        '''Validates the date format sent in str needs to be in a format like this: 2.12.2024'''
        if dateString.lower() in ('q', 'b'):
            return dateString
        try:
            # Attempt to parse the string with the given format
            date = datetime.strptime(dateString, '%d.%m.%Y')
            # Check if the day and month are valid
            if not (1 <= date.day <= 31):
                return False
            if not (1 <= date.month <= 12):
                return False
            return True
        except ValueError as e:
            return False

    @staticmethod
    def validateOpeningHours(hoursStr) -> str | bool:
        '''Validate whether opening hours that where sent in are in a valid format'''

        if hoursStr.lower() in ('q', 'b'):
            return hoursStr
    
        pattern = r"^([01]\d|2[0-3])-[0-5]\d$"
        
        match = re.match(pattern, hoursStr)
        if not match:
            return False
        return True


