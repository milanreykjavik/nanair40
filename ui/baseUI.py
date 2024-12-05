import os

class BaseUI:
    @staticmethod
    def getOptions(options: list) -> str:
        '''Returns a string that represents the options the user can do'''
        returnStr = '\n'
        for option in options:
            returnStr += f'       {option}\n'# Formats the options 

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




    def takeInputAndPrintMenu(self, possibilites: list, menuInformation: tuple) -> str:
        '''Asks the user a option based on the option list entered, it prints the baseMenuScreen after every one guess, the menu screen is determained by the second argument, when the user enters a available option, then that option is returned'''
        options_list = self.available_options(possibilites) 

        while True:
            self.printBaseMenu(menuInformation[0], menuInformation[1], menuInformation[2])
            user_option = input(' ') 

        
            if user_option.upper() in options_list or not possibilites:
                return user_option
            




    @staticmethod
    def printMainMenu(errorMessage='') -> None:
        clearTerminal()
        print(f'''
--------------------------------------------------------------------------------
   _  __     _  __    ___   _           
  / |/ /__ _/ |/ /   / _ | (_)___        __|__   
 /    / _ `/    /   / __ |/ / __/    ---@-(")-@---
/_/|_/\_,_/_/|_/   /_/ |_/_/_/           ! ! !
~Where dividing by zero makes sense                
--------------------------------------------------------------------------------
	MAIN MENU:
	-----------
	[M]anager
	[J]anitor (Maintenance)
	[S]earh (Front desk)	
	[Q]uit
-------------------------------------------------------------------------------
Choose a option:''', end='')
        
        



def clearTerminal():
    """Clear the terminal screen before a new menu is printed"""
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Unix/Linux/Mac
        os.system('clear')



