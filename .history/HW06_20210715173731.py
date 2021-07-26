"""
Georgia Institute of Technology - CS1301
HW06 - Text Files & CSV
Collaboration Statement:
"""

#########################################

"""
Function Name: findCuisine()
Parameters: filename (str), cuisine (str)
Returns: list of restaurants (list)
"""

#########################################
########## WRITE FUNCTION HERE ##########
#########################################

def findCuisine(filename, cuisine):
    file = open(filename,'r')
    content = file.readlines()
    listOfRestaurants = []
    for i in range(len(content)):
        if content[i].strip() == cuisine:
            listOfRestaurants.append(content[i-1].strip()) #add the name of the restaurant, which is the previous line
    file.close()
    return listOfRestaurants

"""
Function Name: restaurantFilter()
Parameters: filename (str)
Returns: dictionary that maps cuisine type (str)
to a list of restaurants of the same cuisine type (list)
"""

#########################################
########## WRITE FUNCTION HERE ##########
#########################################

def restaurantFilter(filename):
    dict = {}
    file = open(filename,'r')
    content = file.readlines()
    cuisines = []

    for i in range(1,len(content),4):
        if cu



"""
Function Name: createDictionary()
Parameters:  filename (str), output filename (str)
Returns: None (NoneType)
"""

#########################################
########## WRITE FUNCTION HERE ##########
#########################################


"""
Function Name: extraHours()
Parameters:  filename (str), hour (int)
Returns: list of (person, extra money) tuples (tuple)
"""

#########################################
########## WRITE FUNCTION HERE ##########
#########################################


"""
Function Name: seniorStaffAverage()
Parameters:  filename (str), year (int)
Returns: average age of senior staff members (float)
"""

#########################################
########## WRITE FUNCTION HERE ##########
#########################################


"""
Function Name: ageDict()
Parameters:  filename (str), list of age ranges represented by strings (list)
Returns: dictionary (dict) that maps each age range (str) to a list of employees (list)
"""

#########################################
########## WRITE FUNCTION HERE ##########
#########################################

# print(findCuisine('restaurants.txt', 'Mexican'))

print(restaurantFilter('restaurants.txt'))

