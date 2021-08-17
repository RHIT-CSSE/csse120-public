"""
PRACTICE Exam 1, problem 0.

These problems illustrate concepts that previous problems have not emphasized:
  -- determining whether a number is odd or even (Problem 0a)
  -- returning True or False (Problem 0a)
  -- boolean operators (and, or, not) (Problem 0a)
  -- is_prime (Problem 0b)
  -- animation (Problem 0c)

Authors: David Mutchler, Vibha Alangar, Dave Fisher, Matt Boutell, Mark Hays,
         Mohammed Noureddine, Sana Ebrahimi, Sriram Mohan, their colleagues and
         PUT_YOUR_NAME_HERE.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg
import testing_helper
import time


def main():
    """ Calls the   TEST   functions in this module. """
    print("-----------------------------------------------")
    print("Un-comment each of the following TEST functions")
    print("as you implement the functions that they test.")
    print("-----------------------------------------------")

    # run_test_problem0a()
    # run_test_problem0b()
    # run_test_problem0c()


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


def run_test_problem0a():
    """ Tests the   problem0a   function. """
    print()
    print("--------------------------------------------------")
    print("Testing the   problem0a   function:")
    print("--------------------------------------------------")

    format_string = "    problem0a( {} )"
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    expected = False
    print_expected_result_of_test([83135], expected, test_results,
                                  format_string)
    actual = problem0a(83135)  # Run the code to be tested
    print_actual_result_of_test(expected, actual, test_results)
    if actual == "False":
        print("Your function returned the STRING 'False',")
        print("which is WRONG.  It should have returned")
        print("the built-in constant False.")
        print("Ask for help as needed.")

    # Test 2:
    expected = False
    print_expected_result_of_test([306], expected, test_results, format_string)
    actual = problem0a(306)  # Run the code to be tested
    print_actual_result_of_test(expected, actual, test_results)

    # Test 3:
    expected = True
    print_expected_result_of_test([247], expected, test_results, format_string)
    actual = problem0a(247)  # Run the code to be tested
    print_actual_result_of_test(expected, actual, test_results)
    if actual == "True":
        print("Your function returned the STRING 'True',")
        print("which is WRONG.  It should have returned")
        print("the built-in constant True.")
        print("Ask for help as needed.")

    # Test 4:
    expected = False
    print_expected_result_of_test([803], expected, test_results,
                                  format_string)
    actual = problem0a(803)  # Run the code to be tested
    print_actual_result_of_test(expected, actual, test_results)

    # Test 5:
    expected = False
    print_expected_result_of_test([830931], expected, test_results,
                                  format_string)
    actual = problem0a(830931)  # Run the code to be tested
    print_actual_result_of_test(expected, actual, test_results)

    # Test 6:
    expected = True
    print_expected_result_of_test([730931], expected, test_results,
                                  format_string)
    actual = problem0a(730931)  # Run the code to be tested
    print_actual_result_of_test(expected, actual, test_results)

    # Test 7:
    expected = False
    print_expected_result_of_test([200], expected, test_results, format_string)
    actual = problem0a(200)  # Run the code to be tested
    print_actual_result_of_test(expected, actual, test_results)

    # Test 8:
    expected = False
    print_expected_result_of_test([9020], expected, test_results, format_string)
    actual = problem0a(9020)  # Run the code to be tested
    print_actual_result_of_test(expected, actual, test_results)

    # Test 9:
    expected = False
    print_expected_result_of_test([9021], expected, test_results,
                                  format_string)
    actual = problem0a(9021)  # Run the code to be tested
    print_actual_result_of_test(expected, actual, test_results)

    # Test 10:
    expected = True
    print_expected_result_of_test([9022], expected, test_results,
                                  format_string)
    actual = problem0a(9022)  # Run the code to be tested
    print_actual_result_of_test(expected, actual, test_results)

    # Test 11:
    expected = True
    print_expected_result_of_test([441399999], expected, test_results,
                                  format_string)
    actual = problem0a(441399999)  # Run the code to be tested
    print_actual_result_of_test(expected, actual, test_results)

    # Test 12:
    expected = True
    print_expected_result_of_test([1111111111111], expected, test_results,
                                  format_string)
    actual = problem0a(1111111111111)  # Run the code to be tested
    print_actual_result_of_test(expected, actual, test_results)

    # Test 13:
    expected = True
    print_expected_result_of_test([69], expected, test_results,
                                  format_string)
    actual = problem0a(69)  # Run the code to be tested
    print_actual_result_of_test(expected, actual, test_results)

    print_summary_of_test_results(test_results)


# IMPORTANT:  See the IMPORTANT notes and HINTS in the _TODO_ below.
def problem0a(n):
    """
    What comes in:  An integer.
    What goes out:
      -- Returns True if the sum of the digits in the given integer
         is odd AND is greater than 11, else returns False.
    Side effects:   None.
    Examples:
      -- If the given integer is 83135, this function returns False,
           since (8 + 3 + 1 + 3 + 5) is 20, which is NOT odd.
      -- If the given integer is 306, this function returns False,
           since (3 + 0 + 6) is 9, which IS odd but is NOT greater than 11.
      -- If the given integer is 247, this function returns True,
           since (2 + 4 + 7) is 13, which IS odd and IS greater than 11.
      -- If the given integer is 803, this function returns False,
           since (8 + 0 + 3) is 11, which IS odd and but is NOT greater than 11.
    """
    # -------------------------------------------------------------------------
    # TODO: 3. Implement and test this function.
    #          Tests have been written for you (above).
    #  ########################################################################
    #   IMPORTANT:
    #    **  For full credit you must appropriately
    #    **  use (call) the   sum_of_digits   function
    #    **  that is DEFINED ABOVE.
    #   HINT:  To test whether a number  m   is even or odd,
    #        compute m % 2, i.e., the REMAINDER from m // 2.
    #        If that remainder is 0, the number is even.
    #        If that remainder is 1, the number is odd.
    #        Simply try a few examples to convince yourself of this.
    #        ASK FOR HELP if you do not understand this hint.
    #   HINT:  To test whether both condition1 and condition2 are True,
    #          use      condition1 and condition2   [and similarly for 'or']
    # -------------------------------------------------------------------------


def run_test_problem0b():
    """ Tests the   problem0b   function. """
    print()
    print("--------------------------------------------------")
    print("Testing the   problem0b   function:")
    print("--------------------------------------------------")

    format_string = "    problem0b( {} )"
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    expected = 6
    print_expected_result_of_test([13], expected, test_results, format_string)
    actual = problem0b(13)  # Run the code to be tested
    print_actual_result_of_test(expected, actual, test_results)

    # Test 2:
    expected = 1
    print_expected_result_of_test([2], expected, test_results, format_string)
    actual = problem0b(2)  # Run the code to be tested
    print_actual_result_of_test(expected, actual, test_results)

    # Test 3:
    expected = 46
    print_expected_result_of_test([200], expected, test_results, format_string)
    actual = problem0b(200)  # Run the code to be tested
    print_actual_result_of_test(expected, actual, test_results)

    # Test 4:
    expected = 4
    print_expected_result_of_test([8], expected, test_results, format_string)
    actual = problem0b(8)  # Run the code to be tested
    print_actual_result_of_test(expected, actual, test_results)

    # Test 5:
    expected = 4
    print_expected_result_of_test([7], expected, test_results, format_string)
    actual = problem0b(7)  # Run the code to be tested
    print_actual_result_of_test(expected, actual, test_results)

    # Test 6:
    expected = 3
    print_expected_result_of_test([6], expected, test_results, format_string)
    actual = problem0b(6)  # Run the code to be tested
    print_actual_result_of_test(expected, actual, test_results)

    # Test 7:
    expected = 168
    print_expected_result_of_test([997], expected, test_results, format_string)
    actual = problem0b(997)  # Run the code to be tested
    print_actual_result_of_test(expected, actual, test_results)

    # Test 8:
    expected = 168
    print_expected_result_of_test([998], expected, test_results, format_string)
    actual = problem0b(997)  # Run the code to be tested
    print_actual_result_of_test(expected, actual, test_results)

    # Test 9:
    expected = 168
    print_expected_result_of_test([999], expected, test_results, format_string)
    actual = problem0b(997)  # Run the code to be tested
    print_actual_result_of_test(expected, actual, test_results)

    # Test 10:
    expected = 170
    print_expected_result_of_test([1018], expected, test_results, format_string)
    actual = problem0b(1018)  # Run the code to be tested
    print_actual_result_of_test(expected, actual, test_results)

    # Test 11:
    expected = 171
    print_expected_result_of_test([1019], expected, test_results, format_string)
    actual = problem0b(1019)  # Run the code to be tested
    print_actual_result_of_test(expected, actual, test_results)

    # Test 12:
    expected = 171
    print_expected_result_of_test([1020], expected, test_results, format_string)
    actual = problem0b(1020)  # Run the code to be tested
    print_actual_result_of_test(expected, actual, test_results)

    # Test 13:
    expected = 172
    print_expected_result_of_test([1021], expected, test_results, format_string)
    actual = problem0b(1021)  # Run the code to be tested
    print_actual_result_of_test(expected, actual, test_results)

    # Test 14:
    expected = 172
    print_expected_result_of_test([1022], expected, test_results, format_string)
    actual = problem0b(1022)  # Run the code to be tested
    print_actual_result_of_test(expected, actual, test_results)

    # Test 15:
    expected = 172
    print_expected_result_of_test([1023], expected, test_results, format_string)
    actual = problem0b(1023)  # Run the code to be tested
    print_actual_result_of_test(expected, actual, test_results)

    print_summary_of_test_results(test_results)


# IMPORTANT: See the IMPORTANT notes in the _TODO_ below.
def problem0b(n):
    """
    What comes in:  An integer n >= 2.
    What goes out:
      -- Returns the number of integers from 2 to n, inclusive,
         that are prime.
    Side effects:   None.
    Examples:
      -- If n is 13, this function returns 6,
           since there are 6 primes -- namely, 2, 3, 5, 7, 11, and 13 --
           between 2 and 13.
      -- If n is 2, this function returns 1,
           since there is one prime (namely, 2) between 2 and 2.
      -- If n is 200, the correct answer is 46,
           since there are 46 primes between 2 and 200.
     """
    # -------------------------------------------------------------------------
    # TODO: 4. Implement and test this function.
    #          Tests have been written for you (above).
    #  ########################################################################
    #   IMPORTANT:
    #    **  For full credit you must appropriately
    #    **  use (call) the   is_prime   function that is DEFINED ABOVE.
    #  _
    #   IMPORTANT: In this and ALL problems through Exam 1, when using a RANGE
    #     expression, you may use only its SINGLE-ARGUMENT form,
    #     for pedagogical reasons.
    #         range(m)         OK!
    #         range(a, b)      NOT Ok!
    #         range(m, n, -1)  NOT Ok!
    # -------------------------------------------------------------------------


def run_test_problem0c():
    """ Tests the   problem0c  function. """
    print()
    print("--------------------------------------------------")
    print("Testing the  problem0c  function:")
    print("  See the graphics windows that pop up.")
    print("--------------------------------------------------")

    # TWO tests on ONE window.
    title = "Tests 1 & 2 of problem0c: blue circle + 6 circles;"
    title += " then green circle + 3 circles"
    window1 = rg.RoseWindow(650, 300, title)

    circle1 = rg.Circle(rg.Point(100, 50), 30)
    circle1.fill_color = "blue"
    problem0c(circle1, 6, window1)  # Run the code to be tested
    window1.continue_on_mouse_click()

    circle2 = rg.Circle(rg.Point(75, 200), 75)
    circle2.fill_color = "green"
    problem0c(circle2, 3, window1)  # Run the code to be tested
    window1.close_on_mouse_click()

    # A third test on ANOTHER window.
    title = "Test 3 of problem0c:  red circle + 10 circles"
    window2 = rg.RoseWindow(600, 200, title)

    circle3 = rg.Circle(rg.Point(50, 50), 20)
    circle3.fill_color = "red"
    problem0c(circle3, 10, window2)  # Run the code to be tested
    window2.close_on_mouse_click()


# IMPORTANT:  See the HINT in the _TODO_ below.
def problem0c(circle, n, window):
    """
    See   problem0c_picture.pdf   in this project for pictures
    that may help you better understand the following specification:
    
    What comes in:
      -- An rg.Circle.
      -- A positive integer n.
      -- An rg.RoseWindow.
    What goes out:  Nothing (i.e., None).
    Side effects:
      Draws the given rg.Circle and n additional rg.Circles
      on the given rg.RoseWindow such that:
        -- The circles form a row of touching rg.Circles with the
             leftmost circle being the given rg.Circle.
        -- There is a 0.5 second pause after each rg.Circle is drawn.
      Must  ** NOT close **   the window.

    Type hints:
      :type circle: rg.Circle
      :type n: int
      :type window: rg.RoseWindow
    """
    # -------------------------------------------------------------------------
    # TODO: 5. Implement and test this function.
    #          Tests have been written for you (above).
    #  ########################################################################
    #   HINT:   render(0.5)
    #     renders with a half-second pause after rendering.
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
