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
    cake_time = cakes*100 #time in minutes for each cake
    cupcakes_time = cupcakes*70 #same as above but for the other items
    cookies_time = cookies*45

    total_time = cake_time + cupcakes_time + cookies_time #stores the total time used to make all the items

    hours = total_time//60 #converts the total minutes into the appropriate amount of hours and minutes
    minutes = total_time % 60 

    print('It will take {} hours and {} minutes to make {} cakes, {} cupcakes, and {} cookies.'.format(hours, minutes, cakes, cupcakes, cookies)) #formats the 

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



bake(1, 3, 12)