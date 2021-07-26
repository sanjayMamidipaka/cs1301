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
        line = content[i].strip()
        if line not in cuisines:
            cuisines.append(line)

    for i in range(len(cuisines)):
        dict[cuisines[i]] = []

    for i in range(0,len(content),4):
        line = content[i].strip()
        lineBelow = content[i+1].strip()
        dict[lineBelow].append(line)

    return dict



"""
Function Name: createDirectory()
Parameters:  filename (str), output filename (str)
Returns: None (NoneType)
"""

#########################################
########## WRITE FUNCTION HERE ##########
#########################################

def createDirectory(filename, outputFilename):
    readFile = open(filename, 'r')
    writeFile = open(outputFilename, 'w')
    content = readFile.readlines()
    fastfood = []
    sitdown = []
    fastfoodcounter = 1
    sitdowncouter = 1

    for i in range(2,len(content), 4):
        restaurant = content[i-2].strip()
        cuisine = content[i-1].strip()
        group = content[i].strip()

        if group == 'Fast Food':
            fastfood.append(str(fastfoodcounter) + '. ' + restaurant + ' - ' + cuisine + '\n')
            fastfoodcounter += 1
        else:
            sitdown.append(str(sitdowncouter) + '. ' + restaurant + ' - ' + cuisine)
            sitdowncouter += 1

    writeFile.write('Restaurant Directory' + '\n')
    writeFile.write('Fast Food' + '\n')
    writeFile.writelines(fastfood)
    writeFile.write('Sit-down' + '\n')
    for i in range(len(sitdown)):
        if i != len(sitdown)-1:
            writeFile.write(sitdown[i] + '\n')
        else:
            writeFile.write(sitdown[i])





"""
Function Name: extraHours()
Parameters:  filename (str), hour (int)
Returns: list of (person, extra money) tuples (tuple)
"""

#########################################
########## WRITE FUNCTION HERE ##########
#########################################

def extraHours(filename, hour):
    file = open()

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

#print(restaurantFilter('restaurants.txt'))

#print(createDirectory('restaurants.txt','output.txt'))

print(extraHours('groc.csv', 30))






