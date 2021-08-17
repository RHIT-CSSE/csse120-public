"""
PRACTICE Exam 1, problem 3.

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

    # run_test_problem3a()
    # run_test_problem3b()


def run_test_problem3a():
    """ Tests the   problem3a   function. """
    print()
    print("--------------------------------------------------")
    print("Testing the   problem3a  function:")
    print("--------------------------------------------------")

    format_string = "    problem3a( {}, {} )"
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    expected = (1 / (4 ** 1)) + (2 / (5 ** 2)) + (3 / (6 ** 3)) + \
               (4 / (7 ** 4)) + (5 / (8 ** 5)) + (6 / (9 ** 6))
    # which is approximately 0.3457187393495064
    print_expected_result_of_test([6, 4], expected, test_results,
                                  format_string, suffix="  (approximately)")
    actual = problem3a(6, 4)  # Run the code to be tested
    print_actual_result_of_test(expected, actual, test_results, precision=14)

    # Test 2:
    expected = (1 / (1 ** 1)) + (2 / (2 ** 2)) + (3 / (3 ** 3))
    # which is approximately 1.6111111111111112
    print_expected_result_of_test([3, 1], expected, test_results,
                                  format_string, suffix="  (approximately)")
    actual = problem3a(3, 1)  # Run the code to be tested
    print_actual_result_of_test(expected, actual, test_results, precision=14)

    # Test 3:
    expected = (1 / (35 ** 1)) + (2 / (36 ** 2))
    # which is approximately 0.03011463844797178
    print_expected_result_of_test([2, 35], expected, test_results,
                                  format_string, suffix="  (approximately)")
    actual = problem3a(2, 35)  # Run the code to be tested
    print_actual_result_of_test(expected, actual, test_results, precision=14)

    # Test 4:
    expected = (1 / (0.1 ** 1)) + (2 / (1.1 ** 2)) + (3 / (2.1 ** 3)) + \
               (4 / (3.1 ** 4))  # which is approximately 12.020144157845959
    print_expected_result_of_test([4, 0.1], expected, test_results,
                                  format_string, suffix="  (approximately)")
    actual = problem3a(4, 0.1)  # Run the code to be tested
    print_actual_result_of_test(expected, actual, test_results, precision=14)

    # Test 5:
    expected = 1 / 1  # which is 1
    print_expected_result_of_test([1, 1], expected, test_results,
                                  format_string, suffix="  (approximately)")
    actual = problem3a(1, 1)  # Run the code to be tested
    print_actual_result_of_test(expected, actual, test_results, precision=14)

    # Test 6:
    expected = (1 / (5 ** 1)) + (2 / (6 ** 2)) + (3 / (7 ** 3)) + \
               (4 / (8 ** 4)) + (5 / (9 ** 5)) + (6 / (10 ** 6)) + \
               (7 / (11 ** 7))
    # which is approximately 0.2653695083904117
    print_expected_result_of_test([7, 5], expected, test_results,
                                  format_string, suffix="  (approximately)")
    actual = problem3a(7, 5)  # Run the code to be tested
    print_actual_result_of_test(expected, actual, test_results, precision=14)

    # Test 7:
    expected = (1 / (2 ** 1)) + (2 / (3 ** 2)) + (3 / (4 ** 3))
    # which is approximately 0.7690972222222222
    print_expected_result_of_test([3, 2], expected, test_results,
                                  format_string, suffix="  (approximately)")
    actual = problem3a(3, 2)  # Run the code to be tested
    print_actual_result_of_test(expected, actual, test_results, precision=14)

    # Test 8:
    expected = (1 / (1 ** 1)) + (2 / (2 ** 2)) + (3 / (3 ** 3)) + (4 / (4 ** 4))
    # which is approximately 1.6267361111111112
    print_expected_result_of_test([4, 1], expected, test_results,
                                  format_string, suffix="  (approximately)")
    actual = problem3a(4, 1)  # Run the code to be tested
    print_actual_result_of_test(expected, actual, test_results, precision=14)

    # Test 9:
    expected = 22.213482474800703
    print_expected_result_of_test([13, 0.05], expected, test_results,
                                  format_string, suffix="  (approximately)")
    actual = problem3a(13, 0.05)  # Run the code to be tested
    print_actual_result_of_test(expected, actual, test_results, precision=14)

    # Test 10:
    expected = 0.5961871168220374
    print_expected_result_of_test([3, 2.5], expected, test_results,
                                  format_string, suffix="  (approximately)")
    actual = problem3a(3, 2.5)  # Run the code to be tested
    print_actual_result_of_test(expected, actual, test_results, precision=14)

    # Test 11:
    expected = 102.38398042755968
    print_expected_result_of_test([10, 0.01], expected, test_results,
                                  format_string, suffix="  (approximately)")
    actual = problem3a(10, 0.01)  # Run the code to be tested
    print_actual_result_of_test(expected, actual, test_results, precision=14)

    # SUMMARY of test results:
    print_summary_of_test_results(test_results)


def problem3a(m, r):
    """
    What comes in:  A positive integer m and a number r.
    What goes out:
      -- Returns the sum that is the first  m  terms of the series
           (1 / (r ** 1))  +  (2 / ((r+1) ** 2))  +  (3 / ((r+2) ** 3) + ...
    Side effects:   None.
    Examples:
      -- problem3a(6, 4) returns
             (1 / (4 ** 1))  +  (2 / (5 ** 2))  +  (3 / (6 ** 3))
          +  (4 / (7 ** 4))  +  (5 / (8 ** 5))  +  (6 / (9 ** 6)),
           which is approximately 0.3457187393495064
      -- problem3a(3, 1) returns
             (1 / (1 ** 1))  +  (2 / (2 ** 2))  +  (3 / (3 ** 3)),
           which is approximately 1.6111111111111112
      -- problem3a(2, 35) returns
             (1 / (35 ** 1))  +  (2 / (36 ** 2)),
           which is approximately 0.03011463844797178
      -- problem3a(4, 0.1) returns
             (1 / (0.1 ** 1))  +  (2 / (1.1 ** 2))  +  (3 / ( 2.1 ** 3))
                               +  (4 / (3.1 ** 4 )),
           which is approximately 12.020144157845959
     """
    ###########################################################################
    # TODO: 2. Implement and test this function.
    #          Tests have been written for you (above).
    #  ------------------------------------------------------------------------
    #  DIFFICULTY AND TIME RATINGS (see top of this file for explanation)
    #    DIFFICULTY:      6
    #    TIME ESTIMATE:   7 to 12 minutes.
    ###########################################################################


def run_test_problem3b():
    """ Tests the   problem3b   function. """
    print()
    print("--------------------------------------------------")
    print("Testing the   problem3b  function:")
    print("--------------------------------------------------")

    format_string = "    problem3b( {}, {}, {} )"
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    expected = (2 / 5) + (3 / 7) + (4 / 9) + (5 / 11) + (6 / 13) + (7 / 15)
    # which is approximately 2.655766455766456
    print_expected_result_of_test([6, 2, 5], expected, test_results,
                                  format_string, suffix="  (approximately)")
    actual = problem3b(6, 2, 5)  # Run the code to be tested
    print_actual_result_of_test(expected, actual, test_results, precision=8)

    # Test 2:
    expected = (10 / 6) + (11 / 8) + (12 / 10)
    # which is approximately 4.241666666666667
    print_expected_result_of_test([3, 10, 6], expected, test_results,
                                  format_string, suffix="  (approximately)")
    actual = problem3b(3, 10, 6)  # Run the code to be tested
    print_actual_result_of_test(expected, actual, test_results, precision=8)

    # Test 3:
    expected = (20 / 4)  # which is 5
    print_expected_result_of_test([1, 20, 4], expected, test_results,
                                  format_string, suffix="  (approximately)")
    actual = problem3b(1, 20, 4)  # Run the code to be tested
    print_actual_result_of_test(expected, actual, test_results, precision=8)

    # Test 4:
    expected = (10 / 10) + (11 / 12) + (12 / 14) + (13 / 16)
    # which is approximately 3.5863095238095237
    print_expected_result_of_test([4, 10, 10], expected, test_results,
                                  format_string, suffix="  (approximately)")
    actual = problem3b(4, 10, 10)  # Run the code to be tested
    print_actual_result_of_test(expected, actual, test_results, precision=8)

    # Test 5:
    expected = 19.37465007372624
    print_expected_result_of_test([30, 10, 11], expected, test_results,
                                  format_string, suffix="  (approximately)")
    actual = problem3b(30, 10, 11)  # Run the code to be tested
    print_actual_result_of_test(expected, actual, test_results, precision=8)

    # Test 6:
    expected = 50.0
    print_expected_result_of_test([100, 4, 8], expected, test_results,
                                  format_string, suffix="  (approximately)")
    actual = problem3b(100, 4, 8)  # Run the code to be tested
    print_actual_result_of_test(expected, actual, test_results, precision=8)

    # Test 7:
    expected = 49.5
    print_expected_result_of_test([99, 4, 8], expected, test_results,
                                  format_string, suffix="  (approximately)")
    actual = problem3b(99, 4, 8)  # Run the code to be tested
    print_actual_result_of_test(expected, actual, test_results, precision=8)

    # Test 8:
    expected = 50.5
    print_expected_result_of_test([101, 4, 8], expected, test_results,
                                  format_string, suffix="  (approximately)")
    actual = problem3b(101, 4, 8)  # Run the code to be tested
    print_actual_result_of_test(expected, actual, test_results, precision=8)

    # Test 9:
    expected = 53.15592858306353
    print_expected_result_of_test([101, 5, 7], expected, test_results,
                                  format_string, suffix="  (approximately)")
    actual = problem3b(101, 5, 7)  # Run the code to be tested
    print_actual_result_of_test(expected, actual, test_results, precision=8)

    # Test 10:
    expected = 51.642171094650834
    print_expected_result_of_test([100, 1, 1], expected, test_results,
                                  format_string, suffix="  (approximately)")
    actual = problem3b(100, 1, 1)  # Run the code to be tested
    print_actual_result_of_test(expected, actual, test_results, precision=8)

    # Test 11:
    expected = 52.14465865683989
    print_expected_result_of_test([101, 1, 1], expected, test_results,
                                  format_string, suffix="  (approximately)")
    actual = problem3b(101, 1, 1)  # Run the code to be tested
    print_actual_result_of_test(expected, actual, test_results, precision=8)

    # Test 12:
    expected = 52.64712171102708
    print_expected_result_of_test([102, 1, 1], expected, test_results,
                                  format_string, suffix="  (approximately)")
    actual = problem3b(102, 1, 1)  # Run the code to be tested
    print_actual_result_of_test(expected, actual, test_results, precision=8)

    # Test 13:
    expected = 487.5687456418132
    print_expected_result_of_test([1000, 6, 23], expected, test_results,
                                  format_string, suffix="  (approximately)")
    actual = problem3b(1000, 6, 23)  # Run the code to be tested
    print_actual_result_of_test(expected, actual, test_results, precision=8)

    # Test 14:
    expected = 1801.8405099999466
    print_expected_result_of_test([999, 600, 25], expected, test_results,
                                  format_string, suffix="  (approximately)")
    actual = problem3b(999, 600, 25)  # Run the code to be tested
    print_actual_result_of_test(expected, actual, test_results, precision=8)

    # Test 15:
    expected = 7736.352797543001
    print_expected_result_of_test([2999, 10000, 2001], expected, test_results,
                                  format_string, suffix="  (approximately)")
    actual = problem3b(2999, 10000, 2001)  # Run the code to be tested
    print_actual_result_of_test(expected, actual, test_results, precision=8)

    # SUMMARY of test results:
    print_summary_of_test_results(test_results)


def problem3b(m, r, s):
    """
    What comes in:  Positive integers m, r and s.
    What goes out:
      -- Returns the sum that is the first  m  terms of the series
           (r / s)  +  ((r + 1) / (s + 2))  +  ((r + 2) / (s + 4))
                    +  ((r + 3) / (s + 6)  +  ((r + 4) / (s + 8)) + ...
    Side effects:   None.
    Examples:
      -- problem3b(6, 2, 5) returns
             (2 / 5) + (3 / 7) + (4 / 9) + (5 / 11) + (6 / 13) + (7 / 15),
           which is approximately 2.655766455766456
      -- problem3b(3, 10, 6) returns
             (10 / 6) + (11 / 8) + (12 / 10),
           which is approximately 4.241666666666667
      -- problem3b(1, 20, 4) returns
             (20 / 4), which is 5.
      -- problem3b(4, 10, 10) returns
             (10 / 10) + (11 / 12) + (12 / 14) + (13 / 16)
           which is approximately 3.5863095238095237
     """
    ###########################################################################
    # TODO: 3. Implement and test this function.
    #          Tests have been written for you (above).
    #  ------------------------------------------------------------------------
    #  DIFFICULTY AND TIME RATINGS (see top of this file for explanation)
    #    DIFFICULTY:      6
    #    TIME ESTIMATE:   7 to 12 minutes.
    ###########################################################################


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
