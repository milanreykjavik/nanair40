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
    def takeInput(self, possibilites: list) -> int:
        index = int(input()) 
        if 0 < index < len(possibilites): 
            return self.takeInput(possibilites)
        return index
