"""
Practice DEFINING and CALLING
     FUNCTIONS

Authors: David Mutchler, Yiji Zhang, Mark Hays, Derek Whitley, Vibha Alangar,
         Matt Boutell, Dave Fisher, Sriram Mohan, Mohammed Noureddine,
         Amanda Stouder, Curt Clifton, Valerie Galluzzi, their colleagues and
         PUT_YOUR_NAME_HERE.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

###############################################################################
# TODO: 2.
#   Allow this module to use the  rosegraphics.py  module by marking the
#     src
#   folder in this project as a "Sources Root", as follows:
#  _
#     In the Project window (to the left), right click on the src  folder,
#     then select  Mark Directory As  ~  Sources Root.
###############################################################################

import rosegraphics as rg


def main():
    """
    TESTS the functions that you will write below.
    You write the tests per the _TODO_s below.
    """
    window = rg.TurtleWindow()
    # Put your TESTS immediately below this line, as directed by _TODO_s below.

    window.close_on_mouse_click()


###############################################################################
# TODO: 3a.  Define a function immediately below this _TODO_.
#   It takes two arguments that denote, for a right triangle,
#   the lengths of the two sides adjacent to its right angle,
#   and it returns the length of the hypotenuse of that triangle.
#     HINT: Apply the Pythagorean theorem.
#  _
#   You may name the function and its parameters whatever you wish,
#   but choose DESCRIPTIVE (self-documenting) names.
#
# TODO: 3b.  In main, CALL your function TWICE (with different values
#   for the arguments) and print the returned values,
#   to test whether you defined the function correctly.
###############################################################################


###############################################################################
# TODO: 4a.  Define a function immediately below this _TODO_.
#   It takes two arguments:
#     -- a string that represents a color (e.g. "red")
#     -- a positive integer that represents the thickness of a Pen.
#  _
#   The function should do the following (in the order listed):
#     a. Constructs two SimpleTurtle objects, where:
#          - one has a Pen whose color is "green" and has the GIVEN thickness
#          - the other has a Pen whose color is the GIVEN color
#              and whose thickness is 5
#  _
#        Note: the "GIVEN" color means the PARAMETER that represents a color.
#        Likewise, the "GIVEN" thickness means the PARAMETER for thickness.
#  _
#     b. Makes the first (green) SimpleTurtle move FORWARD 100 pixels.
#  _
#     c. Makes the other (thickness 5) SimpleTurtle move BACKWARD 100 pixels.
#  _
#   You may name the function and its parameters whatever you wish,
#   but choose DESCRIPTIVE (self-documenting) names.
#
# TODO: 4b.  In main, CALL your function at least TWICE (with different values
#   for the arguments) to test whether you defined the function correctly.
###############################################################################

###############################################################################
# TODO: 5.
#   COMMIT-and-PUSH your work (after changing this _TODO_ to DONE).
#  _
#   As a reminder, here is how you should do so:
#     1. Select   VCS      from the menu bar (above).
#     2. Choose   Commit   from the pull-down menu that appears.
#     3a. In the   Commit Changes   window that pops up,
#         - If there is no message in the
#             Commit Message
#          sub-box, put one there, e.g. "Done."
#     3b:  In that same   Commit Changes   window that pops up:
#        - Press the   Commit and Push   button.
#           (Note: If you see only a Commit button:
#              - HOVER over the  Commit  button
#                (in the lower-right corner of the window)
#              - CLICK on  Commit and Push.)
#  _
#   COMMIT adds the changed work to the version control system on your COMPUTER.
#   PUSH adds the changed work into your repository in the "cloud".
#  _
#   Always PUSH (in addition to the COMMIT) so that your work
#   is backed-up in the cloud.  If you COMMIT but forget to PUSH,
#   you can subsequently do the PUSH by:
#      VCS ~ Git ~ Push...
#  _
#   Oh, one more thing:
#     Do you have any blue bars on the scrollbar-like thing to the
#     right?  If so, click on each blue bar and change its _TODO_ to
#     DONE and then run the module (to make sure you did not break
#     anything) and COMMIT-and-PUSH again.
#  _
#   You can COMMIT-and-PUSH as often as you like.
#   DO IT FREQUENTLY; AT LEAST once per module.
###############################################################################


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
