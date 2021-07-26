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

    resultDict['Animals Not Found'] = tuple(animalsNotFoundList)

    return resultDict
"""
Function Name: classRoster()  
Parameters: students mapped to their classes (dict)
Returns: classes mapped to their students (dict)
"""

#########################################
########## WRITE FUNCTION HERE ##########
#########################################

def classRoster(students):
    classList = []
    for classes in students.values():
        for class1 in classes:
            if class1 not in classList:
                classList.append(class1)

    classDictionary = {}
    for i in classList:
        classDictionary[i] = []

    for class2 in classList:
        for student, classes in students.items():
            if class2 in classes:
                classDictionary[class2] += [student]
        classDictionary[class2] = sorted(classDictionary[class2])


    return classDictionary


"""
Function Name: musicFestival()  
Parameters: festivals mapped to list of headlining artists (dict),
            artists (list), number of artists (int)
Returns: festival name mapped to number of matching artists (dict)
"""

#########################################
########## WRITE FUNCTION HERE ##########
#########################################

def musicFestival(festivals, artists, numberOfArtists):
    festivalNames = festivals.keys()
    finalDict = {}
    for i in festivalNames:
        finalDict[i] = 0

    for artist in artists:
        for festival, artistsPerforming in 


# cities = ['Atlanta', 'New York', 'Boston', 'LosAngeles']
# print(vowelCounter(cities))

# numDict = {1:0, 2:3, 4:5, '&':7, 0:9, 5:13}
# print(calculator(numDict))

# animals = ['Dolphin', 'Sea Lion', 'Jellyfish','Humpback Whale', 'Lion', 'Tiger','Eagle', 'Platypus']
# print(scavengerHunt(animals))

# students = {'Kathleen':['cs1332','cs2050','psyc2015'],'Elizabeth':['math3012','cs2050','cs1332','cs3510'],'Emily': ['cs1301','psyc2015','cs3510']}
# print(classRoster(students))

festivals = {"Music Midtown": ["Maroon 5", "MileyCyrus", "21 Savage","DaBaby", "Megan Thee Stallion", "Lauv","Machine Gun Kelly", "Jonas Brothers"],"Shaky Knees": ["The Strokes", "Mac Demarco","The Backseat Lovers", "Dominic Fike","St. Vincent"],"Lollapalooza": ["Dominic Fike", "Dayglow", "Lauv","Boy Pablo","The Backseat Lovers","Mt.Joy", "Young the Giant"]}
artistList = ["Declan Mckenna", "Peach Pit", "GlassAnimals", "The BackseatLovers", "COIN", "Dominic Fike"]
musicFestival(festivals, artistList, 2)