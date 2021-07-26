# -*- coding: utf-8 -*-

def summerWeather(weather):
    output = ['sunny', 0, 'rainy', 0]
    sunnyDays = 0
    rainyDays = 0
    for char in weather:
        if char == 's':
            sunnyDays += 1
        else if char == 'r':
            rainyDays += 1

    output[1] = sunnyDays
    output[3] = rainyDays
    return output

summerWeather('ss')

