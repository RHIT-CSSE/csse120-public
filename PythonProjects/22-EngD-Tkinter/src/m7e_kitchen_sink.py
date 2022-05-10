"""
Example showing a "kitchen sink" of tkinter/ttk widgets.

Do NOT use the CODE herein as an example -- it is TERRIBLE code
spliced together from the INDIVIDUAL examples
in the    more_examples   folder in this project.

Look at those INDIVIDUAL examples for CODE to use as examples.

Authors: David Mutchler and his colleagues
         at Rose-Hulman Institute of Technology.
"""

import tkinter
from tkinter import ttk
import time


# -----------------------------------------------------------------------------
# Code for the root (main) window and the widgets that appear on it.
# -----------------------------------------------------------------------------
def main():
    # Root (main) window:
    root = tkinter.Tk()
    root.title("A kitchen sink of ttk/Tkinter widgets")
    ttk.Style().configure('TLabel', font="Consolas")

    # Frame and sub-frames:
    frame = ttk.Frame(root, padding=10, borderwidth=10, relief="groove")
    instructions_frame = ttk.Frame(frame, padding=20, relief="raised")
    buttons_frame = ttk.Frame(frame, padding=20, relief="groove")

    frame.grid()
    instructions_frame.grid(row=0, column=0)
    buttons_frame.grid(row=0, column=1)

    # Label for instructions, Buttons:
    make_instructions(instructions_frame)
    make_buttons(root, buttons_frame)

    # Menu:
    make_menu(root)

    # Key binding:
    root.bind_all("<Key-Up>", lambda event: make_canvas())

    root.mainloop()


def make_instructions(frame):
    instructions = ["This shows a 'kitchen sink' of tkinter/ttk widgets.",
                    "Try its various buttons et al to experience them.",
                    "",
                    "Do NOT use this module's CODE as sample code;",
                    "it is NOT written for clarity",
                    "and has TERRIBLE style.",
                    "",
                    "Instead, for sample code look at the modules",
                    "in the   more_examples   folder in this project."]
    centered_instructions = make_centered_instructions(instructions)
    ttk.Label(frame, text=centered_instructions).grid()


def make_buttons(root, frame):
    buttons_info = [["Entry box", make_entry_box],
                    ["Canvas", make_canvas],
                    ["Checkboxes and Radiobuttons", make_checks_and_radios],
                    ["Images", make_images],
                    ["Pop-up Windows", make_pop_up_windows],
                    ["Show events and binding", show_events],
                    ["Quit", root.destroy]]

    labels_info = ["Notice the pull-down MENU up top",
                   "Press the UP ARROW key and see what happens!"]

    for button_info in buttons_info:
        button = ttk.Button(frame, text=button_info[0])
        button["command"] = button_info[1]
        button.grid()

    for label_info in labels_info:
        label = ttk.Label(frame, text="\n" + label_info + "\n")
        label.grid()


def make_frame():
    window = tkinter.Toplevel()
    frame = ttk.Frame(window, border=20)
    frame.grid()
    return frame


def make_centered_instructions(instructions):
    longest = len(instructions[0])
    for instruction in instructions:
        if len(instruction) > longest:
            longest = len(instruction)

    centered_instructions = ""
    for instruction in instructions:
        centered_instruction = instruction.center(longest)
        centered_instructions += centered_instruction + "\n"

    return centered_instructions


# -----------------------------------------------------------------------------
# Code that demonstrates an Entry box and a Button.
# -----------------------------------------------------------------------------
def make_entry_box():
    # Window and frame for this widget:
    frame = make_frame()

    # Instructions:
    instructions = ["",
                    "Type something in the Entry box",
                    "that appears to the right.",
                    "",
                    "Then press the above Button",
                    "and watch what appears",
                    "in the Label to the right.",
                    "",
                    "Then repeat the above several times",
                    "to see how the Label to the right",
                    "stores the history of the contents",
                    "of the Entry box."]
    centered_instructions = make_centered_instructions(instructions)
    label = ttk.Label(frame, text=centered_instructions)
    label.grid(row=1, column=0)

    # Entry box and its cumulative contents:
    entry_box = ttk.Entry(frame)
    entry_box.grid(row=0, column=1)

    label_for_contents = ttk.Label(frame, text="The Entry box contained:")
    label_for_contents.grid(row=1, column=1)

    # Button that appends what is in the Entry box to the Label for contents:
    button = ttk.Button(frame, text="Append contents of Entry box")
    button["command"] = lambda: append_contents(entry_box, label_for_contents)
    button.grid(row=0, column=0)


