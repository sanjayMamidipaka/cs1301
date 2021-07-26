"""
Georgia Institute of Technology - CS1301
Homework 08 - Object Oriented Programming
"""

class Mario:

    def __i
    
    # the following method is provided to you
    def __eq__(self, other):
        return (self.name == other.name and
                self.lives == other.lives and
                self.coins == other.coins and
                self.isAlive == other.isAlive)

    # the following method is provided to you
    def __repr__(self):
        return f"Mario({self.name})"


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
    
