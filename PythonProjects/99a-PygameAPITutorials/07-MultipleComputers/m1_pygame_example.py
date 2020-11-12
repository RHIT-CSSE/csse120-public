"""
This example shows how two computers can interact with one another by using
a module called  simpleMQTT  to send/receive messages to/from each other.

See   m0_simplest_example.py   for a simpler example.

This example adds to the  m0  example in that this example:
  -- Uses PyGame.
  -- Shows the following solution to the problem in which two objects
     need each other:
        a = Thing_1()
        b = Thing_2(a)
        a.set_b(b)
     See the accompanying video for details.

WATCH THE VIDEO associated with this example to:
  1. Learn how to RUN this example.
  2. Understand what this example DOES.
  3. Understand the CODE in this example.

But briefly:
  -- Each computer runs this program (but see the call to main below).
  -- Each computer's PyGame screen shows a black Player and a red Zombie.
       -- The user moves the Player by using the arrow keys.
       -- Doing so ALSO moves the ZOMBIE on the OTHER computer to match
          the PLAYER's movement on THIS computer (and vice versa).

Authors: David Mutchler, Dave Fisher, Sana Ebrahimi, Mohammad Noureddine
  and their colleagues at Rose-Hulman Institute of Technology,
  licensed under CC BY-NC-SA 4.0.  To view a copy of this license, visit
      https://creativecommons.org/licenses/by-nc-sa/4.0.
"""

import sys
import time

import pygame

import simpleMQTT as mq


# -----------------------------------------------------------------------------
# See Note 1 below.
# -----------------------------------------------------------------------------
class Controller:
    """ Receives and acts upon messages received from the other computer. """

    def __init__(self, zombie):
        self.zombie = zombie  # type: Player

    # noinspection PyUnusedLocal
    def act_on_message_received(self, message, sender_id):
        """
        Moves this Controller's "zombie" Player to the position
        that was sent by the other computer.
        Parameters:
          -- message: Must be a string that represents two non-negative
                      integers separated by one or more spaces, e.g. "100 38"
          -- sender_id: The number of the computer sending the message
                        (unused by this method)
          :type message:   str
          :type sender_id: int
        """
        x = float(message.split()[0])
        y = float(message.split()[1])
        self.zombie.move_to(x, y)


class Player:
    """ A Player in the game.  For now, simply a filled circle. """

    def __init__(self, screen, x, y, speed_x, speed_y, color):
        self.screen = screen
        self.x = x
        self.y = y
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.color = pygame.Color(color)

        # ---------------------------------------------------------------------
        # See Note 2 below.
        # ---------------------------------------------------------------------
        # noinspection PyTypeChecker
        self.sender = None  # type: mq.Sender

    def set_sender(self, sender):
        self.sender = sender

    def draw(self):
        """ Draws this Player, for now as a filled circle of radius 10. """
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), 10)

    def move_by_keys(self):
        """
        Moves this Player via the four arrow keys. Never called on the Zombie.
        """
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_UP]:
            self.y = self.y - self.speed_y
        if pressed_keys[pygame.K_DOWN]:
            self.y = self.y + self.speed_y
        if pressed_keys[pygame.K_LEFT]:
            self.x = self.x - self.speed_x
        if pressed_keys[pygame.K_RIGHT]:
            self.x = self.x + self.speed_x

        # ---------------------------------------------------------------------
        # See Note 3 below.
        #   The following statement tells the other computer to move
        #   its "zombie" to the place where this Player is.
        # ---------------------------------------------------------------------
        self.sender.send_message("{} {}".format(self.x, self.y))

    def move_to(self, x, y):
        """ Moves this Player to the given position. """
        self.x = x
        self.y = y


###############################################################################
# Run this program on two computers.
#   On one of them, run by calling:  main(1)
#   On the other,   run by calling:  main(2)
###############################################################################
def main(who_am_i):
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption("Computer {}".format(who_am_i))
    screen = pygame.display.set_mode((400, 300))

    # -------------------------------------------------------------------------
    # There are two instances of the Player class: a Player and a Zombie.
    # The Player moves per the arrow keys.  The Zombie moves per messages
    # sent from the other computer.
    #
    # The Player is black and starts:
    #   -- on the LEFT side of the PyGame screen if this is computer 1
    #   -- on the RIGHT side of the PyGame screen if this is computer 2
    # The Zombie is red and starts in the MIDDLE of the PyGame screen
    # -------------------------------------------------------------------------
    if who_am_i == 1:
        player_x = screen.get_width() * 0.25
    else:
        player_x = screen.get_width() * 0.75
    zombie_x = screen.get_width() * 0.5
    y = screen.get_height() * 0.5
    speed = 2  # Controls the effect of the arrow keys; irrelevant for Zombie
    player = Player(screen, player_x, y, speed, speed, "black")
    zombie = Player(screen, zombie_x, y, 0, 0, "red")

    # -------------------------------------------------------------------------
    # See Note 4 below.
    # -------------------------------------------------------------------------
    unique_id = "csse120-david-mutchler"
    sender = mq.Sender(who_am_i)
    controller = Controller(zombie)
    receiver = mq.Receiver(controller)
    mq.activate(unique_id, sender, receiver)

    # -------------------------------------------------------------------------
    # See Note 5 below.
    # -------------------------------------------------------------------------
    sender.verbosity = receiver.verbosity = 3  # Set to 0 for no debug messages

    # ---------------------------------------------------------------------
    # See Note 2 below.
    # ---------------------------------------------------------------------
    player.set_sender(sender)

    background = pygame.color.Color("grey")
    # -------------------------------------------------------------------------
    # See Note 6 below
    # -------------------------------------------------------------------------
    while True:
        screen.fill(background)
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        player.move_by_keys()
        player.draw()
        zombie.draw()

        pygame.display.update()


