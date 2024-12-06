import os
from typing import Callable, List, Any

class BaseUI:
    @staticmethod
    def getOptions(options: list) -> str:
        '''Returns a string that represents the options the user can do'''
        returnStr = '\n'
        for option in options:
            returnStr += f'       [{option[0]}]{option[1:]}\n'# Formats the options 

        return returnStr
    
    @staticmethod
    def available_options(possibilites) -> list:
        '''Returns a list of letters, with every single letter the user can choose from'''
        options = ['Q', 'B']

        for word in possibilites:
            options.append(word[1])

        return options


    @staticmethod
    def getHeader()->str:
        '''Returns the standard header'''
        return f'''
===============================================================================
                                    NaN Air
===============================================================================
          
    '''

    @staticmethod
    def getFooter(inputOption: str = '')->str:
        '''Returns the standard footer'''
        return (f'''
-------------------------------------------------------------------------------
        [Q]uit   [B]ack

{inputOption}
    ''')


    def printBaseMenu(self, name: str, options: list = [], inputOption: str = '') -> None:
        '''Prints the menu based on the arguments given'''
        baseMenu = ''
        baseMenu += self.getHeader()
        baseMenu += f'''   {name}
       -----------------'''
        baseMenu += self.getOptions(options)
        baseMenu += self.getFooter(inputOption)


        clearTerminal()
        print(baseMenu.strip(), end='')



    @staticmethod
    def isValidInput(possibilites: list, choice: str) -> int:
        if choice == 'q':
            return 2
        if all(choice.upper() not in option[0] for option in possibilites):
            return 0

        return 1

    def returnTable(self, functions: List[Callable[[], Any]], possibilites: List[List[str]], choice: str) -> Any:
        if not self.isValidInput(possibilites, choice):
            return input(' ')

        if len(possibilites) != len(functions):
            return None # raise exception THIS CANNOT HAPPEN

        data = {}
        for i in range(len(possibilites)):
            if possibilites[i][0] == choice.upper():
                return functions[i]()

        #if any(choice.upper() not in option[0] for option in possibilites):
        #return functions[possibilites.index(


    def takeInputAndPrintMenu(self, possibilites: list, menuInformation: tuple) -> str:
        '''Asks the user a option based on the option list entered, it prints the baseMenuScreen after every one guess, the menu screen is determained by the second argument, when the user enters a available option, then that option is returned'''
        options_list = self.available_options(possibilites) 

        while True:
            self.printBaseMenu(menuInformation[0], menuInformation[1], menuInformation[2])
            user_option = input(' ') 

            if not self.isValidInput(possibilites, user_option):
                return user_option

            break

        
                    




    def printMainMenu(self, name: str, options: list = [], errorMessage: str = '') -> None:
        clearTerminal()
        print(f'''
--------------------------------------------------------------------------------
   _  __     _  __    ___   _           
  / |/ /__ _/ |/ /   / _ | (_)___        __|__   
 /    / _ `/    /   / __ |/ / __/    ---@-(")-@---
/_/|_/\_,_/_/|_/   /_/ |_/_/_/           ! ! !
~Where dividing by zero makes sense                
--------------------------------------------------------------------------------
    {name}:
	-----------
    {self.getOptions(options)}
-------------------------------------------------------------------------------
Choose a option:''', end='')
        
        



def clearTerminal():
    """Clear the terminal screen before a new menu is printed"""
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Unix/Linux/Mac
        os.system('clear')
