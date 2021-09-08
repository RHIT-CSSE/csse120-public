"""
This module demonstrates the ACCUMULATOR pattern in three classic forms:
   SUMMING:       total = total + number
   COUNTING:      count = count + 1
   IN GRAPHICS:   x = x + pixels

Authors: David Mutchler, Yiji Zhang, Mark Hays, Derek Whitley, Vibha Alangar,
         Matt Boutell, Dave Fisher, Sriram Mohan, Mohammed Noureddine,
         Amanda Stouder, Curt Clifton, Valerie Galluzzi, their colleagues and
         PUT_YOUR_NAME_HERE.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

###############################################################################
# TODO: 2. Read the following, then change its _TODO_ to DONE.
#   Throughout these exercises, you must use  RANGE  statements.
#   At this point of the course, you are restricted to the SINGLE-ARGUMENT
#   form of RANGE statements, like this:
#         range(blah):
#   There is a MULTIPLE-ARGUMENT form of RANGE statements (e.g. range(a, b))
#   but you are NOT permitted to use the MULTIPLE-ARGUMENT form yet, for
#   pedagogical reasons.  Change the above _TODO_ to DONE after reading this.
###############################################################################

###############################################################################
# TODO: 3.
#   RUN this program, then READ its code.
#     Then answer the following, GETTING HELP AS NEED!  (Ask questions!!!)
#     Write your answers in any reasonable way (your choice).
#     _
#     For the first several questions, some students find the following
#     picture helpful.  (Your instructor may explain it in whole-group.)
#     _
#         0  1  2  3  4  ...  r-1  r  r+1  r+2  r+3  ...  s
#         |..... r numbers .....|
#         |................ s+1 numbers ..................|
#  Hence:                          |... (s+1)-r numbers ...|
#     _
#     a. If you want a loop that runs   r   times,
#          which of the following three choices would you use?
#     _
#            for k in range(r - 1):
#            for k in range(r):
#            for k in range(r + 1):
#     _
#     b. If you want a loop that runs from 0 to s, inclusive,
#          what expression would you use in the _____ below?
#     _
#            for k in range(_____):
#     _
#     c. If you want a loop that runs from r to s, inclusive, assuming s >= r,
#          what expression would you use in the _____ below?
#     _
#            for k in range(_____):
#     _
#     d. If you want a loop that runs from (r + 4) to (s - 10),
#          including the (r + 4) but not including the (s - 10),
#          what expression would you use in the _____ below?
#     _ 
#            for k in range(_____):
#     _
#     e. The following code snippet attempts to return the number
#          of integers from r to s, inclusive, whose cosines are positive.
#          It has at least 5 distinct errors (one per line).
#          Correct the errors.
#     _
#              for k in range(r - s):
#                  count = 0
#                  if math.cos(r) > 0:
#                      count = 1
#                  return count
#     _
#     f. The code in the "graphics accumulation" example below includes:
#              for _ in range(n):
#        What does the   _   (underscore) mean?
#     _
#     g. The code in the "graphics accumulation" example below includes:
#     _
#              x = starting_point.x
#              for _ in range(n):
#                  center = rg.Point(x, y)
#                  circle = rg.Circle(point, radius)
#                  circle.attach_to(window)
#                  x = x + diameter
#     _
#        If you want the row-of-circles that the above creates,
#        one of the following two attempts is a CORRECT attempt
#        (i.e., is equivalent in its functionality to the above)
#        and one is WRONG.  Which is the WRONG one?
#     _
#              x = starting_point.x
#              for k in range(n):
#                  center = rg.Point(x + (k * diameter), y)
#                  circle = rg.Circle(point, radius)
#                  circle.attach_to(window)
#     _
#              x = starting_point.x
#              for k in range(n):
#                  center = rg.Point(x + (k * diameter), y)
#                  circle = rg.Circle(point, radius)
#                  circle.attach_to(window)
#                  x = x + (2 * radius)
#  _
#  ############################################################################
#   *** MAKE SURE YOU UNDERSTAND THE 3   ACCUMULATOR   PATTERNS    ***
#   *** shown in this module:  SUMMING, COUNTING, and IN GRAPHICS  ***
#  ############################################################################
#   _
#   When you are confident that you understand the 3 accumulator patterns
#   and have correct answers to the above questions (ASK QUESTIONS AS NEEDED!),
#   check your work by asking a student assistant to look at your answers.
#   _
#   After checking your work (making corrections as needed),
#   change the above _TODO_ to DONE.
###############################################################################

import rosegraphics as rg
import math


def main():
    """ Calls the   TEST   functions in this module. """
    run_test_summing_example()
    run_test_counting_example()
    run_test_draw_row_of_circles()


def run_test_summing_example():
    """ Tests the   summing_example   function. """
    print()
    print("--------------------------------------------------")
    print("Testing the   summing_example   function:")
    print("--------------------------------------------------")

    # Test 1:
    expected = 100
    answer = summing_example(4)
    print("Test 1 expected:", expected)
    print("       actual:  ", answer)

    # Test 2:
    expected = 44100
    answer = summing_example(20)
    print("Test 2 expected:", expected)
    print("       actual:  ", answer)

    # Test 3:
    expected = 0
    answer = summing_example(0)
    print("Test 3 expected:", expected)
    print("       actual:  ", answer)


def summing_example(n):
    """
    What comes in:  The sole argument is a non-negative integer n.
    What goes out:  Returns the sum
         (1 cubed) + (2 cubed) + (3 cubed) + ... + (n cubed).
    Side effects:   None.
    Examples:
      -- If the integer is 4,
           this function returns (1 + 8 + 27 + 64), which is 100.
      -- If the integer is 20, this function returns 44,100.
    Type hints:
      :type n: int
      :rtype: int
    """
    total = 0  # Initialize to 0 BEFORE the loop
    for k in range(n):  # Loop
        total = total + ((k + 1) ** 3)  # Accumulate INSIDE the loop.

    return total  # Return the result AFTER the loop


def run_test_counting_example():
    """ Tests the   counting_example   function. """
    print()
    print("--------------------------------------------------")
    print("Testing the   counting_example   function:")
    print("--------------------------------------------------")

    # Test 1:
    expected = 2
    answer = counting_example(2)
    print("Test 1 expected:", expected)
    print("       actual:  ", answer)

    # Test 2:
    expected = 12
    answer = counting_example(20)
    print("Test 2 expected:", expected)
    print("       actual:  ", answer)

    # Test 3:
    expected = 1
    answer = counting_example(0)
    print("Test 3 expected:", expected)
    print("       actual:  ", answer)


def counting_example(n):
    """
    What comes in:  The sole argument is a non-negative integer n.
    What goes out:  Returns the number of integers from 0 to n,
      inclusive, whose cosine is positive.
    Side effects:   None.
    Examples:
      -- counting_example(2) returns 2
             since the cosine(0) is 1 (positive)
             and   the cosine(1) is about 0.54 (positive)
             and   the cosine(2) is about -0.42 (negative)

      -- counting_example(20) returns 12
             since the cosines of 0, 1, 5, 6, 7, 11, 12, 13, 14, 18, 19 and 20
             are positive

      -- counting_example(0) returns 1
             since the cosine(0) is positive.
    Type hints:
      :type n: int
      :rtype: int
    """
    count = 0  # Initialize to 0 BEFORE the loop
    for k in range(n + 1):  # Loop
        if math.cos(k) > 0:  # If the condition holds:
            count = count + 1  # Increment INSIDE the loop.

    return count  # Return the result AFTER the loop


def run_test_draw_row_of_circles():
    """ Tests the   draw_row_of_circles   function. """
    print()
    print("--------------------------------------------------")
    print("Testing the  draw_row_of_circles  function:")
    print("  See the graphics windows that pop up.")
    print("--------------------------------------------------")

    # -------------------------------------------------------------------------
    # TWO tests on ONE window.
    # -------------------------------------------------------------------------
    title = "Tests 1 and 2 of DRAW_ROW_OF_CIRCLES:"
    title = title + " 7 GREEN circles, 4 BLUE circles!"
    window1 = rg.RoseWindow(500, 250, title)

    # Test 1:
    center = rg.Point(50, 50)
    draw_row_of_circles(7, center, "green", window1)

    # Test 2:
    center = rg.Point(100, 150)
    draw_row_of_circles(4, center, "blue", window1)
    window1.close_on_mouse_click()

    # -------------------------------------------------------------------------
    # A third test on ANOTHER window.
    # -------------------------------------------------------------------------
    title = "Test 3 of DRAW_ROW_OF_CIRCLES:  Row of 12 RED circles!"
    window2 = rg.RoseWindow(600, 150, title)

    # Test 3:
    center = rg.Point(50, 50)
    draw_row_of_circles(12, center, "red", window2)

    window2.close_on_mouse_click()


def draw_row_of_circles(n, starting_point, color, window):
    """
    What comes in:  The four arguments are:
      -- A positive integer n.
      -- An rg.Point.
      -- A color appropriate for rosegraphics (e.g. "red")
      -- An rg.RoseWindow.
    What goes out:  Nothing (i.e., None).
    Side effects:
      Draws  n  rg.Circle objects in a row,
      all on the given rg.RoseWindow, such that:
        -- The first rg.Circle is centered at the given starting_point.
        -- Each rg.Circle just touches the previous one (to its left).
        -- Each rg.Circle has radius 20.
        -- Each rg.Circle is filled with the given color.
      Must  ** render **     but   ** NOT close **   the rg.RoseWindow.

     Type hints:
      :type n:               int
      :type starting_point:  rg.Point
      :type color:           str
      :type window:          rg.RoseWindow
    """
    # -------------------------------------------------------------------------
    # The example below shows one way to solve problems using
    #   HELPER variables (aka AUXILIARY variables)
    # In this approach:
    #  1. You determine all the variables that you need
    #       to construct/draw whatever the problem calls for.
    #       We call these HELPER variables.
    #  2. You initialize them BEFORE the loop, choosing values that
    #       make them just right for constructing and drawing the
    #       FIRST object to be drawn, in the FIRST time through the loop.
    #       For example,   x = starting_point.x   in the example below.
    #  3. You determine how many times the loop should run
    #       (generally, however many objects you want to draw)
    #       and write the FOR statement for the loop.
    #       For example,    for _ in range(n):  in the example below.
    #  4. Inside the loop you write the statements to construct and
    #       draw the FIRST object to be drawn, using your helper
    #       variables.  This is easy because you chose just the right
    #       values for those helper variables for this FIRST object.
    #  5. Test: Make sure the FIRST object appears.
    #       (It will be redrawn many times, that is OK).
    #  6. Add code at the BOTTOM of the loop that changes the helper
    #       variables appropriately for the NEXT time through the loop.
    #       For example,   x = x + diameter   in the example below.
    #  7. Test and fix as needed.
    #
    # Many students (and professionals) find this technique less
    # error-prone that using the loop variable to do all the work.
    # -------------------------------------------------------------------------

    radius = 20
    diameter = 2 * radius

    x = starting_point.x  # Initialize x and y BEFORE the loop.  Choose ...
    y = starting_point.y  # ... values that make the FIRST object easy to draw.

    for _ in range(n):  # Loop that does NOT use its index variable

        # ---------------------------------------------------------------------
        # Construct the relevant object(s),
        # based on the current x, y and other variables.
        # ---------------------------------------------------------------------
        center = rg.Point(x, y)
        circle = rg.Circle(center, radius)
        circle.fill_color = color

        # Attach the object(s) to the window.
        circle.attach_to(window)

        # ---------------------------------------------------------------------
        # Increment x (and in other problems, other variables)
        # for the thing(s) to draw in the NEXT iteration of the loop.
        # ---------------------------------------------------------------------
        x = x + diameter

    window.render()


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
