"""
This module demonstrates the WAIT-FOR-EVENT pattern using
the WHILE TRUE pattern:

   while True:
       ...
       if <event has occurred>:
           break
       ...

See the module that is the COMPANION to this one for the same examples,
but using the ITCH pattern for WHILE loops.

Authors: David Mutchler, Vibha Alangar, Dave Fisher, Matt Boutell, Mark Hays,
         Mohammed Noureddine, Sana Ebrahimi, Sriram Mohan, their colleagues and
         PUT_YOUR_NAME_HERE.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

###############################################################################
# TODO: 2.  Read and run this program.  Then do the following problems,
#   putting your answers RIGHT HERE IN THIS DOCUMENT.
#  __
#   1. True or False?  Write your answer here: _______
#      In the approach demonstrated in this module, all the loops begin with:
#         while True:
#  __
#   2. What 5-letter word causes the program to break out of a loop
#      and continue execution below the loop?
#          Write your answer here: ______
#  __
#   3. True or False?  Write your answer here: _______
#      A  break  statement works in a  FOR   loop as well as in a  WHILE  loop.
#  __
#   4. Run and read the code below for:
#            demonstrate_wait_for_circle_to_reach_edge.
#      Where in the loop are the   IF and break   statements:
#      Choose your answer from:
#          -- At the beginning of the loop
#          -- In the middle of the loop
#          -- At the end of the loop
#  __
#   5. Is   demonstrate_wait_for_circle_to_reach_edge   100% clear to you?
#        Yes or No?     [If No, ASK FOR HELP NOW!]
#  __
#   6. Run and read the code below for:
#            demonstrate_wait_for_sentinel.
#      What number is used as the SENTINEL in that function? ________
#  __
#   7. Is the concept of a SENTINEL and the code for
#      demonstrate_wait_for_sentinel   100% clear to you?
#        Yes or No?     [If No, ASK FOR HELP NOW!]
#  __
#   8. Run and read the code below for:
#            wait_for_small_enough_number.
#      Where in the loop are the   IF and break   statements:
#      Choose your answer from:
#          -- At the beginning of the loop
#          -- In the middle of the loop
#          -- At the end of the loop
#  __
#   9. Is   wait_for_small_enough_number   100% clear to you?
#        Yes or No?     [If No, ASK FOR HELP NOW!]
#  __
#  10. Read the comment about   random.seed(...)   that begins at about
#      line number 87 below.  Do you understand what  random.seed(...) does?
#        Yes or No?     [If No, ASK FOR HELP NOW!]
#  __
#   After you have PUT YOUR ANSWERS IN THIS COMMENT as described above,
#     a. Find someone who has had THEIR answer checked.
#     b. Ask THEM to check YOUR answers to the above.
#     c. Change the above _TODO_ to DONE.
#  __
#   As always, ask questions as needed!
###############################################################################

###############################################################################
# Students: Before you leave these examples,
#   *** MAKE SURE YOU UNDERSTAND THE   WAIT-FOR-EVENT   PATTERN,
#   *** with its use of   while True:   and   break.
###############################################################################

import math
import random
import time
import rosegraphics as rg


def main():
    """ Demonstrates applications of the wait-for-event pattern. """
    wait_for_circle_to_reach_edge()
    # wait_for_sentinel()
    # wait_for_small_enough_number()

    # The rest of  main  is just for fun, for those interested:
    # just_for_fun_long_waits()


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

    while True:
        # Construct and draw a purple circle.
        circle = rg.Circle(rg.Point(x, y), radius)
        circle.fill_color = "purple"
        circle.attach_to(window)

        # If the circle has reached a right/bottom border of the window,
        # break out of the loop
        right_edge = x + radius
        bottom_edge = y + radius

        if right_edge >= window.width or bottom_edge >= window.height:
            break

        # Make the next circle be down, to the right, and bigger.
        k = k + 1
        x = x + 2
        y = y + 1
        radius = radius + (k / 100)

        # Render. Allow a little time to elapse, else the animation flashes by.
        window.render(0.01)

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
    while True:
        number = int(input("Enter a positive integer, or -1 to quit: "))
        if number == -1:
            break
        print("The square root of {} is about {:0.5f}.\n".
              format(number, math.sqrt(number)))
        total = total + math.sqrt(number)

    print("The total of the square roots is", total)


# -----------------------------------------------------------------------------
# Set the random "seed" for the sequence of pseudo-random numbers.
# See the   m3e_random_numbers   module for details.
# -----------------------------------------------------------------------------
t = time.time()  # The number of seconds since January 1, 1970, as a float
random.seed((t * 10000) % 10000)  # The first 4 decimals of t


# -----------------------------------------------------------------------------
# Demonstrates waiting for a "small enough" random number to be generated.
# -----------------------------------------------------------------------------
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

    count = 0
    while True:
        count = count + 1
        number = random.randrange(1, max_number + 1)
        if print_it:
            print("   Randomly generated number: {}".format(number))
        if number <= small_number:
            break

    if print_it:
        print("{} random integers between 1 and {} were generated".format(
            count, max_number))
        print()

    return count


# -----------------------------------------------------------------------------
# Demonstrates more waiting for events, this time waiting
# for statistically unlikely events.
# -----------------------------------------------------------------------------
def just_for_fun_long_waits(iterations_asked_for=60, probability_required=0.2):
    """
    Demonstrates how long you have to wait for statistically unlikely events.
    In particular, this function prints how many times we had to run
    the above   wait_for_small_enough_number   function before it took
    the given number of iterations until the event first occurred,
    where the event occurs with the given probability.

    For example, if  probability_required = 0.2,  then we would expect about 5
    iterations before the event occurs.  So the probability of having to wait
    for ** 60 ** iterations before the event occurs should be VERY small, that
    is, it should take MANY iterations of THIS function to achieve that result.
    """
    print()
    print("----------------------------------------------------------")
    print("Demonstrating WAIT FOR AN UNLIKELY EVENT, namely,")
    print("that it requires a lot of calls to")
    print("  wait_for_small_enough_number")
    print("for a call that took a lot of iterations before returning.")
    print("Modify the arguments in this  just_for_fun_long_waits  module")
    print("if you want to play around with statistics.")
    print("----------------------------------------------------------")

    print("")
    print("The 'event' here occurs with probability {:0.2f}.".format(
        probability_required))
    print("We will now repeat the following experiment:")
    print("  1. Repeatedly generate random numbers until the 'event' occurs.")
    print("  2. See if the number of iterations needed until the 'event'")
    print("       occurred is at least {}.".format(iterations_asked_for))
    print("  3. If not, return to step 1.")
    print("")
    print("Note that if the event is not too unlikely and the")
    print("required number of iterations needed is not small, then")
    print("it should take a LONG time for this experiment to conclude.")
    print("FWIW, probability theory suggests that the expected number")
    print("of iterations of this experiment is:")
    print("   1 / ([1 - probability_required] ** iterations_asked_for).")
    print("For the above numbers, that equals about {:,}.".format(
        round(1 / (1 - probability_required) ** iterations_asked_for)))
    print("but expect large variations from run to run.")

    max_number = 1000  # Has an effect on the variance (spread) of results
    small_number = round(probability_required * max_number)
    count = 0
    while True:
        count = count + 1
        n = wait_for_small_enough_number(small_number, max_number,
                                         print_it=False)
        if n >= iterations_asked_for:
            break

    print()
    print("In fact,   {:,}   iterations were required.".format(count))


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
