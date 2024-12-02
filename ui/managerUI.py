from baseUI import BaseUI

def printManagerMenu(name: str, options: list) -> None:
    baseUI = BaseUI()
    baseMenu = ""
    baseMenu += baseUI.getHeader()
    baseMenu += name
    baseMenu += baseUI.getOptions(options)
    baseMenu += baseUI.getFooter("input")

print(printManagerMenu("Manager",['Add employee', 'Edit employee', 'List employees']))
