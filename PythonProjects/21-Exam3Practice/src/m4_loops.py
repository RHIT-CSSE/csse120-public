"""
PRACTICE Exam 3.

This problem provides practice at:  LOOPS, including:
  ***  FOR and WHILE loops.  ***

Authors: David Mutchler, Vibha Alangar, Dave Fisher, Matt Boutell, Mark Hays,
         Mohammed Noureddine, Sana Ebrahimi, Sriram Mohan, their colleagues and
         PUT_YOUR_NAME_HERE.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

###############################################################################
# TODO: 2.  [Note: same _TODO_ as its matching one in module m1.]
#  Students:
#  __
#  These problems have DIFFICULTY and TIME ratings:
#    DIFFICULTY rating:  1 to 10, where:
#       1 is very easy
#       3 is an "easy" Exam 3 question.
#       5 is a "typical" Exam 3 question.
#       7 is a "hard" Exam 3 question.
#      10 is an EXTREMELY hard problem (too hard for a Exam 3 question)
#  __
#    TIME ratings: A ROUGH estimate of the number of minutes that we
#       would expect a well-prepared student to take on the problem.
#  __
#    IMPORTANT: For ALL the problems in this module,
#      if you reach the time estimate and are NOT close to a solution,
#      STOP working on that problem and ASK YOUR INSTRUCTOR FOR HELP on it,
#      in class or via Piazza.
#  __
#  After you read (and understand) the above, change this _TODO_ to DONE.
###############################################################################

import simple_testing as st
import time
import math
import testing_helper


def main():
    """ Calls the   TEST   functions in this module. """
    print()
    print("Un-comment and re-comment calls in MAIN one by one as you work.")

    # run_test_practice_problem3a()
    # run_test_practice_problem3b()


# -----------------------------------------------------------------------------
# Students: Some of the testing code below uses SimpleTestCase objects,
#           from the imported   simple_testing (st)   module.
# -----------------------------------------------------------------------------


def run_test_practice_problem3a():
    """ Tests the   practice_problem3a  function. """
    ###########################################################################
    # TODO: 3. Implement this TEST function.
    #   It TESTS the  practice_problem3a  function defined below.
    #   Include at least ** 1 ** ADDITIONAL test beyond those we wrote.
    #  __
    #   Try to choose tests that might expose errors in your code!
    #  __
    #   As usual, include both EXPECTED and ACTUAL results in your tests
    #   and compute the latter BY HAND (not by running your program).
    ###########################################################################
    # DIFFICULTY AND TIME RATINGS (see top of this file for explanation)
    #    DIFFICULTY:      3
    #    TIME ESTIMATE:   10 minutes.
    ###########################################################################

    # -------------------------------------------------------------------------
    # Many tests, followed by extra ones appended at the end.
    # They use the imported   simple_testing (st)   module.
    # Each test is a SimpleTestCase with 3 arguments:
    #   -- the function to test,
    #   -- a list containing the argument(s) to send to the function,
    #   -- the correct returned value.
    # For example, the first test below will call
    #   practice_problem3a(6, 8, 0.81)
    # and compare the returned value against [7, 8] (the correct answer).
    # -------------------------------------------------------------------------
    tests = [st.SimpleTestCase(practice_problem3a,
                               [6, 8, 0.81],
                               [7, 8]),
             st.SimpleTestCase(practice_problem3a,
                               [-4, 9, 0.25],
                               [0, 1, 2, 6, 7, 8]),
             st.SimpleTestCase(practice_problem3a,
                               [-5, 4, 0.25],
                               [-5, 0, 1, 2]),
             st.SimpleTestCase(practice_problem3a,
                               [-3, 8, 0.65],
                               [0, 1, 6, 7, 8]),
             st.SimpleTestCase(practice_problem3a,
                               [-4, 8, 0.65],
                               [0, 1, 6, 7, 8]),
             st.SimpleTestCase(practice_problem3a,
                               [-5, 8, 0.65],
                               [-5, 00, 1, 6, 7, 8]),
             st.SimpleTestCase(practice_problem3a,
                               [-3, 3, -1.0],
                               [-1, 0, 1, 2, 3]),
             st.SimpleTestCase(practice_problem3a,
                               [-3, 4, -1.0],
                               [-1, 0, 1, 2, 3]),
             st.SimpleTestCase(practice_problem3a,
                               [-3, 5, -1.0],
                               [-1, 0, 1, 2, 3, 5]),
             st.SimpleTestCase(practice_problem3a,
                               [-3, 6, -1.0],
                               [-1, 0, 1, 2, 3, 5, 6]),
             st.SimpleTestCase(practice_problem3a,
                               [30, 0, -1000],
                               []),
             st.SimpleTestCase(practice_problem3a,
                               [100, 1000, 1.414],
                               [139, 183, 516, 560, 849, 893]),
             st.SimpleTestCase(practice_problem3a,
                               [-1000, 1000000, math.sqrt(2) - 0.0000000001],
                               [286602, 599291, 911980]),
             st.SimpleTestCase(practice_problem3a,
                               [-1000, 1000000, 1.414213562373],
                               [286602]),
             st.SimpleTestCase(practice_problem3a,
                               [-1000, 1000000, 1.414213562374],
                               []),
             ]
    # More tests, with larger lists as the expected returned values
    big_list = []
    for k in range(900, 1001):
        big_list.append(k)
    tests.append(st.SimpleTestCase(practice_problem3a,
                                   [900, 1000,
                                    - math.sqrt(2) + 0.00001],
                                   big_list))

    big_list_without_915 = big_list.copy()
    big_list_without_915.remove(915)
    tests.append(st.SimpleTestCase(practice_problem3a,
                                   [900, 1000,
                                    - math.sqrt(2) + 0.0001],
                                   big_list_without_915))

    # -------------------------------------------------------------------------
    # Run the tests in the   tests   list constructed above.
    # -------------------------------------------------------------------------
    st.SimpleTestCase.run_tests('practice_problem3a', tests)

    ###########################################################################
    # TODO: 3 continued:  More tests:
    #      YOU add at least **   1   ** additional test here.
    #  __
    #   You can use the   SimpleTestCase  class as above, or use
    #   the ordinary   expected/actual   way, your choice.
    #  __
    #   SUGGESTION: Ask an assistant to CHECK your tests to confirm
    #               that they are adequate tests!
    ###########################################################################


def practice_problem3a(start, stop, threshold):
    """
    What comes in:
      -- Non-negative integers start and stop, with stop >= start
      -- A number:  threshold
    What goes out:  Returns a list of all the integers,
      starting at start and ending at stop (inclusive),
      for which the sum of the integer's sine and cosine
      is bigger than the given threshold.
    Side effects: None.
    Examples:
      For the following examples, the following numbers are helpful.
      They are listed here just to help you avoid needing a calculator..
      Each is rounded to 2 decimal places for the sake of brevity.
        -5:  sin =  0.96,  cos =  0.28,  sum =  1.24
        -4:  sin =  0.76,  cos = -0.65,  sum =  0.10
        -3:  sin = -0.14,  cos = -0.99,  sum = -1.13
        -2:  sin = -0.91,  cos = -0.42,  sum = -1.33
        -1:  sin = -0.84,  cos =  0.54,  sum = -0.30
         0:  sin =  0.00,  cos =  1.00,  sum =  1.00
         1:  sin =  0.84,  cos =  0.54,  sum =  1.38
         2:  sin =  0.91,  cos = -0.42,  sum =  0.49
         3:  sin =  0.14,  cos = -0.99,  sum = -0.85
         4:  sin = -0.76,  cos = -0.65,  sum = -1.41
         5:  sin = -0.96,  cos =  0.28,  sum = -0.68
         6:  sin = -0.28,  cos =  0.96,  sum =  0.68
         7:  sin =  0.66,  cos =  0.75,  sum =  1.41
         8:  sin =  0.99,  cos = -0.15,  sum =  0.84
         9:  sin =  0.41,  cos = -0.91,  sum = -0.50
        10:  sin = -0.54,  cos = -0.84,  sum = -1.38
        11:  sin = -1.00,  cos =  0.00,  sum = -1.00
        12:  sin = -0.54,  cos =  0.84,  sum =  0.31
        13:  sin =  0.42,  cos =  0.91,  sum =  1.33

    So  practice_problem3a(6, 8, 0.81)  returns  [7, 8]  since:
      -- sin(6) + cos(6) is 0.68 -- NOT bigger than 0.81
      -- sin(7) + cos(7) is 1.41 -- YES, bigger than 0.81
      -- sin(8) + cos(8) is 0.84 -- YES, bigger than 0.81

    and  practice_problem3a(-4, 9, 0.25) returns  [0, 1, 2, 6, 7, 8]
    because those are the only integers between -4 and 9, inclusive,
    whose sine plus cosine is greater than 0.25.
    [Look at the above numbers and make sure that you agree!]
    Type hints:
      :type start: int
      :type stop:  int
      :type threshold: float
    """
    ###########################################################################
    # TODO: 4. Implement and test this function.
    #          Some tests are already written for you (above),
    #          but you are required to write ADDITIONAL tests (above).
    ###########################################################################
    # DIFFICULTY AND TIME RATINGS (see top of this file for explanation)
    #    DIFFICULTY:      4
    #    TIME ESTIMATE:   5 minutes.
    ###########################################################################


def run_test_practice_problem3b():
    """ Tests the   practice_problem3b  function. """
    ###########################################################################
    # TODO: 5. Implement this TEST function.
    #   It TESTS the  practice_problem3b  function defined below.
    #   Include at least ** 2 ** ADDITIONAL tests beyond those we wrote.
    #  __
    #   Try to choose tests that might expose errors in your code!
    #  __
    #   As usual, include both EXPECTED and ACTUAL results in your tests
    #   and compute the latter BY HAND (not by running your program).
    ###########################################################################
    # DIFFICULTY AND TIME RATINGS (see top of this file for explanation)
    #    DIFFICULTY:      3
    #    TIME ESTIMATE:   10 minutes.
    ###########################################################################

    # -------------------------------------------------------------------------
    # Many tests, followed by extra ones appended at the end.
    # They use the imported   simple_testing (st)   module.
    # Each test is a SimpleTestCase with 3 arguments:
    #   -- the function to test,
    #   -- a list containing the argument(s) to send to the function,
    #   -- the correct returned value.
    # For example, the first test below will call
    #   practice_problem3b(-2, 2, 1.3)
    # and compare the returned value against [1, 7] (the correct answer).
    # -------------------------------------------------------------------------
    tests = [st.SimpleTestCase(practice_problem3b,
                               [-2, 2, 1.3],
                               [1, 7]),
             st.SimpleTestCase(practice_problem3b,
                               [-5, 3, 0.25],
                               [-5, 0, 1]),
             st.SimpleTestCase(practice_problem3b,
                               [-5, 4, 0.25],
                               [-5, 0, 1, 2]),
             st.SimpleTestCase(practice_problem3b,
                               [-5, 5, 0.25],
                               [-5, 0, 1, 2, 6]),
             st.SimpleTestCase(practice_problem3b,
                               [-5, 6, 0.25],
                               [-5, 0, 1, 2, 6, 7]),
             st.SimpleTestCase(practice_problem3b,
                               [-5, 7, 0.25],
                               [-5, 0, 1, 2, 6, 7, 8]),
             st.SimpleTestCase(practice_problem3b,
                               [-3, 3, -1.0],
                               [-1, 0, 1]),
             st.SimpleTestCase(practice_problem3b,
                               [-3, 4, -1.0],
                               [-1, 0, 1, 2]),
             st.SimpleTestCase(practice_problem3b,
                               [-3, 5, -1.0],
                               [-1, 0, 1, 2, 3]),
             st.SimpleTestCase(practice_problem3b,
                               [-3, 6, -1.0],
                               [-1, 0, 1, 2, 3, 5]),
             st.SimpleTestCase(practice_problem3b,
                               [30, 0, -1000],
                               []),
             st.SimpleTestCase(practice_problem3b,
                               [100, 5, 1.414],
                               [139, 183, 516, 560, 849]),
             st.SimpleTestCase(practice_problem3b,
                               [0, 1, 1.414213562373],
                               [286602]),
             ]
    # More tests, with larger lists as the expected returned values
    big_list = []
    for k in range(888, 988):
        big_list.append(k)
    tests.append(st.SimpleTestCase(practice_problem3b,
                                   [888, 100,
                                    - math.sqrt(2) + 0.00000000001],
                                   big_list))

    another_big_list = big_list.copy()
    another_big_list.remove(915)
    another_big_list.remove(959)
    another_big_list.append(988)
    another_big_list.append(989)
    tests.append(st.SimpleTestCase(practice_problem3b,
                                   [888, 100,
                                    - math.sqrt(2) + 0.001],
                                   another_big_list))

    # -------------------------------------------------------------------------
    # Run the tests in the   tests   list constructed above.
    # -------------------------------------------------------------------------
    st.SimpleTestCase.run_tests('practice_problem3b', tests)

    ###########################################################################
    # TODO: 5 continued:  More tests:
    #      YOU add at least **   2   ** additional tests here.
    #  __
    #   You can use the   SimpleTestCase  class as above, or use
    #   the ordinary   expected/actual   way, your choice.
    #  __
    #   SUGGESTION: Ask an assistant to CHECK your tests to confirm
    #               that they are adequate tests!
    ###########################################################################


def practice_problem3b(start, n, threshold):
    """
    What comes in:
      -- An integer:  start
      -- An non-negative integer:  n
      -- A number:  threshold
    What goes out:  Returns a list of the first n integers,
      starting at start, for which the sum of the integer's
      sine and cosine is bigger than the given threshold.
    Side effects: None.
    Examples:
      For the following examples, the following numbers are helpful.
      They are listed here just to help you avoid needing a calculator..
      Each is rounded to 2 decimal places for the sake of brevity.
        -5:  sin =  0.96,  cos =  0.28,  sum =  1.24
        -4:  sin =  0.76,  cos = -0.65,  sum =  0.10
        -3:  sin = -0.14,  cos = -0.99,  sum = -1.13
        -2:  sin = -0.91,  cos = -0.42,  sum = -1.33
        -1:  sin = -0.84,  cos =  0.54,  sum = -0.30
         0:  sin =  0.00,  cos =  1.00,  sum =  1.00
         1:  sin =  0.84,  cos =  0.54,  sum =  1.38
         2:  sin =  0.91,  cos = -0.42,  sum =  0.49
         3:  sin =  0.14,  cos = -0.99,  sum = -0.85
         4:  sin = -0.76,  cos = -0.65,  sum = -1.41
         5:  sin = -0.96,  cos =  0.28,  sum = -0.68
         6:  sin = -0.28,  cos =  0.96,  sum =  0.68
         7:  sin =  0.66,  cos =  0.75,  sum =  1.41
         8:  sin =  0.99,  cos = -0.15,  sum =  0.84
         9:  sin =  0.41,  cos = -0.91,  sum = -0.50
        10:  sin = -0.54,  cos = -0.84,  sum = -1.38
        11:  sin = -1.00,  cos =  0.00,  sum = -1.00
        12:  sin = -0.54,  cos =  0.84,  sum =  0.31
        13:  sin =  0.42,  cos =  0.91,  sum =  1.33

    So if start is -5 and threshold is 0.25 and:
       -- n is 3, then this function returns [-5, 0, 1]
             because sin(-5) + cos(-5) IS > 0.25 and
                     sin(-4) + cos(-4) is NOT > 0.25 and
                     sin(-3) + cos(-3) is NOT > 0.25 and
                     sin(-2) + cos(-2) is NOT > 0.25 and
                     sin(-1) + cos(-1) is NOT > 0.25 and
                     sin(0) + cos(0) IS > 0.25 and
                     sin(1) + cos(1) IS > 0.25 and
             and that makes the required  3  such numbers.
       -- n is 4, then this function returns [-5, 0, 1, 2]
       -- n is 5, then this function returns [-5, 0, 1, 2, 6]
       -- n is 6, then this function returns [-5, 0, 1, 2, 6, 7]
       -- n is 7, then this function returns [-5, 0, 1, 2, 6, 7, 8]

    while if start is -3 and the threshold is -1.0 and:
       -- n is 3, then this function returns [-1, 0, 1]
       -- n is 4, then this function returns [-1, 0, 1, 2]
       -- n is 5, then this function returns [-1, 0, 1, 2, 3]
       -- n is 6, then this function returns [-1, 0, 1, 2, 3, 5]

    and if n is 0 (regardless of what start is),
       this function returns []

    and if threshold is more than the square root of 2,
       this function returns (regardless of what start and n are):
          [start, start + 1, start + 2, ... start + n - 1].

    Type hints:
      :type start: int
      :type n:     int
      :type threshold: float
    """
    ###########################################################################
    # TODO: 6. Implement and test this function.
    #          Some tests are already written for you (above),
    #          but you are required to write ADDITIONAL tests (above).
    ###########################################################################
    # DIFFICULTY AND TIME RATINGS (see top of this file for explanation)
    #    DIFFICULTY:      5
    #    TIME ESTIMATE:   < 15 minutes.
    ###########################################################################


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# The   try .. except   prevents error messages on the console from being
# intermingled with ordinary output to the console.
# -----------------------------------------------------------------------------
try:
    main()
except Exception:
    testing_helper.print_colored('ERROR - While running this test,',
                                 color='red')
    testing_helper.print_colored('your code raised the following exception:',
                                 color='red')
    print()
    time.sleep(1)
    raise
