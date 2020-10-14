"""
This module demonstrates why MUTATION is DANGEROUS:

Example 1:
  -- A function has a error (it mutates a parameter when it shouldn't).
  -- That error does not become apparent in testing the function,
     but the error messes up ANOTHER function that CALLS the first one.

Example 2:
  -- The author constructs a BankAccount with $1,000 savings.
  -- She shows her checking and savings balances.
       Surely that is safe!
  -- But unbeknownst to her, evil David has put nasty code into the
       show_balances   method, that steals the rest of her savings!
  -- So her money is now gone!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Mark Hays, Amanda Stouder, Derek Whitley, and their colleagues.
"""

import rosegraphics as rg
import random

# -----------------------------------------------------------------------------
# Students: Read and run this program.
#           Do you see how   MUTATION   made the nasty stuff possible?
#           If objects were immutable, the  show_balances  method simply
#           could NOT steal her money!
# -----------------------------------------------------------------------------


def main():
    one_example_of_danger()
    another_example_of_danger()


def one_example_of_danger():
    # -------------------------------------------------------------------------
    # Students:
    #   1. Read the   move_randomly   specification below.
    #   2. Run   run_test_move_randomly.
    #   3. Does the code pass the test?  (Answer: Yes.)
    #
    # Then:
    #   1. Read the   repeat_move_randomly   specification below.
    #   2. Run   run_test_repeat_move_randomly.
    #   3. Does the code pass the test?  (Answer: No.)
    #
    # So, you would think that the   REPEAT_move_randomly   code
    # has an error.  But look at that code, and you will see that
    # it definitely is OK!
    #
    # Can you figure out what went wrong?
    # Once you do so, do you see why mutation is dangerous?
    # -------------------------------------------------------------------------

    # Un-comment these as you do the above exercise.
    run_test_move_randomly()
    run_test_repeat_move_randomly()


def run_test_move_randomly():
    """ Tests the   move_randomly   function. """
    window = rg.RoseWindow(800, 500)

    circle1 = rg.Circle(rg.Point(400, 250), 50)
    circle1.fill_color = 'blue'
    circle1.attach_to(window)
    move_randomly(window, circle1, 50, 0.05)

    circle2 = rg.Circle(rg.Point(200, 100), 30)
    circle2.fill_color = 'red'
    circle2.attach_to(window)
    move_randomly(window, circle2, 250, 0.01)

    window.close_on_mouse_click()


def move_randomly(window, circle, times_to_move, seconds_per_move):
    """
    Repeatedly moves a copy of the given circle a small random distance
    on the given window.  Does this the given number of times, rendering
    and pausing for the given number of seconds after each move.
    Includes a small 'drift' to the right.

    Preconditions:
      :type window: rg.RoseWindow
      :type circle: rg.Circle
      :type times_to_move: int
      :type seconds_per_move: float | int
    where the times_to_move and seconds_per_move are non-negative
    and where the circle is already attached to the given window.
    """
    # -------------------------------------------------------------------------
    # Students: The following implementation of the above specification
    #           has an error.
    #   1. Do the tests expose the error?
    #   2. Can you spot the error?
    # -------------------------------------------------------------------------
    for _ in range(times_to_move):
        dx = random.randrange(-5, 7)
        dy = random.randrange(-5, 6)
        circle.move_by(dx, dy)
        window.render(seconds_per_move)


def run_test_repeat_move_randomly():
    """ Tests the   repeat_move_randomly   function. """
    window = rg.RoseWindow(800, 500)

    circle = rg.Circle(rg.Point(400, 250), 50)
    circle.fill_color = 'green'
    circle.attach_to(window)
    repeat_move_randomly(5, circle, window)

    window.close_on_mouse_click()


def repeat_move_randomly(n, circle, window):
    """
    Runs   move_randomly   n   times using the given circle and window,
    each time making 200 random moves with 0 seconds pause after each.
    Waits for a mouse click after each of the   n   trials.

    Preconditions:
      :type n: int
      :type circle: rg.Circle
      :type window: rg.RoseWindow
    where n is non-negative and the circle is already attached
    to the given window.
    """
    for _ in range(n):
        move_randomly(window, circle, 200, 0)
        window.continue_on_mouse_click()


def another_example_of_danger():
    # -------------------------------------------------------------------------
    # Students:
    #   1. Read the code in this function.
    #        -- Do NOT read the code of the BankAccount class.
    #           Imagine that you are a USER, not an AUTHOR,
    #           of the BankAccount class.
    #   2. Predict what the last line of this function will print.
    #   3. Run the function.
    #        -- Does the function print what you expected? (Answer: No.)
    #
    # Can you figure out what went wrong?
    # Once you do so, do you see why mutation is dangerous?
    # -------------------------------------------------------------------------
    my_money = BankAccount(1000, 300)  # $1,000 in savings. $300 in checking
    print('Savings, checking:', my_money.savings, my_money.checking)

    my_money.pay_for_college(100)  # Uses $100 of my savings as tuition
    my_money.show_balances()

    my_money.pay_for_college(100)  # Should have plenty left, but ...!
    my_money.show_balances()


class BankAccount(object):
    def __init__(self, savings, checking):
        self.savings = savings
        self.checking = checking

    def show_balances(self):
        print('Your savings  balance is: ', self.savings)
        print('Your checking balance is: ', self.checking)

        # ---------------------------------------------------------------------
        # The following line is an "error" inserted by evil David!
        # One would NOT expect a   SHOW_balances   method to mutate
        # the object, but there is nothing to prevent that.
        # Hence, the danger.
        # ---------------------------------------------------------------------
        self.give_money_to_david()

    def pay_for_college(self, tuition):
        print()
        message = 'Using {} of your savings to pay for college.'
        print(message.format(tuition))

        if self.savings >= tuition:
            self.savings = self.savings - tuition
        else:
            print('Yikes! Your savings is not enough! Where did it go?!')

    def give_money_to_david(self):
        # Imagine that the money sneaks into David's account...
        self.savings = 0


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
