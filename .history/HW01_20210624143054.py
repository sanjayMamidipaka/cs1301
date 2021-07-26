"""
Georgia Institute of Technology - CS1301
HW01 - Functions and Expressions
Collaboration Statement:
"""

#########################################

"""
Function Name: bake()
Parameters: cakes (int), cupcakes (int), cookies (int)
Returns: None
"""
def bake(cakes, cupcakes, cookies):
    cake_time = cakes*100
    cupcakes_time = cupcakes*70
    cookies_time = cookies*45

    total_time = cake_time + cupcakes_time + cookies_time

    hours = total_time/60
    minutes = total_time % 60

    print('It will take 12 hours and 10 minutes to make 2 cakes,5 cupcakes, and 4cookies.)

#########################################

"""
Function Name: cakeVolume()
Parameters: radius (int), height (int)
Returns: None
"""
def cakeVolume(radius, height):
    pass

#########################################

"""
Function Name: celebrate()
Parameters: pizzas (int), pastas (int), burgers (int), tipPercent (int)
Returns: None
"""
def celebrate(pizzas, pastas, burgers, tipPercent):
    pass

#########################################

"""
Function Name: bookstore()
Parameters: daysBorrowed (int)
Returns: None
"""
def bookstore(daysBorrowed):
    pass

#########################################

"""
Function Name: monthlyAllowance()
Parameters: allowance (int), savingsPercentage (int)
Returns: None
"""
def monthlyAllowance(allowance, savingsPercentage):
    pass



print(1)