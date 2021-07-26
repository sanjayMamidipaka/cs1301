"""
Georgia Institute of Technology - CS1301 - Summer 2021
HW08 Part 2 - Recursion
Collaboration Statement:
"""

#########################################

"""
Function Name: doubleChars()  
Parameters: sentence (str)   
Returns: number of times there are two of the same
         characters in a row (int)
"""

#########################################
########## WRITE FUNCTION HERE ##########
#########################################

def doubleChars(sentence):
    if len(sentence) < 2:
        return 0
    else:
        firstChar = sentence[0]
        secondChar = sentence[1]

        if firstChar == secondChar:
            return 1 + doubleChars(sentence[1:])
        else:
            return doubleChars(sentence[1:])

"""
Function Name: sumOfNums()  
Parameters: string of characters (str)
Returns: sum of the digits within the string (int)
"""

#########################################
########## WRITE FUNCTION HERE ##########
#########################################

def sumOfNums(stringOfNums):
    if len(stringOfNums) == 0:
        return 0
    else:
        firstCharacter = 0
        try:
            firstCharacter = int(stringOfNums[0])
        except Exception as e:
            pass
        



sentence = "The year was 2004..Hilary Duff ruled the world!!"  
print(doubleChars(sentence))  