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
        launch_timer()
    else:
        # ask for an other input
        print("not OK")
        if display == False:
            error_message.pack()
            display = True

def launch_timer():
    timeChoose = int(entry.get())
    start_seconds = time.time()
    current_seconds = time.time()
    perfect_seconds = 0
    countdown = Tk()
    countdown.geometry("200x200")
    start_message = Label(countdown, text="Time start now")
    start_message.pack()
    while current_seconds - start_seconds < timeChoose:
        time_elapse = round(current_seconds - start_seconds)
        if time_elapse > perfect_seconds:
            '''
            if perfect_seconds != 0:
                time_elapse_label.destroy()
            '''
            time_elapse_label = Label(countdown, text=time_elapse)
            time_elapse_label.pack()
            perfect_seconds = time_elapse
        current_seconds = time.time()
    stop_message = Label(countdown, text="Time finish")
    stop_message.pack()
    countdown.mainloop()

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