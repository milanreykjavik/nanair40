

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


