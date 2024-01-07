"""
Timer V2 is a timer with a new window appear on your screen to tell you when it's finish
"""

import time  # for manage the time
from tkinter import * # for the user interface  

def callback (input):
    if input.isdigit():
        return True
    elif input is "":
        return True
    else:
        return False

def launch():
    if timeChoose.get().isdigit():
        timeElapse = int(timeChoose.get())
        print(timeElapse)
        #start_message = Label(root, text="Start timer").pack(side=BOTTOM)
        # new window
        countDown = Tk()
        countDown.title("Timer count down")
        countDown.geometry("300x300+400+50")
        time.sleep(timeElapse)
        end_message = Label(countDown, text="Your timer is finish").pack()
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
        
# do a complete user interface for the timer (asking to sending)
# display the time elpased --> V3