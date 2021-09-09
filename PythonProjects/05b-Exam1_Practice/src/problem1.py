"""
PRACTICE Exam 1, problem 1.

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
import testing_helper
import time


def main():
    """ Calls the   TEST   functions in this module. """
    print("-----------------------------------------------")
    print("Un-comment each of the following TEST functions")
    print("as you implement the functions that they test.")
    print("-----------------------------------------------")

    # run_test_problem1a()
    # run_test_problem1b()
    # run_test_problem1c()


###############################################################################
# TODO: 2.  READ the green doc-string for the:
#     - is_prime
#     - sum_of_digits
#   functions defined below.  You do NOT need to understand their
#   implementations, just their specification (per the doc-string).
#   You should  ** CALL **  those functions as needed in implementing the
#   other functions.  After you have READ this, change its _TODO_ to DONE.
###############################################################################

def is_prime(n):
    """
    What comes in:  An integer n >= 2.
    What goes out:
      -- Returns True if the given integer is prime,
         else returns False.
    Side effects:   None.
    Examples:
      -- is_prime(11) returns  True
      -- is_prime(12) returns  False
      -- is_prime(2)  returns  True
    Note: The algorithm used here is simple and clear but slow.
    """
    for k in range(2, (n // 2) + 1):
        if n % k == 0:
            return False

    return True
    # -------------------------------------------------------------------------
    # Students:
    #   Do NOT touch the above  is_prime  function - it has no _TODO_.
    #   Do NOT copy code from this function.
    #
    # Instead, ** CALL ** this function as needed in the problems below.
    # -------------------------------------------------------------------------


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


def run_test_problem1a():
    """ Tests the   problem1a   function. """
    # -------------------------------------------------------------------------
    # TODO: 3. Implement this TEST function.
    #   It TESTS the  problem1a  function defined below.
    #   Include at least **   6   ** tests (we wrote five for you).
    #  ------------------------------------------------------------------------
    #  DIFFICULTY AND TIME RATINGS (see top of this file for explanation)
    #    DIFFICULTY:      3
    #    TIME ESTIMATE:   5 minutes.
    # -------------------------------------------------------------------------
    print()
    print("--------------------------------------------------")
    print("Testing the   problem1a   function:")
    print("--------------------------------------------------")

    format_string = "    problem1a( {}, {} )"
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    expected = -1.601215  # This is APPROXIMATELY the correct answer.
    print_expected_result_of_test([3, 5], expected, test_results,
                                  format_string)
    actual = problem1a(3, 5)  # Run the code to be tested
    print_actual_result_of_test(expected, actual, test_results, precision=6)

    # Test 2:
    expected = 0.06332106  # This is APPROXIMATELY the correct answer.
    print_expected_result_of_test([2, -3], expected, test_results,
                                  format_string)
    actual = problem1a(2, -3)  # Run the code to be tested
    print_actual_result_of_test(expected, actual, test_results, precision=8)

    # Test 3:
    expected = 1.32357900  # This is APPROXIMATELY the correct answer.
    print_expected_result_of_test([30, 101], expected, test_results,
                                  format_string)
    actual = problem1a(30, 101)  # Run the code to be tested
    print_actual_result_of_test(expected, actual, test_results, precision=8)

    # Test 4:
    expected = 0.7311900132  # This is APPROXIMATELY the correct answer.
    print_expected_result_of_test([9999, 9999], expected, test_results,
                                  format_string)
    actual = problem1a(9999, 9999)  # Run the code to be tested
    print_actual_result_of_test(expected, actual, test_results, precision=9)

    # Test 5:
    expected = 1.27818068564  # This is APPROXIMATELY the correct answer.
    print_expected_result_of_test([30, 100], expected, test_results,
                                  format_string)
    actual = problem1a(30, 100)  # Run the code to be tested
    print_actual_result_of_test(expected, actual, test_results, precision=11)

    print_summary_of_test_results(test_results)

    # -------------------------------------------------------------------------
    # TODO: 3 (continued).
    #  Below this comment, add 1 more test case of your own choosing.
    #  You do NOT need to use the above form.  Instead, use the usual:
    #     # Test NNN:
    #     expected = XXX
    #     actual = problem1a(YYY, ZZZ)
    #     print()
    #     print("Expected:", expected)
    #     print("Actual:  ", actual)
    # -------------------------------------------------------------------------


def problem1a(m, n):
    """
    What comes in:  Integers m and n with abs(m) <= abs(n).
    What goes out:
      -- Returns the sum of the sines of the integers
         from m squared to n squared, inclusive,
         where m and n are the given arguments.
    Side effects:   None.
    Examples:
      -- If m is 3 and n is 5, this function returns:
            sine(9) + sine(10) + sine(11) +  ...  + sine(24) + sine(25),
         which is about -1.601215.
      -- If m is 2 and n is -3, this function returns:
            sine(4) + sine(5) + sine(6) + sine(7) + sine(8) + sine(9),
         which is about 0.06332106.
      -- If m is 30 and n is 101, the correct answer is about 1.32357900.
    """
    # -------------------------------------------------------------------------
    # TODO: 4. Implement and test this function.
    #   Note that you should write its TEST function first (above).
    #  ------------------------------------------------------------------------
    #  DIFFICULTY AND TIME RATINGS (see top of this file for explanation)
    #    DIFFICULTY:      4
    #    TIME ESTIMATE:   5 to 8 minutes.
    # -------------------------------------------------------------------------


def run_test_problem1b():
    """ Tests the   problem1b   function. """
    # -------------------------------------------------------------------------
    # TODO: 5. Implement this TEST function.
    #   It TESTS the  problem1b  function defined below.
    #   Include at least **   9   ** tests (we wrote seven for you).
    #  ------------------------------------------------------------------------
    #  DIFFICULTY AND TIME RATINGS (see top of this file for explanation)
    #    DIFFICULTY:      3
    #    TIME ESTIMATE:   5 minutes.
    # -------------------------------------------------------------------------
    print()
    print("--------------------------------------------------")
    print("Testing the   problem1b   function:")
    print("--------------------------------------------------")

    format_string = "    problem1b( {}, {} )"
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    expected = 5
    print_expected_result_of_test([3, 5], expected, test_results,
                                  format_string)
    actual = problem1b(3, 5)  # Run the code to be tested
    print_actual_result_of_test(expected, actual, test_results)

    # Test 2:
    expected = 1
    print_expected_result_of_test([2, 1], expected, test_results,
                                  format_string)
    actual = problem1b(2, 1)  # Run the code to be tested
    print_actual_result_of_test(expected, actual, test_results)

    print_summary_of_test_results(test_results)

    # Test 3:
    expected = 44
    print_expected_result_of_test([5, 40], expected, test_results,
                                  format_string)
    actual = problem1b(5, 40)  # Run the code to be tested
    print_actual_result_of_test(expected, actual, test_results)

    # Test 4:
    expected = 44
    print_expected_result_of_test([5, 42], expected, test_results,
                                  format_string)
    actual = problem1b(5, 42)  # Run the code to be tested
    print_actual_result_of_test(expected, actual, test_results)

    # Test 5:
    expected = 45
    print_expected_result_of_test([5, 43], expected, test_results,
                                  format_string)
    actual = problem1b(5, 43)  # Run the code to be tested
    print_actual_result_of_test(expected, actual, test_results)

    # Test 6:
    expected = 45
    print_expected_result_of_test([5, 44], expected, test_results,
                                  format_string)
    actual = problem1b(5, 44)  # Run the code to be tested
    print_actual_result_of_test(expected, actual, test_results)

    # Test 7:
    expected = 46
    print_expected_result_of_test([5, 45], expected, test_results,
                                  format_string)
    actual = problem1b(5, 45)  # Run the code to be tested
    print_actual_result_of_test(expected, actual, test_results)

    print_summary_of_test_results(test_results)

    # -------------------------------------------------------------------------
    # TODO: 5 (continued).
    #  Below this comment, add 2 more test cases of your own choosing.
    #  You do NOT need to use the above form.  Instead, use the usual:
    #     # Test NNN:
    #     expected = XXX
    #     actual = problem1b(YYY, ZZZ)
    #     print()
    #     print("Expected:", expected)
    #     print("Actual:  ", actual)
    # -------------------------------------------------------------------------


# IMPORTANT: See the IMPORTANT note in the _TODO_ below.
def problem1b(m, f):
    """
    What comes in:  Positive integers m and f such that m >= 2.
    What goes out:
      -- Returns the number of integers from m to (f * m),
         inclusive, that are prime.
    Side effects:   None.
    Examples:
      -- If m is 3 and f is 5, this function returns 5,
           since 3, 5, 7, 11, and 13 are the integers between 3 and 15,
           inclusive, that are prime.
      -- If m is 2 and f is 1, this function returns 1,
           since there is one prime (namely, 2) between 2 and 2.
      -- If m is 5 and f is 40, the correct answer is 44,
           since there are 44 primes between 5 and 200.
     """
    # -------------------------------------------------------------------------
    # TODO: 6. Implement and test this function.
    #   Note that you should write its TEST function first (above).
    #  ########################################################################
    #  IMPORTANT:
    #    **  For full credit you must appropriately
    #    **  use (call) the   is_prime   function that is DEFINED ABOVE.
    #  ------------------------------------------------------------------------
    #  DIFFICULTY AND TIME RATINGS (see top of this file for explanation)
    #    DIFFICULTY:      5
    #    TIME ESTIMATE:   5 to 10 minutes.
    # -------------------------------------------------------------------------


def run_test_problem1c():
    """ Tests the   problem1c   function. """
    print()
    print("--------------------------------------------------")
    print("Testing the   problem1c   function:")
    print("--------------------------------------------------")

    format_string = "    problem1c( {} )"
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    expected = 3
    print_expected_result_of_test([10], expected, test_results, format_string)
    actual = problem1c(10)  # Run the code to be tested
    print_actual_result_of_test(expected, actual, test_results)

    # Test 2:
    expected = 6
    print_expected_result_of_test([11], expected, test_results, format_string)
    actual = problem1c(11)  # Run the code to be tested
    print_actual_result_of_test(expected, actual, test_results)

    # Test 3:
    expected = 33
    print_expected_result_of_test([25], expected, test_results, format_string)
    actual = problem1c(25)  # Run the code to be tested
    print_actual_result_of_test(expected, actual, test_results)

    # Test 4:
    expected = 2
    print_expected_result_of_test([2], expected, test_results, format_string)
    actual = problem1c(2)  # Run the code to be tested
    print_actual_result_of_test(expected, actual, test_results)

    # Test 5:
    expected = 6
    print_expected_result_of_test([3], expected, test_results, format_string)
    actual = problem1c(3)  # Run the code to be tested
    print_actual_result_of_test(expected, actual, test_results)

    # Test 6:
    expected = 19416
    print_expected_result_of_test([10007], expected, test_results,
                                  format_string)
    actual = problem1c(10007)  # Run the code to be tested
    print_actual_result_of_test(expected, actual, test_results)

    # Test 7:
    expected = 19416
    print_expected_result_of_test([10008], expected, test_results,
                                  format_string)
    actual = problem1c(10008)  # Run the code to be tested
    print_actual_result_of_test(expected, actual, test_results)

    # Test 8:
    expected = 19200
    print_expected_result_of_test([10009], expected, test_results,
                                  format_string)
    actual = problem1c(10009)  # Run the code to be tested
    print_actual_result_of_test(expected, actual, test_results)

    print_summary_of_test_results(test_results)


# IMPORTANT: See the IMPORTANT note in the _TODO_ below.
def problem1c(n):
    """
    What comes in:  An integer n >= 2.
    What goes out:
      -- Returns the sum of the digits in the product
         of all the primes from 2 to n, inclusive.
    Side effects:   None.
    Example:
      -- If n is 10, this function returns 3,
           because the primes less than or equal to 10
           are 2, 3, 5 and 7, and the product of those numbers
           is (2 * 3 * 5 * 7), which is 210,
           and the sum of the digits in 210 is 3.
      -- If n is 11, this function returns 6,
           because the primes less than or equal to 11
           are 2, 3, 5, 7 and 11, and the product of those numbers
           is (2 * 3 * 5 * 7 * 11), which is 2310,
           and the sum of the digits in 2310 is 6.
      -- If n is 25, this function returns 33,
           because the primes less than or equal to 25
           are 2, 3, 5, 7, 11, 13, 17, 19, and 23,
           and the product of those numbers is 223092870,
           and the sum of the digits in 223092870 is 33.
    """
    # -------------------------------------------------------------------------
    # TODO: 7. Implement and test this function.
    #          Tests have been written for you (above).
    #  ########################################################################
    #  IMPORTANT:
    #    **  For full credit you must appropriately
    #    **  use (call) the   is_prime   and   sum_of_digits
    #    **  functions that are DEFINED ABOVE.
    #  ------------------------------------------------------------------------
    #  DIFFICULTY AND TIME RATINGS (see top of this file for explanation)
    #    DIFFICULTY:      7
    #    TIME ESTIMATE:   7 to 15 minutes.
    # -------------------------------------------------------------------------


###############################################################################
# Our tests use the following to print error messages in red.
# Do NOT change it.  You do NOT have to do anything with it.
###############################################################################

def print_expected_result_of_test(arguments, expected,
                                  test_results, format_string, suffix=""):
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
    print("ERROR - While running this test,", color="red")
    print("your code raised the following exception:", color="red")
    print()
    time.sleep(1)
    raise
