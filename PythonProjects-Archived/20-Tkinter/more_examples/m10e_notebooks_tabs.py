"""
Example showing for tkinter and ttk how to:
  -- Make "tabs" on what is called a ttk.Notebook.
     Each tab is a page accessed by a tab as in Google and many other apps.

Authors: David Mutchler and his colleagues
         at Rose-Hulman Institute of Technology.
"""

import tkinter
from tkinter import ttk


def main():
    # Root (main) window:
    root = tkinter.Tk()
    root.title("Notebooks (i.e., tabbed pages)")

    # ttk.Notebook on the root:
    notebook = ttk.Notebook(root)
    notebook.grid()

    # Three "tabs" of the Notebook, each containing a Frame, as is typical.
    frame1 = ttk.Frame(notebook)
    frame2 = ttk.Frame(notebook)
    frame3 = ttk.Frame(notebook)

    # The  add   method adds a Frame (or other widget) to the Notebook.
    notebook.add(frame1, text="Dog tab")
    notebook.add(frame2, text="Cats are here")
    notebook.add(frame3, text="Owl")

    # The rest are objects on the Frames, just as examples.
    # Here I have put an image and a button on each frame/tab.
    button = ttk.Button(frame1, text="bark")
    button["command"] = lambda: bark(frame1)
    basset_hound = tkinter.PhotoImage(file="BassetHound.png")
    label = ttk.Label(frame1, image=basset_hound)
    label.grid(row=0, column=0)
    button.grid(row=0, column=1)

    button = ttk.Button(frame2, text="meow")
    button["command"] = lambda: meow(frame2)
    cat = tkinter.PhotoImage(file="Cat.png")
    label = ttk.Label(frame2, image=cat)
    label.grid()
    button.grid()

    button = ttk.Button(frame3, text="hoot")
    button["command"] = lambda: hoot(frame3)
    owl = tkinter.PhotoImage(file="Owl.png")
    label = ttk.Label(frame3, image=owl)
    label.grid(row=0, column=1)
    button.grid(row=0, column=0)

    # The mainloop:
    root.mainloop()


def bark(frame):
    ttk.Label(frame, text="Woof!").grid(column=1)


def meow(frame):
    ttk.Label(frame, text="Meowwwww!").grid()


def hoot(frame):
    ttk.Label(frame, text="whoooo whooo WHOOOO!").grid()


main()