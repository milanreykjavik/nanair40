def printBaseMenu(name: str, options: list) -> None:
    baseMenu: str = f"""
===============================================================================
                                NaN Air
===============================================================================

    {name}
        -----------------
    [E]mployee menu
    [P]roperties menu
    [W]orkorders menu
    [C]onstructors

-------------------------------------------------------------------------------
    [Q]uit

Choose a option:
    """

    print(baseMenu)


printBaseMenu("Manager Menu", ["1", "2", "3"])


def takeInput(possibilites: list) -> int:
    inp = input()

    # you need to check if option si valid
    # return -1 if option is invalid and let user choose again
    return 0 # I want you to return index (number) of option user choose from the list
