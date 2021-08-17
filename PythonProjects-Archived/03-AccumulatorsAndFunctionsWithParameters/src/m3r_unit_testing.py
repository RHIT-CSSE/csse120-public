"""
This module helps you understand:
  -- UNIT TESTING.
  -- the difference between PRINT and RETURN

Authors: David Mutchler, Vibha Alangar, Dave Fisher, Matt Boutell, Mark Hays,
         Mohammed Noureddine, Sana Ebrahimi, Sriram Mohan, their colleagues and
         PUT_YOUR_NAME_HERE.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

###############################################################################
# TODO: 2.  If you have not already done so:
#   Allow this module to use the  rosegraphics.py  module by marking the
#     src
#   folder in this project as a "Sources Root", as follows:
#     ____
#     In the Project window (to the left), right click on the src  folder,
#     then select  Mark Directory As  ~  Sources Root.
###############################################################################

import rosegraphics as rg
import math


def main():
    """ Calls the   TEST   functions in this module. """
    run_test_distance()


def run_test_distance():
    """ Tests the distance function by using 3 tests. """
    # Test 1:
    expected = math.sqrt(2)
    answer = distance(rg.Point(1, 1))
    print("Test 1 expected:", expected)
    print("       actual:  ", answer)

    # Test 2:
    expected = 5
    answer = distance(rg.Point(3, 4))
    print("Test 2 expected:", expected)
    print("       actual:  ", answer)

    # Test 3:
    expected = 0
    answer = distance(rg.Point(0, 0))
    print("Test 3 expected:", expected)
    print("       actual:  ", answer)


def distance(point):
    """
    What comes in:  An rg.Point.
    What goes out:  Returns the distance that the rg.Point is from (0, 0).
    Side effects:   None.
    Example:
      If the argument is  rg.Point(3, 4)  this function returns 5.
    Type hints:
      :type point: rg.Point
      :rtype: float
    """
    # This code has an error, on purpose.  Do NOT fix it.
    x_squared = point.x * point.x
    y_squared = point.y * point.x

    return math.sqrt(x_squared + y_squared)


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()

###############################################################################
# TODO: 3.
#   READ the following, asking questions as needed.
#   When you believe that you understand what is says about UNIT TESTING,
#   mark the above _TODO_ as DONE.
#  _
#   In most exercises we will follow the  UNIT TESTING
#   that the above code illustrates.
#  _
#   Look at the  DISTANCE  function defined above.
#   It is the function that we want to test.  Read its doc-string.
#  _
#   Now look at the  RUN_TEST_DISTANCE  function defined above.
#   It is the function that  TESTS  the DISTANCE function.
#   We call this  UNIT TESTING  because we are testing a single UNIT
#   of the program, here, the function DISTANCE.
#  _
#   A   run_test_blah   function does the following several times:
#  _
#     1.  The  HUMAN  tester figures out the CORRECT (EXPECTED) answer
#         on a particular test case, usually by working the problem
#         by hand or by trusting a test case provided by the instructor.
#  _
#         For example, in the above   run_test_distance   function,
#         the human tester figured out, by doing the problem by hand,
#         that the distance that (3, 4) is from (0, 0) is 5:
#             expected = 5
#  _
#     2.  The  run_test_distance  function CALLS the function to test,
#         sending it the test case the human tester chose, like this:
#             answer = distance(rg.Point(3, 4))
#  _
#         The code CAPTURES the returned value in a variable (namely, answer).
#  _
#     3.  The  run_test_distance  function then PRINTS both the EXPECTED
#         answer (5 in our example) and the ACTUAL answer returned
#         (the value of the variable answer).
#             print('Test 3 expected:', expected)
#             print('       actual:  ', answer)
#  _
#   The above forms a single TEST for a function that returns a value.
#   When the software developer / tester runs the run_test_distance function,
#   she compares the EXPECTED and ACTUAL values that are printed.
#     -- If they are the same, the code PASSED the test.
#     -- If they are different, the code FAILED the test.
#  _
#   If the code failed the test, the software developer then uses tools
#   like a debugger to find the source of the error and fix it.
#   The error might be in the code (as in the above example)
#   or in the test (if the human tester came up with a wrong answer).
#  _
#   RUN this program now.  Did the DISTANCE function pass its tests?
#   (Answer: it passed TWO of its tests but NOT all three.)
#  _
#   Testing is a BIG topic, but UNIT TESTING like the code above is a start.
#  _
#   One more thing:
#   Students sometimes confuse PRINT and RETURN because you will almost
#   always test your functions using this
#      capture-in-variable-then-print-variable
#   approach.  From that alone, it looks like the function could have
#   PRINTED the result instead of RETURNING it.
#   But remember -- in REAL programs, functions rarely print anything;
#     ** Functions  RETURN  values for OTHER functions to use. **
#   We are teaching you practices that scale up, so we demand that most
#   of the functions that you write from here on RETURN a value instead
#   of PRINTING it.
###############################################################################
