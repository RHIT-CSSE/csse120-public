"""
This module lets you practice correcting SYNTAX (notation) errors.

Authors: David Mutchler, Yiji Zhang, Mark Hays, Derek Whitley, Vibha Alangar,
         Matt Boutell, Dave Fisher, Sriram Mohan, Mohammed Noureddine,
         Amanda Stouder, Curt Clifton, Valerie Galluzzi, their colleagues and
         PUT_YOUR_NAME_HERE.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

###############################################################################
# TODO: 2.
#   Locate the syntax (notation) errors in this file
#   by looking for red underlines.
#  _
#   For each error, try to make sense of its message.
#     -- HOVER and/or expand as needed -- ** make SURE you see the message! **
#  _
#   Then fix the errors, one by one.  IMPORTANT:
#     -- Fixing one error may bring up additional errors
#          (after a few seconds or when you run or save the module).
#     -- Each time, fix the error that is nearest the TOP of the module,
#          although sometimes that fix does not "take effect"
#          until you have fixed major errors beneath it.
#     -- Often the SOURCE of the error may be on the line
#          just BEFORE the line with a red underline.
#     -- New errors may appear during the RUN of the module.
#  _
#    Finish this _TODO_ by RUNNING the corrected program
#    and making sure that it RUNS CORRECTLY.
#      That is, make sure that (per the green doc-strings) the program
#      prints two calculated values and makes a SimpleTurtle do some things.
###############################################################################

import rosegraphics as rg


def main():
    """ Calls the other functions in this module to demo them. """
    print_math()
    tutle_fn()


def print_math:
    """ Prints some calculated values. """
    x = cos(pi)
    print(x)

    y = sin(pi)
    print(The sine of PI is, y)


def turtle_fun():
    """
    Constructs a TurtleWindow,
    constructs a classic SimpleTurtle and asks it to do some things,
    and waits for the user to click anywhere in the window to close it.
    """
    window = rg.TurtleWindow()

    alan = rg.SimpleTurtle()
alan.pen = rg.Pen('blue', 30)
    alan.paint_bucket = rg.PaintBucket('yellow')

    alan.back(3 * (47 + 16)
    al.begin_fill()
    alan.circle(25)
    alan.end_fill()

    forward(200)

    window.close_on_mouse_click()

###############################################################################
# TODO: 3.
#  All professional code must meet the STANDARDS of the organization (company).
#  For us, we will use the widely-used PEP 8 standard.
#  AFTER you have corrected the errors in the above,
#  do     Code ~ Reformat Code
#  It will try to correct any remaining PEP 8 style violations.
#  (Note: It generally corrects some PEP 8 errors but not all.)
#  _
#   When finished, COMMIT-and-PUSH your work, as always.
###############################################################################

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
