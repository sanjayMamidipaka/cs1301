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
    highestRated = (0,0,0)
    for i in restaurantList:
        if i[2] in categoryList:
            if i[1] > highestRated[1]:
                highestRated = i

    return highestRated

"""
Function Name: snackTime()  
Parameters: taList (list)
Returns: list (list)
"""

#########################################
########## WRITE FUNCTION HERE ##########
#########################################

def snackTime(taList):
    taNames = []
    taIndices = []
    taOptimalSnacksList = []
    counter = -1
    for ta in taList:
        if ta[2] >= 11 and ta[2] <= 14 or ta[2] >= 21 and ta[2] <= 23: #checking if ta snacking time is optimal or not
            if ta[0] not in taNames:
                counter += 1
                taNames.append(ta[0])
                taOptimalSnacksList.append([ta[0]])

    for ta in taList:
        if ta[2] >= 11 and ta[2] <= 14 or ta[2] >= 21 and ta[2] <= 23:
            taName = ta[0]
            index = taNames.index(taName)
            taOptimalSnacksList[index].append(ta[0])


    
    return taOptimalSnacksList


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

# categoryList = ["Mexican"] 
# restaurantList = [ ("Fogo de Chao", 4.8, "Brazilian"), ("El Rey", 4.5, "Mexican") ] 
# print(restaurantRatings(categoryList, restaurantList))

taList = [ ("Corinne", "pickles", 3), ("Michael", "pringles", 13), ("Kathleen", "trail mix", 21)] 
print(snackTime(taList))

