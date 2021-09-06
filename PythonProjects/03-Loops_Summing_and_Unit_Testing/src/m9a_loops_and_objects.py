"""
This module demonstrates simple LOOPS of the form:
   for k in range(blah):
      ... k ...

and also USING OBJECTS.

Authors: David Mutchler, Vibha Alangar, Dave Fisher, Matt Boutell, Mark Hays,
         Mohammed Noureddine, Sana Ebrahimi, Sriram Mohan, their colleagues and
         PUT_YOUR_NAME_HERE.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


###############################################################################
# TODO: Read the following, then change its _TODO_ to DONE.
#   Throughout these exercises, you must use  RANGE  statements.
#   At this point of the course, you are restricted to the SINGLE-ARGUMENT
#   form of RANGE statements, like this:
#      range(blah):
#   There is a MULTIPLE-ARGUMENT form of RANGE statements (e.g. range(a, b))
#   but you are NOT permitted to use the MULTIPLE-ARGUMENT form yet,
#   for pedagogical reasons.
###############################################################################


def main():
    """ Calls the other functions to demonstrate and/or test them. """
    # Test your functions by putting calls to them here:


def print_sequence1():
    """
    Prints:
       0
       10
       20
       30
       40
       ...
       200
    """
    # -------------------------------------------------------------------------
    # TODO: 2. Implement this function, per its doc-string above.
    #   Put a statement in  main  to test this function.
    #   REQUIREMENT: You must use a   RANGE  statement to solve this problem.
    # -------------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print("Running print_sequence1:")
    print('--------------------------------------------------')


def draw_circles1():
    """
    -- Constructs an rg.RoseWindow whose width and height are both 400.
    -- Constructs and draws 19 rg.Circle objects such that:
         -- Each is centered at (200, 200)
         -- They have radii:  10  20  30  40 ... 190, respectively.
    -- Waits for the user to press the mouse, then closes the window.
    See   CIRCLES.pdf  in this project for a picture of the correct drawing.
    """
    # -------------------------------------------------------------------------
    # TODO: 3. Implement this function, per its doc-string above.
    #   Put a statement in  main  to test this function.
    #   REQUIREMENT: You must use a   RANGE  statement to solve this problem.
    #   HINT: Module  m2r_using_rosegraphics  has helpful examples for this.
    # -------------------------------------------------------------------------
    print()
    print("--------------------------------------------------")
    print("Running draw_circles1:  See graphics window")
    print("--------------------------------------------------")


def print_sequence2():
    """
    Prints:
      50
      70
      90
      110
      130
      ...
      390.
    """
    # -------------------------------------------------------------------------
    # TODO: 4. Implement this function, per its doc-string above.
    #   Put a statement in  main  to test this function.
    #   REQUIREMENT: You must use a   RANGE  statement to solve this problem.
    # -------------------------------------------------------------------------
    print()
    print("--------------------------------------------------")
    print("Running print_sequence2:")
    print("--------------------------------------------------")


def draw_circles2():
    """
    -- Constructs an rg.RoseWindow whose width and height are both 400.
    -- Constructs and draws rg.Circle objects such that:
         -- Each has radius 10.
         -- Each has fill_color 'blue'.
         -- They are centered at, respectively:
               (50, 100)   (70, 100)   (90, 100)  (110, 100) ... (390, 100)
    -- Waits for the user to press the mouse, then closes the window.
    See   CIRCLES.pdf  in this project for a picture of the correct drawing.
    """
    # -------------------------------------------------------------------------
    # TODO: 5. Implement this function, per its doc-string above.
    #   Put a statement in  main  to test this function.
    #   REQUIREMENT: You must use a   RANGE  statement to solve this problem.
    #   HINT: Module  m2r_using_rosegraphics  has helpful examples for this.
    # -------------------------------------------------------------------------
    print()
    print("--------------------------------------------------")
    print('Running draw_circles2:  See graphics window')
    print("--------------------------------------------------")


def print_sequence3():
    """
    Prints:
      1
      2
      3 
      4
      ...
      100.
    """
    # -------------------------------------------------------------------------
    # TODO: 6. Implement this function, per its doc-string above.
    #   Put a statement in  main  to test this function.
    #   REQUIREMENT: You must use a   RANGE  statement to solve this problem.
    # -------------------------------------------------------------------------
    print()
    print("--------------------------------------------------")
    print("Running print_sequence3:")
    print("--------------------------------------------------")


def draw_circles3():
    """
    -- Constructs an rg.RoseWindow whose width and height are both 300.
    -- Constructs and draws 100 rg.Circle objects such that:
         -- Each is centered at (200, 150)
         -- They have radii:  1  2  3  4  ... 100, respectively.
    -- Waits for the user to press the mouse, then closes the window.
    See   CIRCLES.pdf  in this project for a picture of the correct drawing.
    """
    # -------------------------------------------------------------------------
    # TODO: 7. Implement this function, per its doc-string above.
    #   Put a statement in  main  to test this function.
    #   REQUIREMENT: You must use a   RANGE  statement to solve this problem.
    # -------------------------------------------------------------------------
    print()
    print("--------------------------------------------------")
    print('Running draw_circles3:  See graphics window')
    print("--------------------------------------------------")


def print_cosines():
    """
    For each of the integers 0  1  2  ... 100,
    prints 80 times the cosine of that integer.
    Thus, the numbers printed should be about:
       80.0
       43.224184469451174
       -33.29174692377139
       -79.19939972803563
       -52.29148966908895
       22.6929748370581
       76.81362293202928
       60.31218034746437
         ...
       -65.54305962331674
       3.185670431451112
       68.9855097830147
    """
    # -------------------------------------------------------------------------
    # TODO: 8. Implement this function, per its doc-string above.
    #   Put a statement in  main  to test this function.
    #   REQUIREMENT: You must use a   RANGE  statement to solve this problem.
    #  _
    #   HINT: You need to   import math   at the top of this file
    #       to use math functions like the ones for cosine and sine.
    #       Once you have that import in place, typing
    #            math.
    #       (note the DOT) and pausing will display options that make
    #       it plain what the notation for the cosine function is.
    # -------------------------------------------------------------------------
    print()
    print("--------------------------------------------------")
    print("Running print_cosines:")
    print("--------------------------------------------------")


def draw_cosines_and_sines():
    """
    -- Constructs a window whose width and height are both 400.
    -- Constructs and draws rg.Circle objects such that:
         -- Each has radius 10.
         -- They are centered at, respectively:
               ( 200 + (80 * cos(0)), 200 + (80 * sin(0) )
               ( 200 + (80 * cos(1)), 200 + (80 * sin(1) )
               ( 200 + (80 * cos(2)), 200 + (80 * sin(2) )
               ( 200 + (80 * cos(3)), 200 + (80 * sin(3) )
                   ...
               ( 200 + (80 * cos(100)), 200 + (80 * sin(100) )
    -- Waits for the user to press the mouse, then closes the window.
    See   CIRCLES.pdf  in this project for a picture of the correct drawing.
    """
    # -------------------------------------------------------------------------
    # TODO: 9. Implement this function, per its doc-string above.
    #   Put a statement in  main  to test this function.
    #   REQUIREMENT: You must use a   RANGE  statement to solve this problem.
    # -------------------------------------------------------------------------
    print()
    print("--------------------------------------------------")
    print("Running draw_cosines_and_sines:  See graphics window")
    print("--------------------------------------------------")


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
