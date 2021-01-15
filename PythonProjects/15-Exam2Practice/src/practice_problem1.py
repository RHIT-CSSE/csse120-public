"""
PRACTICE Exam 2, practice_problem 1.

Authors: David Mutchler, Sana Ebrahimi, Sriram Mohan, Mohammed Noureddine,
         Vibha Alangar, Matt Boutell, Dave Fisher, their colleagues, and
         PUT_YOUR_NAME_HERE.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

###############################################################################
# Students:
#
# These problems have DIFFICULTY and TIME ratings:
#  DIFFICULTY rating:  1 to 10, where:
#     1 is very easy
#     3 is an "easy" Exam 2 question.
#     5 is a "typical" Exam 2 question.
#     7 is a "hard" Exam 2 question.
#    10 is an EXTREMELY hard problem (too hard for an Exam 2 question)
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
import rosegraphics as rg


def main():
    """ Calls the   TEST   functions in this module. """
    print("-----------------------------------------------")
    print("Un-comment each of the following TEST functions")
    print("as you implement the functions that they test.")
    print("-----------------------------------------------")

    # run_test_practice_problem1a()
    # run_test_practice_problem1b()
    # run_test_practice_problem1c()
    # run_test_practice_problem1d()
    # run_test_practice_problem1e()
    # run_test_practice_problem1f()
    # run_test_practice_problem1g()
    # run_test_practice_problem1h()
    # run_test_practice_problem1i()
    # run_test_practice_problem1j()


###############################################################################
# Students: Some of the testing code below uses a simple testing framework.
# Ask for help if the tests that we supply are not clear to you.
###############################################################################

def run_test_practice_problem1a():
    """ Tests the   practice_problem1a  function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   practice_problem1a   function:')
    print('--------------------------------------------------')

    format_string = '    problem1a( {}, {} )'
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    expected = [8, 16, 11, -14, 14]
    print_expected_result_of_test([[2, 10, 5, -20, 8], 6], expected,
                                  test_results, format_string)
    actual = practice_problem1a([2, 10, 5, -20, 8], 6)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 2:
    expected = [800]
    print_expected_result_of_test([[795], 5], expected, test_results,
                                  format_string)
    actual = practice_problem1a([795], 5)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 3:
    expected = []
    print_expected_result_of_test([[], 50], expected, test_results,
                                  format_string)
    actual = practice_problem1a([], 50)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 4:
    expected = [1, 1, 2, 3, 10, -11, 12, 0, 0, 1]
    print_expected_result_of_test([[1, 1, 2, 3, 10, -11, 12, 0, 0, 1], 0],
                                  expected, test_results, format_string)
    actual = practice_problem1a([1, 1, 2, 3, 10, -11, 12, 0, 0, 1], 0)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 5:
    expected = [-99, -99, -110, -100, -100, 0]
    print_expected_result_of_test([[1, 1, -10, 0, 0, 100], -100],
                                  expected, test_results, format_string)
    actual = practice_problem1a([1, 1, -10, 0, 0, 100], -100)
    print_actual_result_of_test(expected, actual, test_results)

    print_summary_of_test_results(test_results)


def practice_problem1a(sequence, delta):
    """
    What comes in:
      -- A sequence of integers, e.g. ([2, 10, 5, -20, 8])
      -- A number  delta
    What goes out:
      -- Returns a new list that is the same as the given list,
           but with each number in the list having had the given
             delta
           added to it (see example below)
    Side effects: None.
    Example:
       Given the list  [2, 10, 5, -20, 8]  and the number  6,
         this problem returns  [8, 16, 11, -14, 14]
    Type hints:
      :type sequence: [int]
      :type delta:    int
    """
    # -------------------------------------------------------------------------
    # TODO: 2. Implement and test this function.
    #     The testing code is already written for you (above).
    #  ------------------------------------------------------------------------
    #  DIFFICULTY AND TIME RATINGS (see top of this file for explanation)
    #    DIFFICULTY:      3
    #    TIME ESTIMATE:   5 minutes.
    # -------------------------------------------------------------------------


