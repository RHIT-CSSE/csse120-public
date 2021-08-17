"""
Example showing for tkinter and ttk, how to:
  -- make multiple screens appear SEQUENTIALLY (one after the other),
  -- with the user interacting with each as it appears,
  -- and data persisting from one screen to the next.

There are many ways to accomplish this.  This example shows a simple,
principled way to handle a wide variety of interfaces with multiple screens.

Authors: David Mutchler and his colleagues
         at Rose-Hulman Institute of Technology.
"""

import tkinter
from tkinter import ttk


def main():
    gui = GUI()
    gui.start()


class GUI(object):
    # In this example, the tkinter.Tk object is the main and ONLY window.
    # Each SCREEN is a FRAME in the one and only window.
    root = tkinter.Tk()
    root.title("Example showing multiple windows appearing sequentially")


class Screen(object):
    def __init__(self, root, frame):
        self.root = root
        self.frame = frame

    def show
        self.frame = ttk.LabelFrame(text="Frame 1")  # a ttk.Frame works too

    def show_next_screen(self, next_frame):
        self.frame.destroy()
        next_frame.grid()

    # Make all the frames, but do not grid any of them yet.
    # Put each on the root window.

    frame1 = ttk.Frame(root)
    frame1.grid()

    # Label
    label = ttk.Label(frame1, text="This is a Label above a Button")
    label.grid()

    # Two buttons
    change_title_button = ttk.Button(frame1, text="Change the Title (above)")
    change_title_button.grid()
    change_title_button["command"] = lambda: change_title(root)

    quit_button = ttk.Button(frame1, text="Quit")
    quit_button.grid()
    quit_button["command"] = lambda: close_window(root)

    # Another Label, with its text set another way
    label2 = ttk.Label(frame1)
    label2["text"] = "Later, we will put Labels BESIDE Buttons"
    label2.grid()

    root.mainloop()


def change_title(root):
    # Make a new 8-letter title chosen randomly from 'A' to 'Z'.
    new_title = ""
    for _ in range(8):
        new_title = new_title + chr(ord("A") + random.randrange(26))

    root.title(new_title)


def close_window(root):
    root.destroy()


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()