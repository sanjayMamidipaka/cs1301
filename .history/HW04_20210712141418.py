"""
Georgia Institute of Technology - CS1301
HW04 - Lists
 and Tuples
Collaboration Statement:
"""

#########################################

"""
Function Name: roadTrip()  
Parameters: state (str), list of tuples (list)
Returns: list of crops (list)
"""

#########################################
########## WRITE FUNCTION HERE ##########
#########################################

def roadTrip(state, crops):
    listOfCrops = []
    for group in crops:
        if group[1] == state:
            listOfCrops.append(group[0])

    return listOfCrops


"""
Function Name: groceryShopping()  
Parameters: groceryList (list), priceList (list), budget (float)
Returns: purchaseList(str)
"""

#########################################
########## WRITE FUNCTION HERE ##########
#########################################

def groceryShopping(groceryList, priceList, budget):
    totalCost = 0
    finalItems = []
    for i in range(len(groceryList)):
        if priceList[i] + totalCost <= budget:
            totalCost += priceList[i]
            finalItems.append((groceryList[i], priceList[i]))

    return finalItems



"""
Function Name: restaurantRatings()  
Parameters: categoryList(list), restaurantList(list)
Returns: tuple(tuple)
"""

#########################################
########## WRITE FUNCTION HERE ##########
#########################################

def restaurantRatings(categoryList, restaurantList):
    

"""
Function Name: snackTime()  
Parameters: taList (list)
Returns: list (list)
"""

#########################################
########## WRITE FUNCTION HERE ##########
#########################################


"""
Function Name: coffeeBreak()  
Parameters: list of drinks (list), budget (float)
Returns: name of drink (str)
"""

#########################################
########## WRITE FUNCTION HERE ##########
#########################################



# state = 'GA'
# crops = [('peaches', 'GA'), ('potatoes', 'ID'), ('peanuts', 'GA')]
# print(roadTrip(state, crops))

# groceryList = ["chips", "bagels", "coffee", "lettuce", "milk", "steak"]
# priceList = [3.50, 6.50, 3.75, 3.00, 4.40, 16.99] 
# budget = 14.50
# print(groceryShopping(groceryList, priceList, budget))