def append_contents(entry_box, label):
    contents_of_entry_box = entry_box.get()
    label["text"] = label["text"] + "\n" + contents_of_entry_box


# -----------------------------------------------------------------------------
# Code that demonstrates a Canvas for drawing.
# -----------------------------------------------------------------------------
def make_canvas():
    frame = make_frame()
    pen_data = PenData("blue", "red")

    instructions = ["Click the left mouse button to make circles.",
                    "Drag the left mouse button to draw."]
    centered_instructions = make_centered_instructions(instructions)
    label = ttk.Label(frame, text=centered_instructions)
    label.grid()

    # Make a tkinter.Canvas on a Frame.
    # Note that Canvas is a tkinter (NOT a ttk) class.
    canvas = tkinter.Canvas(frame, background='lightgray')
    canvas.grid()

    # Make callbacks for mouse events.
    canvas.bind("<Button-1>", lambda event: left_mouse_click(event))
    canvas.bind("<B1-Motion>", lambda event: left_mouse_drag(event, pen_data))
    canvas.bind("<B1-ButtonRelease>",
                lambda event: left_mouse_release(pen_data))  # @UnusedVariable

    # Make a button to change the color.
    button = ttk.Button(frame, text="Flip pen color")
    button["command"] = lambda: flip_pen_color(pen_data)
    button.grid()


class PenData(object):
    def __init__(self, color, other_color):
        self.color = color
        self.other_color = other_color
        self.mouse_position_x = None
        self.mouse_position_y = None
        self.is_dragging = False


def left_mouse_click(event):
    canvas = event.widget
    canvas.create_oval(event.x - 10, event.y - 10,
                       event.x + 10, event.y + 10,
                       fill="green", width=3)


def left_mouse_drag(event, data):
    # data.mouse_position_x and _y keep track of the PREVIOUS mouse
    # position while we are dragging.
    canvas = event.widget
    if data.is_dragging:
        canvas.create_line(data.mouse_position_x, data.mouse_position_y,
                           event.x, event.y,
                           fill=data.color, width=5)
    else:
        data.is_dragging = True  # Start dragging

    data.mouse_position_x = event.x
    data.mouse_position_y = event.y


def left_mouse_release(data):
    data.is_dragging = False


def flip_pen_color(data):
    temp = data.other_color
    data.other_color = data.color
    data.color = temp


# -----------------------------------------------------------------------------
# Code that demonstrates Checkboxes and Radiobuttons
# -----------------------------------------------------------------------------
def make_checks_and_radios():
    frame = make_frame()

    instructions = ["Check the Checkbox and select various Radiobuttons.",
                    "Look in the Console to see what gets PRINTED in response."]
    centered_instructions = make_centered_instructions(instructions)
    label = ttk.Label(frame, text=centered_instructions)

    # Checkbutton's and Radiobutton's have their own labels.
    checkbutton = ttk.Checkbutton(frame, text="Robots rule!")

    # Radiobutton's. We often put them onto a sub-frame,
    # to group them visually.  The 'value' identifies which is selected.
    radio_frame = ttk.Frame(frame, borderwidth=10, relief="groove")
    radio1 = ttk.Radiobutton(radio_frame, text="Peter Pevensie",
                             value="peter")
    radio2 = ttk.Radiobutton(radio_frame, text="Susan Pevensie",
                             value="susan")
    radio3 = ttk.Radiobutton(radio_frame, text="Edmund Pevensie",
                             value="edmund")
    radio4 = ttk.Radiobutton(radio_frame, text="Lucy Pevensie",
                             value="lucy")

    # This Button will show how it can interact with other widgets.
    button = ttk.Button(frame, text="Reset the checkbox and radiobuttons")

    # Checkbutton's and Radiobutton's can have an "observer" variable
    # that is bound to the state of the Checkbutton / Radiobutton.
    checkbutton_observer = tkinter.StringVar()
    checkbutton["variable"] = checkbutton_observer

    radio_observer = tkinter.StringVar()
    for radio in [radio1, radio2, radio3, radio4]:
        radio["variable"] = radio_observer  # They all need the SAME observer

    # Bind callbacks using "command" and lambda, as we have seen elsewhere.
    checkbutton["command"] = lambda: checkbutton_changed(checkbutton_observer)

    for radio in [radio1, radio2, radio3, radio4]:
        radio["command"] = lambda: radiobutton_changed(radio_observer)

    button["command"] = lambda: button_pressed(checkbutton_observer,
                                               radio_observer)

    # Layout the widgets.  You can learn more about layout in another example.
    checkbutton.grid(row=0, column=0, padx=20)
    radio_frame.grid(row=0, column=1, padx=20)
    label.grid(row=1, column=0, columnspan=2, pady=20)
    button.grid(row=2, column=0, columnspan=2)

    for radio in [radio1, radio2, radio3, radio4]:
        radio.grid(sticky='w')


