"""
This example shows how two computers can interact with one another by using
a module called  simpleMQTT  to send/receive messages to/from each other.

This is the SIMPLEST example that we could make.
IMPORTANT:  Note that this example:
  - Is a "chat" program: two users, on two computers, talk to each other.
  - Is NOT a very good user interface.
  - Is NOT a PyGame project.  (Instead, it does Console input and output.)

WATCH THE VIDEO associated with this example to:
  1. Learn how to RUN this example.
  2. Understand what this example DOES.
  3. Understand the CODE in this example.

But briefly:
  -- Each computer runs this program (but see the call to main below).
  -- Whatever the user types on THEIR computer's console
       also appears on the OTHER computer's console, as in a "chat" program.

Authors: David Mutchler, Dave Fisher, Sana Ebrahimi, Mohammad Noureddine
  and their colleagues at Rose-Hulman Institute of Technology,
  licensed under CC BY-NC-SA 4.0.  To view a copy of this license, visit
      https://creativecommons.org/licenses/by-nc-sa/4.0.
"""
import time

import simpleMQTT as mq


# -----------------------------------------------------------------------------
# See Note 1 below.
# -----------------------------------------------------------------------------
class Controller:
    """ Receives and acts upon messages received from the other computer. """

    def __init__(self, name_of_friend):
        self.name_of_friend = name_of_friend

    # noinspection PyUnusedLocal
    def act_on_message_received(self, message, sender_id):
        print("{} says: {}".format(self.name_of_friend, message))


###############################################################################
# Run this program on two computers.
#   On one of them, run by calling:  main(1)
#   On the other,   run by calling:  main(2)
###############################################################################
def main(who_am_i):
    name_of_friend = input("Enter your chat friend's name: ")

    # -------------------------------------------------------------------------
    # See Note 2 below.
    # -------------------------------------------------------------------------
    unique_id = "csse120-david-mutchler-example-0"
    sender = mq.Sender(who_am_i)
    controller = Controller(name_of_friend)
    receiver = mq.Receiver(controller)
    mq.activate(unique_id, sender, receiver)

    # -------------------------------------------------------------------------
    # See Note 3 below.
    # -------------------------------------------------------------------------
    sender.verbosity = receiver.verbosity = 3  # Set to 0 for no debug messages

    # -------------------------------------------------------------------------
    # See Note 4 below
    # -------------------------------------------------------------------------
    print("In this window, repeatedly type messages to send to your friend.")
    while True:
        message = input()
        sender.send_message(message)


# -----------------------------------------------------------------------------
# See Note 5 below.
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
#    The method can do whatever you want it to do; in this example,
#    it simply prints the message, as a "chat" program would.
#
#    In this example, the class for that object is called Controller.
#    You can call it whatever you want.
#
# Note 2:
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
# Note 3:
#    Printing the messages sent and received is invaluable for debugging.
#    By default, Senders and Receivers print all messages.
#      FYI: Setting  verbosity  to  0  disables printing of debugging messages.
#      ADVICE: Do NOT set verbosity to 0 until your program WORKS CORRECTLY.
#
# Note 4:
#    The code enters the "game loop" here.  In this example, the program
#    repeatedly inputs a message to send, then sends it.
#    Meanwhile, the Receiver is listening in the background, sending each
#    message received to the Controller, which prints the message.
#
#    In this simple example, no attempt is made to "untangle" the printing.
#
# Note 5:
#   Run the program on two computers, or twice on your computer (see the video).
#     On one of the computers, run by calling:  main(1)
#     On the other computer,   run by calling:  main(2)
#   The argument is the computer's "number".
#   It helps prevent a computer running this program from talking to itself.
#
#   The  if __name__ == '__main__'  makes external programs able to run main.
#   The  try .. except  helps avoid intermingling ordinary and error output.
###############################################################################
