"""
This module lets you practice various patterns
for ITERATING through SEQUENCES, including:
  -- Beginning to end
  -- Other ranges (e.g., backwards and every-3rd-item)
  -- The COUNT/SUM/etc pattern
  -- The FIND pattern (via LINEAR SEARCH)

Authors: David Mutchler, Sana Ebrahimi, Mohammed Noureddine, Vibha Alangar,
         Matt Boutell, Dave Fisher, Mark Hays, their colleagues, and
         PUT_YOUR_NAME_HERE.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg
import testing_helper
import time
import sys


def main():
    """ Calls the   TEST   functions in this module. """
    run_test_sum_radii()
    run_test_count_last_n_odds()
    run_test_index_of_first_negative()
    run_test_contains_an_a()
    run_test_number_of_stutters()


###############################################################################
# Many problems simply iterate (loop) through ALL of the sequence,
# as in the  sum_radii  problem below.
###############################################################################
def run_test_sum_radii():
    """ Tests the   sum_radii   function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   sum_radii   function:')
    print('--------------------------------------------------')

    format_string = '    sum_radii( {} )'
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    circle1 = rg.Circle(rg.Point(100, 100), 25)
    circle2 = rg.Circle(rg.Point(100, 100), 50)
    circle3 = rg.Circle(rg.Point(100, 100), 10)
    sequence = (circle1, circle2, circle3)
    expected = 85
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = sum_radii(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 2:
    circle1 = rg.Circle(rg.Point(200, 20), 80)
    circle2 = rg.Circle(rg.Point(300, 100), 60)
    circle3 = rg.Circle(rg.Point(100, 150), 0)
    circle4 = rg.Circle(rg.Point(0, 0), 30)
    sequence = (circle1, circle2, circle3, circle4)
    expected = 170
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = sum_radii(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 3:
    circle1 = rg.Circle(rg.Point(100, 120), 20)
    sequence = (circle1,)
    expected = 20
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = sum_radii(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 4:
    sequence = ()
    expected = 0
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = sum_radii(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    print_summary_of_test_results(test_results)


def sum_radii(circles):
    """
    What comes in:
      -- a sequence of rg.Circle objects
    What goes out:
      Returns the sum of the radii of the given sequence of rg.Circles.
    Side effects: None.
    Example:  If
          circle1 = rg.Circle(rg.Point(999, 100), 25)
          circle2 = rg.Circle(rg.Point(888, 200), 50)
          circle3 = rg.Circle(rg.Point(777, 300), 10)
      then   sum_radii([circle1, circle2, circle3])
      returns 25 + 50 + 10, which is 85.
    Type hints:
      :type circles:  list | tuple of rg.Circle
      :rtype: int | float
    """
    # -------------------------------------------------------------------------
    # TODO: 2. Implement and test this function.
    #     The testing code is already written for you (above).
    #  ___
    #  Note: No fair using "slices" on ANY of these problems,
    #        if you happen to know what they are.
    #  ___
    #  Likewise, no fair using any already-defined methods/functions
    #  on sequences or lists or strings, if you happen to know any.
    #  ___
    #  Instead, use explicit loops, as you have for other problems.
    # -------------------------------------------------------------------------


###############################################################################
# Some problems iterate (loop) through PART of the sequence,
# perhaps BACKWARDS, as in the   count_last_n_odds   problem below.
###############################################################################
def run_test_count_last_n_odds():
    """ Tests the   count_last_n_odds   function. """
    print()
    print("--------------------------------------------------")
    print("Testing the   count_last_n_odds   function:")
    print("--------------------------------------------------")

    format_string = '    count_last_n_odds( {}, {} )'
    test_results = [0, 0]  # Number of tests passed, failed.

    # -------------------------------------------------------------------------
    # Tests 1 through 5 all use the same sequence:
    # -------------------------------------------------------------------------
    sequence = (13, 66, 15, 3)

    # Tests 1 through 5: Loop using the following arguments, expected answers.
    values_for_n = (0, 1, 2, 3, 4)
    expected_answers = (0, 1, 2, 2, 3)

    for k in range(len(values_for_n)):
        expected = expected_answers[k]
        value_for_n = values_for_n[k]
        print_expected_result_of_test([sequence, value_for_n], expected,
                                      test_results, format_string)
        actual = count_last_n_odds(sequence, value_for_n)
        print_actual_result_of_test(expected, actual, test_results)

    # -------------------------------------------------------------------------
    # Tests 6 through 15 all use the same sequence:
    # -------------------------------------------------------------------------
    sequence = (1, 5, 88, 44, 33, 77, 10, 12, 9)

    # Tests 6 through 15: Loop using the following arguments, expected answers.
    values_for_n = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
    expected_answers = (0, 1, 1, 1, 2, 3, 3, 3, 4, 5)

    for k in range(len(values_for_n)):
        expected = expected_answers[k]
        value_for_n = values_for_n[k]
        print_expected_result_of_test([sequence, value_for_n], expected,
                                      test_results, format_string)
        actual = count_last_n_odds(sequence, value_for_n)
        print_actual_result_of_test(expected, actual, test_results)

    # -------------------------------------------------------------------------
    # Tests 16 through 21 all use the same sequence:
    # -------------------------------------------------------------------------
    sequence = (17, 88, -5, -10, 0)

    # Tests 16 through 21: Loop using the following arguments, expected answers.
    values_for_n = [0, 1, 2, 3, 4, 5]
    expected_answers = [0, 0, 0, 1, 1, 2]

    for k in range(len(values_for_n)):
        expected = expected_answers[k]
        value_for_n = values_for_n[k]
        print_expected_result_of_test([sequence, value_for_n], expected,
                                      test_results, format_string)
        actual = count_last_n_odds(sequence, value_for_n)
        print_actual_result_of_test(expected, actual, test_results)

    # Test 22:
    sequence = (33,)
    expected = 1
    print_expected_result_of_test([sequence, 1], expected, test_results,
                                  format_string)
    actual = count_last_n_odds(sequence, 1)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 23:
    sequence = (34,)
    expected = 0
    print_expected_result_of_test([sequence, 1], expected, test_results,
                                  format_string)
    actual = count_last_n_odds(sequence, 1)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 24:
    sequence = ()
    expected = 0
    print_expected_result_of_test([sequence, 0], expected, test_results,
                                  format_string)
    actual = count_last_n_odds(sequence, 0)
    print_actual_result_of_test(expected, actual, test_results)

    print_summary_of_test_results(test_results)


def count_last_n_odds(integers, n):
    """
    What comes in:
      -- a sequence of integers
      -- a non-negative integer  n  that is less than or equal to
           the length of the given sequence
    What goes out:  Returns the number of odd integers
      in the last n items of the given sequence.
    Side effects: None.
    Examples:
      If the sequence is (13, 66, 15, 3), then:
       count_last_n_odds(sequence, 0) is 0  [no odds]
       count_last_n_odds(sequence, 1) is 1  [1 odd, namely 3]
       count_last_n_odds(sequence, 2) is 2  [2 odds, namely 3 and 15]
       count_last_n_odds(sequence, 3) is 2  [2 odds, namely 3 and 15]
       count_last_n_odds(sequence, 4) is 3  [3 odds: 3, 15 and 13]
    Type hints:
      :type integers: list | tuple of int
      :type n: int
      :rtype: int
    """
    # -------------------------------------------------------------------------
    # TODO: 3. Implement and test this function.
    #     The testing code is already written for you (above).
    #     If you have questions about the testing code, ask for help.
    # -------------------------------------------------------------------------


###############################################################################
# Some problems iterate (loop) through PART of the sequence,
# stopping when the loop FINDS something of interest
# (or continuing to the end if it does NOT find the thing of interest),
# as in the  index_of_first_negative   and   contains_an_a   problems below.
###############################################################################
def run_test_index_of_first_negative():
    """ Tests the   index_of_first_negative   function. """
    print()
    print("--------------------------------------------------")
    print("Testing the   index_of_first_negative   function:")
    print("--------------------------------------------------")

    format_string = '    index_of_first_negative( {} )'
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    sequence = [90, 0, 20, -5, 30, -10, 15]
    expected = 3
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = index_of_first_negative(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 2:
    sequence = (-5, 30, -10, 15)
    expected = 0
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = index_of_first_negative(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 3:
    sequence = (5, 30, 10, 15, -1)
    expected = 4
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = index_of_first_negative(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 4:
    sequence = (5, 30, 10, 15, 1, 6, 8, 10, 12, 0, 0, 30, 5)
    expected = -1
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = index_of_first_negative(sequence)
    print_actual_result_of_test(expected, actual, test_results)
    if actual == "-1":
        print("  Your answer is WRONG.")
        print("  You returned the STRING \"-1\"")
        print("  when you should have returned just -1")

    # Test 5:
    sequence = ()
    expected = -1
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = index_of_first_negative(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 6:
    sequence = (-1900,)
    expected = 0
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = index_of_first_negative(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 7:
    sequence = (1900,)
    expected = -1
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = index_of_first_negative(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    print_summary_of_test_results(test_results)


def index_of_first_negative(numbers):
    """
    What comes in:
      -- a sequence of numbers
    What goes out: Returns the INDEX of the first negative number
      in the given sequence of numbers, or -1 if the sequence
      contains no negative numbers.
      Note: "first" negative number means the negative number
      whose index is smallest -- see the examples.
    Side effects: None.
    Examples: If the argument is:
      -- [4, 30, -19, 8, -3, -50, 100], this function returns 2
            since the first negative number is -19, which is at index 2

      -- [-8, 44, 33], this function returns 0
            since the first negative number is -8, which is at index 0

      -- [1, 29, 22, 8], this function returns -1
            since the list contains no negative numbers
    Type hints:
      :type numbers: list | tuple of float | int
      :rtype: int
    """
    # -------------------------------------------------------------------------
    # TODO: 4. Implement and test this function.
    #     The testing code is already written for you (above).
    #     If you have questions about the testing code, ask for help.
    # -------------------------------------------------------------------------


def run_test_contains_an_a():
    """ Tests the   contains_an_a   function. """
    print()
    print("--------------------------------------------------")
    print("Testing the   contains_an_a   function:")
    print("--------------------------------------------------")

    format_string = '    contains_an_a( {} )'
    test_results = [0, 0]  # Number of tests passed, failed.

    # Tests:
    strings_for_tests = (
        "nope",
        "yes a is here",
        "many aaaaas aaa aaa",
        "not until the very end is a",
        "a @ the beginning",
        "",
        "BLAH BLAH BLAH",
        "BLAH BLAH BLAH \t MORE BLAH",
        "BLAH BLAH BLAH \t MORE BLaH",
    )
    expected_answers = (
        False, True, True, True, True, False, False, False, True)

    for k in range(len(strings_for_tests)):
        string = strings_for_tests[k]
        expected = expected_answers[k]
        print_expected_result_of_test([string], expected, test_results,
                                      format_string)
        actual = contains_an_a(string)
        print_actual_result_of_test(expected, actual, test_results)
        if type(actual) is str and actual == str(expected):
            print("Your code FAILED this test for   contains_an_a.")
            print("  You appear to have returned the STRING:")
            print("      \"" + actual + "\"")
            print("  instead of the built-in constant:")
            print("       " + str(expected))

    print_summary_of_test_results(test_results)


def contains_an_a(s):
    """
    What comes in:
      -- a string
    What goes out: Returns  True  if the given string contains
      the character "a".  Returns  False  if the given string
      does not contain the character "a".
    Side effects: None.
    Examples:
      -- contains_an_a("blah blah blah")  returns True
      -- contains_an_a("BLAH BLAH BLAH")  returns False
      -- contains_an_a("abc")             returns True
      -- contains_an_a("")                returns False
    Type hints:
      :type s: str
      :rtype: bool
    """
    # -------------------------------------------------------------------------
    # TODO: 5. Implement and test this function.
    #     The testing code is already written for you (above).
    #     If you have questions about the testing code, ask for help.
    #  ___
    #  Implementation requirement:
    #   Use an explicit loop, as you have done in the other problems.
    #   No fair using the   count   or   find   string methods.
    #  ___
    #  IMPORTANT:
    #   -- True  and  False  are built-in constants.
    #      Do NOT return the STRING "True" or the STRING "False".
    # -------------------------------------------------------------------------


###############################################################################
# Some problems iterate (loop) through the sequence accessing TWO
# (or more) places in the sequence AT THE SAME ITERATION,
# as in the  number_of_stutters  problem below.
###############################################################################
def run_test_number_of_stutters():
    """ Tests the   number_of_stutters   function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   number_of_stutters   function:')
    print('--------------------------------------------------')

    format_string = '    number_of_stutters( {} )'
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    string = "xhhbrrs"
    expected = 2
    print_expected_result_of_test([string], expected, test_results,
                                  format_string)
    actual = number_of_stutters(string)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 2:
    string = "xxxx"
    expected = 3
    print_expected_result_of_test([string], expected, test_results,
                                  format_string)
    actual = number_of_stutters(string)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 3:
    string = "xaxaxa"
    expected = 0
    print_expected_result_of_test([string], expected, test_results,
                                  format_string)
    actual = number_of_stutters(string)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 4:
    string = "xxx yyy xxxx"
    expected = 7
    print_expected_result_of_test([string], expected, test_results,
                                  format_string)
    actual = number_of_stutters(string)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 5:
    string = "xxxyyyxxxx"
    expected = 7
    print_expected_result_of_test([string], expected, test_results,
                                  format_string)
    actual = number_of_stutters(string)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 6:
    string = "4404040412345"
    expected = 1
    print_expected_result_of_test([string], expected, test_results,
                                  format_string)
    actual = number_of_stutters(string)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 7:
    string = "4040404123455"
    expected = 1
    print_expected_result_of_test([string], expected, test_results,
                                  format_string)
    actual = number_of_stutters(string)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 8:
    string = "4040400412345"
    expected = 1
    print_expected_result_of_test([string], expected, test_results,
                                  format_string)
    actual = number_of_stutters(string)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 9:
    string = "404040412345"
    expected = 0
    print_expected_result_of_test([string], expected, test_results,
                                  format_string)
    actual = number_of_stutters(string)
    print_actual_result_of_test(expected, actual, test_results)

    print_summary_of_test_results(test_results)


def number_of_stutters(s):
    """
    What comes in:
      -- a string s
    What goes out: Returns the number of times a letter is repeated
      twice-in-a-row in the given string s.
    Side effects: None.
    Examples:
      -- number_of_stutters('xhhbrrs')  returns 2
      -- number_of_stutters('xxxx')     returns 3
      -- number_of_stutters('xaxaxa')   returns 0
      -- number_of_stutters('xxx yyy xxxx')  returns 7
      -- number_of_stutters('xxxyyyxxxx')    returns 7
      -- number_of_stutters('')  returns 0
    Type hints:
       :type s: str
    """
    # -------------------------------------------------------------------------
    # TODO: 6. Implement and test this function.
    #     The testing code is already written for you (above).
    # -------------------------------------------------------------------------


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
    sys.stdout.flush()
    time.sleep(1)
    raise