def checkbutton_changed(checkbutton_observer):
    print("The checkbutton changed to", checkbutton_observer.get())


def radiobutton_changed(radiobutton_observer):
    print("The radiobutton changed to", radiobutton_observer.get())


def button_pressed(checkbutton_observer, radiobutton_observer):
    print("After 2 seconds, I will toggle the Checkbutton")
    print("and reset the Radiobutton to Peter's.")
    time.sleep(2)

    if checkbutton_observer.get() == "1":
        checkbutton_observer.set("0")
    else:
        checkbutton_observer.set("1")

    radiobutton_observer.set("peter")


# -----------------------------------------------------------------------------
# Code that demonstrates showing Images.
# -----------------------------------------------------------------------------
def make_images():
    frame = make_frame()

    # Just PNG and GIFs in the out-of-the-box version of Python.
    image1 = tkinter.PhotoImage(file="image1.png")
    image2 = tkinter.PhotoImage(file="image2.gif")

    label = ttk.Label(frame, image=image1)
    label.image = image1
    label.grid(pady=20)

    button = ttk.Button(frame, image=image2)
    button.image = image2
    button.grid()


# -----------------------------------------------------------------------------
# Code that demonstrates pop-up windows (Toplevel objects).
# -----------------------------------------------------------------------------
def make_pop_up_windows():
    pop_up([], 1)


def pop_up(windows, number):
    """ Pops up a window, with a Label that shows some info. """
    window = tkinter.Toplevel()  # Note Toplevel, NOT Tk.
    windows.append(window)

    label = ttk.Label(window, text="Window #{}".format(number))
    label.grid()

    add_window_button = ttk.Button(window, text="Add another window")
    add_window_button["command"] = lambda: pop_up(windows, number + 1)
    add_window_button.grid()

    close_windows_button = ttk.Button(window, text="Close all these windows")
    close_windows_button["command"] = lambda: destroy_windows(windows)
    close_windows_button.grid()


def destroy_windows(windows):
    """ Destroys all the given windows. """
    for window in windows:
        window.destroy()


# -----------------------------------------------------------------------------
# Code that demonstrates a pull-down Menu with menu items.
# -----------------------------------------------------------------------------
def make_menu(root):
    # The default is for menus to be "tear-off" -- they can be dragged
    # off the menubar.  Use whichever style best suits your GUI.
    root.option_add("*tearOff", False)

    # Step 1:  Make the menu bar
    menubar = tkinter.Menu(root)
    root["menu"] = menubar

    # Step 2:  Make the pull-down menu's on the menu bar.
    choose_demo = tkinter.Menu(menubar)
    menubar.add_cascade(menu=choose_demo, label="Choose what to demo")

    # Step 3:  Make menu items for each menu on the menu bar.
    # Bind callbacks using lambda, as we have seen elsewhere,
    # but this time with a    command=...   optional argument supplied.

    menu_items_info = [["Entry box", make_entry_box],
                       ["Canvas", make_canvas],
                       ["Checkboxes and Radiobuttons", make_checks_and_radios],
                       ["Images", make_images],
                       ["Pop-up Windows", make_pop_up_windows],
                       ["Show events and binding", show_events],
                       ["Quit", root.destroy]]

    for menu_item_info in menu_items_info:
        choose_demo.add_command(label=menu_item_info[0],
                                command=menu_item_info[1])


