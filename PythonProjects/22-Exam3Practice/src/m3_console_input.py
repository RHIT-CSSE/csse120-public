"""
PRACTICE Exam 3.

This problem provides practice at: *** INPUT from the CONSOLE. ***

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

import time
import testing_helper
import math


def main():
    """ TESTs the functions in this module (by calling them). """
    run_test_input_it_all()


def run_test_input_it_all():
    """ Tests the   input_it_all    function. """
    # -------------------------------------------------------------------------
    # TODO: 3. READ the tests below.  They require that you input specific
    #   inputs (although your function should work for any valid inputs).
    #  After you read (and understand) the above, change this _TODO_ to DONE.
    # -------------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   input_it_all   function:')
    print('--------------------------------------------------')

    format_string = '    input_it_all()'
    test_results = [0, 0]  # Number of tests passed, failed.

    # -------------------------------------------------------------------------
    # Test 1:  for this test, you must ENTER INPUTS exactly as described in
    #          the FIRST example in the specification of input_it_all.
    # -------------------------------------------------------------------------
    expected = "2 1.888 3.888 -0.68 RobotsRobots"
    print_expected_result_of_test([], expected, test_results, format_string)
    actual = input_it_all()
    print_actual_result_of_test(expected, actual, test_results)

    # -------------------------------------------------------------------------
    # Test 2:  for this test, you must ENTER INPUTS exactly as described
    #          in the SECOND example in the specification of input_it_all.
    # -------------------------------------------------------------------------
    expected = \
        "4 3.48 7.48 0.93 Peace & LovePeace & LovePeace & LovePeace & Love"
    print_expected_result_of_test([], expected, test_results, format_string)
    actual = input_it_all()
    print_actual_result_of_test(expected, actual, test_results)

    # SUMMARY of test results:
    print_summary_of_test_results(test_results)


def input_it_all():
    """
    What comes in: Nothing.
    What goes out: Returns a string as described in Side effects (below).
    Side effects:
      Prompts the user for and inputs:
        -- A positive floating point number
        -- A positive integer
        -- A string
      in that order (via three separate INPUT statements).
      Then returns the string that contains:
         -- The second input, followed by a space, followed by:
         -- The first input, followed by a space, followed by:
                [Note the REVERSAL of the print:  2nd input THEN 1st input]
         -- The sum of the first and second inputs,
              followed by a space, followed by:
         -- The sine of (the sum of the first and second inputs),
              rounded to 2 decimal places, followed by a space, followed by:
         -- The third input, repeated the second input number of times.
      No input validation is required.

    Examples:
    Here is a sample run, where the user input is to the right of the colons:
         Enter a floating point number: 1.888
         Enter a positive integer: 2
         Enter a string: Robots

      This example returns the string
           "2 1.888 3.888 -0.68 RobotsRobots"

    Here is another sample run, with different inputs:
         Enter a floating point number: 3.48
         Enter a positive integer: 4
         Enter a string: Peace & Love.

      This example returns the string
           "4 3.48 7.48 0.93 Peace & LovePeace & LovePeace & LovePeace & Love"
    """
    # -------------------------------------------------------------------------
    # TODO: 4. Implement and test this function.
    #          The testing code is already written for you (above).
    #  __
    #  HINT: When you add an  import math   statement,
    #    ALWAYS put it at the BEGINNING of the module,
    #    NOT ** INSIDE ** the definition of the function.
    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------
    # DIFFICULTY AND TIME RATINGS (see top of this file for explanation)
    #    DIFFICULTY:      3
    #    TIME ESTIMATE:  15 minutes.
    # -------------------------------------------------------------------------


###############################################################################
# Our tests use the following to print error messages in red.
# Do NOT change it.  You do NOT have to do anything with it.
###############################################################################

def print_function_call_of_test(arguments, test_results, format_string):
    testing_helper.print_function_call_of_test(arguments, test_results,
                                               format_string)


def print_expected_result_of_test(arguments, expected,
                                  test_results, format_string, suffix=''):
    testing_helper.print_expected_result_of_test(arguments, expected,
                                                 test_results, format_string,
                                                 suffix)


def print_actual_result_of_test(expected, actual, test_results,
                                precision=None):
    testing_helper.print_actual_result_of_test(expected, actual,
                                               test_results, precision)


def print_summary_of_test_results(test_results):
    testing_helper.print_summary_of_test_results(test_results)


# To allow color-coding the output to the console:
USE_COLORING = True  # Change to False to revert to OLD style coloring

testing_helper.USE_COLORING = USE_COLORING
if USE_COLORING:
    # noinspection PyShadowingBuiltins
    print = testing_helper.print_colored
else:
    # noinspection PyShadowingBuiltins
    print = testing_helper.print_uncolored

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# The   try .. except   prevents error messages on the console from being
# intermingled with ordinary output to the console.
# -----------------------------------------------------------------------------
try:
    main()
except Exception:
    print('ERROR - While running this test,', color='red')
    print('your code raised the following exception:', color='red')
    print()
    time.sleep(1)
    raise
