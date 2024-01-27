'''
Timer V3,
goal: user interface and seconds elapsed on the screen, in console
'''

import time  # for manage the time
from tkinter import * # for the user interface

# user interface
print("==================================================")
print("\tWelcome in the timer's interface")
print("==================================================")
print("Write below the time you want to elapse (in seconds please)")

# asking user
while True:
    try:
        # user input
        timeToElapse = int(input())
    except TypeError:   # if it isn't a number
        print("Make sure to write number")
    else:
        # success message
        print("The time has been correcty store")
        break

print("\nTime begin to elapse...")
startSeconds = time.time()  # get the number of seconds since the epochs
currentSeconds = time.time()
oldSecondsElapsed = 0
# until the time select by the user is elapsed
while currentSeconds - startSeconds < timeToElapse:
    secondsElapsed = round(currentSeconds - startSeconds)   # the current time elapsed, round to an integer
    # when the perfectly one second has been elapsed
    if secondsElapsed > oldSecondsElapsed:
        print(secondsElapsed, "seconds has been elapsed", end="\r")
        oldSecondsElapsed = round(currentSeconds - startSeconds)    # update the variable for the next time
    currentSeconds = time.time()    # always update the current time
print("\nTime finish to elapse")