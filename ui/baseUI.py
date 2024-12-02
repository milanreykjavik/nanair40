

def getOptions(options: list) -> str:
    returnStr = '\n'

    for option in options:
        firstLetter = option[0]
        returnStr += f'{"":<7}[{firstLetter}]{option[1:]}\n'


    
    return returnStr

def getHeader()->str:
    return f'''
===============================================================================
                                NaN Air
===============================================================================
          
'''

def getFooter(inputOption: str)->str:
    return f'''
-------------------------------------------------------------------------------
    [Q]uit   [B]ack

{inputOption}:
'''




def printBaseMenu(name: str, options: list, inputOption: str) -> None:
    baseMenu = ''
    baseMenu += getHeader()
    baseMenu += f'''       {name}
        -----------------'''
    baseMenu += getOptions(options)
    baseMenu += getFooter(inputOption)

    print(baseMenu)




printBaseMenu('Manager menu', ['Add employee', 'Edit employee', 'List employees'])


def takeInput(possibilites: list) -> int:
    inp = input()

    # you need to check if option si valid
    # return -1 if option is invalid and let user choose again
    return 0 # I want you to return index (number) of option user choose from the list

def takeInput(possibilites: list) -> int:
    inp = input()

    # you need to check if option si valid
    # return -1 if option is invalid and let user choose again
    return 0 # I want you to return index (number) of option user choose from the list

