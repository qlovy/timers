'''
Timer V3,
goal: user interface and seconds elapsed on the screen
'''

import time  # for manage the time
from tkinter import * # for the user interface

# user interface
print("==================================================")
print("\tWelcome in the timer's interface")
print("==================================================")
print("Write below the time you want to elapse (in seconds please)")

while True:
    try:
        timeToElapse = int(input())
    except TypeError:
        print("Make sure to write number")
    else:
        print("The time has been correcty store")
        break

print("\nTime begin to elapse...")
startSeconds = time.time()
currentSeconds = time.time()
oldSecondsElapsed = 0
while currentSeconds - startSeconds < timeToElapse:
    secondsElapsed = round(currentSeconds - startSeconds)
    if secondsElapsed > oldSecondsElapsed:
        print(secondsElapsed, "seconds has been elapsed", end="\r")
        oldSecondsElapsed = round(currentSeconds - startSeconds)
    currentSeconds = time.time()
print("\nTime finish to elapse")