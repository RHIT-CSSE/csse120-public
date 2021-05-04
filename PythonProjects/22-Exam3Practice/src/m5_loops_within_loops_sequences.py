"""
PRACTICE Exam 3.

This problem provides practice at:
  ***  LOOPS WITHIN LOOPS in SEQUENCE of SEQUENCES problems.  ***

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


def main():
    """ Calls the   TEST   functions in this module. """
    print()
    print("Un-comment and re-comment calls in MAIN one by one as you work.")

    run_test_sum_bigger_than_average()

    # biggest diff from s[x] to s[x+1]:  one dim
    #   then two dim
    # find prime, looking only at last m outer, n inner.
    # two 2-d lists.  List that is same as 2nd,
    #   but contains only items
    #   that are bigger than sum of all items in 1st one.
    # list that is odd-indexed outer, even-indexed inner


def plus_minus_minus(sequence):
    """
    What comes in:  A sequence of numbers whose length is at least 2.
    What goes out:
     Returns the first number in the sequence,
       minus the second number in the sequence,
       minus the third number in the sequence,
       plus  the fourth number in the sequence,
       minus the fifth number in the sequence,
       minus the sixth number in the sequence,
       plus  the seventh number in the sequence,
       minus the eighth number in the sequence,
       minus the ninth number in the sequence,
       etc.
    Side effects:  None.
    Examples:
      biggest_diff_1( [5, 1, 2, 10, 3, 4, 5, 6, 1, 6, 3] )
        returns  5 - 1 - 2 + 10 - 3 - 4 + 5 - 6 - 1 + 6 - 3, which is 6.

      biggest_diff_1( [14, 11, 10] )  returns 14 - 11 - 10, which is -7.

      biggest_diff_1( [14, 11] )  returns 14 - 11, which is 3.

      ** ASK YOUR INSTRUCTOR FOR HELP **
      ** if these examples and the above specification are not clear to you. **
    Type hints:
      :type sequence: list[int] | tuple[int]
    """
    ###########################################################################
    # TODO: 2. Implement and test this function.
    #          Tests have been written for you (above).
    ###########################################################################
    ###########################################################################
    # -------------------------------------------------------------------------
    # DIFFICULTY AND TIME RATINGS (see top of this file for explanation)
    #    DIFFICULTY:      5
    #    TIME ESTIMATE:  10 minutes.
    # -------------------------------------------------------------------------
    total = 0
    for k in range(len(sequence)):
        if k % 3 == 0:
            total = total + sequence[k]
        else:
            total = total - sequence[k]
    return total


def run_test_sum_bigger_than_average():
    """ Tests the   sum_bigger_than_average   function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   sum_bigger_than_average  function:')
    print('--------------------------------------------------')

    format_string = '    sum_bigger_than_average( {} )'
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    numbers = ([5, 1, 8, 3],
               [0, -3, 7, 8, 1],
               [6, 3, 5, 5, -10, 12])
    expected = 5 + 8 + 7 + 8 + 6 + 5 + 5 + 12  # which is 56 (A = 17/4 = 4.25)
    print_expected_result_of_test([numbers], expected, test_results,
                                  format_string)
    actual = sum_bigger_than_average(numbers)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 2:
    numbers = ([5, 1, 1, 1, 1, 3],
               [1, 4, 4, 1, 1, 1, 1],
               [6, 3, 2, 3, 4, 5, 6, 7, 8, 9],
               [1, 2, 3, 2, 1])
    # so A = 12/6 = 2 and
    expected = 5 + 3 + 4 + 4 + 6 + 3 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 3  # = 70
    print_expected_result_of_test([numbers], expected, test_results,
                                  format_string)
    actual = sum_bigger_than_average(numbers)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 3:
    numbers = ([5, 1, 1, 1, 1],
               [1, 6, 5, 1, 1, 1, 1],
               [6, 3, 2, 3, 4, 5, 6, 7, 8, 9],
               [1, 2, 3, 4, 5],
               [5, 6, 7, 8, 9, 10, 11, 12])
    expected = 151
    print_expected_result_of_test([numbers], expected, test_results,
                                  format_string)
    actual = sum_bigger_than_average(numbers)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 4:
    numbers = ([1, 2, 1, 1, 1],
               [1, 6, 5, 1, 1, 1, 1],
               [6, 3, 2, 3, 4, 5, 6, 7, 8, 9],
               [1, 2, 3, 4, 5],
               [5, 6, 7, 8, 9, 10, 11, 12])
    expected = 148
    print_expected_result_of_test([numbers], expected, test_results,
                                  format_string)
    actual = sum_bigger_than_average(numbers)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 5:
    numbers = ([100, 200, 1, 1, 1],
               [1, 6, 5, 1, 1, 1, 1],
               [6, 3, 2, 3, 4, 5, 6, 7, 8, 9],
               [1, 2, 3, 4, 5],
               [5],
               [5, 6, 7, 8, 9, 10, 11, 12])
    expected = 300
    print_expected_result_of_test([numbers], expected, test_results,
                                  format_string)
    actual = sum_bigger_than_average(numbers)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 6:
    numbers = ([100, 200, 99],
               [300])
    expected = 500
    print_expected_result_of_test([numbers], expected, test_results,
                                  format_string)
    actual = sum_bigger_than_average(numbers)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 7:
    numbers = ([98, 200, 99],
               [300])
    expected = 500
    print_expected_result_of_test([numbers], expected, test_results,
                                  format_string)
    actual = sum_bigger_than_average(numbers)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 8:
    numbers = ([100, 200, 99],
               [50])
    expected = 200
    print_expected_result_of_test([numbers], expected, test_results,
                                  format_string)
    actual = sum_bigger_than_average(numbers)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 9:
    numbers = ([-4],
               [],
               [],
               [-3, 0, 1, 2, 3],
               [-3.99],
               [-4.0000000001])
    expected = -0.99  # from -3 + 0 + 1 + 2 + 3 + (-3.99)
    print_expected_result_of_test([numbers], expected, test_results,
                                  format_string, suffix="(approximately)")
    actual = sum_bigger_than_average(numbers)
    print_actual_result_of_test(expected, actual, test_results, precision=6)

    # Test 10:
    numbers = ([-99999999999],
               [],
               [])
    expected = 0
    print_expected_result_of_test([numbers], expected, test_results,
                                  format_string)
    actual = sum_bigger_than_average(numbers)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 11:
    numbers = ([1, 4],
               [3, 3, 3, 3],
               [],
               [2.49, 2.48, 2.49],
               [])
    expected = 4 + 3 + 3 + 3 + 3  # = 16
    print_expected_result_of_test([numbers], expected, test_results,
                                  format_string)
    actual = sum_bigger_than_average(numbers)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 12:
    numbers = ([1, -1],)
    expected = 1
    print_expected_result_of_test([numbers], expected, test_results,
                                  format_string)
    actual = sum_bigger_than_average(numbers)
    print_actual_result_of_test(expected, actual, test_results)

    # SUMMARY of test results:
    print_summary_of_test_results(test_results)


