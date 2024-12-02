

def printOptions(options: list) -> str:
    returnStr = ''

    for option in options:
        firstLetter = option[0]
        returnStr += f'{"":<7}[{firstLetter}]{option[1:]}\n'


    
    return returnStr







def printBaseMenu(name: str, options: list) -> None:
    baseMenu: str = f"""
===============================================================================
                                NaN Air
===============================================================================

    {name}
        -----------------
{printOptions(options)}
-------------------------------------------------------------------------------
    [Q]uit

Choose a option:
    """

    print(baseMenu)


printBaseMenu("Manager Menu", ["Add employee", "Edit employee", "List employee"])






