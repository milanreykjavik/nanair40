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
