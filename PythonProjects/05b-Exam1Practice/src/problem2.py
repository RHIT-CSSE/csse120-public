"""
PRACTICE Exam 1, problem 2.

Authors: David Mutchler, Vibha Alangar, Dave Fisher, Matt Boutell, Mark Hays,
         Mohammed Noureddine, Sana Ebrahimi, Sriram Mohan, their colleagues and
         PUT_YOUR_NAME_HERE.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

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
import rosegraphics as rg


def main():
    """ Calls the   TEST   functions in this module. """
    print("-----------------------------------------------")
    print("Un-comment each of the following TEST functions")
    print("as you implement the functions that they test.")
    print("-----------------------------------------------")

    # run_test_problem2a()
    # run_test_problem2b()


def run_test_problem2a():
    """ Tests the   problem2a  function. """
    print()
    print("--------------------------------------------------")
    print("Testing the  problem2a  function:")
    print("  See the graphics windows that pop up.")
    print("--------------------------------------------------")

    # TWO tests on ONE window.
    title = "Tests 1 & 2 of problem2a: "
    title += "red to blue, then blank to green"
    window = rg.RoseWindow(450, 250, title)

    circle = rg.Circle(rg.Point(100, 50), 30)
    rectangle = rg.Rectangle(rg.Point(100, 120), rg.Point(200, 170))
    rectangle.outline_color = "blue"
    circle.fill_color = "red"
    problem2a(circle, rectangle, window)  # Run the code to be tested
    window.continue_on_mouse_click()

    circle = rg.Circle(rg.Point(300, 100), 50)
    rectangle = rg.Rectangle(rg.Point(300, 170), rg.Point(400, 120))
    rectangle.outline_color = "green"
    problem2a(circle, rectangle, window)  # Run the code to be tested
    window.close_on_mouse_click()

    # A third test on ANOTHER window.
    title = "Test 3 of problem2a: yellow to black"
    window = rg.RoseWindow(400, 300, title)

    circle = rg.Circle(rg.Point(100, 50), 30)
    rectangle = rg.Rectangle(rg.Point(100, 100), rg.Point(50, 250))
    rectangle.outline_color = "black"
    circle.fill_color = "yellow"
    problem2a(circle, rectangle, window)  # Run the code to be tested
    window.close_on_mouse_click()


# IMPORTANT: See the IMPORTANT note in the _TODO_ below.
def problem2a(circle, rectangle, window):
    """
    See   problem2a_picture.pdf   in this project for pictures
    that may help you better understand the following specification:
    
    What comes in:
      -- An rg.Circle.
      -- An rg.Rectangle.
      -- An rg.RoseWindow.
    What goes out:  Nothing (i.e., None).
    Side effects:
      -- Draws the given rg.Circle and rg.Rectangle
           on the given rg.RoseWindow,
           then waits for the user to click the window.
      -- Then draws an rg.Line from the upper-right corner
           of the rg.Rectangle to its lower-left corner,
           with the line drawn as an arrow,
           then waits for the user to click the window.
      -- Changes the fill color of the given rg.Circle to the
           outline color of the given rg.Rectangle,
           then renders the window again
           (with no waiting for a click from the user this time).
      Must  ** NOT close **   the window.

    Type hints:
      :type circle:    rg.Circle
      :type rectangle: rg.Rectangle
      :type window:    rg.RoseWindow
    """
    # -------------------------------------------------------------------------
    # TODO: 2. Implement and test this function.
    #          Tests have been written for you (above).
    #  _
    #  IMPORTANT: Drawing the line as an arrow is a BONUS point;
    #             try briefly to do it, then find its answer on Piazza.
    #  ------------------------------------------------------------------------
    #  DIFFICULTY AND TIME RATINGS (see top of this file for explanation)
    #    DIFFICULTY:      5                (not counting the arrow)
    #    TIME ESTIMATE:   10 to 15 minutes (not counting the time for arrow)
    # -------------------------------------------------------------------------


def run_test_problem2b():
    """ Tests the  problem2b   function. """
    print()
    print("--------------------------------------------------")
    print("Testing the   problem2b   function:")
    print("  See the graphics windows that pop up.")
    print("--------------------------------------------------")

    # TWO tests on ONE window.
    title = "Tests 1 & 2 of problem2b: "
    title += "6 on blue with delta=15, 3 on green with delta=50"
    window = rg.RoseWindow(550, 450, title)

    rectangle = rg.Rectangle(rg.Point(100, 100), rg.Point(140, 120))
    rectangle.fill_color = "blue"
    problem2b(rectangle, 6, 15, window)  # Run the code to be tested
    window.continue_on_mouse_click()

    rectangle = rg.Rectangle(rg.Point(400, 300), rg.Point(350, 200))
    rectangle.fill_color = "green"
    problem2b(rectangle, 3, 50, window)  # Run the code to be tested
    window.close_on_mouse_click()

    title = "Test 3 of problem2b: 10 on red with delta=12"
    window = rg.RoseWindow(400, 350, title)

    rectangle = rg.Rectangle(rg.Point(250, 150), rg.Point(200, 200))
    rectangle.fill_color = "red"
    problem2b(rectangle, 10, 12, window)  # Run the code to be tested
    window.close_on_mouse_click()


def problem2b(rect, n, delta, win):
    """
    See   problem2b_picture.pdf   in this project for pictures
    that may help you better understand the following specification:
    
    What comes in:
      -- An rg.Rectangle.
      -- A positive integer n.
      -- A positive integer delta.
      -- An rg.RoseWindow.
    What goes out:  Nothing (i.e., None).
    Side effects:
      Draws n rg.Rectangles on the given rg.RoseWindow such that:
        -- The first rg.Rectangle is the given one.
        -- Subsequent rg.Rectangles have the same center
            as the given rg.Rectangle, but their width
            and height are each   (2 * delta)   greater than
            the width and height of the previous rg.Rectangle.
              -- That is, the distance from each line of each rg.Rectangle
                 to the corresponding line of the rg.Rectangle next to it
                 is delta.  (See problem2b_picture.)
      Must render but   ** NOT close **   the window.

    Type hints:
      :type rect:   rg.Rectangle
      :type n:      int
      :type delta:  int
      :type win:    rg.RoseWindow
    """
    # -------------------------------------------------------------------------
    # TODO: 3. Implement and test this function.
    #          Tests have been written for you (above).
    #  ------------------------------------------------------------------------
    #  DIFFICULTY AND TIME RATINGS (see top of this file for explanation)
    #    DIFFICULTY:      7
    #    TIME ESTIMATE:   10 to 15 minutes.
    # -------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