def run_test_practice_problem1b():
    """ Tests the    practice_problem1b    function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   practice_problem1b  function:')
    print('--------------------------------------------------')

    format_string = '    practice_problem1b( {} )'
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    expected = 1
    sequence = (9, 0, 8, 0, 0, 4, 4, 0)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice_problem1b(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 2:
    expected = 4
    sequence = (9, 9, 9, 9, 0, 9, 9, 9)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice_problem1b(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 3:
    expected = -1
    sequence = (4, 5, 4, 5, 4, 5, 4)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice_problem1b(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 4:
    expected = 0
    sequence = [0, 0, 0]
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice_problem1b(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 5:
    expected = 0
    sequence = [0, 0]
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice_problem1b(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 6:
    expected = 0
    sequence = [0, 77]
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice_problem1b(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 7:
    expected = 1
    sequence = [-40, 0]
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice_problem1b(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 8:
    expected = -1
    sequence = [-40, 67]
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice_problem1b(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 9:
    expected = 1
    sequence = (1, 0, 2, 0, 0, 0, 0, 6, 9, 0, 0, 12)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice_problem1b(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # SUMMARY of test results:
    print_summary_of_test_results(test_results)


def practice_problem1b(sequence):
    """
    What comes in: A sequence of integers.
    What goes out: Returns the first (i.e., lowest-index) place (i.e., index)
      for which the item at that place equals 0.
      Returns -1 if the sequence contains no items equal to 0.
    Side effects: None.
    Examples:
      Given sequence (9, 0, 8, 0, 0, 4, 4, 0)
         -- this function returns 1
              since 0 first appears at index 1

      Given sequence [9, 9, 9, 9, 0, 9, 9, 9]
         -- this function returns 4
              since 0 first appears at index 4

      Given sequence (4, 5, 4, 5, 4, 5, 4)
         -- this function returns -1
              since none of the items are 0.

      Given sequence [0, 0, 0]
         -- this function returns 0
              since 0 first appears at index 0

    Type hints:
      :type: sequence: list    or tuple or string
    """
    # -------------------------------------------------------------------------
    # TODO: 3. Implement and test this function.
    #     The testing code is already written for you (above).
    #  ------------------------------------------------------------------------
    #  DIFFICULTY AND TIME RATINGS (see top of this file for explanation)
    #    DIFFICULTY:      3
    #    TIME ESTIMATE:   5 minutes
    # -------------------------------------------------------------------------


def run_test_practice_problem1c():
    """ Tests the    practice_problem1c    function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   practice_problem1c  function:')
    print('--------------------------------------------------')

    format_string = '    practice_problem1c( {} )'
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    expected = 99
    sequence = (20, 12, 133, 18, 9, 13, 3, 99, 20, 19, 200)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice_problem1c(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 2:
    expected = 125
    sequence = (20, 125, 133, 18, 9, 13, 3, 99, 20, 19, 200, 124, 124, 124)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice_problem1c(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 3:
    expected = 100
    sequence = (125, 100)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice_problem1c(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 4:
    expected = 13
    sequence = (9, 9, 12, 13, 10, 8, 8, 9, 8, 11)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice_problem1c(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 5:
    expected = -9999999999
    sequence = (8888888888, -9999999999)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice_problem1c(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 6:
    expected = 8888888888
    sequence = (-9999999999, 8888888888)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice_problem1c(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 7:
    expected = -11
    sequence = (-3, -77, 20000, -33, 40000, -55, 60000, -11)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice_problem1c(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 8:
    expected = -99999999999999
    sequence = (0, -99999999999999)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice_problem1c(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # SUMMARY of test results:
    print_summary_of_test_results(test_results)


def practice_problem1c(sequence):
    """
    What comes in:
      A sequence of numbers, where the length of the sequence >= 2.
    What goes out:
      Returns the largest of the numbers at ODD INDICES of the sequence.
    Side effects: None.
    Examples:
      If the sequence is:
          (20, 12, 133, 18, 9, 13, 3, 99, 20, 19, 200)
      then the largest of the numbers at ODD indices is the largest of
           12      18     13     99      19        which is 99.
      So the function returns 99 in this example.

    Type hints:
      :type sequence: (list | tuple) of (float | int)
    """
    # -------------------------------------------------------------------------
    # TODO: 4. Implement and test this function.
    #     The testing code is already written for you (above).
    #  ------------------------------------------------------------------------
    #  DIFFICULTY AND TIME RATINGS (see top of this file for explanation)
    #    DIFFICULTY:      5
    #    TIME ESTIMATE:   10 minutes.
    # -------------------------------------------------------------------------


def run_test_practice_problem1d():
    """ Tests the    practice_problem1d    function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   practice_problem1d  function:')
    print('--------------------------------------------------')

    format_string = '    practice_problem1d( {}, {} )'
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    expected = [40, 10, 22, 30, 91, 20, 80, 12, 11, 10, 40, 22, 25, 27]
    sequence1 = [40, 22, 91, 80, 11, 40, 25]
    sequence2 = [10, 30, 20, 12, 10, 22, 27]
    print_expected_result_of_test([sequence1, sequence2], expected,
                                  test_results, format_string)
    actual = practice_problem1d(sequence1, sequence2)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 2:
    expected = ["h", "t", "e", "h", "l", "e", "l", "r", "o", "e"]
    sequence1 = "hello"
    sequence2 = "there"
    print_expected_result_of_test([sequence1, sequence2], expected,
                                  test_results, format_string)
    actual = practice_problem1d(sequence1, sequence2)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 3:
    expected = [40, 10, 22, 30, 91, 20, 80, 12, 11, 10, 40, 22, 25, 27]
    sequence1 = (40, 22, 91, 80, 11, 40, 25)
    sequence2 = [10, 30, 20, 12, 10, 22, 27]
    print_expected_result_of_test([sequence1, sequence2], expected,
                                  test_results, format_string)
    actual = practice_problem1d(sequence1, sequence2)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 4:
    expected = [40, 10, 22, 30, 91, 20, 80, 12, 11, 10, 40, 22, 25, 27]
    sequence1 = [40, 22, 91, 80, 11, 40, 25]
    sequence2 = (10, 30, 20, 12, 10, 22, 27)
    print_expected_result_of_test([sequence1, sequence2], expected,
                                  test_results, format_string)
    actual = practice_problem1d(sequence1, sequence2)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 5:
    expected = [333, 100]
    sequence1 = [333]
    sequence2 = [100]
    print_expected_result_of_test([sequence1, sequence2], expected,
                                  test_results, format_string)
    actual = practice_problem1d(sequence1, sequence2)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 6:
    expected = []
    sequence1 = []
    sequence2 = []
    print_expected_result_of_test([sequence1, sequence2], expected,
                                  test_results, format_string)
    actual = practice_problem1d(sequence1, sequence2)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 7:
    expected = list(range(1, 101))
    sequence1 = list(range(1, 100, 2))
    sequence2 = list(range(2, 101, 2))
    print_expected_result_of_test([sequence1, sequence2], expected,
                                  test_results, format_string)
    actual = practice_problem1d(sequence1, sequence2)
    print_actual_result_of_test(expected, actual, test_results)

    # SUMMARY of test results:
    print_summary_of_test_results(test_results)


def practice_problem1d(sequence1, sequence2):
    """
    What comes in:
      Two sequences, where both have the same length.
    What goes out:
      Returns a list containing the items in the sequences
      in a pattern like this:
        If  sequence1 is [r0, r1, r2, r3, r4, ...]
        and sequence2 is [s0, s1, s2, s3, s4, ...]
        then this problem returns:
          [r0, s0, r1, s1, r2, s2, r3, s3, r4, s4, ...]
    Side effects: None.
    Examples:
      If the sequences are:
         [40, 22, 91, 80, 11, 40, 25]
         [10, 30, 20, 12, 10, 22, 27]
      then this function returns the list:
         [40, 10, 22, 30, 91, 20, 80, 12, 11, 10, 40, 22, 25, 27]

      If the sequences are:
         "hello"
         "there"
      then this function returns the list:
         ["h", "t", "e", "h", "l", "e", "l", "r", "o", "e"]
    Type hints:
      :type sequence1: (list | tuple | str)
      :type sequence2: (list | tuple | str)
    """
    # -------------------------------------------------------------------------
    # TODO: 5. Implement and test this function.
    #     The testing code is already written for you (above).
    #  ------------------------------------------------------------------------
    #  DIFFICULTY AND TIME RATINGS (see top of this file for explanation)
    #    DIFFICULTY:      5
    #    TIME ESTIMATE:   10 minutes.
    # -------------------------------------------------------------------------


def run_test_practice_problem1e():
    """ Tests the    practice_problem1e    function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   practice_problem1e  function:')
    print('--------------------------------------------------')

    format_string = '    practice_problem1e( {} )'
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    expected = 161
    sequence = (12, 33, 18, 9, 13, 3, 99, 20, 19, 20)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice_problem1e(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 2:
    expected = 29
    sequence = (3, 12, 10, 8, 8, 9, 8, 11)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice_problem1e(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 3:
    expected = -9999999999
    sequence = (-9999999999, 8888888888)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice_problem1e(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 4:
    expected = 8888888888
    sequence = (8888888888, -9999999999)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice_problem1e(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 5:
    expected = -176
    sequence = (-77, 20000, -33, 40000, -55, 60000, -11)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice_problem1e(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 6:
    expected = 0
    sequence = ()
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice_problem1e(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 7:
    expected = 0
    sequence = []
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice_problem1e(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 8:
    expected = 8
    sequence = [8]
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice_problem1e(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 9:
    expected = -77
    sequence = (-77, 8)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice_problem1e(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 10:
    expected = 0
    sequence = (-77, 8, 77)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice_problem1e(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 11:
    expected = 1
    sequence = (-77, 8, 78)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice_problem1e(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 12:
    expected = 1
    sequence = (-77, 8, 78, 100)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice_problem1e(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # SUMMARY of test results:
    print_summary_of_test_results(test_results)


def practice_problem1e(sequence):
    """
    What comes in:
      A sequence of numbers.
    What goes out:
      Returns the sum of the numbers at EVEN INDICES of the sequence.
    Side effects: None.
    Examples:
      If the sequence is:
          (12, 33, 18, 9, 13, 3, 99, 20, 19, 20)
      then this function returns
           12 + 18 + 13 + 99 + 19, which is 161.
    Type hints:
      :type sequence: list(float)    or tuple(float)
    """
    # -------------------------------------------------------------------------
    # TODO: 6. Implement and test this function.
    #     The testing code is already written for you (above).
    #  ------------------------------------------------------------------------
    #  DIFFICULTY AND TIME RATINGS (see top of this file for explanation)
    #    DIFFICULTY:      5
    #    TIME ESTIMATE:   8 minutes.
    # -------------------------------------------------------------------------


def run_test_practice_problem1f():
    """ Tests the    practice_problem1f    function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   practice_problem1f  function:')
    print('--------------------------------------------------')

    format_string = '    practice_problem1f( {} )'
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    expected = [1, 3, 4, 7]
    sequence = (9, 0, 8, 0, 0, 4, 4, 0)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice_problem1f(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 2:
    expected = [4]
    sequence = (9, 9, 9, 9, 0, 9, 9, 9)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice_problem1f(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 3:
    expected = []
    sequence = (4, 5, 4, 5, 4, 5, 4)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice_problem1f(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 4:
    expected = [0, 1, 2]
    sequence = [0, 0, 0]
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice_problem1f(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 5:
    expected = [0, 1]
    sequence = [0, 0]
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice_problem1f(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 6:
    expected = [0]
    sequence = [0, 77]
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice_problem1f(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 7:
    expected = [1]
    sequence = [-40, 0]
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice_problem1f(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 8:
    expected = []
    sequence = [-40, 67]
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice_problem1f(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 9:
    expected = [1, 3, 4, 5, 6, 9, 10]
    sequence = (1, 0, 2, 0, 0, 0, 0, 6, 9, 0, 0, 12)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice_problem1f(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # SUMMARY of test results:
    print_summary_of_test_results(test_results)


def practice_problem1f(sequence):
    """
    What comes in: A non-empty sequence of integers.
    What goes out: Returns a list of integers,
      where the integers are the places (indices)
      for which the item at that place equals 0.
    Side effects: None.
    Examples:
      Given sequence (9, 0, 8, 0, 0, 4, 4, 0)
         -- this function returns [1, 3, 4, 7]
              since 0 appears at indices 1, 3, 4, and 7.

      Given sequence [9, 9, 9, 9, 0, 9, 9, 9]
         -- this function returns [4]
              since 0 appears only at index 4.

      Given sequence (4, 5, 4, 5, 4, 5, 4)
         -- this function returns []
              since none of the items are 0.

      Given sequence [0, 0, 0]
         -- this function returns [0, 1, 2]
              since 0 appears at indices 0, 1 and 2.

    Type hints:
      :type: sequence: list    or tuple or string
    """
    # -------------------------------------------------------------------------
    # TODO: 7. Implement and test this function.
    #     The testing code is already written for you (above).
    #  ------------------------------------------------------------------------
    #  DIFFICULTY AND TIME RATINGS (see top of this file for explanation)
    #    DIFFICULTY:      5
    #    TIME ESTIMATE:   8 minutes.
    # 
    # -------------------------------------------------------------------------


def run_test_practice_problem1g():
    """ Tests the    practice_problem1g    function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   practice_problem1g  function:')
    print('--------------------------------------------------')

    format_string = '    practice_problem1g( {} )'
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    expected = True
    sequence = [12, 33, 18, 'hello', 9, 13, 3, 9]
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice_problem1g(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 2:
    expected = False
    sequence = [12, 12, 33, 'hello', 5, 33, 5, 9]
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice_problem1g(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 3:
    expected = True
    sequence = (77, 112, 33, 'hello', 0, 43, 5, 77)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice_problem1g(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 4:
    expected = False
    sequence = [1, 1, 1, 1, 1, 1, 2]
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice_problem1g(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 5:
    expected = False
    sequence = ['aa', 'a']
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice_problem1g(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 6:
    expected = True
    sequence = 'aaa'
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice_problem1g(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 7:
    expected = True
    sequence = ['aa', 'a', 'b', 'a', 'b', 'a']
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice_problem1g(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 8:
    expected = False
    sequence = [9]
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice_problem1g(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 9:
    expected = True
    sequence = [12, 33, 18, 'hello', 9, 13, 3, 9]
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice_problem1g(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 10:
    expected = False
    sequence = ['hello there', 'he', 'lo', 'hello']
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice_problem1g(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 11:
    expected = False
    sequence = ((8,), '8', (4 + 4, 4 + 4), [8, 8], 7, 8)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice_problem1g(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 12:
    expected = True
    sequence = [(8,), '8', [4 + 4, 4 + 4], (8, 8), 7, [8, 8]]
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice_problem1g(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 13:
    expected = False
    sequence = [(8,), '8', [4 + 4, 4 + 4], [8, 8], 7, (8, 8)]
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice_problem1g(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # SUMMARY of test results:
    print_summary_of_test_results(test_results)


def practice_problem1g(sequence):
    """
    What comes in: A non-empty sequence.
    What goes out: Returns True if the last item of the sequence
      appears again somewhere else in the sequence.  Returns False
      if the last item of the sequence does NOT appear somewhere
      else in the sequence.
    Side effects: None.
    Examples:
      If the sequence is [12, 33, 18, 'hello', 9, 13, 3, 9],
      this function returns True because the last item (9)
      DOES appear elsewhere in the sequence (namely, at index 4).

      If the sequence is [12, 12, 33, 'hello', 5, 33, 5, 9],
      this function returns False because the last item (9)
      does NOT appear elsewhere in the sequence.

      If the sequence is (77, 112, 33, 'hello', 0, 43, 5, 77),
      this function returns True because the last item (77)
      DOES appear elsewhere in the sequence (namely, at index 0).

      If the sequence is [9], this function returns False
      because the last item (9) does NOT appear elsewhere
      in the sequence.

      If the sequence is [12, 33, 8, 'hello', 99, 'hello'],
      this function returns True since the last item ('hello')
      DOES appear elsewhere in the sequence
      (namely, at indices 3 and 5).

      If the sequence is ['hello there', 'he', 'lo', 'hello'],
      this function returns False because the last item ('hello')
      does NOT appear elsewhere in the sequence.

      If the sequence is 'hello there',
      this function returns True since the last item ('e') DOES
      appear elsewhere in the sequence (namely, at indices 1 and 8).

    Type hints:
      :type: sequence: list    or tuple or string
    """
    # -------------------------------------------------------------------------
    # TODO: 8. Implement and test this function.
    #     The testing code is already written for you (above).
    #  ___
    #  IMPLEMENTATION REQUIREMENT:  You are NOT allowed to use the
    #    'count' or 'index' methods for sequences in this problem
    #    (because here we want you to demonstrate your ability
    #    to use explicit looping).
    #  ------------------------------------------------------------------------
    #  DIFFICULTY AND TIME RATINGS (see top of this file for explanation)
    #    DIFFICULTY:      5
    #    TIME ESTIMATE:   8 minutes.
    # -------------------------------------------------------------------------


def run_test_practice_problem1h():
    """ Tests the    practice_problem1h    function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   practice_problem1h  function:')
    print('--------------------------------------------------')

    format_string = '    practice_problem1h( {} )'
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    c = rg.Circle(rg.Point(7, 30), 10)
    expected = rg.Circle(rg.Point(7, 30), 10)
    circles = (rg.Circle(rg.Point(5, 10), 20),
               rg.Circle(rg.Point(2, 20), 20),
               c,
               rg.Circle(rg.Point(10, 40), 20),
               rg.Circle(rg.Point(2, 50), 10))
    print_expected_result_of_test([circles], expected, test_results,
                                  format_string)
    actual = practice_problem1h(circles)
    print_actual_result_of_test(expected, actual, test_results)

    if actual == c and actual is not c:
        message = ("Technically, *** FAILED the above test. ***\n"
                   + "because you appear to have returned a CLONE\n"
                   + "of the correct rg.Circle instead of\n"
                   + "the rg.Circle itself.")
        testing_helper.print_colored(message, color='red')

    # Test 2:
    c = rg.Circle(rg.Point(58, 10), 20)
    expected = rg.Circle(rg.Point(58, 10), 20)
    circles = (c,)
    print_expected_result_of_test([circles], expected, test_results,
                                  format_string)
    actual = practice_problem1h(circles)
    print_actual_result_of_test(expected, actual, test_results)

    if actual == c and actual is not c:
        message = ("Technically, *** FAILED the above test. ***\n"
                   + "because you appear to have returned a CLONE\n"
                   + "of the correct rg.Circle instead of\n"
                   + "the rg.Circle itself.")
        testing_helper.print_colored(message, color='red')

    # Test 3:
    c = rg.Circle(rg.Point(10005, 300), 100)
    expected = rg.Circle(rg.Point(10005, 300), 100)
    circles = (rg.Circle(rg.Point(84, 100), 300),
               rg.Circle(rg.Point(28, 200), 200),
               c)
    print_expected_result_of_test([circles], expected, test_results,
                                  format_string)
    actual = practice_problem1h(circles)
    print_actual_result_of_test(expected, actual, test_results)

    if actual == c and actual is not c:
        message = ("Technically, *** FAILED the above test. ***\n"
                   + "because you appear to have returned a CLONE\n"
                   + "of the correct rg.Circle instead of\n"
                   + "the rg.Circle itself.")
        testing_helper.print_colored(message, color='red')

    # Test 4:
    c = rg.Circle(rg.Point(5, 10), 13)
    expected = rg.Circle(rg.Point(5, 10), 13)
    circles = (c,
               rg.Circle(rg.Point(0, 20), 20),
               rg.Circle(rg.Point(7, 30), 19),
               rg.Circle(rg.Point(10, 40), 14),
               rg.Circle(rg.Point(2, 50), 14))

    print_expected_result_of_test([circles], expected, test_results,
                                  format_string)
    actual = practice_problem1h(circles)
    print_actual_result_of_test(expected, actual, test_results)

    if actual == c and actual is not c:
        message = ("Technically, *** FAILED the above test. ***\n"
                   + "because you appear to have returned a CLONE\n"
                   + "of the correct rg.Circle instead of\n"
                   + "the rg.Circle itself.")
        testing_helper.print_colored(message, color='red')

    # Test 5:  Perhaps not a valid test since it assumes an rg.Circle
    #          can have a NEGATIVE radius, but it will catch some dubious code.
    small = -9999999999999999999999999999
    c = rg.Circle(rg.Point(7, 30), small)
    expected = rg.Circle(rg.Point(7, 30), small)
    circles = (rg.Circle(rg.Point(0, 20), small + 0.0000001),
               c,
               rg.Circle(rg.Point(10, 40), small),
               rg.Circle(rg.Point(2, 50), small + 1))

    print_expected_result_of_test([circles], expected, test_results,
                                  format_string)
    actual = practice_problem1h(circles)
    print_actual_result_of_test(expected, actual, test_results)

    if actual == c and actual is not c:
        message = ("Technically, *** FAILED the above test. ***\n"
                   + "because you appear to have returned a CLONE\n"
                   + "of the correct rg.Circle instead of\n"
                   + "the rg.Circle itself.")
        testing_helper.print_colored(message, color='red')

    # SUMMARY of test results:
    print_summary_of_test_results(test_results)


def practice_problem1h(circles):
    """
    What comes in:  A non-empty sequence of rg.Circles.
    What goes out:  Returns the rg.Circle in the list whose radius is smallest.
      Breaks ties in favor of the leftmost (smallest index) of those tied.
    Side effects: None.
    Examples:
      If the sequence is a list containing these 5 rg.Circles:
        rg.Circle(rg.Point(5, 10), 20)
        rg.Circle(rg.Point(2, 20), 10)
        rg.Circle(rg.Point(7, 30), 30)
        rg.Circle(rg.Point(10, 40), 20)
        rg.Circle(rg.Point(2, 50), 10)
      then this function returns the rg.Circle at index 1 of the sequence.
    Type hints:
      :type circles: [rg.Circle]
    """
    # -------------------------------------------------------------------------
    # TODO: 9. Implement and test this function.
    #     The testing code is already written for you (above).
    #  ------------------------------------------------------------------------
    #  DIFFICULTY AND TIME RATINGS (see top of this file for explanation)
    #    DIFFICULTY:      7
    #    TIME ESTIMATE:   10 minutes.
    # -------------------------------------------------------------------------


def run_test_practice_problem1i():
    """ Tests the    practice_problem1i    function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   practice_problem1i  function:')
    print('--------------------------------------------------')

    format_string = '    practice_problem1i( {} )'
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    expected = [2, 5]
    sequence = (9, 33, 8, 8, 0, 4, 4, 8)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice_problem1i(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 2:
    expected = [0, 1, 2, 5, 6]
    sequence = (9, 9, 9, 9, 0, 9, 9, 9)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice_problem1i(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 3:
    expected = []
    sequence = (4, 5, 4, 5, 4, 5, 4)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice_problem1i(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 4:
    expected = [1, 4, 5]
    sequence = 'abbabbb'
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice_problem1i(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 5:
    expected = []
    sequence = [509]
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice_problem1i(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # SUMMARY of test results:
    print_summary_of_test_results(test_results)


def practice_problem1i(sequence):
    """
    What comes in: A non-empty sequence.
    What goes out: Returns a list of integers,
      where the integers are the places (indices)
      where an item in the given sequence appears twice in a row.
    Side effects: None.
    Examples:
      Given sequence (9, 33, 8, 8, 0, 4, 4, 8)
         -- this function returns [2, 5]
              since 8 appears twice in a row starting at index 2
              and 4 appears twice in a row starting at index 5

      Given sequence (9, 9, 9, 9, 0, 9, 9, 9)
         -- this function returns [0, 1, 2, 5, 6]

      Given sequence (4, 5, 4, 5, 4, 5, 4)
         -- this function returns []

      Given sequence 'abbabbb'
         -- this function returns [1, 4, 5]

    Type hints:
      :type sequence: list | tuple | string
    """
    # -------------------------------------------------------------------------
    # TODO: 10. Implement and test this function.
    #     The testing code is already written for you (above).
    #  ------------------------------------------------------------------------
    #  DIFFICULTY AND TIME RATINGS (see top of this file for explanation)
    #    DIFFICULTY:      7
    #    TIME ESTIMATE:   15 minutes.
    # -------------------------------------------------------------------------


def run_test_practice_problem1j():
    """ Tests the   practice_problem1j  function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   practice_problem1j  function:')
    print('--------------------------------------------------')

    format_string = '    practice_problem1j( {} )'
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    expected = 'hBo'
    print_expected_result_of_test([('hello', 'Bye', 'ok joe')], expected,
                                  test_results, format_string)
    actual = practice_problem1j(('hello', 'Bye', 'ok joe'))
    print_actual_result_of_test(expected, actual, test_results)

    # Test 2:
    expected = 'ABCD'
    print_expected_result_of_test([('Alice', 'Bob', 'Carson', 'Devi')],
                                  expected, test_results, format_string)
    actual = practice_problem1j(('Alice', 'Bob', 'Carson', 'Devi'))
    print_actual_result_of_test(expected, actual, test_results)

    # Test 3:
    expected = 'to!'
    print_expected_result_of_test([('', 'tricky', '', 'one, no?', '!')],
                                  expected, test_results, format_string)
    actual = practice_problem1j(('', 'tricky', '', 'one, no?', '!'))
    print_actual_result_of_test(expected, actual, test_results)

    # Test 4:
    expected = 'mom'
    print_expected_result_of_test([('my very long string', 'ok', 'mmmm')],
                                  expected,
                                  test_results, format_string)
    actual = practice_problem1j(('my very long string', 'ok', 'mmmm'))
    print_actual_result_of_test(expected, actual, test_results)

    # Test 5:
    jokes = """
        Q: What is it called when a cat wins a dog show?
        A: A CAT-HAS-TROPHY!

        Q: What do you call a pile of kittens?
        A: a meowntain

        Q: Why don't cats like online shopping?
        A: They prefer a cat-alogue.

        Q: What did the cat say when he lost all his money?
        A: I'm paw!

        Q: Did you hear about the cat who swallowed a ball of yarn?
        A: She had a litter of mittens.

        Q: What do you call a lion who has eaten your mother's sister?
        A: An aunt-eater!

        Q: What is it called when a cat wins a dog show?
        A: A CAT-HAS-TROPHY!

        source: http://www.jokes4us.com/animaljokes/catjokes.html
        """
    # 5th test: Split  jokes  at spaces to get a list of strings.
    sequence = jokes.split()
    expected = ('QWiicwacwadsAACQWdycapokAamQWdclosAT' +
                'pacQWdtcswhlahmAIpQDyhatcwsaboyAShalom' +
                'QWdycalwheymsAAaQWiicwacwadsAACsh')

    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice_problem1j(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # SUMMARY of test results:
    print_summary_of_test_results(test_results)


def practice_problem1j(sequence):
    """
    What comes in:
      -- A sequence of strings, e.g. ('hello', 'Bye', 'ok joe')
    What goes out:
      -- Returns the string that contains the first letter in
           each of the strings in the given sequence,
           in the order in which they appear in the sequence.
           (So 'hBo' for the example sequence above).
    Side effects: None.
    Examples:
       Given ['hello', 'Bye', 'ok joe']          returns 'hBo'.
       Given ('Alice, 'Bob', 'Carson', 'Devi')   returns 'ABCD'.
       Given ('', 'tricky', '', 'one, no?', '!') returns 'to!'
       Given [] returns ''
       Given ('my very long string', 'ok', 'mmmm') returns 'mom'
    Type hints:
      :type sequence: [str]
    """
    # -------------------------------------------------------------------------
    # TODO: 11. Implement and test this function.
    #     The testing code is already written for you (above).
    #  ------------------------------------------------------------------------
    #  DIFFICULTY AND TIME RATINGS (see top of this file for explanation)
    #    DIFFICULTY:      7
    #    TIME ESTIMATE:   10 minutes.
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
    time.sleep(1)
    raise
