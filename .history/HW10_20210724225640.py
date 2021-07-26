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

    def loseLife(self)
    
    def gainLife(self):
        if self.lives > 0 and self.lives < 3:
            self.lives += 1
        elif self.lives >= 3:
            self.coins += 10

    def __str__(self):
        return "Hi! I am {}. I have {} lives left and {} coins.".format(self.name, self.lives, self.coins)


##########################################################


class Bowser:

    # the following method is provided to you
    def __eq__(self, other):
        return (self.name == other.name and
                self.lives == other.lives and
                self.isAlive == other.isAlive)

    # the following method is provided to you
    def __repr__(self):
        return f"Bowser({self.name})"


##########################################################


class World:
    
    # the following method is provided to you
    def __repr__(self):
        return f"World({self.name}, {self.bowser})"
    

mario = Mario('mario1', 5, 20, False)
print(mario)