"""
Georgia Institute of Technology - CS1301
HW03 - Strings and Lists
Collaboration Statement:
"""

#########################################

"""
Function Name: movieNight()  
Parameters: subtitle (str)
Returns: fixed subtitle (str)
"""

#########################################
########## WRITE FUNCTION HERE ##########
#########################################

def movieNight(subtitle):
    newSubtitle = ''
    for i in subtitle:
        if not i.isdigit():
            newSubtitle += i 
    return newSubtitle

"""
Function Name: longestWord()
Parameters: sentence (str)
Returns: longest word (str)
"""

#########################################
########## WRITE FUNCTION HERE ##########
#########################################

def longestWord(sentence):
    newSentence = ''
    for i in sentence:
        if not i == ',':
            newSentence += i
    list1 = newSentence.split(' ')
    
    length = 0
    longestWord = ''
    for i in list1:
        if len(i) >= length:
            length = len(i)
            longestWord = i

    return longestWord

"""
Function Name: tennisMatch()
Parameters: player1 (str), player2 (str), matchRecord (str)
Returns: game statement (str)
"""

#########################################
########## WRITE FUNCTION HERE ##########
#########################################

def tennisMatch(player1, player2, matchRecord):
    player1Points = 0
    player2Points = 0
    matchesWonPlayer1 = 0
    matchesWonPlayer2 = 0
    for i in matchRecord:
        if i == '1':
            player1Points += 1
        elif i == '2':
            player2Points += 1
        elif i == '-':
            if player1Points > player2Points:
                matchesWonPlayer1 += 1
            elif player2Points > player1Points:
                matchesWonPlayer2 += 1

            player1Points = 0
            player2Points = 0

    if matchesWonPlayer1 > matchesWonPlayer2:
        return player1 + ' won! The score was ' + str(matchesWonPlayer1) + str('-') + str(matchesWonPlayer2)
    elif matchesWonPlayer2 > matchesWonPlayer1:
        return player2 + ' won! The score was ' + str(matchesWonPlayer2) + str('-') + str(matchesWonPlayer1)
    else:
        return "It's a tie"




"""
Function Name: freshFruit()
Parameters: barcodes (list), startIndex (int), stopIndex (int)
Returns: freshest barcode (int)
"""

#########################################
########## WRITE FUNCTION HERE ##########
#########################################

def freshFruit(barcodes, startIndex, stopIndex):
    newList = barcodes[startIndex:stopIndex+1]
    maxElement = newList[0]

    for i in newList:
        if i > maxElement:
            maxElement = i 

    return maxElement


"""
Function Name: highestSum()
Parameters: stringList (list)
Returns: highest sum index (int)
"""

#########################################
########## WRITE FUNCTION HERE ##########
#########################################

def highestSum(stringList):
    tempSum = 0
    listOfLengths = 0
    for string in stringList:
        for i in string:
            







# subtitle = "Mr. and M4rs. Dursley of nu28mber four, Privet Drive, wer903e proud to say th6at they we6re perfectly norm3al, tha894nk you ve89ry much."
# print(movieNight(subtitle))

# sentence = " abc def ghi jkl mno "
# print(longestWord(sentence))

# print(tennisMatch("Emily", "Kathleen", "1122-22211-11122-1212-"))

# print(freshFruit([313414, 2241221, 32432, 49204, 493204, 23212], 2, 4))

