"""
PRACTICE Exam 1, problem 3.

Authors: David Mutchler, Sana Ebrahimi, Mohammed Noureddine, Vibha Alangar,
         Matt Boutell, Dave Fisher, their colleagues, and
         PUT_YOUR_NAME_HERE.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg

###############################################################################
# Students:
#
# These problems have DIFFICULTY and TIME ratings:
#  DIFFICULTY rating:  1 to 10, where:
#     1 is very easy
#     3 is an "easy" Test 1 question.
#     5 is a "typical" Test 1 question.
#     7 is a "hard" Test 1 question.
#    10 is an EXTREMELY hard problem (too hard for a Test 1 question)
#
#  TIME ratings: A ROUGH estimate of the number of minutes that we
#     would expect a well-prepared student to take on the problem.
#
#  IMPORTANT: For ALL the problems in this module,
#    if you reach the time estimate and are NOT close to a solution,
#    STOP working on that problem and ASK YOUR INSTRUCTOR FOR HELP
#    on it, in class or via Piazza.
###############################################################################


def main():
    """ Calls the   TEST   functions in this module. """
    run_test_problem3a()
    run_test_problem3b()


def run_test_problem3a():
    """ Tests the   problem3a   function. """
    # -------------------------------------------------------------------------
    # TODO: 2. Implement this TEST function.
    #   It TESTS the  problem3a  function defined below.
    #   Include at least **   5   ** tests (we wrote four for you).
    #  ------------------------------------------------------------------------
    #  DIFFICULTY AND TIME RATINGS (see top of this file for explanation)
    #    DIFFICULTY:      4
    #    TIME ESTIMATE:   10 to 15 minutes.
    # -------------------------------------------------------------------------
    # Window 1:
    title = 'Problem 3a. Test 1: Start at (30, 30), 6 lines'
    window1 = rg.RoseWindow(350, 200, title)

    # Test 1 (it is on window 1):
    point = rg.Point(30, 30)
    expected = 36
    answer = problem3a(window1, point, 6)
    print()
    print('Test 1 expected:', expected)
    print('       actual:  ', answer)

    window1.close_on_mouse_click()

    # Window 2:
    title = 'Problem 3a.  Test 2: Start at (80, 10), 9 lines.'
    title += '  Test 3: Start at (30, 50), 3 lines.'
    window2 = rg.RoseWindow(550, 200, title)

    # Test 2 (it is on window 2):
    point = rg.Point(80, 10)
    expected = 75
    answer = problem3a(window2, point, 9)
    print()
    print('Test 2 expected:', expected)
    print('       actual:  ', answer)

    # Test 3 (it is also on window 2):
    point = rg.Point(30, 50)
    expected = 9
    answer = problem3a(window2, point, 3)
    print()
    print('Test 3 expected:', expected)
    print('       actual:  ', answer)

    window2.close_on_mouse_click()

    # Window 3:
    title = 'Problem 3a. Test 4: Start at (30, 30), 20 lines'
    window3 = rg.RoseWindow(450, 300, title)

    # Test 4 (it is on window 3):
    point = rg.Point(30, 30)
    expected = 218
    answer = problem3a(window3, point, 20)
    print()
    print('Test 4 expected:', expected)
    print('       actual:  ', answer)

    window3.close_on_mouse_click()

    # -------------------------------------------------------------------------
    # TODO: 2 (continued).
    #   Below this comment (or integrated with one of the above tests,
    #   your choice), add 1 more test case of your own choosing.
    # -------------------------------------------------------------------------


def problem3a(window, point, n):
    """
    See   problem3a_picture.pdf   in this project for pictures
    that may help you better understand the following specification:

    What comes in:
      -- An rg.RoseWindow.
      -- An rg.Point.
      -- A nonnegative integer n.
    What goes out:
      -- Returns the sum of the thicknesses of the rg.Lines
         that are drawn as described in the Side effects (below).
    Side effects:
      Draws   n  rg.Lines on the given rg.RoseWindow,
      as follows:
        -- There are the given number (n) of rg.Lines.
        -- Each rg.Line is vertical and has length 50.
              (All units are pixels.)
        -- The top of the first (leftmost) rg.Line
              is at the given rg.Point.
        -- Each successive rg.Line is 20 pixels to the right
              and 10 pixels down from the previous rg.Line.
        -- The first rg.Line has thickness 1.
        -- Each successive rg.Line has thickness 2 greater than
              the rg.Line to its left, but no greater than 13.
              (So once a rg.Line has thickness 13,
              it and all the rg.Lines to its right have thickness 13.)
    Type hints:
        :type window: rg.RoseWindow
        :type point:  rg.Point
        :type n:      int
    """
    # -------------------------------------------------------------------------
    # TODO: 3. Implement and test this function.
    #   Note that you should write its TEST function first (above).
    #  ------------------------------------------------------------------------
    #  DIFFICULTY AND TIME RATINGS (see top of this file for explanation)
    #    DIFFICULTY:      7 or 8
    #    TIME ESTIMATE:   20 to 35 minutes.
    # -------------------------------------------------------------------------


def run_test_problem3b():
    """ Tests the   problem3b   function. """
    # Test 1 is ALREADY DONE (here).
    expected = 158
    answer = problem3b(4, rg.Point(100, 50))
    print()
    print('Test 1 expected:', expected)
    print('       actual:  ', answer)

    # Test 2 is ALREADY DONE (here).
    expected = 539
    answer = problem3b(7, rg.Point(30, 30))
    print()
    print('Test 2 expected:', expected)
    print('       actual:  ', answer)


def problem3b(m, point1):
    """
    See   problem3b_picture.pdf   in this project for pictures
    that may help you better understand the following specification:

    What comes in:
      -- A positive integer m.
      -- An rg.Point.
    What goes out:
      -- Returns the sum of the thicknesses of ALL of the lines drawn
         (over all  m  sets of lines).
    Side effects:
      -- Constructs and displays an rg.RoseWindow
         that is 400 wide by 650 tall.
      -- Draws, on the rg.RoseWindow,  m  SETS of lines, where:
          -- Each SET of lines is drawn
                 *** by a call to ** problem3a **. ***
          -- The first set has 3 lines that start at point1
               (the given point).
          -- The second set has 5 lines that start 60 pixels
               directly below point1.
          -- The third set has 7 lines that start 120 pixels
               directly below point1.
          -- The fourth set has 9 lines that start 180 pixels
               directly below point1.
          -- etc until  m  SETS of lines are drawn (where m is given).
          -- Each set of lines should have widths (thicknesses)
               per problem3a.
      -- Waits for the user to click the mouse (and displays an
           appropriate message prompting the user to do so),
           then closes the window.

    Type hints:
        :type m:      int
        :type point1: rg.Point
    """
    # -------------------------------------------------------------------------
    # TODO: 4. Implement and test this function.
    #          Tests have been written for you (above).
    #  ########################################################################
    #  IMPORTANT:
    #    **  For full credit you must appropriately use (call)
    #    **  the   problem3a   function that you implemented above.
    #  ------------------------------------------------------------------------
    #  DIFFICULTY AND TIME RATINGS (see top of this file for explanation)
    #    DIFFICULTY:      8 or 9
    #    TIME ESTIMATE:   20 to 30 minutes.
    # -------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
