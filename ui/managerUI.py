from baseUI import *

def printManagerMenu(name: str, options: list) -> None:
    baseMenu = ""
    baseMenu += getHeader()
    baseMenu += name
    baseMenu += getOptions(options)
    baseMenu += getFooter()

print(printManagerMenu("Manager",['Add employee', 'Edit employee', 'List employees']))