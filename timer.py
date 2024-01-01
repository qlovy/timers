"""
This file show the possibility with the timer module

This also the first version of the timer V1

PS: maybe add the dateTime module ??

"""

import time

# time from epoch (1 January 1970 00:00:00)
seconds = time.time()
print("The number of seconds from the epoch ", seconds)

# convertion of time from the epoch in datetime
localTime = time.ctime(seconds)
print("The local time ", localTime)

# delay
print("This is the start of the countdown of 5 seconds")
time.sleep(5)
print("The countdown is over")

# timer V1
while True:
    try:
        timeChosen = int(input("\nSelect your time for the timer (in seconds pls)\n"))
    except:
        print("\nMake sure to write a number")
    else:
        print("\nYour timer start now")
        time.sleep(timeChosen)
        print("\nDing Ding Ding, it's over now !")