# -----------------------------------------------------------------------------
# Code that demonstrates binding events to code.
# -----------------------------------------------------------------------------
def show_events():
    frame = make_frame()
    data = Data()

    main_frame = ttk.Frame(frame, padding=20)
    main_frame.grid()

    intro = 'This example shows how keys can be associated\n' \
            + 'with widgets.  The widget must have the "focus"\n' \
            + 'for its event to fire.\n\n' \
            + 'In this example, the <Return> (Enter key) event\n' \
            + 'is associated with each of the 2 Entry boxes,\n' \
            + 'and the u and d keys and mouse press are associated\n' \
            + 'with the button.\n\n' \
            + 'Try the u and d keys, with and without the button having\n' \
            + 'the focus.  Try entering numbers in the Entry boxes\n' \
            + 'with and without pressing the Enter key.\n' \
            + 'See what is PRINTED in the Console.'
    intro_label = ttk.Label(main_frame, text=intro)
    intro_label.grid()

    number_text = 'The number is {}'.format(data.number)
    number_label = ttk.Label(main_frame, text=number_text)
    number_label.grid()
    data.number_label = number_label

    # --------------------------------------------------------------------
    # In the previous module, you saw   bind_all   which binds the Event
    # to ALL the widgets on the root.  If you want the callback to occur
    # only when a certain Widget has the "focus" (and the Event occurs),
    # use   bind   (not bind_all), per the following examples:
    # --------------------------------------------------------------------

    entry1 = ttk.Entry(main_frame, width=4)
    entry1.grid()
    entry1.bind('<Return>', lambda event: callback1(event, data))
    data.entry_box1 = entry1

    entry2 = ttk.Entry(main_frame, width=4)
    entry2.grid()
    entry2.bind('<Return>', lambda event: callback2(event, data))
    data.entry_box2 = entry2

    # --------------------------------------------------------------------
    # You can bind Events to Buttons (and any other Widget).  So the
    # first   button.bind   below shows an alternative to ['command'].
    # --------------------------------------------------------------------

    button_text = 'Use the TAB key to give me the "focus",'
    button_text = button_text + '\n then press the u or d key'
    button = ttk.Button(main_frame, text=button_text)
    button.grid()

    button.bind('<Button-1>', lambda event: callback3(event, data))
    button.bind('<Key-u>', lambda event: callback3(event, data))
    button.bind('<Key-d>', lambda event: callback3(event, data))


class Data(object):
    def __init__(self):
        self.number = 0
        self.entry_box1 = None
        self.entry_box2 = None
        self.number_label = None


def callback1(event, data):
    """
    Increases the number in the given Data object by the value
    of the Entry box bound to the given Event.
    """
    widget = event.widget
    number_in_entry_box = int(widget.get())
    print('This is callback1, which uses Widget: ' + str(widget))
    data.number = data.number + number_in_entry_box

    print('  The number is now ' + str(data.number))
    data.number_label['text'] = 'The number is {}'.format(data.number)


def callback2(event, data):
    """
    Decreases the number in the given Data object by the value
    of the Entry box bound to the given Event.
    """
    widget = event.widget
    number_in_entry_box = int(widget.get())
    print('This is callback2, which uses Widget: ' + str(widget))
    data.number = data.number - number_in_entry_box

    print('  The number is now ' + str(data.number))
    data.number_label['text'] = 'The number is {}'.format(data.number)


def callback3(event, data):
    """
    Increments or decrements the number in the given Data object
    depending on the given Event.
    """
    print('hello')
    if event.type == '2':  # 2 is the KEY type in Windows, it seems
        if event.keysym == 'u':
            print('u key was pressed while the button had focus')
            data.number = data.number + 1
        elif event.keysym == 'd':
            print('d key was pressed while the button had focus')
            data.number = data.number - 1
        else:
            print('Unexpected - key ' + event.keysym + ' was pressed.')
    elif event.type == '4':  # 4 is the BUTTON type in Windows, it seems
        print('button was pressed')
        data.number = data.number + 1  # So mouse press is same as u key.
    else:
        print('Unexpected - event type ' + event.type + ' occurred.')

    print('  The number is now ' + str(data.number))
    data.number_label['text'] = 'The number is {}'.format(data.number)


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
