#!/usr/bin/python3
import time
from math import floor
'''
The Guassian Algorithmn for determing the day of the week (0-6), a purely
mathematical function, compared to tabular methods (mod 7 from a know date.)

http://calendars.wikia.com/wiki/Calculating_the_day_of_the_week#The_algorithm_to_calculate_the_day_of_the_week

https://en.wikipedia.org/wiki/Determination_of_the_day_of_the_week#Gauss.27_algorithm

From calendars.wikia.com:
w = (d + floor(2.6m-0.2) + y + floor(y/4) + floor(c/4) - 2c) % 7

'''
def leapYear(y):
    if (y % 4) != 0:
        return False
    elif (y % 100) != 0:
        return True
    elif (y % 400) != 0:
        return False
    else: return True

def calcWeekDay(curDay,curMonth,curYear):
    leapBool = leapYear(curYear)
    
    if curMonth == 1 or curMonth == 2:
        curYear = curYear - 1

    m = ((curMonth + 9) % 12) + 1

    y = str(curYear)
    c = y[0:2]
    y = y[2:4]

    d = curDay

    m = float(m)
    y = float(y)
    c = float(c)
    d = float(d)

    w = (d + (floor((2.6*m)-0.2)) + y + (floor(y/4)) + (floor(c/4)) - (2*c))
    w = w%7
    return int(w), leapBool
    

#For direct testing
if __name__ == "__main__":
    weekNames = ("Sun","Mon","Tue","Wed","Thu","Fri","Sat")
    monthNames=("NULL","January","February","March","April","May","June","July","August","September","October","November","December")

    w = calcWeekDay(1,1,2015)[0]
    print("First day of",monthNames[1],2015, "is", weekNames[w])

    w = calcWeekDay(1,2,2015)[0]
    print("First day of",monthNames[2],2015, "is", weekNames[w])

    w = calcWeekDay(1,2,2013)
    print("Feb 2013 is a leap year?",w[1],weekNames[w[0]]) 

