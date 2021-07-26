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

    def gainCoins():



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
    
