def getOptions(options: list) -> str:
    returnStr = '\n'

    for option in options:
        firstLetter = option[0]
        returnStr += f'{"":<7}[{firstLetter}]{option[1:]}\n'

    return returnStr

def getHeader():
    return '''
===============================================================================
                                NaN Air
===============================================================================
          
'''




def getFooter():
    return '''
-------------------------------------------------------------------------------
    [Q]uit   [B]ack

Choose a option:
'''






def printBaseMenu(name: str, options: list) -> None:
    baseMenu = ''
    baseMenu += getHeader()
    baseMenu += '''    Manager Menu
        -----------------'''
    baseMenu += getOptions(options)
    baseMenu += getFooter()

    print(baseMenu)






printBaseMenu('Manager menu', ['Add employee', 'Edit employee', 'List employees'])


def takeInput(possibilites: list) -> int:
    inp = input()

    # you need to check if option si valid
    # return -1 if option is invalid and let user choose again
    return 0 # I want you to return index (number) of option user choose from the list


