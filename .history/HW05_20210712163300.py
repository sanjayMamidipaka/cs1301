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
    

    for i in vowelDictionary.keys():
        for letter in i:
            if letter in 'aeiouAEIOU':
                vowelDictionary[i] += 1

    return vowelDictionary

"""
Function Name: calculator()  
Parameters: dictionary of numerators and denominators (dict)
Returns: sum of valid fractions and the count of errors (tuple)
"""

#########################################
########## WRITE FUNCTION HERE ##########
#########################################

def calculator(fractionDictionary):
    sum = 0.0
    errorCount = 0
    for i in fractionDictionary:
        try:
            sum += i/fractionDictionary[i]
        except Exception as e:
            errorCount += 1

    return (round(sum, 2), errorCount)

"""
Function Name: scavengerHunt()  
Parameters: list of animals (list)
Returns: results of the scavenger hunt (dict)
"""

#########################################
########## WRITE FUNCTION HERE ##########
#########################################

def scavengerHunt(animalList):
    animalsNotFoundList = []
    resultDict = {'Animals Not Found': (), 'Total Points': 0}
    for animal in animalList:
        calculatedValue = calculate(animal)
        if calculatedValue == 0:
            animalsNotFoundList.append(animal)
        else:
            resultDict['Total Points'] += calculatedValue

    
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


# cities = ['Atlanta', 'New York', 'Boston', 'LosAngeles']
# print(vowelCounter(cities))

# numDict = {1:0, 2:3, 4:5, '&':7, 0:9, 5:13}
# print(calculator(numDict))

animals = ['Dolphin', 'Sea Lion', 'Jellyfish','Humpback Whale', 'Lion', 'Tiger','Eagle', 'Platypus']
print(scavengerHunt(animals))

