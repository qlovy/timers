"""
TimerV4,
goals: user interface with tkinter and countdown of the time choose by the user
"""

import time  # for manage the time
from tkinter import *  # for the user interface


def read_entry():
    global display  # for using it in the function
    if entry.get().isdigit():
        # Launch the process
        error_message.destroy()  # remove the error message
        launch_timer()
    else:
        # ask for other input
        if not display:
            error_message.pack()
            display = True


def launch_timer():
    time_choose = int(entry.get())  # convert the value of the entry
    start_message = Label(window, text="Time starts now")
    start_message.pack(pady=(40, 10))
    start_seconds = time.time()  # the reference time
    current_seconds = time.time()  # the current time
    time_elapse = round(current_seconds - start_seconds)
    perfect_seconds = 0  # use for the perfect "change" of second
    while time_elapse < time_choose:
        time_elapse = round(current_seconds - start_seconds)  # update the value
        message = "Time elapsed: " + str(time_elapse)
        if time_elapse != perfect_seconds:  # detection of one second being elapsed
            # if we are at the start of the countdown
            if perfect_seconds != 0:
                time_spend.destroy()  # remove the message
            time_spend = Label(window, text=message)
            time_spend.pack()  # display the message of the time elapse
            perfect_seconds = time_elapse  # update the value
        current_seconds = time.time()  # get the current time
        window.update()
    end_message = Label(window, text="Time is finished")
    end_message.pack(pady=10)


display = False

# user interface
window = Tk()

# dimension of the window
window.geometry("500x400")

# title of the window
title = Label(window, text="Welcome in Timer V4", font=("Arial", 25))
title.pack(padx=50, pady=20)

# entry text and entry
entry_text = Label(window, text="How many seconds do you want to elapse ?")
entry_text.pack()
entry = Entry(window)
entry.pack(pady=10)

# error message
error_message = Label(window, text="Make sure to write an number")

# button
submit_button = Button(window, text="Submit", command=read_entry)
submit_button.pack(pady=10)
quit_button = Button(window, text="Quit", command=window.destroy)
quit_button.pack()

window.mainloop()
