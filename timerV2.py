"""
Timer V2 is a timer with a new window appear on your screen to tell you when it's finish
"""

import time  # for manage the time
from tkinter import * # for the user interface  

# confirm the stat of the input
def callback (input):
    # number
    if input.isdigit():
        return True
    # nothing
    elif input == "":
        return True
    # other character
    else:
        return False

def launch():
    if timeChoose.get().isdigit():
        timeElapse = int(timeChoose.get())
        # new window
        countDown = Tk()
        countDown.title("Timer count down")
        countDown.geometry("300x300+400+50")
        time.sleep(timeElapse)
        end_message = Label(countDown, text="Your timer is finish").pack()
        quit_button = Button(countDown, text="Quit", command=countDown.destroy).pack()
        countDown.mainloop()

# USER INTERFACE

# root window
root = Tk()
root.title("Timer V2")
# set minimum and the maximum size of the window
root.minsize(200, 200) # width, height
root.maxsize(500, 500)
# set the window to theses dimensions
root.geometry("300x300+50+50") # width x height + x + y

# label
title = Label(root, text="Welcome in your timer", font=("Ubuntu", 20), padx=10,pady=10).pack()
sub_title = Label(root, text="Select the time to elapse (seconds)", pady=10).pack()

# Entry
timeChoose = Entry(root, foreground="black", font=("Ubuntu"))
timeChoose.pack()

# Register callback function
reg = root.register(callback)
timeChoose.config(validate="key", validatecommand=(reg, '%P'))

# Button
LaunchButton = Button(root, text="Launch", command=launch).pack(side=LEFT)  # launch the timer
QuitButton = Button(root, text="Quit", command=root.destroy).pack(side=LEFT)    # quit the window

root.mainloop() # display the window