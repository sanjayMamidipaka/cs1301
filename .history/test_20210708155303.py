# -*- coding: utf-8 -*-
print(88/2)
print(type(88/2))

print(int(8.8) + float("3"))

print(True and False and True or False or not True)
print(not (False or True and False) and (False and False or True))
print(not False or True and False)
print(12/0)

activity = 'sk0y'
myActivity = ''
mySum = 0
for char in activity:
    if char in '0123456789':
        num = int(char)
        mySum += 12 / num 
    else:
        