# -----------------------------------------------------------------------------
# See Note 7 below.
# -----------------------------------------------------------------------------
if __name__ == '__main__':
    try:
        main(2)  # On one computer, use 1.  On the other computer, use 2.
    except Exception:
        mq.print_in_red("ERROR - While running this program,")
        mq.print_in_red("your code raised the following exception:")
        print()
        time.sleep(1)
        raise

###############################################################################
# NOTES mentioned in the simpleMQTT code above.
#
# Note 1:
#    You MUST have some object to receive messages.
#    That object MUST be an instance of a class that has a method named
#        act_on_message_received
#    The method MUST be spelled exactly as shown above.
#    The method MUST have exactly 3 parameters: self, message, sender_id.
#
#    In this example, the class for that object is called Controller.
#    You can call it whatever you want.
#
#    The   act_on_message_received   method can do whatever you want it to do.
#    In this example:
#      -- The Controller stores the "Zombie"
#           when the Controller is constructed (see its  __init__)
#      -- When a message arrives (via the  act_on_message_received  method,
#           the Controller decodes the message into x and y coordinates
#           and sets the Zombie's position to that (x, y).
#   The "decoding" the STRING message into NUMBERS x and y is done by:
#      1. Apply the  split  method to the message to SPLIT the STRING
#         at white space (here, space characters) into a LIST of STRINGS.
#           Example:   "100 38".split()  =   ["100", "38"]
#      2. Access the items at indices 0 (for x) and 1 (for y).
#           Examples:  "100 38".split()[0]  =>  ["100", "38"][0]  =>  "100"
#                      "100 38".split()[1]  =>  ["100", "38"][1]  =>  "38"
#      3. Convert from a string to a FLOAT.  Example:
#            float("100 38".split()[0]) => ["100", "38"][0] => "100" => 100.0
#         (This program stores coordinates as floats and sends them that way.)
#
#
# Note 2:
#    The  Player  object needs a Sender to send the Player's position
#    to the other computer, for the OTHER computer to use as ITS Zombie.
#
#    It so happens that the Player is constructed in this example BEFORE
#    the Sender is constructed.  (It did not HAVE to be that way, but in
#    some other example it might need to be.)  So it is IMPOSSIBLE to
#    have the Sender be an argument to the Player's __init__.
#
#    Instead, the Player stores   self.sender   as None  TEMPORARILY.
#    Soon after the Player is constructed, the Sender is constructed,
#    and at THAT time the Player applies its  set_sender  method
#    to store the REAL Sender in self.sender.
#    This happens before any messages need to be sent, so all is well.
#
# Note 3:
#    This shows why the Player must have the Sender as an instance variable.
#
# Note 4:
#    All this is the same as the  m0  example EXCEPT that here the Controller
#    takes an argument that is an OBJECT (the Player that is the Zombie)
#    that the Controller asks to move when the Controller acts on a message.
#
#    [The rest of this note is repeated from  m0  example.]
#    You MUST have a unique_id. It distinguishes YOUR simpleMQTT-enabled
#    program from OTHER simpleMQTT-enabled programs that may be running
#    at the same time as yours and with the same Broker as yours.
#    Choose a string that is unique to you,
#    e.g. something involving your name and/or your program's name.
#
#    You MUST construct a Sender.
#    Its first argument MUST be a positive integer that denotes the
#    "computer number" for the computer on which you are running this program.
#    Computers are numbered 1, 2, 3, ... in simpleMQTT.
#
#    If you want to receive messages, you MUST construct an object like the
#    Controller object described in Note 1, and you MUST construct a Receiver
#    whose first argument is that Controller object.
#
#   You MUST call the   mq.activate  function to enable communication.
#
# Note 5:  [same as the corresponding note in the  m0  example]
#    Printing the messages sent and received is invaluable for debugging.
#    By default, Senders and Receivers print all messages.
#      FYI: Setting  verbosity  to  0  disables printing of debugging messages.
#      ADVICE: Do NOT set verbosity to 0 until your program WORKS CORRECTLY.
#
# Note 6:
#    The code enters the "game loop" here.  In this example, the program
#    repeatedly moves the Player per the arrow keys and draws both Player
#    objects (the arrow-key-driven Player and the Zombie).
#    Meanwhile, the Receiver is listening in the background, sending each
#    message received to the Controller, which changes the position of
#    the Zombie, hence "moving" it the next time the Zombie is drawn.
#
#    In this simple example, no attempt is made to "untangle" the printing.
#
# Note 7:  [same as the corresponding note in the  m0  example]
#   Run the program on two computers, or twice on your computer (see the video).
#     On one of the computers, run by calling:  main(1)
#     On the other computer,   run by calling:  main(2)
#   The argument is the computer's "number".
#   It helps prevent a computer running this program from talking to itself.
#
#   The  if __name__ == '__main__'  makes external programs able to run main.
#   The  try .. except  helps avoid intermingling ordinary and error output.
###############################################################################
