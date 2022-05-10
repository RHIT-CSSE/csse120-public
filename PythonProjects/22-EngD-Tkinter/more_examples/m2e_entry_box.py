"""
Example showing for tkinter and ttk:
  -- ttk.Entry
  -- Using its GET and SET methods to get/set an Entry's information
     (as opposed to using a CONTROL VARIABLE as in a subsequent module)

     This is the SIMPLER way to use an Entry box.
     See a subsequent module for a more complicated alternative that is
     sometimes more convenient than this way.

Authors: David Mutchler and his colleagues
         at Rose-Hulman Institute of Technology.
"""

import tkinter
from tkinter import ttk


def main():
    root = tkinter.Tk()

    frame1 = ttk.Frame(root, padding=10)
    frame1.grid()

    my_entry_box = ttk.Entry(frame1)
    my_entry_box.grid()

    print_entry_button = ttk.Button(frame1, text="Print entry")
    print_entry_button["command"] = lambda: print_contents(my_entry_box)
    print_entry_button.grid()

    root.mainloop()


def print_contents(entry_box):
    """
    Prints onto the Console the contents of the given ttk.Entry.

    In this example, it is used as the function that is "CALLED BACK"
    when an event (namely, the pressing of a certain Button) occurs.

    Type hints:
      :type entry_box: ttk.Entry
    """
    contents_of_entry_box = entry_box.get()
    print(contents_of_entry_box)


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
