# -*- coding: utf-8 -*-
print(88/2)
print(type(88/2))

print(int(8.8) + float("3"))

print(True and False and True or False or not True)
print(not (False or True and False) and (False and False or True))
print(not False or True and False)
print(12/0)

def beach(act):
    if act == 'sleep':
        return 'No fun!':
    else:
        print('Fun!')

def vacation(act):
    if beach(act) == 'No Fun!':
        print('bad vacay')
    elif beach(act) == 'Fun!':
        print('best vacay')
    else:
        print("It's a good day!")

vacation('swim')