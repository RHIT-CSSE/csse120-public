"""
Example showing for tkinter and ttk how to do:
  -- Simple animation
  -- on a tkinter Canvas.

References:
  -- https://effbot.org/tkinterbook/canvas.htm
       This is the simplest explanation,
       but very old and possibly somewhat out of date.
       Everywhere that it says "pack" use "grid" instead.
  -- The  tkinter.pdf   document in this project.
       This is by far the most complete reference work for tkinter and ttk.
       It is for reference, NOT a tutorial.
  -- https://tkdocs.com/tutorial/canvas.html
       This is a more complete and up-to-date tutorial than the one above.
       It shows each example in four different languages.
       Python is the fourth (last) one.  Ignore the other-language examples.

The key ideas are:

  1. Drawing (and hence animation) is on a tkinter.Canvas.

  2. You put an object onto a Canvas with:
        id = canvas.create_XXX(POSITION, OTHER-OPTIONS)

     where XXX can be any of:
       oval, arc, bitmap, image, line, polygon, rectangle, text, window,
     and where the specifics of  POSITION  and  OTHER-OPTIONS  depends on the
     type of object being created.  See the example in the code below
     for an oval.  See the above reference work for details on other types.

  3. The ID returned by a call to  create_XXX  is how you keep track of objects
       on a Canvas for future animation (movements, color changes, etc.).

  4. There are three basic methods for animating (changing) an object.
     Each method is a Canvas method whose first argument
     is the ID of the object on the Canvas.  You can:
       a. MOVE an object BY a given amount by:
            canvas.move(ID, delta_x, delta_y)
       b. MOVE an object TO a certain position by:
            canvas.coords(ID, NEW_POSITION ...)
          where the specifics of NEW_POSITION depend on the type of the object.
       c. CHANGE OTHER CHARACTERISTICS of objects as in this example:
            canvas.coords(ID, fill="blue")  # Changes the fill color to "blue"
          The specifics of what you can change (and how) depends on the type
          of object.  See the above reference work for details.

  5. You must FIRST construct everything needed for the animation,
       and THEN do the    root.mainloop()   to start the GUI running.
       The code below shows one way to accomplish that, using this structure:

         a. The  main  method constructs and then starts an Animation object.

         b. The Animation object constructs the GUI, passing itself to the GUI
              so that the GUI can later ask the Animation to do stuff.

         c. The GUI contains:
               -- The one-and-only tkinter.Tk  object.
               -- Frame(s) and other widgets as desired.
               -- A  tkinter.Canvas  on a Frame.

         d. When the GUI is constructed, you include all the tkinter/ttk code
            that you have seen in previous examples EXCEPT not (yet) the
               root.mainloop()

         e. The GUI includes a  start  method that contains:
               root.mainloop()

         f. The Animation object (which constructed the GUI) calls the GUI's
              start  method to start the animation running.

         g. The Animation object has a method:
                 run_one_cycle
            that makes all the changes to all the objects in the Animation,
            for ONE cycle of the animation, by using the Canvas methods:
               move    coords    itemconfigure
            The Animation has access to the Canvas because the Animation
            constructed (and stores) the GUI, and the GUI makes and stores
            the Canvas.

         h. The Animation's  run_one_cycle   method
              is called repeatedly BY THE GUI as follows, all in the GUI class:

                def __init__(self, animation):
                    self.animation = animation
                    self.root = tkinter.Tk()
                      ...
                    self.root.after(1000, self.animation_loop)

                def animation_loop(self):
                    self.animation.run_one_cycle()
                    self.root.after(10, self.animation_loop)

              The   after   method sets a TIMER that is triggered
              after the given number of milliseconds (1000 ms in the first call
              to  after  in the above, and 10 ms in the second call to after).
              Because it is a TIMER, Tkinter is able to react to button presses
              and other stuff while the TIMER is waiting to ring its alarm.
              When the TIMER rings its alarm, it calls the second argument
              to the  after  method, which is  self.animation_loop  in the
              above.  So, self.animation_loop is called the first time after
              1 second (1000 ms), and it runs one cycle of the animation at
              that time.  Thereafter it repeatedly:
                -- Waits 10 ms (via a TIMER that allows other stuff to happen)
                -- Calls animation_loop again
                -- Runs one cycle of the animation.

              In the actual code below, instead of running every 10 ms,
              it runs every  animation.cycle_ms, so that the Animation object
              can control the "refresh rate" of the animation.

See the code below for an example that uses the above structure.
While you are not REQUIRED to use the same structure, it is probably a good
idea to do so for any video-game style game.

This example does NOT include any message-passing with MQTT to other computers.
Other examples cover that topic.

SEE THE UML CLASS DIAGRAM include with this project.

Authors: David Mutchler and his colleagues
         at Rose-Hulman Institute of Technology.
"""
import random

import tkinter
from tkinter import ttk

import mqtt_for_csse120 as communicator


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
        # We also need a Receiver and Sender.
        self.gui = GUI(self)
        self.canvas = self.gui.canvas

        receiver = communicator.Receiver(self)
        self.sender = communicator.Sender(receiver, "something_unique",
                                          who_am_i)

        if who_am_i == 1:
            color = "blue"
        else:
            color = "red"
        self.ball = Ball(color,  # So each player's Ball can look different
                         self.canvas)  # Note how each Ball gets the Canvas

    def start(self):
        # Called after the GUI, the Game, and all the animated objects
        # are constructed.  The GUI's  start  method starts the  mainloop
        # in which the program remains for the remainder of its run.
        self.gui.start()

    def act_on_message_received(self, message):
        """
        Called by the Receiver when a message is received.
        The MQTT stuff makes the Receiver ** run in the background **
        and ** automatically ** call the method named  act_on_message_received.
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
        self.sender.send_message("{} {}".format(x, y))


class GUI(object):
    def __init__(self, game):
        """
        Stores the given Game object in order to call the
        Game object's  send_xy  method when ready to send that message.
        Constructs all the GUI widgets, but does NOT (yet) call  root.mainloop.
          :type animation: Game
        """
        self.game = game

        # The usual Tk and Frame objects, plus any other widgets you want.
        self.root = tkinter.Tk()
        self.frame = ttk.Frame(self.root, padding=10)
        self.frame.grid()

        self.canvas = self.make_canvas()
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
        self.canvas.coords(self.id, x, y,
                           x + self.diameter, y + self.diameter)
