"""
Exam 1, problem 3.

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Mark Hays, Amanda Stouder, Aaron Wilkin, their colleagues,
         and PUT_YOUR_NAME_HERE.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

import testing_helper
import time


def main():
    """ Calls the   TEST   functions in this module. """
    print("-----------------------------------------------")
    print("Un-comment each of the following TEST functions")
    print("as you implement the functions that they test.")
    print("-----------------------------------------------")

    # run_test_problem3a()
    # run_test_problem3b()


###############################################################################
# TODO: 2.  READ the doc-string for the  sum_of_digits  function defined below.
#   It is the same  sum_of_digits  function that you have seen before.
#   After you UNDERSTAND the doc-string (JUST the doc-string, NOT the code),
#   ASKING QUESTIONS AS NEEDED, change the above _TODO_ to DONE.
###############################################################################

def sum_of_digits(number):
    """
    What comes in:  An integer.
    What goes out:  Returns the sum of the digits in the given integer.
    Side effects:   None.
    Example:
      If the integer is 83135,
      this function returns (8 + 3 + 1 + 3 + 5), which is 20.
    """
    # -------------------------------------------------------------------------
    # Students:
    #   Do NOT touch the above  sum_of_digits function - it has no _TODO_.
    #   Do NOT copy code from this function.
    #
    # Instead, ** CALL ** this function as needed in the problems below.
    # -------------------------------------------------------------------------
    if number < 0:
        number = -number

    digit_sum = 0
    while True:
        if number == 0:
            break
        digit_sum = digit_sum + (number % 10)
        number = number // 10

    return digit_sum


def run_test_problem3a():
    """ Tests the   problem3a   function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   problem3a  function:')
    print('--------------------------------------------------')

    format_string = '    problem3a( {}, {} )'
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    expected = 6 + 10 + 13 + 14  # which is 43
    print_expected_result_of_test([6, 15], expected, test_results,
                                  format_string)
    actual = problem3a(6, 15)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 2:
    expected = 3
    print_expected_result_of_test([2, 5], expected, test_results,
                                  format_string)
    actual = problem3a(2, 5)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 3:
    expected = 6 + 10 + 13 + 14  # which is 43
    print_expected_result_of_test([6, 14], expected, test_results,
                                  format_string)
    actual = problem3a(6, 14)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 4:
    expected = 10 + 13 + 14  # which is 37
    print_expected_result_of_test([7, 14], expected, test_results,
                                  format_string)
    actual = problem3a(7, 14)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 5:
    expected = 10 + 13 + 14  # which is 37
    print_expected_result_of_test([7, 15], expected, test_results,
                                  format_string)
    actual = problem3a(7, 15)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 6:
    expected = 0
    print_expected_result_of_test([7, 9], expected, test_results,
                                  format_string)
    actual = problem3a(7, 9)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 7:
    expected = 0
    print_expected_result_of_test([7, 7], expected, test_results,
                                  format_string)
    actual = problem3a(7, 7)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 8:
    expected = 6
    print_expected_result_of_test([6, 6], expected, test_results,
                                  format_string)
    actual = problem3a(6, 6)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 9:
    expected = 7401
    print_expected_result_of_test([100, 200], expected, test_results,
                                  format_string)
    actual = problem3a(100, 200)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 10:
    expected = 766497
    print_expected_result_of_test([1000, 2000], expected, test_results,
                                  format_string)
    actual = problem3a(1000, 2000)
    print_actual_result_of_test(expected, actual, test_results)

    # SUMMARY of test results:
    print_summary_of_test_results(test_results)


def problem3a(r, s):
    """
    What comes in:  Positive integers r and s, with r <= s.
    What goes out:
      -- Returns the sum of all the integers from r to s, inclusive,
           for which the sum_of_digits in the cube of the integer is odd.
    Side effects:   None.
    Examples:
      -- problem3a(6, 15) returns 6 + 10 + 13 + 14 (which is 43) because:
          --  6 cubed is  216, whose sum of digits is  9, which is ODD.  (YES!)
          --  7 cubed is  343, whose sum of digits is 10, which is NOT odd.
          --  8 cubed is  512, whose sum of digits is  8, which is NOT odd.
          --  9 cubed is  729, whose sum of digits is 18, which is NOT odd.
          -- 10 cubed is 1000, whose sum of digits is  1, which is ODD.  (YES!)
          -- 11 cubed is 1331, whose sum of digits is  8, which is NOT odd.
          -- 12 cubed is 1728, whose sum of digits is 18, which is NOT odd.
          -- 13 cubed is 2197, whose sum of digits is 19, which is ODD.  (YES!)
          -- 14 cubed is 2744, whose sum of digits is 17, which is ODD.  (YES!)
          -- 15 cubed is 3375, whose sum of digits is 18, which is NOT odd.

      -- problem3a(2, 5) returns 3 because:
          -- 2 cubed is     8, whose sum of digits is  8, which is NOT odd.
          -- 3 cubed is    27, whose sum of digits is  9, which is ODD.  (YES!)
          -- 4 cubed is    64, whose sum of digits is 10, which is NOT odd.
          -- 5 cubed is   125, whose sum of digits is  8, which is NOT odd.
    """
    # -------------------------------------------------------------------------
    # TODO: 3. Implement and test this function.
    #          Tests have been written for you (above).
    #  ########################################################################
    #   IMPORTANT:
    #    **  For full credit you must appropriately
    #    **  use (call) the   sum_of_digits   function
    #    **  that is DEFINED ABOVE.
    ###########################################################################


