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
    for i in list1:
        if len(i) >=

"""
Function Name: tennisMatch()
Parameters: player1 (str), player2 (str), matchRecord (str)
Returns: game statement (str)
"""

#########################################
########## WRITE FUNCTION HERE ##########
#########################################



"""
Function Name: freshFruit()
Parameters: barcodes (list), startIndex (int), stopIndex (int)
Returns: freshest barcode (int)
"""

#########################################
########## WRITE FUNCTION HERE ##########
#########################################


"""
Function Name: highestSum()
Parameters: stringList (list)
Returns: highest sum index (int)
"""

#########################################
########## WRITE FUNCTION HERE ##########
#########################################




# subtitle = "Mr. and M4rs. Dursley of nu28mber four, Privet Drive, wer903e proud to say th6at they we6re perfectly norm3al, tha894nk you ve89ry much."
# print(movieNight(subtitle))

# sentence = " Pop stars, Dua Lipa wit DaBaby "
# print(longestWord(sentence))