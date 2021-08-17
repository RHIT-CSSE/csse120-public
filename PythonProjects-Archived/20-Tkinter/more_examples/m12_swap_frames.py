"""
A simple example to show how to swap between frames.
It assumes that you are using   grid   as your layout manager,
It assumes that you are using the  ttk  extension to Tkinter.
"""

from tkinter import *
from tkinter.ttk import *


# The following functions hide one Frame and make the other Frame visible.
def show_frame1():
    global frame1, frame2
    frame2.grid_remove()
    frame1.grid()


def show_frame2():
    global frame1, frame2
    frame1.grid_remove()
    frame2.grid()


# Root (main) window
root = Tk()

# A Frame object on the root window.  It has a Label and Button on it.
# Pressing the button makes its Frame disappear and the other Frame appear.
frame1 = Frame(root, padding=10)
label1 = Label(frame1, text="This is frame 1")
button1 = Button(frame1, text="Switch to Frame 2", command=show_frame2)
label1.grid(row=1, column=1)  # Uses  grid  instead of  place  as layout manager
button1.grid(row=1, column=2)

# The other Frame object, with its own Label and Button.
frame2 = Frame(root, padding=10)
label2 = Label(frame2, text="This is frame 2")
button2 = Button(frame2, text="Switch to Frame 1", command=show_frame1)
label2.grid(row=1, column=1)  # Do you see how  grid  works?
button2.grid(row=2 ,column=1)

# Initially, frame1 appears.
frame1.grid()

root.mainloop()