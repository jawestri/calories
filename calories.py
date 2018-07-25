# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 14:29:04 2018

@author: jamiew
"""

# import csv file and read in speeds in mph and times of walk in ms
import csv
with open('C:\\Users\\jamiew\\Documents\\python\\test.csv') as f:
    readCSV = csv.reader(f, delimiter=',')
    speeds = []
    times = []
    for row in readCSV:
        speed = float(row[0])
        time = float(row[1])
        speeds.append(speed)
        times.append(time)


ssum = sum(speeds)
avg_speed = ssum/len(speeds)
vo2 = (avg_speed*1.8)+avg_speed+3.5
mets = vo2/3.5
ms = times[-1]
convert = 2.7778 * (10**-7)
hours = (ms * convert)
      
        
weight= float(input('Enter Weight in lbs:'))
age = float(input('Enter Age:'))
height = float(input('Enter height in inches:'))
gender = input('Enter m for male, f for female: ')
if gender == 'm':
    bmr= 66 + ( 6.23 * weight) + ( 12.7 * height) - ( 6.8 * age)
elif gender == 'f':
    bmr = 655 + ( 4.35 * weight) + ( 4.7 * height) - ( 4.7 * age) 

calories = bmr * (mets/24) * hours

print("\nYour BMR: %s" % bmr)
print("Your calories burned during walk: %s" % calories)
print("Your average speed during walk: %s" % avg_speed)
print("Total time of walk: %s" % hours)
print("Mets: %s" % mets)