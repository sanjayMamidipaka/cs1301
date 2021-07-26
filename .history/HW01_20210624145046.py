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

    print('It will take {} hours and {} minutes to make {} cakes, {} cupcakes, and {} cookies.'.format(hours, minutes, cakes, cupcakes, cookies)) #formats the information and prints out the results

#########################################

"""
Function Name: cakeVolume()
Parameters: radius (int), height (int)
Returns: None
"""
def cakeVolume(radius, height):
    volume = 3.14 * radius**2 * height #calculating volume with the volume formula
    rounded_volume = round(volume, 2) #rounding my answer to 2 places
    print('The volume of the cake is {}.'.format(rounded_volume))

#########################################

"""
Function Name: celebrate()
Parameters: pizzas (int), pastas (int), burgers (int), tipPercent (int)
Returns: None
"""
def celebrate(pizzas, pastas, burgers, tipPercent):
    pizzas_price = pizzas*14
    pastas_price = pastas*10
    burgers_price = burgers*7
    total_price = pizzas_price + pastas_price + burgers_price
    total_price_rounded = round(total_price, 2)
    tip = total_price * (tipPercent/100)
    tip_rounded = round(tip, 2)
    print('You paid ${} and tipped ${}.').format(total_price_rounded, tip_rounded)

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
cakeVolume(5, 8)
celebrate(3, 4, 2, 10)