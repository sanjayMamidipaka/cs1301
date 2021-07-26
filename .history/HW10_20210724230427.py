"""
Georgia Institute of Technology - CS1301
Homework 08 - Object Oriented Programming
"""

class Mario:

    def __init__(self, name, lives, coins, isAlive):
        self.name = name
        self.lives = lives
        self.coins = coins 
        self.isAlive = isAlive 

    
    # the following method is provided to you
    def __eq__(self, other):
        return (self.name == other.name and
                self.lives == other.lives and
                self.coins == other.coins and
                self.isAlive == other.isAlive)

    # the following method is provided to you
    def __repr__(self):
        return f"Mario({self.name})"

    def gainCoins(self, numberOfCoins):
        self.coins += numberOfCoins

    def gainCoins(self):
        self.coins += 5

    def loseLife(self):
        if self.lives != 0:
            self.lives -= 1

            if self.lives == 0:
                self.isAlive = False
    
    def gainLife(self):
        if self.lives > 0 and self.lives < 3:
            self.lives += 1
        elif self.lives >= 3:
            self.coins += 10

    def __str__(self):
        return "Hi! I am {}. I have {} lives left and {} coins.".format(self.name, self.lives, self.coins)


##########################################################


class Bowser:

    def __init__(self, name, lives, isAlive):
        self.name = name 
        self.lives = lives 
        self.isAlive = isAlive 
    
    # the following method is provided to you
    def __eq__(self, other):
        return (self.name == other.name and
                self.lives == other.lives and
                self.isAlive == other.isAlive)

    # the following method is provided to you
    def __repr__(self):
        return f"Bowser({self.name})"

    def loseLife(self):
        if self.lives != 0:
            self.lives -= 1

            if self.lives == 0:
                self.isAlive = False

    def __str__(self):
        return "Hi! I am {} and I have {} lives left.".format(self.name, self.lives)



##########################################################


class World:
    
    def __init__(self, name, characters, bowser, isWon):
        self.name = name 
        self.characters = characters 
        self.bowser = bowser 
        self.isWon = isWon 

    def __init__(self, name, bowser, isWon):
        self.name = name 
        self.characters =  
        self.bowser = bowser 
        self.isWon = isWon 
    
    # the following method is provided to you
    def __repr__(self):
        return f"World({self.name}, {self.bowser})"
    