def run_test_problem3b():
    """ Tests the   problem3b   function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   problem3b  function:')
    print('--------------------------------------------------')

    format_string = '    problem3b( {}, {} )'
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    expected = 1 / 4 + 2 / 25 + 3 / 216 + 4 / (7 ** 4) + 5 / (8 ** 5) + 6 / (
            9 ** 6)
    print_expected_result_of_test([6, 4], expected, test_results,
                                  format_string, suffix='  (approximately)')
    actual = problem3b(6, 4)
    print_actual_result_of_test(expected, actual, test_results, precision=8)

    # Test 2:
    expected = 1 / 1 + 2 / 4 + 3 / 27  # which is approximately XXX
    print_expected_result_of_test([3, 1], expected, test_results,
                                  format_string, suffix='  (approximately)')
    actual = problem3b(3, 1)
    print_actual_result_of_test(expected, actual, test_results, precision=8)

    # Test 3:
    expected = 1 / 35 + 2 / (36 ** 2)  # which is approximately XXX
    print_expected_result_of_test([2, 35], expected, test_results,
                                  format_string, suffix='  (approximately)')
    actual = problem3b(2, 35)
    print_actual_result_of_test(expected, actual, test_results, precision=8)

    # Test 4:
    expected = 12.020144157845959
    print_expected_result_of_test([4, 0.1], expected, test_results,
                                  format_string, suffix='  (approximately)')
    actual = problem3b(4, 0.1)
    print_actual_result_of_test(expected, actual, test_results, precision=8)

    # Test 5:
    expected = 1 / 1
    print_expected_result_of_test([1, 1], expected, test_results,
                                  format_string, suffix='  (approximately)')
    actual = problem3b(1, 1)
    print_actual_result_of_test(expected, actual, test_results, precision=8)

    # Test 6:
    expected = 1 / 5 + 2 / (6 ** 2) + 3 / (7 ** 3) + 4 / (8 ** 4) + 5 / (
            9 ** 5) + 6 / (10 ** 6) + 7 / (11 ** 7)
    print_expected_result_of_test([7, 5], expected, test_results,
                                  format_string, suffix='  (approximately)')
    actual = problem3b(7, 5)
    print_actual_result_of_test(expected, actual, test_results, precision=8)

    # Test 7:
    expected = 1 / 2 + 2 / (3 ** 2) + 3 / (4 ** 3)
    print_expected_result_of_test([3, 2], expected, test_results,
                                  format_string, suffix='  (approximately)')
    actual = problem3b(3, 2)
    print_actual_result_of_test(expected, actual, test_results, precision=8)

    # Test 8:
    expected = 1 / 1 + 2 / (2 ** 2) + 3 / (3 ** 3) + 4 / (4 ** 4)
    print_expected_result_of_test([4, 1], expected, test_results,
                                  format_string, suffix='  (approximately)')
    actual = problem3b(4, 1)
    print_actual_result_of_test(expected, actual, test_results, precision=8)

    # Test 9:
    expected = 22.21348247480059
    print_expected_result_of_test([12, 0.05], expected, test_results,
                                  format_string, suffix='  (approximately)')
    actual = problem3b(12, 0.05)
    print_actual_result_of_test(expected, actual, test_results, precision=8)

    # Test 10:
    expected = 0.5961871168220374
    print_expected_result_of_test([3, 2.5], expected, test_results,
                                  format_string, suffix='  (approximately)')
    actual = problem3b(3, 2.5)
    print_actual_result_of_test(expected, actual, test_results, precision=8)

    # SUMMARY of test results:
    print_summary_of_test_results(test_results)


def problem3b(m, r):
    """
    What comes in:  A positive integer m and a number r.
    What goes out:
      -- Returns the sum that is the first  m  terms of the series
           1/r  +  (2 / ((r+1) ** 2))  +  (3 / ((r+2) ** 3) + ...
    Side effects:   None.
    Examples:
      -- problem3b(6, 4) returns
           1/4  +  2/(5**2)  +  3/(6**3)  +  4/(7**4)  +  5/(8**5)  + 6/(9**6),
           which is approximately 0.3457187393495064.
      -- problem3b(3, 1) returns
           1/1  +  2/(2 ** 2)  +  3/(3 ** 3), which is approximately 0.6111111.
      -- problem3b(2, 35) returns
           1/35  +  2/(36**2), which is approximately 0.03011463844797178.
      -- problem3b(4, 0.1) returns
           1/(0.1)  +  2/((1.1)**2)  +  3/((2.1)**3)  +  4/(3.1)**4)),
           which is approximately 12.020144157845959.
     """
    ###########################################################################
    # TODO: 4. Implement and test this function.
    #          Tests have been written for you (above).
    ###########################################################################


###############################################################################
# Our tests use the following to print error messages in red.
# Do NOT change it.  You do NOT have to do anything with it.
###############################################################################

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
