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

    if clothingItem == 'tank':
        if size == 'S':
            print("1 colors are available in this item and size.")
        elif size == 'M':
            print("1 colors are available in this item and size.")
        elif size == 'L':
            print("2 colors are available in this item and size.")

    if clothingItem == 'flipflops':
        if size == 'S':
            print("1 colors are available in this item and size.")
        elif size == 'M':
            print("1 colors are available in this item and size.")
        elif size == 'L':
            print("2 colors are available in this item and size.")

"""
Function Name: stopGame()  
Parameters: initialPrice (float), finalPrice (float), percentGrowth (float)
Returns: numberOfDays (int)  
"""

#########################################
########## WRITE FUNCTION HERE ##########
#########################################

def stopGame(initialPrice, finalPrice, percentGrowth):
    if finalPrice <= initialPrice:
        return 0
    
    newPrice = initialPrice
    days = 0

    while (newPrice <= finalPrice):
        newPrice = newPrice * (1 + (percentGrowth/100))
        days += 1

    return days


"""
Function Name: adventure()
Parameters: startDay (int), stopDay (int), hikeLimit(int)  
Returns: None (NoneType)
"""

#########################################
########## WRITE FUNCTION HERE ##########
#########################################

def adventure(startDay, stopDay, hikeLimit):
    numberOfHikes = 0
    for i in range(startDay, stopDay+1):
        if i % 3  == 0 and i % 4 == 0:
            print('Roadtrip!') 
        elif i % 3 == 0:
            print()



print(stopGame(232.0, 20000.0, 15.0))

