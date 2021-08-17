"""
Example showing for tkinter and ttk how to do:
  -- A GUI including a Canvas for drqwing objects
  -- while sending and receiving messages from other computers.

For the tkinter/ttk code, see the 22-TkinterAnimation code (but ignore the
part of that code that runs the animation by using root.after).

The novel part of this example is the message-passing to/from other computers.
The key ideas are:

  1. The   mqtt_for_csse120   module defines Sender and Receiver classes
       for sending and receiving messages from other computers.
       They use MQTT as the underlying communication protocol.

  2. PyCharm will not let you run the same module twice at the same time.
       So, to test your program on your own (single) computer, you run the
       main1  module  AND the  main2  module.  The former constructs a Game
       object with who_am_i set to 1, the latter sets it to 2.
       That way, the two runs will send to each other and NOT to themselves!

       When running on two computers (with a friend running one of them),
       decide who will run  main1  and the other should run  main2.

  3. The Game object constructs a Receiver and Sender:
        receiver = communicator.Receiver(self)
        self.sender = communicator.Sender(receiver, "something_unique",
                                          who_am_i)
     where  communicator  is an abbreviation for the  mqtt_for_csse120  module.

     The "something_unique" should be any string that only YOUR programs will
     be using (so you are not communicating with random other programs).
     We suggest you use your own username as that string, e.g.
        self.sender = communicator.Sender(receiver, "alangavr", who_am_i)

  4. To send a message, just use:
        self.sender.send_message(message)  where message is any STRING.

  5. The Receiver object that the Game object constructs causes a process
       to run **in the BACKGROUND** listening for messages.  That process
       has been coded to call the specially-name method of the Game class:
           act_on_message_received

       So the Game class MUST have a method like this:
           def act_on_message_received(self, message):
              # This is called when a message comes from another computer.
              # You do whatever you want with that message.

  6. The basic structure of the code below is very similar to the structure
       from the 22-TkinterAnimation code, but with the animation part removed.

SEE THE UML CLASS DIAGRAM include with this project.

Authors: David Mutchler and his colleagues
         at Rose-Hulman Institute of Technology.
"""
import tkinter
from tkinter import ttk

import old_mqtt_for_csse120 as communicator


def main(who_am_i):
    game = Game(who_am_i)
    game.start()


class Game(object):
    """ A Game played on two (or more) computers. """

    def __init__(self, who_am_i):
        # Construct the GUI, which constructs and stores a Canvas.
        # Store that Canvas in THIS object too, so that animated objects can
        # act upon it.  Here, our animated objects are a single Ball.
        # Each Ball needs to have the Canvas so that the Ball can change its
        # position (and anything else it might want to change).

        self.gui = GUI(self)
        canvas = self.gui.canvas

        # Make a Receiver and Sender for messages to/from other computers.
        receiver = communicator.Receiver(self)
        self.sender = communicator.Sender(receiver, "something_unique",
                                          who_am_i)

        # So each player's Ball looks different, we base the color on who_am_i.
        if who_am_i == 1:
            color = "blue"
        else:
            color = "red"
        self.ball = Ball(color, canvas)  # How each Ball gets the Canvas

    def start(self):
        # Called after the GUI, the Game, and all the animated objects
        # are constructed.  The GUI's  start  method starts the  mainloop
        # in which the program remains for the remainder of its run.
        self.gui.start()

    def act_on_message_received(self, message):
        """
        Called by the Receiver when a message is received.
        The MQTT code makes the Receiver **run in the background**
        and **automatically** call this method named  act_on_message_received.
        The method name must be exactly as it is here.
        """
        # The message always arrives as a STRING.
        # The  split  method returns a LIST of the words in that string
        # (where words are by definition separated by spaces, tabs or newlines).
        message_parts = message.split()
        x = int(message_parts[0])
        y = int(message_parts[1])

        self.ball.move_to(x, y)

    def send_xy(self, x, y):
        """ Combine the two numbers into a SINGLE, space-separated string. """
        self.sender.send_message("{} {}".format(x, y))


class GUI(object):
    def __init__(self, game):
        """
        Stores the given Game object in order to call the
        Game object's  send_xy  method when ready to send that message.
        Constructs all the GUI widgets, but does NOT (yet) call  root.mainloop.
          :type game: Game
        """
        self.game = game

        # The usual Tk and Frame objects, plus any other widgets you want.
        self.root = tkinter.Tk()
        self.frame = ttk.Frame(self.root, padding=10)
        self.frame.grid()

        # A Canvas for the Ball object.
        self.canvas = self.make_canvas()

        # A Chooser by which the user can enter an x and y to send to the
        # other computer/player, which moves ITS Ball to that x and y.
        self.make_chooser_for_xy()

    def make_canvas(self):
        canvas_width = 400
        canvas_height = 300
        canvas = tkinter.Canvas(self.frame, width=canvas_width,
                                height=canvas_height)
        canvas.width = canvas_width
        canvas.height = canvas_height
        canvas.grid()
        return canvas

    def make_chooser_for_xy(self):
        entry_for_x = ttk.Entry(self.frame)
        entry_for_y = ttk.Entry(self.frame)
        send_button = ttk.Button(self.frame, text="Send X and Y")
        send_button["command"] = lambda: self.send_xy(entry_for_x, entry_for_y)

        entry_for_x.grid()
        entry_for_y.grid()
        send_button.grid()

    def send_xy(self, entry_for_x, entry_for_y):
        # Get the data from the Entry boxes. Game sends them to other computer.
        x = int(entry_for_x.get())
        y = int(entry_for_y.get())
        self.game.send_xy(x, y)

    def start(self):
        # Called by the Game object when the program is ready to enter the
        # Tk object's mainloop and remain there for the remainder of the run.
        self.root.mainloop()


class Ball(object):
    def __init__(self, color, canvas):
        """
        The Ball needs the Canvas so that it can update its characteristics
        (position, fill color, etc) as the game runs.
          :type color   str
          :type canvas: tkinter.Canvas
        """
        self.canvas = canvas

        # Set the characteristics of the Ball: specific x, y and diameter.
        # It will use the given color.
        x = 200
        y = 200
        self.diameter = 20

        # Make the item on the Canvas for drawing the Ball, storing its ID
        # for making changes to the Ball (moving it, changing color, etc.).
        # Here, each Ball is a filled circle (actually an oval),
        # defined by its upper-left and lower-right corners.
        self.id = self.canvas.create_oval(x, y,
                                          x + self.diameter, y + self.diameter,
                                          fill=color)

    def move_to(self, x, y):
        self.canvas.coords(self.id, x, y, x + self.diameter, y + self.diameter)
