class BaseUI:
    @staticmethod
    def getOptions(options: list) -> str:
        returnStr = '\n'

        for option in options:
            firstLetter = option[0]
            returnStr += f'{"":<7}[{firstLetter}]{option[1:]}\n'

        return returnStr


    @staticmethod
    def getHeader()->str:
        return f'''
    ===============================================================================
                                    NaN Air
    ===============================================================================
          
    '''

    @staticmethod
    def getFooter(inputOption: str)->str:
        return f'''
    -------------------------------------------------------------------------------
        [Q]uit   [B]ack

    {inputOption}:
    '''

    def printBaseMenu(self, name: str, options: list, inputOption: str) -> None:
        baseMenu = ''
        baseMenu += self.getHeader()
        baseMenu += f'''       {name}
            -----------------'''
        baseMenu += self.getOptions(options)
        baseMenu += self.getFooter(inputOption)

        print(baseMenu)

    @staticmethod
    def takeInput(possibilites: list) -> int:
        inp = input()

        # you need to check if option si valid
        # return -1 if option is invalid and let user choose again
        return 0 # I want you to return index (number) of option user choose from the list


