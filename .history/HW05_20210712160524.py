from points import calculate
"""
Georgia Institute of Technology - CS1301
HW05 - Modules, Dictionaries, Try/Except
Collaboration Statement:
"""

#########################################

"""
Function Name: vowelCounter()  
Parameters: cities (list)
Returns: number of vowels in each city (int)
"""

#########################################
########## WRITE FUNCTION HERE ##########
#########################################

def vowelCounter(cities):
    vowelDictionary = dict.fromkeys(cities, 0)
    print(vowelDictionary)

    for i in vowelDictionary.keys():
        for letter in i:
            if letter in 'aeiouAEIOU':
                vowelDictionary[i] += 1

"""
Function Name: calculator()  
Parameters: dictionary of numerators and denominators (dict)
Returns: sum of valid fractions and the count of errors (tuple)
"""

#########################################
########## WRITE FUNCTION HERE ##########
#########################################

"""
Function Name: scavengerHunt()  
Parameters: list of animals (list)
Returns: results of the scavenger hunt (dict)
"""

#########################################
########## WRITE FUNCTION HERE ##########
#########################################

"""
Function Name: classRoster()  
Parameters: students mapped to their classes (dict)
Returns: classes mapped to their students (dict)
"""

#########################################
########## WRITE FUNCTION HERE ##########
#########################################


"""
Function Name: musicFestival()  
Parameters: festivals mapped to list of headlining artists (dict),
            artists (list), number of artists (int)
Returns: festival name mapped to number of matching artists (dict)
"""

#########################################
########## WRITE FUNCTION HERE ##########
#########################################


cities = ['Atlanta', 'New York', 'Boston', 'LosAngeles']
vowelCounter(cities)

