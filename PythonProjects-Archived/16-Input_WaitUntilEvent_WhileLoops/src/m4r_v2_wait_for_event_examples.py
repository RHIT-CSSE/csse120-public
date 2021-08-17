"""
This module demonstrates the WAIT-FOR-EVENT pattern using
the ITCH pattern (Initialize, Test, CHange something):

   Initialize as needed so that the CONDITION can be TESTED.
   while <some CONDITION>: # Test the CONDITION, continue WHILE it is true.
       ...
       ...
       CHange something that (eventually) affects the CONDITION.
         (else otherwise you will be in an infinite loop)

See the module that is the COMPANION to this one for the same examples,
but using the WHILE TRUE pattern for WHILE loops.

Authors: David Mutchler, Vibha Alangar, Dave Fisher, Matt Boutell, Mark Hays,
         Mohammed Noureddine, Sana Ebrahimi, Sriram Mohan, their colleagues and
         PUT_YOUR_NAME_HERE.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

###############################################################################
# TODO: 2.  Read and run this program.  Then do the following problems,
#   putting your answers RIGHT HERE IN THIS DOCUMENT.
#  __
#   1. Which version of   demonstrate_wait_for_sentinel  feels clearer to you?
#        -- The version in this module, or
#        -- The version in the previous module
#   Note: reasonable people could disagree on the answer to this question.
#  __
#   2. Can you READ and TRACE-BY-HAND   while CONDITION:   loops,
#        as exemplified in this module?
#        Yes or No?     [If No, ASK FOR HELP NOW!]
###############################################################################

###############################################################################
# Students: Before you leave these examples,
#   *** MAKE SURE YOU UNDERSTAND THE   WAIT-FOR-EVENT   PATTERN,
#   *** with its use of a    WHILE <condition>:   statement.
###############################################################################

import math
import random
import time
import rosegraphics as rg


def main():
    """ Demonstrates applications of the wait-for-event pattern. """
    # wait_for_circle_to_reach_edge()
    # wait_for_sentinel()
    wait_for_small_enough_number()


# -----------------------------------------------------------------------------
# Demonstrates waiting for a sequence of "growing" circles
# to reach the edge of the window in which they are drawn.
# -----------------------------------------------------------------------------
def wait_for_circle_to_reach_edge():
    """
    Demonstrates the   wait_for_event   pattern, where the event
    is that a growing graphical object has grown beyond the window size.

    This particular example draws, moves and grows purple circles
    until a circle extends beyond the border of the window.
    """
    print()
    print("---------------------------------------------------------")
    print("Demonstrating the WAIT FOR EVENT pattern in graphics:")
    print("See the graphics window that pops up.")
    print("---------------------------------------------------------")

    window = rg.RoseWindow(700, 450, "Animation until a TOO-BIG circle")

    x = 20
    y = 50
    radius = 5
    k = 0
    window.continue_on_mouse_click()

    # If the circle has reached a right/bottom border of the window,
    # exit the loop
    right_edge = x + radius
    bottom_edge = y + radius

    while right_edge < window.width and bottom_edge < window.height:
        # Construct and draw a purple circle.
        circle = rg.Circle(rg.Point(x, y), radius)
        circle.fill_color = "purple"
        circle.attach_to(window)

        # Make the next circle be down, to the right, and bigger.
        k = k + 1
        x = x + 2
        y = y + 1
        radius = radius + (k / 100)

        # Render. Allow a little time to elapse, else the animation flashes by.
        window.render(0.01)

        # Prepare the stopping condition for the WHILE statement above:
        right_edge = x + radius
        bottom_edge = y + radius

    window.close_on_mouse_click()


# -----------------------------------------------------------------------------
# Demonstrates waiting for a "sentinel" value to be input.
# -----------------------------------------------------------------------------
def wait_for_sentinel():
    """
    Demonstrates the   wait_for_event   pattern, where the event
    is inputting a SENTINEL value to signal the end of user input.

    This particular example inputs positive integers and processes them
    by printing their square roots, and when input is finished,
    printing the sum of those square roots.  User input stops when
    the user inputs the agreed-upon SENTINEL value of -1.
    """
    print()
    print("----------------------------------------------")
    print("Demonstrating the WAIT FOR SENTINEL pattern:")
    print("----------------------------------------------")

    total = 0
    number = int(input("Enter a positive integer, or -1 to quit: "))
    while number != -1:
        print("The square root of {} is about {:0.5f}.\n".
              format(number, math.sqrt(number)))
        total = total + math.sqrt(number)
        number = int(input("Enter a positive integer, or -1 to quit: "))

    print("The total of the square roots is", total)


# -----------------------------------------------------------------------------
# Demonstrates waiting for a "small enough" random number to be generated.
# Start by setting the random "seed" for the sequence of pseudo-random numbers.
# See the   m3e_random_numbers   module for details.
# -----------------------------------------------------------------------------
t = time.time()  # The number of seconds since January 1, 1970, as a float
random.seed((t * 10000) % 10000)  # The first 4 decimals of t


def wait_for_small_enough_number(small_number=10, max_number=50, print_it=True):
    """
    What comes in:  Two optional positive integers,
      with the second greater than the first,
      and an optional indicator for whether to print intermediate results.
    What goes out:
      Returns the number of random integers that are generated,
      as described below.
    Side effects:
      -- Repeatedly generates random integers between 1 and max_number,
           inclusive, where max_number is the second given integer.
      -- Stops when the random integer is less than or equal to
           small_number, where small_number is the first given integer.
      -- Optionally prints the random numbers as they are generated.

    Note that, each time through the loop, the probability that the
    stopping-event occurs is   small_number / max_number  (0.2 by default).
    Probability theory tells us that the expected number of times that
    the loop will run is max_number / small_number  (5 by default).
    """
    if print_it:
        print()
        print("----------------------------------------------------------")
        print("Demonstrating WAIT FOR A SMALL ENOUGH")
        print("  randomly generated number")
        print("----------------------------------------------------------")

        print("I will now generate random integers between")
        print("1 and {}, stopping when a generated random".format(max_number))
        print("integer is less than or equal to {}.".format(small_number))
        print()

    number = random.randrange(1, max_number + 1)
    if print_it:
        print("   Randomly generated number: {}".format(number))
    count = 1
    while number > small_number:
        number = random.randrange(1, max_number + 1)
        count = count + 1
        if print_it:
            print("   Randomly generated number: {}".format(number))

    if print_it:
        print("{} random integers between 1 and {} were generated".format(
            count, max_number))
        print()

    return count


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
