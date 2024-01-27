'''
TimerV4,
goals: user interface with tkinter and countdown of the time choose by the user
'''

import time  # for manage the time
from tkinter import * # for the user interface

def read_entry():
    global display
    if entry.get().isdigit():
        # Launch the process
        print("OK")
        error_message.destroy()
    else:
        # ask for an other input
        print("not OK")
        if display == False:
            error_message.pack()
            display = True

display = False
# user interface
window = Tk()

# dimension of the window
window.geometry("500x600")

# title of the window
title = Label(window, text = "Welcome in Timer V4", font=("Arial", 25))
title.pack(padx=50, pady=20)

# entry text and entry
entry_text = Label(window, text = "How many seconds you want to elapse ?")
entry_text.pack()
entry = Entry(window)
entry.pack(pady=10)

# error message
error_message = Label(window, text="Make sure to write an number")

#button
submit_button = Button(window, text="Submit", command=read_entry).pack(pady=10)
quit_button = Button(window, text="Quit", command=window.destroy).pack()
'''
countdown = Tk()
countdown.geometry("200x200")
message = Label(countdown, text="test").pack()
countdown.mainloop()
'''

window.mainloop()
'''
# asking user
while True:
    try:
        # user input
        timeToElapse = 
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
'''