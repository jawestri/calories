# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 11:35:48 2018
@author: jamiew
"""

import pandas as panda
import matplotlib.pyplot as plt


def calories(s, t, b, n):
    # calc avg speed, mets, and convert ms to hours
    ssum = sum(s)
    avg_speed = ssum/len(s)
    vo2 = (avg_speed*1.8)+avg_speed+3.5
    mets = vo2/3.5
    ms = t[-1]
    convert = 2.7778 * (10**-7)
    hours = (ms * convert)
    # calc calories based on sensor data and user input
    calories = b * (mets/24) * hours

    # display calorie results along with calculation variables
    print("\nFor walk: %s" % n)
    print("Your calories burned during walk: %.2f" % calories)
    print("Your average speed during walk(in mph): %.2f" % avg_speed)
    print("Your BMR: %.2f" % b)
    print("Total time of walk(in hours): %.2f" % hours)
    print("Mets: %.2f" % mets)

# import csv file and read the columns for time and speed
data = panda.read_csv("C:\\Users\\jamiew\\Documents\\GitHub\\test.csv")
data1 = panda.read_csv("C:\\Users\\jamiew\\Documents\\GitHub\\calories\\sensor.csv")
time = data['time']
speed = data['speed']
time1 = data1['time']
speed1 = data1['speed']

# plot graph x = time, y = speed
plt.plot(time, speed, 'm', label='Walk 1')
plt.plot(time1, speed1, 'b', label='Walk 2')
plt.xlabel("Time Elapsed(ms)")
plt.ylabel("Speed  (MPH)")
plt.title("Speed vs. Time")
legend = plt.legend(loc='upper right', shadow=True)
plt.show()

# convert imports to list for calculations
speeds = data.speed.tolist()
times = data.time.tolist()
speeds1 = data1.speed.tolist()
times1 = data1.time.tolist()

# request user import to calc bmr, depends on weight,height, age, gender
print("For estimated calories burn per walk enter following data--")
weight = float(input('Enter Weight in lbs:'))
age = float(input('Enter Age:'))
height = float(input('Enter height in inches:'))
gender = input('Enter m for male, f for female: ')
if gender == 'm':
    bmr = 66 + (6.23 * weight) + (12.7 * height) - (6.8 * age)
elif gender == 'f':
    bmr = 655 + (4.35 * weight) + (4.7 * height) - (4.7 * age)

# call cal calc func
print("\nThe following results are just an estimate based on average speed, your Basal Metabolic Rate(BMR), Metabolic Equivalent Task(Met), and total duration of walk.")
calories(speeds, times, bmr, 1)
calories(speeds1, times1, bmr, 2)