def sum_bigger_than_average(numbers):
    """
    What comes in:  A non-empty sequence of sequences of numbers,
      with the first sub-sequence being non-empty.
    What goes out:  Returns the sum of all the numbers in the subsequences
      that are bigger than A,
      where A is the average of the numbers in the FIRST sub-sequence.
    Side effects:  None.
    Examples:
      Suppose that  numbers  is:
          ([5, 1, 8, 3],
           [0, -3, 7, 8, 1],
           [6, 3, 5, 5, -10, 12])
      Then: the average of the numbers in the first sub-sequence is
        (5 + 1 + 8 + 3) / 4, which is 17 / 4, which is 4.25, and so
        sum_bigger_than_average(numbers)   returns   (5 + 8 + 7 + 8 + 6 + 5 + 5 + 12),
        which is 56, since the numbers in that sum are the numbers
        in the subsequences that are bigger than 4.25.
      ** ASK YOUR INSTRUCTOR FOR HELP **
      ** if this example and the above specification are not clear to you. **
     """
    ###########################################################################
    # TODO: 6. Implement and test this function.
    #          Tests have been written for you (above).
    ###########################################################################
    ###########################################################################
    # -------------------------------------------------------------------------
    # DIFFICULTY AND TIME RATINGS (see top of this file for explanation)
    #    DIFFICULTY:      7
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
                                                 test_results,
                                                 format_string,
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
