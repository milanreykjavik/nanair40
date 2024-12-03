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
        options = []

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

        if error_message:
            baseMenu += error_message

        clearTerminal()
        print(baseMenu.strip(), end='')






    def takeInput(self, possibilites: list) -> str:
        '''Takes input and checks whether the input is valid based on the options given, if not a error will be raised'''
        user_option = input(' ') 

        options_list = self.available_options(possibilites) 

        if user_option.upper() in options_list:
            return user_option
        
        elif user_option.lower() == 'b':
            return 'b'
        
        elif user_option.lower() == 'q':
            return 'q' 
        
        raise InvalidInputError("smuuuu")

        

    @staticmethod
    def printMainMenu(errorMessage=''):
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

    
