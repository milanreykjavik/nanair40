import os

class BaseUI:
    @staticmethod
    def getOptions(options: list) -> str:
        '''Returns a string that represents the options the user can do with brackets around first letter'''
        returnStr = '\n' 
        for option in options: # loop thorugh every option
            if len(option) > 1:
                returnStr += f'       [{option[0]}]{option[1:]}\n'# Formats the options
                continue
            returnStr += ""

        return returnStr # return all options

    @staticmethod
    def getOptionsNoBrackets(options: list) -> str:
        '''Returns a string that represents the options the user can do WITHOUT BRACKETS'''
        returnStr = '\n'
        for option in options: # loop trough all options
            if len(option) > 1:
                returnStr += f'       {option}\n'# Formats the options
                continue
            returnStr += ""

        return returnStr

    
    @staticmethod
    def available_options(possibilites) -> list:
        '''Returns a list of letters, with every single letter the user can choose from'''
        options = ['Q', 'B'] # options are always quit and back
        if not possibilites: # if there are no possibilities sent then nothing is returned
            return options

        for word in possibilites: # get the first letter of every word for the possibilities
            options.append(word[0])

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
       -----------------''' # top name header of the body is created
        baseMenu += self.getOptions(options) # ADD THE optiosn list with brackets to the body
        baseMenu += self.getFooter(inputOption)


        clearTerminal() # TERMINAL is cleared after every menu print
        print(baseMenu.strip(), end='')

    def printBaseMenuNoBrackets(self, name: str, options: list = [], inputOption: str = '') -> None:
        '''Prints the menu based on the arguments given'''
        baseMenu = ''
        baseMenu += self.getHeader()
        baseMenu += f'''   {name}
       -----------------'''  # top name header of the body is created
        baseMenu += self.getOptionsNoBrackets(options) # ADD THE optiosn list WITHOUT brackets to the body
        baseMenu += self.getFooter(inputOption)


        clearTerminal() # TERMINAL is cleared after every menu print
        print(baseMenu.strip(), end='')


    def takeInputAndPrintMenuWithoutBrackets(self, possibilites: list, menuInformation: tuple, errorMessage = 'Please choose from the options available\n') -> str:
        '''Asks the user a option based on the option list entered, it prints the baseMenuScreen after every one guess, the menu screen is determained by the second argument, when the user enters a available option, then that option is returned'''
        error = False # error message is false to begin with

        menuInformation = list(menuInformation) 
        options_list = self.available_options(possibilites) #

        while True:
            if error: # if error is true then we add the error message to the prompt
                menuInformation[2] = errorMessage + menuInformation[2]
                errorMessage = '' # make error message empty so that we dont stack error messages to the prompt
            self.printBaseMenuNoBrackets(menuInformation[0], menuInformation[1], menuInformation[2]) # print the menu with the menu info parameters
    
            user_option = input(' ') 
            if user_option.upper() in options_list or not possibilites: # if the userInput is not in available possibilites then he is asked agin
                return user_option                                      # but if there were no possibilities to begin with then the input is returned
            
            error = True # if nothing was returned before then error is now true and error message will be added no next prompt



    def takeInputAndPrintMenu(self, possibilites: list, menuInformation: tuple, errorMessage = 'Please choose from the options available\n') -> str:
        '''Asks the user a option based on the option list entered, it prints the baseMenuScreen after every one guess, the menu screen is determained by the second argument, when the user enters a available option, then that option is returned'''
        error = False # error message is false to begin with
        menuInformation = list(menuInformation)
        options_list = self.available_options(possibilites) 

        while True:
            if error:
                menuInformation[2] = errorMessage + menuInformation[2]
                errorMessage = ''
            self.printBaseMenu(menuInformation[0], menuInformation[1], menuInformation[2])
    
            user_option = input(' ') 

        
            if user_option.upper() in options_list or not possibilites: # if the userInput is not in available possibilites then he is asked agin
                return user_option                                      # but if there were no possibilities to begin with then the input is returned
        
            error = True # if nothing was returned before then error is now true and error message will be added no next prompt



    @staticmethod
    def printMainMenu(errorMessage='') -> None:
        ###
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
        
    def getValidInput(self, name, prompt, validationFunc, userDict: dict = {}, errorMessage = 'Invalid Input\n') -> str:
        '''Prints out menu with the optioins given, ask the user for some value then that value is validated with the validation function that was entered'''
        error = False # error is false to begin with
        while True:
            if error: # if error is true then we add the error message before the prompt
                prompt = errorMessage + prompt
                errorMessage = ''
            # print the menu with no brackets with key: value, in the dictionary that was given
            self.printBaseMenuNoBrackets(name, [f'{key}: {value if value else ''}' for key, value in userDict.items()], prompt)
            user_input = input(' ').capitalize()
        
            # if the validation function returns true then we can return that value
            if validationFunc(user_input):
                return user_input
            error = True # error messages are now true and the user 
        
        



def clearTerminal() -> str:
    """Clear the terminal screen before a new menu is printed"""
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Unix/Linux/Mac
        os.system('clear')
