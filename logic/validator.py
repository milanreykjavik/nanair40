from baseClasses.Employee import Employee
from dataControl.dataWrapper import DataWrapper
import re

employee = Employee()
dataWrapper = DataWrapper()


def validateEmail(email) -> bool:
    if type(email) != str:
        return False
    emailPattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if re.fullmatch(emailPattern, email):
        return True
    return False

def validateKennitala(kennitala) -> bool:
    if not kennitala:
        return False
    if not type(kennitala) == str:
        return False
    if not kennitala.isdigit():
        return False
    if len(str(kennitala)) != 10:
        return False
    return True


def validatePhone(phone) -> bool:
    if not phone:
        return False
    phoneWhitelist = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "+"]
    if type(phone) != str:
        return False
    if len(phone) < 7 or len(phone) > 15:
        return False
    cnt = 0
    for i in phone:
        if i == "+":
            cnt+=1
        if cnt >= 2:
            return False
        if i not in phoneWhitelist:
            return False
    return True


def validateOpeningHours(openingHours) -> bool:
    if not openingHours:
        return False
    if type(openingHours) != str:
        return False
    charWhitelist = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ":"]
    cnt = 0
    count = 0
    after = False
    if openingHours[0] == ":":
        return False
    for i in openingHours:
        if count > 2:
            return False
        if i == "-":
            after = True
            cnt+=1
        if cnt >= 2:
            return False
        if i not in charWhitelist:
            return False
        if after:
            count = 0
        count+=1
    op = openingHours.split(":")
    if int(op[0]) > 24 or int(op[1]) > 24:
        return False

    return True

def checkEntries(entries) -> bool:
    if any(not(entry) for entry in entries):
        return False
    return True
