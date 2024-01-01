"""
Timer V2 is a timer with a new window appear on your screen to tell you when it's finish
"""

import time
import tkinter as tk

while True:
    try:
        timeChosen = int(input("\nSelcet the time for the timer (in seconds pls)"))
    except:
        print("\nMake sur to write an numbre")
    else:
        print("\nThe timer starts now")
        time.sleep(timeChosen)
        # the new window
        window = tk.Tk()
        title = tk.Label(text = "Your timer is finished")
        title.pack()
        window.mainloop()

# do a complete user interface for the timer (asking to sending)
# display the time elpased
