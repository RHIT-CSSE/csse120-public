"""
PRACTICE Exam 2, Demo File.
These problems are similar to the ACTUAL practice problems.
Your instructor might or might not want to "live-code" some of these
with you, as a warm-up for the actual 

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
import math
import rosegraphics as rg


def main():
    """ Calls the   TEST   functions in this module. """
    print("-----------------------------------------------")
    print("Un-comment each of the following TEST functions")
    print("as you implement the functions that they test.")
    print("-----------------------------------------------")

    # run_test_practice_problem1()
    # run_test_practice_problem2()
    # run_test_practice_problem3()
    # run_test_practice_problem4()
    # run_test_practice_problem5()
    # run_test_practice_problem6()
    # run_test_practice_problem7()
    # run_test_practice_problem8()


def is_prime(n):
    """
    What comes in:   An integer.
    What goes out:  Returns True if the given integer is prime.
                    Returns False if the given integer is NOT prime.
    Side effects: None.
    Examples:
      This function returns True or False, depending on whether
      the given integer is prime or not.  Since the smallest prime is 2,
      this function returns False on all integers < 2.
      It returns True on 2, 3, 5, 7, and other primes.
    Note: The algorithm used here is simple and clear but slow.
    Type hints:
      :type n: int
    """
    if n < 2:
        return False

    for k in range(2, int(math.sqrt(n) + 0.1) + 1):
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


###############################################################################
# Students: Some of the testing code below uses a simple testing framework.
# Ask for help if the tests that we supply are not clear to you.
###############################################################################

def run_test_practice_problem1():
    """ Tests the    practice_problem31    function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   practice_problem1 function:')
    print('--------------------------------------------------')

    format_string = '    practice_problem1( {} )'
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    expected = True
    sequence = [12, 33, 18, 45, 9, 13, 3, 90]
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice_problem1(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 2:
    expected = False
    sequence = [12, 12, 33, 44, 5, 33, 5, 23]
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice_problem1(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 3:
    expected = True
    sequence = (77, 112, 33, 1, 0, 43, 5, 115)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice_problem1(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 4:
    expected = False
    sequence = [1, 1, 1, 1, 1, 1, 0]
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice_problem1(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 5:
    expected = True
    sequence = [9]
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice_problem1(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 6:
    expected = True
    sequence = [12, 33, 18, 45, 9, 13, 3, 59]
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice_problem1(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # SUMMARY of test results:
    print_summary_of_test_results(test_results)


def practice_problem1(sequence):
    """
    What comes in: A non-empty sequence.
    What goes out: Returns True if the lat item of the sequence
      is the largest item in the sequence  Returns False
      if the last item of the sequence is not the largest in the sequence.
    Side effects: None.

    Type hints:
      :type: sequence: list    or tuple or string
    """

    # -------------------------------------------------------------------------
    # ToDo: 1. Implement and test this function.
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


def run_test_practice_problem2():
    """ Tests the    practice_problem2   function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   practice_problem2  function:')
    print('--------------------------------------------------')

    format_string = '    practice_problem2( {} )'
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    expected = [0]
    sequence = (9, 0, 8, 0, 0, 4, 4, 0)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice_problem2(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 2:
    expected = [0, 1, 2, 3, 5, 6, 7]
    sequence = (9, 9, 9, 9, 0, 9, 9, 9)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice_problem2(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 3:
    expected = []
    sequence = (4, 6, 4, 6, 4, 6, 4)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice_problem2(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 4:
    expected = [0, 1, 2]
    sequence = [3, 5, 7]
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice_problem2(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 5:
    expected = [1]
    sequence = [0, 5]
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice_problem2(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 6:
    expected = [0]
    sequence = [1, 56]
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice_problem2(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 7:
    expected = [1]
    sequence = [-40, 3]
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice_problem2(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 8:
    expected = []
    sequence = [-40, 68]
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice_problem2(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 9:
    expected = [0, 8]
    sequence = (1, 0, 2, 0, 0, 0, 0, 6, 9, 0, 0, 12)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice_problem2(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # SUMMARY of test results:
    print_summary_of_test_results(test_results)


def practice_problem2(sequence):
    """
    What comes in: A non-empty sequence of integers.
    What goes out: Returns a list of integers,
      where the integers are the places (indices)
      for which the item at that place is odd.
    Side effects: None.


    Type hints:
      :type: sequence: list    or tuple or string
    """

    # -------------------------------------------------------------------------
    # ToDo: 2. Implement and test this function.
    #     The testing code is already written for you (above).
    #  ------------------------------------------------------------------------
    #  DIFFICULTY AND TIME RATINGS (see top of this file for explanation)
    #    DIFFICULTY:      5
    #    TIME ESTIMATE:   8 minutes.
    # -------------------------------------------------------------------------


def run_test_practice_problem3():
    """ Tests the    practice_problem3    function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   practice_problem3  function:')
    print('--------------------------------------------------')

    format_string = '    practice_problem3( {} )'
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    expected = 1
    sequence = (9, 54, 8, 0, 0, 4, 4, 0)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice_problem3(sequence, 54)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 2:
    expected = 4
    sequence = (9, 9, 9, 9, 10, 9, 9, 9)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice_problem3(sequence, 10)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 3:
    expected = -1
    sequence = (4, 5, 4, 5, 4, 5, 4)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice_problem3(sequence, 25)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 4:
    expected = 1
    sequence = [0, 54, 0]
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice_problem3(sequence, 54)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 5:
    expected = -1
    sequence = [0, 0]
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice_problem3(sequence, 45)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 6:
    expected = 1
    sequence = [0, 77]
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice_problem3(sequence, 77)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 7:
    expected = 1
    sequence = [-40, 0]
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice_problem3(sequence, 0)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 8:
    expected = -1
    sequence = [-40, 67]
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice_problem3(sequence, 0)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 9:
    expected = 1
    sequence = (1, 0, 2, 0, 0, 0, 0, 6, 9, 0, 0, 12)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice_problem3(sequence, 0)
    print_actual_result_of_test(expected, actual, test_results)

    # SUMMARY of test results:
    print_summary_of_test_results(test_results)


def practice_problem3(sequence, threshold):
    """
    What comes in: A sequence of integers.
    What goes out: Returns the first (leftmost) place (index)
      for which the item at that place is equal to provided threshold
      Returns -1 if the sequence contains no items equal to threshold.
    Side effects: None.


    Type hints:
      :type: sequence: list    or tuple or string
    """

    # -------------------------------------------------------------------------
    # ToDo: 3. Implement and test this function.
    #     The testing code is already written for you (above).
    #  ------------------------------------------------------------------------
    #  DIFFICULTY AND TIME RATINGS (see top of this file for explanation)
    #    DIFFICULTY:      5
    #    TIME ESTIMATE:   10 minutes for both parts of this problem combined.
    # -------------------------------------------------------------------------


def run_test_practice_problem4():
    """ Tests the    practice_problem4   function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   practice_problem4  function:')
    print('--------------------------------------------------')

    format_string = '    practice_problem4( {} )'
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    expected = 140
    sequence = (12, 33, 18, 9, 13, 3, 99, 20, 19, 20)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice_problem4(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 2:
    expected = 19
    sequence = (3, 12, 10, 8, 8, 9, 8, 11)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice_problem4(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 3:
    expected = -9999999999
    sequence = (-9999999999, 8888888888)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice_problem4(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 4:
    expected = 8888888888
    sequence = (8888888888, -9999999999)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice_problem4(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 5:
    expected = 39912
    sequence = (-77, 20000, -33, 40000, -55, 60000, -11)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice_problem4(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 6:
    expected = 0
    sequence = ()
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice_problem4(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 7:
    expected = 0
    sequence = []
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice_problem4(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 8:
    expected = 8
    sequence = [8]
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice_problem4(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 9:
    expected = -77
    sequence = (-77, 8)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice_problem4(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 10:
    expected = -77
    sequence = (-77, 8, 77)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice_problem4(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 11:
    expected = 1
    sequence = (-77, 8, 78, 78)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice_problem4(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 12:
    expected = 23
    sequence = (-77, 8, 78, 100)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice_problem4(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # SUMMARY of test results:
    print_summary_of_test_results(test_results)


def practice_problem4(sequence):
    """
    What comes in:
      A sequence of numbers.
    What goes out:
      Returns the sum of the numbers at INDICES that are multiples of three.
    Side effects: None.
    Examples:
      If the sequence is:
          (12, 33, 18, 9, 13, 3, 99, 20, 19, 20)
      then this function returns
           12 + 9 + 99 + 20, which is 140
    Type hints:
      :type sequence: list(float)    or tuple(float)
    """

    # -------------------------------------------------------------------------
    # Todo: 4. Implement and test this function.
    #     The testing code is already written for you (above).
    #  ------------------------------------------------------------------------
    #  DIFFICULTY AND TIME RATINGS (see top of this file for explanation)
    #    DIFFICULTY:      5
    #    TIME ESTIMATE:   8 minutes.
    # -------------------------------------------------------------------------


def run_test_practice_problem5():
    """ Tests the    practice_problem5    function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   practice_problem5  function:')
    print('--------------------------------------------------')

    format_string = '    practice_problem5( {} )'
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    expected = [1, 3]
    sequence = (9, 33, 8, 8, 0, 4, 4, 8)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice_problem5(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 2:
    expected = [3]
    sequence = (9, 9, 9, 9, 0, 9, 9, 9)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice_problem5(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 3:
    expected = []
    sequence = (4, 4, 4, 4, 4, 4, 4)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice_problem5(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 4:
    expected = [2]
    sequence = 'abbabbb'
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice_problem5(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 5:
    expected = []
    sequence = [509]
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice_problem5(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 6:
    expected = [0, 1, 2, 3]
    sequence = [5, 4, 3, 2, 1]
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice_problem5(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # SUMMARY of test results:
    print_summary_of_test_results(test_results)


def practice_problem5(sequence):
    """
    What comes in: A non-empty sequence.
    What goes out: Returns a list of integers,
      where the integers are the places (indices)
      where an item in the given sequence is greater than the next item
      in the sequence.
    Side effects: None.

    Type hints:
      :type sequence: list | tuple | string
    """

    # -------------------------------------------------------------------------
    # Todo: 5. Implement and test this function.
    #     The testing code is already written for you (above).
    #  ------------------------------------------------------------------------
    #  DIFFICULTY AND TIME RATINGS (see top of this file for explanation)
    #    DIFFICULTY:      7
    #    TIME ESTIMATE:   15 minutes.
    # -------------------------------------------------------------------------


def run_test_practice_problem6():
    """ Tests the    practice_problem6   function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   practice_problem6 function:')
    print('--------------------------------------------------')

    format_string = '    practice_problem6( {} )'
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    expected = 3
    sequence = (12, 133, 18, 9, 13, 3, 99, 20, 19, 200)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice_problem6(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 2:
    expected = 3
    sequence = (125, 133, 18, 9, 13, 3, 99, 20, 19, 200, 124, 124, 124)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice_problem6(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 3:
    expected = 100
    sequence = (25, 100)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice_problem6(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 4:
    expected = 8
    sequence = (3, 12, 10, 8, 8, 9, 8, 11)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice_problem6(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 5:
    expected = 88
    sequence = (-9999999999, 88)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice_problem6(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 6:
    expected = -999
    sequence = (8888888888, -999)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice_problem6(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 7:
    expected = -22
    sequence = (-77, 20000, -33, -11, -55, -22, -11)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice_problem6(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 8:
    expected = 2000
    sequence = (-99999999999999, 2000)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice_problem6(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # SUMMARY of test results:
    print_summary_of_test_results(test_results)


def practice_problem6(sequence):
    """
    What comes in:
      A sequence of numbers, where the length of the sequence >= 2.
    What goes out:
      Returns the smallest of the numbers at odd INDICES of the sequence.
    Side effects: None.
    Examples:


    Type hints:
      :type sequence: (list | tuple) of (float | int)
    """

    # -------------------------------------------------------------------------
    # Todo: 6. Implement and test this function.
    #     The testing code is already written for you (above).
    #  ------------------------------------------------------------------------
    #  DIFFICULTY AND TIME RATINGS (see top of this file for explanation)
    #    DIFFICULTY:      5
    #    TIME ESTIMATE:   10 minutes.
    # -------------------------------------------------------------------------


def run_test_practice_problem7():
    """ Tests the    practice_problem7   function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   practice_problem7  function:')
    print('--------------------------------------------------')

    format_string = '    practice_problem7( {} )'
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    c = rg.Circle(rg.Point(7, 30), 10)
    expected = rg.Circle(rg.Point(5, 10), 20)
    circles = (rg.Circle(rg.Point(5, 10), 20),
               rg.Circle(rg.Point(2, 20), 20),
               c,
               rg.Circle(rg.Point(10, 40), 20),
               rg.Circle(rg.Point(2, 50), 10))
    print_expected_result_of_test([circles], expected, test_results,
                                  format_string)
    actual = practice_problem7(circles)
    print_actual_result_of_test(expected, actual, test_results)

    if actual == c and actual is not c:
        message = ("Technically, *** FAILED the above test. ***\n"
                   + "because you appear to have returned a CLONE\n"
                   + "of the correct rg.Circle instead of\n"
                   + "the rg.Circle itself.")
        testing_helper.print_colored(message, color='red')

    # Test 2:
    c = rg.Circle(rg.Point(58, 10), 5)
    expected = rg.Circle(rg.Point(58, 10), 5)
    circles = (c,)
    print_expected_result_of_test([circles], expected, test_results,
                                  format_string)
    actual = practice_problem7(circles)
    print_actual_result_of_test(expected, actual, test_results)

    if actual == c and actual is not c:
        message = ("Technically, *** FAILED the above test. ***\n"
                   + "because you appear to have returned a CLONE\n"
                   + "of the correct rg.Circle instead of\n"
                   + "the rg.Circle itself.")
        testing_helper.print_colored(message, color='red')

    # Test 3:
    c = rg.Circle(rg.Point(10005, 300), 41)
    expected = rg.Circle(rg.Point(10005, 300), 41)
    circles = (rg.Circle(rg.Point(84, 100), 300),
               rg.Circle(rg.Point(28, 200), 200),
               c)
    print_expected_result_of_test([circles], expected, test_results,
                                  format_string)
    actual = practice_problem7(circles)
    print_actual_result_of_test(expected, actual, test_results)

    if actual == c and actual is not c:
        message = ("Technically, *** FAILED the above test. ***\n"
                   + "because you appear to have returned a CLONE\n"
                   + "of the correct rg.Circle instead of\n"
                   + "the rg.Circle itself.")
        testing_helper.print_colored(message, color='red')

    # Test 4:
    c = rg.Circle(rg.Point(5, 10), 13)
    expected = rg.Circle(rg.Point(7, 30), 19)
    circles = (c,
               rg.Circle(rg.Point(0, 20), 20),
               rg.Circle(rg.Point(7, 30), 19),
               rg.Circle(rg.Point(10, 40), 14),
               rg.Circle(rg.Point(2, 50), 14))

    print_expected_result_of_test([circles], expected, test_results,
                                  format_string)
    actual = practice_problem7(circles)
    print_actual_result_of_test(expected, actual, test_results)

    if actual == c and actual is not c:
        message = ("Technically, *** FAILED the above test. ***\n"
                   + "because you appear to have returned a CLONE\n"
                   + "of the correct rg.Circle instead of\n"
                   + "the rg.Circle itself.")
        testing_helper.print_colored(message, color='red')

        # Test 5:
        c = rg.Circle(rg.Point(5, 10), 13)
        expected = rg.Circle(rg.Point(2, 50), 23)
        circles = (c,
                   rg.Circle(rg.Point(0, 20), 20),
                   rg.Circle(rg.Point(7, 30), 19),
                   rg.Circle(rg.Point(10, 40), 14),
                   rg.Circle(rg.Point(2, 50), 23))

        print_expected_result_of_test([circles], expected, test_results,
                                      format_string)
        actual = practice_problem7(circles)
        print_actual_result_of_test(expected, actual, test_results)

        if actual == c and actual is not c:
            message = ("Technically, *** FAILED the above test. ***\n"
                       + "because you appear to have returned a CLONE\n"
                       + "of the correct rg.Circle instead of\n"
                       + "the rg.Circle itself.")
            testing_helper.print_colored(message, color='red')

    # SUMMARY of test results:
    print_summary_of_test_results(test_results)


def practice_problem7(circles):
    """
    What comes in:  A non-empty sequence of rg.Circles.
    What goes out:  Returns the last rg.Circle in the list whose radius is prime.
    if there are no primes, it returns the first rg.Cirlce
    Side effects: None.

    Type hints:
      :type circles: [rg.Circle]
    """

    # -------------------------------------------------------------------------
    # Todo: 7. Implement and test this function.
    #     The testing code is already written for you (above).
    #  ------------------------------------------------------------------------
    #  DIFFICULTY AND TIME RATINGS (see top of this file for explanation)
    #    DIFFICULTY:      7
    #    TIME ESTIMATE:   10 minutes.
    # -------------------------------------------------------------------------


def run_test_practice_problem8():
    """
    #-------------------------------------------------------------------------
    # Todo: 8.  Write 2 test cases based on the function signature for problem 8
    #     The testing code is already written for you (above).
    #  ------------------------------------------------------------------------
    #  DIFFICULTY AND TIME RATINGS (see top of this file for explanation)
    #    DIFFICULTY:      7
    #    TIME ESTIMATE:   10 minutes.
    # -------------------------------------------------------------------------

    """


def practice_problem8(sequences1, sequences2):
    """
    What comes in:  Two sequences of integers of the same length
    What goes out:  Returns a new list that contains the product of the numbers
    in each position of the two sequences
    Side effects: None.


    """

    # -------------------------------------------------------------------------
    # Todo: 9. Implement and test this function.
    #  ------------------------------------------------------------------------
    #  DIFFICULTY AND TIME RATINGS (see top of this file for explanation)
    #    DIFFICULTY:      4
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
