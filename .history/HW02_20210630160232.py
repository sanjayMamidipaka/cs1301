"""
Georgia Institute of Technology - CS1301
HW02 - Conditionals and Loops
Collaboration Statement:
"""

#########################################

"""
Function Name: snackBar()  
Parameters: snack (str), ingredient (str), yourMoney (float)
Returns: whether you can get the snack (bool) 
"""


#########################################
########## WRITE FUNCTION HERE ##########
#########################################

def snackBar(snack, ingredient, yourMoney):
    if snack == 'Hotdog':
        if not ingredient == 'Gluten' and not ingredient == 'Meat' and yourMoney >= 5.99:
            return True
        else:
            return False
    
    if snack == 'Veggie Burger':
        if not ingredient == 'Gluten' and yourMoney >= 5.99:
            return True
        else:
            return False

    if snack == 'Chili Bowl':
        if not ingredient == 'Meat' and yourMoney >= 3.99:
            return True
        else:
            return False

    if snack == 'Chili Cheese Fries':
        if not ingredient == 'Meat' and not ingredient == 'Diary' and yourMoney >= 4.99:
            return True
        else:
            return False

"""
Function Name: waterGames()
Parameters: gameName (str), numPlayers (int), totalFriends (int)
Returns: None (NoneType)
"""

#########################################
########## WRITE FUNCTION HERE ##########
#########################################

def waterGames(gameName, numPlayers, totalFriends):
    percentPlaying = numPlayers / totalFriends

    if percentPlaying < 0.3:
        print('Let’s choose something else.')
    elif percentPlaying >= 0.3 and percentPlaying < 0.75:
        print('We will {} for a little bit!'.format(gameName))
    elif percentPlaying >= 0.75:
        print("Let's " + gameName + '!!!')

"""
Function Name: summerShopping()
Parameters: clothingItem (str), size (str)
Returns: None (NoneType)
"""

#########################################
########## WRITE FUNCTION HERE ##########
#########################################

def summerShopping(clothingItem, size):
    if clothingItem == 'shorts':
        if size == 'S':
            print("2 colors are available in this item and size.")
        elif size == 'M':
            print("1 colors are available in this item and size.")
        elif size == 'L':
            print("No colors are available in this item and size.")

    if clothingItem == 'tank'

"""
Function Name: stopGame()  
Parameters: initialPrice (float), finalPrice (float), percentGrowth (float)
Returns: numberOfDays (int)  
"""

#########################################
########## WRITE FUNCTION HERE ##########
#########################################


"""
Function Name: adventure()
Parameters: startDay (int), stopDay (int), hikeLimit(int)  
Returns: None (NoneType)
"""

#########################################
########## WRITE FUNCTION HERE ##########
#########################################



waterGames("go water skiing", 3, 4)