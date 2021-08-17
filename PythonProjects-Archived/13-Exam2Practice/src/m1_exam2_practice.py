"""
PRACTICE Exam 2, practice_problem 1.

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
#     3 is an "easy" Exam 2 question.
#     5 is a "typical" Exam 2 question.
#     7 is a "hard" Exam 2 question.
#    10 is an EXTREMELY hard problem (too hard for an Exam 2 question)
#
#  TIME ratings: A ROUGH estimate of the number of minutes that we
#     would expect a well-prepared student to take on the problem.
#
#  TODO: 2. Read and heed the following!
#         IMPORTANT: For ALL the problems in this module,
#         if you reach the time estimate and are NOT close to a solution,
#         STOP working on that problem and ASK YOUR INSTRUCTOR FOR HELP
#         on it, in class or via Piazza.
#             (Mark this _TODO_ as DONE after reading it.)
###############################################################################

###############################################################################
# TODO: 3. Read and heed the following!
#  _
#  For ALL the problems in this module, first work a concrete example by hand,
#  to be sure that you understand the problem AND to see how to solve it.
#  _
#  For each problem, ASK YOURSELF:
#    1. Which of the following pattern(s) does this problem fit?
#        COUNT-SUM-EXAMINE-ITEMS?
#        FIND-ITEM?
#        FIND-BEST?
#        TWO-PLACES-AT-EACH-ITERATION?
#        TWO-SEQUENCES-AT-EACH-ITERATION?
#    2. Should the RANGE iterate through all of the sequence,
#         or just part of it?  Forwards or backwards?
#    3. Does the problem require building up a list? A string?
#    4. Does the problem need just one loop, or more loop(s) after the first?\
#  _
#  Mark this _TODO_ as DONE after reading and UNDERSTANDING it.
###############################################################################

import testing_helper
import time
import rosegraphics as rg
import random


###############################################################################
# Students: Some of the testing code below uses a simple testing framework.
# Ask for help if the tests that we supply are not clear to you.
###############################################################################
def main():
    """ Calls the   TEST   functions in this module. """
    print("-----------------------------------------------")
    print("Un-comment each of the following TEST functions")
    print("as you implement the functions that they test.")
    print("-----------------------------------------------")

    # run_test_practice1a()
    # run_test_practice1b()
    # run_test_practice1c()
    # run_test_practice1d()
    # run_test_practice1e()
    # run_test_practice1f()
    # run_test_practice1g()
    # run_test_practice1h()
    # run_test_practice1i()
    # run_test_practice1j()
    # run_test_practice1k()


###############################################################################
# TODO: 4.  READ the green doc-strings below for the:
#      is_prime
#      get_prime_factorization
#   functions defined below. You do NOT need to understand their
#   implementations, just their specifications (per the doc-strings).
#   You should  ** CALL ** those functions as needed in implementing other
#   function(s) in this module.
#   After you have READ this, change its _TODO_ to DONE.
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


def get_prime_factorization(n):
    """
    What comes in:  A positive integer that is at least 2.
    What goes out:
      -- Returns the list of the prime numbers that,
            when multiplied together, equals the given integer.
            The numbers in the list are returned in ascending order.
    Side effects:   None.
    Examples:
      -- get_prime_factorization(140)  returns  [2, 2, 5, 7]
      -- get_prime_factorization(11)   returns  [11]
      -- get_prime_factorization(91)   returns  [7, 13]
      -- get_prime_factorization(825)  returns  [3, 5, 5, 11]
      -- get_prime_factorization(32)   returns  [2, 2, 2, 2, 2]
      -- get_prime_factorization(210)  returns  [2, 3, 5, 7]
      -- get_prime_factorization(211)  returns  [211]
      -- get_prime_factorization(212)  returns  [2, 2, 53]
    Note: The algorithm used here is simple and clear but not very fast.
    """
    factorization = []
    remaining = n
    for k in range(2, n + 1):
        if is_prime(k):
            while True:
                if remaining % k == 0:
                    factorization.append(k)
                    remaining = remaining // k
                else:
                    break
    return factorization

    # -------------------------------------------------------------------------
    # Students:
    #   Do NOT touch the above  get_prime_factorization  function
    #   - it has no _TODO_.  Do NOT copy code from this function.
    #
    # Instead, ** CALL ** this function as needed in the problems below.
    # -------------------------------------------------------------------------


def run_test_practice1a():
    """ Tests the   practice1a  function. """
    print()
    print("------------------------------------")
    print("Testing the   practice1a   function:")
    print("------------------------------------")

    format_string = "    practice1a( {}, m={} )"
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    expected = [8, 16, 11, -14, 14]
    sequence = [2, 10, 5, -20, 8]
    m = 6
    print_expected_result_of_test([sequence, m], expected,
                                  test_results, format_string)
    actual = practice1a(sequence, m)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 2:
    expected = [8, 16, 11, -14, 14]
    sequence = (2, 10, 5, -20, 8)
    m = 6
    print_expected_result_of_test([sequence, m], expected,
                                  test_results, format_string)
    actual = practice1a(sequence, m)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 3:
    expected = [800]
    sequence = [795]
    m = 5
    print_expected_result_of_test([sequence, m], expected, test_results,
                                  format_string)
    actual = practice1a(sequence, m)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 4:
    expected = []
    sequence = []
    m = 50
    print_expected_result_of_test([sequence, m], expected, test_results,
                                  format_string)
    actual = practice1a(sequence, m)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 5:
    expected = [1, 1, 2, 3, 10, -11, 12, 0, 0, 1]
    sequence = (1, 1, 2, 3, 10, -11, 12, 0, 0, 1)
    m = 0
    print_expected_result_of_test([sequence, m], expected, test_results,
                                  format_string)
    actual = practice1a(sequence, m)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 6:
    expected = [-99, -99, -110, -100, -100, 0]
    sequence = (1, 1, -10, 0, 0, 100)
    m = -100
    print_expected_result_of_test([sequence, m], expected, test_results,
                                  format_string)
    actual = practice1a(sequence, m)
    print_actual_result_of_test(expected, actual, test_results)

    print_summary_of_test_results(test_results)


def practice1a(sequence, delta):
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
       Given the list          [2, 10, 5, -20, 8]  and the number  6,
         this problem returns  [8, 16, 11, -14, 14]
    Type hints:
      :type sequence: [int]
      :type delta:    int
    """
    # -------------------------------------------------------------------------
    # TODO: 5. Implement and test this function.
    #     The testing code is already written for you (above).
    #  ASK YOURSELF:
    #    1. Which of the following pattern(s) does this problem fit?
    #        COUNT-SUM-EXAMINE-ITEMS?
    #        FIND-ITEM?
    #        FIND-BEST?
    #        TWO-PLACES-AT-EACH-ITERATION?
    #        TWO-SEQUENCES-AT-EACH-ITERATION?
    #    2. Should the RANGE iterate through all of the sequence,
    #         or just part of it?  Forwards or backwards?
    #    3. Does the problem require building up a list? A string?
    #    4. Does it need just one loop, or more loop(s) after the first?
    #  ------------------------------------------------------------------------
    #  DIFFICULTY AND TIME RATINGS (see top of this file for explanation)
    #    DIFFICULTY:      3
    #    TIME ESTIMATE:   5 minutes.
    # -------------------------------------------------------------------------


def run_test_practice1b():
    """ Tests the    practice1b    function. """
    print()
    print("------------------------------------")
    print("Testing the   practice1b   function:")
    print("------------------------------------")

    format_string = "    practice1b( {} )"
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    expected = 1
    sequence = [9, 0, 8, 0, 0, 4, 4, 0]
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice1b(sequence)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 2:
    expected = 4
    sequence = (9, 9, 9, 9, 0, 9, 9, 9)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice1b(sequence)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 3:
    expected = -1
    sequence = (4, 5, 4, 5, 4, 5, 4)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice1b(sequence)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 4:
    expected = 0
    sequence = [0, 0, 0]
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice1b(sequence)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 5:
    expected = 0
    sequence = [0, 0]
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice1b(sequence)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 6:
    expected = 0
    sequence = [0, 77]
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice1b(sequence)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 7:
    expected = 1
    sequence = [-40, 0]
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice1b(sequence)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 8:
    expected = -1
    sequence = [-40, 67]
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice1b(sequence)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 9:
    expected = 1
    sequence = (1, 0, 2, 0, 0, 0, 0, 6, 9, 0, 0, 12)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice1b(sequence)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 10:
    expected = -1
    sequence = []
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice1b(sequence)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 11:
    expected = -1
    sequence = ()
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice1b(sequence)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 12:
    expected = 100
    sequence = (100 * [-1]) + [0] + (100 * [-1])
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice1b(sequence)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # SUMMARY of test results:
    print_summary_of_test_results(test_results)


def practice1b(sequence):
    """
    What comes in: A sequence of integers.
    What goes out: Returns the first (i.e., lowest-index) place (i.e., index)
      for which the item at that place equals 0.
      Returns -1 if the sequence contains no items equal to 0.
    Side effects: None.
    Examples:
      Given sequence [9, 0, 8, 0, 0, 4, 4, 0]
         -- this function returns 1
              since 0 first appears at index 1

      Given sequence (9, 9, 9, 9, 0, 9, 9, 9)
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
    # TODO: 6. Implement and test this function.
    #     The testing code is already written for you (above).
    #  ASK YOURSELF:
    #    1. Which of the following pattern(s) does this problem fit?
    #        COUNT-SUM-EXAMINE-ITEMS?
    #        FIND-ITEM?
    #        FIND-BEST?
    #        TWO-PLACES-AT-EACH-ITERATION?
    #        TWO-SEQUENCES-AT-EACH-ITERATION?
    #    2. Should the RANGE iterate through all of the sequence,
    #         or just part of it?  Forwards or backwards?
    #    3. Does the problem require building up a list? A string?
    #    4. Does it need just one loop, or more loop(s) after the first?
    #  ------------------------------------------------------------------------
    #  DIFFICULTY AND TIME RATINGS (see top of this file for explanation)
    #    DIFFICULTY:      3
    #    TIME ESTIMATE:   5 minutes
    # -------------------------------------------------------------------------


def run_test_practice1c():
    """ Tests the   practice1c   function. """
    print()
    print("------------------------------------")
    print("Testing the   practice1c   function:")
    print("------------------------------------")

    format_string = "    practice1c( {}, m={} )"
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1
    expected = [2, 2, 2, 2, 2]
    integers = [825, 11, 140, 32, 91, 72, 64, 6]
    m = 5
    print_expected_result_of_test([integers, m], expected, test_results,
                                  format_string)
    actual = practice1c(integers, m)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 2
    expected = [3, 5, 5, 11]
    integers = [825, 11, 140, 32, 91, 72, 64, 6]
    m = 3
    print_expected_result_of_test([integers, m], expected, test_results,
                                  format_string)
    actual = practice1c(integers, m)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 3
    expected = [2, 2, 2, 2, 2, 2]
    integers = [825, 11, 140, 32, 91, 72, 64, 6]
    m = 6
    print_expected_result_of_test([integers, m], expected, test_results,
                                  format_string)
    actual = practice1c(integers, m)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 4
    expected = []
    integers = [825, 11, 140, 32, 91, 72, 64, 6]
    m = 7
    print_expected_result_of_test([integers, m], expected, test_results,
                                  format_string)
    actual = practice1c(integers, m)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 5
    expected = [2, 2, 2, 3, 3]
    integers = [825, 11, 140, 72, 91, 32, 64, 6]
    m = 5
    print_expected_result_of_test([integers, m], expected, test_results,
                                  format_string)
    actual = practice1c(integers, m)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 6
    expected = [3, 5, 5, 11]
    integers = [825]
    m = 1
    print_expected_result_of_test([integers, m], expected, test_results,
                                  format_string)
    actual = practice1c(integers, m)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 7
    expected = [3, 5, 5, 11]
    integers = [825]
    m = 4
    print_expected_result_of_test([integers, m], expected, test_results,
                                  format_string)
    actual = practice1c(integers, m)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 8
    expected = []
    integers = [825]
    m = 5
    print_expected_result_of_test([integers, m], expected, test_results,
                                  format_string)
    actual = practice1c(integers, m)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 9
    expected = []
    integers = []
    m = 1
    print_expected_result_of_test([integers, m], expected, test_results,
                                  format_string)
    actual = practice1c(integers, m)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 10
    expected = [2, 3]
    integers = [6, 8, 6, 9, 625, 6, 70]
    m = 1
    print_expected_result_of_test([integers, m], expected, test_results,
                                  format_string)
    actual = practice1c(integers, m)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 11
    expected = [2, 3]
    integers = [6, 8, 6, 9, 625, 6, 70]
    m = 2
    print_expected_result_of_test([integers, m], expected, test_results,
                                  format_string)
    actual = practice1c(integers, m)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 12
    expected = [2, 2, 2]
    integers = [6, 8, 6, 9, 625, 6, 70]
    m = 3
    print_expected_result_of_test([integers, m], expected, test_results,
                                  format_string)
    actual = practice1c(integers, m)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 13
    expected = [5, 5, 5, 5]
    integers = [6, 9, 625, 6, 192, 70]
    m = 4
    print_expected_result_of_test([integers, m], expected, test_results,
                                  format_string)
    actual = practice1c(integers, m)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 14
    expected = [2, 2, 2, 2, 2, 2, 3]
    integers = [6, 9, 625, 6, 192, 70]
    m = 7
    print_expected_result_of_test([integers, m], expected, test_results,
                                  format_string)
    actual = practice1c(integers, m)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 15
    expected = [2, 2, 2, 2, 2, 2, 3]
    integers = [192, 6, 9, 625, 6, 128, 70]
    m = 7
    print_expected_result_of_test([integers, m], expected, test_results,
                                  format_string)
    actual = practice1c(integers, m)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 16
    expected = []
    integers = [6, 9, 625, 6, 192, 70]
    m = 10
    print_expected_result_of_test([integers, m], expected, test_results,
                                  format_string)
    actual = practice1c(integers, m)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 17
    expected = [2, 2, 2, 2, 2, 2, 3]
    integers = (192, 6, 9, 625, 6, 128, 70)  # Tests for (incorrect) mutation
    m = 7
    print_expected_result_of_test([integers, m], expected, test_results,
                                  format_string)
    actual = practice1c(integers, m)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Summary:
    print_summary_of_test_results(test_results)


###############################################################################
# Be sure to read the IMPORTANT note in the _TODO_ for the following problem!
###############################################################################
def practice1c(integers, m):
    """
    What comes in:
      -- A sequence of positive integers, each of which is >= 2, and
      -- A positive integer m.
    What goes out:
       Returns the prime factorization of the first (i.e., lowest-index)
       integer in the sequence for which the length of its prime
       factorization is greater than or equal to the given m.
       Returns the empty list if there are no such integers in the sequence.
    Side effects: None
    Examples:

    Note that you are GIVEN (ABOVE) a function to compute prime factorization.

      Suppose that integers = [825, 11, 140, 32, 91, 72, 64, 6].
      Note that the prime factorizations of those integers are:
                for 825: [3, 5, 5, 11]
                for 11:  [11]
                for 140: [2, 2, 5, 7]
                for 32:  [2, 2, 2, 2, 2]
                for 91:  [7, 13]
                for 72:  [2, 2, 2, 3, 3]
                for 64:  [2, 2, 2, 2, 2, 2]
                for 6:   [2, 3]
        -- if m = 5, the first of the above whose length is at least 5
             is [2, 2, 2, 2, 2], so  [2, 2, 2, 2, 2] is returned
        -- if m = 3, the first of the above whose length is at least 3
             is [3, 5, 5, 11], so  [3, 5, 5, 11] is returned
        -- if m = 6, the first of the above whose length is at least 6
             is [2, 2, 2, 2, 2, 2], so  [2, 2, 2, 2, 2, 2] is returned
        -- if m = 7, none of the above has length at least 7
             so  [] is returned

       ** ASK YOUR INSTRUCTOR FOR HELP **
       ** IF YOU DO NOT UNDERSTAND THE ABOVE SPECIFICATION. **
    Type hints:
      :type integers: list[int] | tuple[int]
      :type m: int
    """
    ###########################################################################
    # TODO: 7. Implement and test this function.
    #          Tests have been written for you (above).
    #   IMPORTANT:
    #    **  For full credit you must appropriately use (call)
    #    **  the   get_prime_factorization   function that is DEFINED ABOVE.
    #  ASK YOURSELF:
    #    1. Which of the following pattern(s) does this problem fit?
    #        COUNT-SUM-EXAMINE-ITEMS?
    #        FIND-ITEM?
    #        FIND-BEST?
    #        TWO-PLACES-AT-EACH-ITERATION?
    #        TWO-SEQUENCES-AT-EACH-ITERATION?
    #    2. Should the RANGE iterate through all of the sequence,
    #         or just part of it?  Forwards or backwards?
    #    3. Does the problem require building up a list? A string?
    #    4. Does it need just one loop, or more loop(s) after the first?
    #  ------------------------------------------------------------------------
    #  DIFFICULTY AND TIME RATINGS (see top of this file for explanation)
    #    DIFFICULTY:      6
    #    TIME ESTIMATE:   10 minutes
    ###########################################################################


def run_test_practice1d():
    """ Tests the    practice1d    function. """
    print()
    print("------------------------------------")
    print("Testing the   practice1d   function:")
    print("------------------------------------")

    format_string = "    practice1d( {} )"
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    c = rg.Circle(rg.Point(7, 30), 10)
    expected = c
    circles = (rg.Circle(rg.Point(5, 10), 20),
               rg.Circle(rg.Point(2, 20), 20),
               c,
               rg.Circle(rg.Point(10, 40), 20),
               rg.Circle(rg.Point(2, 50), 10))
    print_expected_result_of_test([circles], expected, test_results,
                                  format_string)
    actual = practice1d(circles)
    print_actual_result_of_test(expected, actual, test_results)

    if actual == c and actual is not c:
        message = ("  Technically, *** FAILED the above test. ***\n"
                   + "  because you appear to have returned a CLONE\n"
                   + "  of the correct rg.Circle instead of\n"
                   + "  the correct rg.Circle itself.")
        testing_helper.print_colored(message, color="red")

    # Test 2:
    c = rg.Circle(rg.Point(58, 10), 20)
    expected = c
    circles = (c,)
    print_expected_result_of_test([circles], expected, test_results,
                                  format_string)
    actual = practice1d(circles)
    print_actual_result_of_test(expected, actual, test_results)

    if actual == c and actual is not c:
        message = ("  Technically, *** FAILED the above test. ***\n"
                   + "  because you appear to have returned a CLONE\n"
                   + "  of the correct rg.Circle instead of\n"
                   + "  the correct rg.Circle itself.")
        testing_helper.print_colored(message, color="red")

    # Test 3:
    c = rg.Circle(rg.Point(10005, 300), 100)
    expected = c
    circles = (rg.Circle(rg.Point(84, 100), 300),
               rg.Circle(rg.Point(28, 200), 200),
               c)
    print_expected_result_of_test([circles], expected, test_results,
                                  format_string)
    actual = practice1d(circles)
    print_actual_result_of_test(expected, actual, test_results)

    if actual == c and actual is not c:
        message = ("  Technically, *** FAILED the above test. ***\n"
                   + "  because you appear to have returned a CLONE\n"
                   + "  of the correct rg.Circle instead of\n"
                   + "  the correct rg.Circle itself.")
        testing_helper.print_colored(message, color="red")

    # Test 4:
    c = rg.Circle(rg.Point(5, 10), 13)
    expected = c
    circles = (c,
               rg.Circle(rg.Point(0, 20), 20),
               rg.Circle(rg.Point(7, 30), 19),
               rg.Circle(rg.Point(10, 40), 14),
               rg.Circle(rg.Point(2, 50), 14))

    print_expected_result_of_test([circles], expected, test_results,
                                  format_string)
    actual = practice1d(circles)
    print_actual_result_of_test(expected, actual, test_results)

    if actual == c and actual is not c:
        message = ("  Technically, *** FAILED the above test. ***\n"
                   + "  because you appear to have returned a CLONE\n"
                   + "  of the correct rg.Circle instead of\n"
                   + "  the correct rg.Circle itself.")
        testing_helper.print_colored(message, color="red")

    # Test 5:  Perhaps not a valid test since it assumes an rg.Circle
    #          can have a NEGATIVE radius, but it will catch some dubious code.
    small = -9999999999999999999999999999
    c = rg.Circle(rg.Point(7, 30), small)
    expected = c
    circles = (rg.Circle(rg.Point(0, 20), small + 1),
               c,
               rg.Circle(rg.Point(7, 30), small),
               rg.Circle(rg.Point(2, 50), small + 1))

    print_expected_result_of_test([circles], expected, test_results,
                                  format_string)
    actual = practice1d(circles)
    print_actual_result_of_test(expected, actual, test_results)

    if actual == c and actual is not c:
        message = ("  Technically, *** FAILED the above test. ***\n"
                   + "  because you appear to have returned a CLONE\n"
                   + "  of the correct rg.Circle instead of\n"
                   + "  the correct rg.Circle itself.")
        testing_helper.print_colored(message, color="red")

    # Test 6:  Tests tie-breaking
    c = rg.Circle(rg.Point(1, 1), 10)
    expected = c
    circles = (rg.Circle(rg.Point(2, 2), 20),
               c,
               rg.Circle(rg.Point(3, 3), 10),
               rg.Circle(rg.Point(4, 4), 10))
    print_expected_result_of_test([circles], expected, test_results,
                                  format_string)
    actual = practice1d(circles)
    print_actual_result_of_test(expected, actual, test_results)

    if actual == c and actual is not c:
        message = ("  Technically, *** FAILED the above test. ***\n"
                   + "  because you appear to have returned a CLONE\n"
                   + "  of the correct rg.Circle instead of\n"
                   + "  the correct rg.Circle itself.")
        testing_helper.print_colored(message, color="red")

    # Tests 7 and following:  Tests that use many random permutations
    number_of_tests = 100000
    c = rg.Circle(rg.Point(0, 0), 0)
    expected = c
    circles = [c]
    for k in range(1, 11):
        circles.append(rg.Circle(rg.Point(k, k), k).clone())

    random.seed(44)  # To make the tests reproducible
    for k in range(number_of_tests):
        random.shuffle(circles)
        actual = practice1d(circles)
        if actual != expected:
            print()
            print("Test {}:".format(7 + k))
            print("  This test case calls   practice1d   on:")
            print("    [")
            for j in range(len(circles) - 1):
                r = circles[j].radius
                print("      Circle(({}, {}), {}),".format(r, r, r))
            r = circles[len(circles) - 1].radius
            print("      Circle(({}, {}), {}) ]".format(r, r, r))
            print("  Expected:", "Circle((0, 0), 0)")
            if isinstance(actual, rg.Circle):
                print("  Actual:  ", "Circle(({}, {}), {})".format(
                    actual.center.x, actual.center.y, actual.radius))
            else:
                print("  Actual:  ", actual)
            print("  *** FAILED the above test. ***", color="red")
            test_results = [test_results[0], test_results[1] + 1]
            break

    # SUMMARY of test results:
    print_summary_of_test_results(test_results)


def practice1d(circles):
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
      :type circles: list[rg.Circle] | tuple[rg.Circle]
    """
    # -------------------------------------------------------------------------
    # TODO: 8. Implement and test this function.
    #     The testing code is already written for you (above).
    #  ASK YOURSELF:
    #    1. Which of the following pattern(s) does this problem fit?
    #        COUNT-SUM-EXAMINE-ITEMS?
    #        FIND-ITEM?
    #        FIND-BEST?
    #        TWO-PLACES-AT-EACH-ITERATION?
    #        TWO-SEQUENCES-AT-EACH-ITERATION?
    #    2. Should the RANGE iterate through all of the sequence,
    #         or just part of it?  Forwards or backwards?
    #    3. Does the problem require building up a list? A string?
    #    4. Does it need just one loop, or more loop(s) after the first?
    #  ------------------------------------------------------------------------
    #  DIFFICULTY AND TIME RATINGS (see top of this file for explanation)
    #    DIFFICULTY:      7
    #    TIME ESTIMATE:   10 minutes.
    # -------------------------------------------------------------------------


def run_test_practice1e():
    """ Tests the    practice1e    function. """
    print()
    print("------------------------------------")
    print("Testing the   practice1e   function:")
    print("------------------------------------")

    format_string = "    practice1e( {} )"
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    expected = [1, 3, 4, 7]
    sequence = (9, 0, 8, 0, 0, 4, 4, 0)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice1e(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 2:
    expected = [4]
    sequence = (9, 9, 9, 9, 0, 9, 9, 9)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice1e(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 3:
    expected = []
    sequence = (4, 5, 4, 5, 4, 5, 4)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice1e(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 4:
    expected = [0, 1, 2]
    sequence = [0, 0, 0]
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice1e(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 5:
    expected = [0, 1]
    sequence = [0, 0]
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice1e(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 6:
    expected = [0]
    sequence = [0, 77]
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice1e(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 7:
    expected = [1]
    sequence = [-40, 0]
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice1e(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 8:
    expected = []
    sequence = [-40, 67]
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice1e(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 9:
    expected = [1, 3, 4, 5, 6, 9, 10]
    sequence = (1, 0, 2, 0, 0, 0, 0, 6, 9, 0, 0, 12)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice1e(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # SUMMARY of test results:
    print_summary_of_test_results(test_results)


def practice1e(sequence):
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
      :type: sequence: list[int] | tuple[int]
    """
    # -------------------------------------------------------------------------
    # TODO: 9. Implement and test this function.
    #     The testing code is already written for you (above).
    #  ASK YOURSELF:
    #    1. Which of the following pattern(s) does this problem fit?
    #        COUNT-SUM-EXAMINE-ITEMS?
    #        FIND-ITEM?
    #        FIND-BEST?
    #        TWO-PLACES-AT-EACH-ITERATION?
    #        TWO-SEQUENCES-AT-EACH-ITERATION?
    #    2. Should the RANGE iterate through all of the sequence,
    #         or just part of it?  Forwards or backwards?
    #    3. Does the problem require building up a list? A string?
    #    4. Does it need just one loop, or more loop(s) after the first?
    #  ------------------------------------------------------------------------
    #  DIFFICULTY AND TIME RATINGS (see top of this file for explanation)
    #    DIFFICULTY:      5
    #    TIME ESTIMATE:   8 minutes.
    # -------------------------------------------------------------------------


def run_test_practice1f():
    """ Tests the    practice1f    function. """
    print()
    print("------------------------------------")
    print("Testing the   practice1f   function:")
    print("------------------------------------")

    format_string = "    practice1f( {}, {} )"
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    expected = [40, 10, 22, 30, 91, 20, 80, 12, 11, 10, 40, 22, 25, 27]
    sequence1 = [40, 22, 91, 80, 11, 40, 25]
    sequence2 = [10, 30, 20, 12, 10, 22, 27]
    print_expected_result_of_test([sequence1, sequence2], expected,
                                  test_results, format_string)
    actual = practice1f(sequence1, sequence2)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 2:
    expected = ["h", "t", "e", "h", "l", "e", "l", "r", "o", "e"]
    sequence1 = "hello"
    sequence2 = "there"
    print_expected_result_of_test([sequence1, sequence2], expected,
                                  test_results, format_string)
    actual = practice1f(sequence1, sequence2)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 3:
    expected = [40, 10, 22, 30, 91, 20, 80, 12, 11, 10, 40, 22, 25, 27]
    sequence1 = (40, 22, 91, 80, 11, 40, 25)
    sequence2 = [10, 30, 20, 12, 10, 22, 27]
    print_expected_result_of_test([sequence1, sequence2], expected,
                                  test_results, format_string)
    actual = practice1f(sequence1, sequence2)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 4:
    expected = [40, 10, 22, 30, 91, 20, 80, 12, 11, 10, 40, 22, 25, 27]
    sequence1 = [40, 22, 91, 80, 11, 40, 25]
    sequence2 = (10, 30, 20, 12, 10, 22, 27)
    print_expected_result_of_test([sequence1, sequence2], expected,
                                  test_results, format_string)
    actual = practice1f(sequence1, sequence2)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 5:
    expected = [333, 100]
    sequence1 = [333]
    sequence2 = [100]
    print_expected_result_of_test([sequence1, sequence2], expected,
                                  test_results, format_string)
    actual = practice1f(sequence1, sequence2)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 6:
    expected = []
    sequence1 = []
    sequence2 = []
    print_expected_result_of_test([sequence1, sequence2], expected,
                                  test_results, format_string)
    actual = practice1f(sequence1, sequence2)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 7:
    expected = ["hi", "bye", "bob", "bob", 403, "1 2 3 4 5"]
    sequence1 = ["hi", "bob", 403]
    sequence2 = ["bye", "bob", "1 2 3 4 5"]
    print_expected_result_of_test([sequence1, sequence2], expected,
                                  test_results, format_string)
    actual = practice1f(sequence1, sequence2)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 8:
    expected = list(range(1, 101))
    sequence1 = list(range(1, 100, 2))
    sequence2 = list(range(2, 101, 2))
    print_expected_result_of_test([sequence1, sequence2], expected,
                                  test_results, format_string)
    actual = practice1f(sequence1, sequence2)
    print_actual_result_of_test(expected, actual, test_results)

    # SUMMARY of test results:
    print_summary_of_test_results(test_results)


def practice1f(sequence1, sequence2):
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
      :type sequence1: list | tuple | str
      :type sequence2: list | tuple | str
    """
    # -------------------------------------------------------------------------
    # TODO: 10. Implement and test this function.
    #     The testing code is already written for you (above).
    #  ASK YOURSELF:
    #    1. Which of the following pattern(s) does this problem fit?
    #        COUNT-SUM-EXAMINE-ITEMS?
    #        FIND-ITEM?
    #        FIND-BEST?
    #        TWO-PLACES-AT-EACH-ITERATION?
    #        TWO-SEQUENCES-AT-EACH-ITERATION?
    #    2. Should the RANGE iterate through all of the sequence,
    #         or just part of it?  Forwards or backwards?
    #    3. Does the problem require building up a list? A string?
    #    4. Does it need just one loop, or more loop(s) after the first?
    #  ------------------------------------------------------------------------
    #  DIFFICULTY AND TIME RATINGS (see top of this file for explanation)
    #    DIFFICULTY:      6
    #    TIME ESTIMATE:   8 minutes.
    # -------------------------------------------------------------------------


def run_test_practice1g():
    """ Tests the    practice1g    function. """
    print()
    print("------------------------------------")
    print("Testing the   practice1g   function:")
    print("------------------------------------")

    format_string = "    practice1g( {} )"
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    expected = [2, 5]
    sequence = (9, 33, 8, 8, 0, 4, 4, 8)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice1g(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 2:
    expected = [0, 1, 2, 5, 6]
    sequence = (9, 9, 9, 9, 0, 9, 9, 9)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice1g(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 3:
    expected = []
    sequence = (4, 5, 4, 5, 4, 5, 4)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice1g(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 4:
    expected = [1, 4, 5]
    sequence = "abbabbb"
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice1g(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 5:
    expected = []
    sequence = [509]
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice1g(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # SUMMARY of test results:
    print_summary_of_test_results(test_results)


def practice1g(sequence):
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

      Given sequence "abbabbb"
         -- this function returns [1, 4, 5]

    Type hints:
      :type sequence: list | tuple | str
    """
    # -------------------------------------------------------------------------
    # TODO: 11. Implement and test this function.
    #     The testing code is already written for you (above).
    #  ASK YOURSELF:
    #    1. Which of the following pattern(s) does this problem fit?
    #        COUNT-SUM-EXAMINE-ITEMS?
    #        FIND-ITEM?
    #        FIND-BEST?
    #        TWO-PLACES-AT-EACH-ITERATION?
    #        TWO-SEQUENCES-AT-EACH-ITERATION?
    #    2. Should the RANGE iterate through all of the sequence,
    #         or just part of it?  Forwards or backwards?
    #    3. Does the problem require building up a list? A string?
    #    4. Does it need just one loop, or more loop(s) after the first?
    #  ------------------------------------------------------------------------
    #  DIFFICULTY AND TIME RATINGS (see top of this file for explanation)
    #    DIFFICULTY:      5
    #    TIME ESTIMATE:   8 minutes.
    # -------------------------------------------------------------------------


def run_test_practice1h():
    """ Tests the    practice1h    function. """
    print()
    print("-----------------------------------")
    print("Testing the   practice1h   function:")
    print("-----------------------------------")

    format_string = "    practice1h( {} )"
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    expected = 13
    sequence = [20, 12, 133, 11, 9, 13, 3, 99, 20, 5, 200]
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice1h(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 2:
    expected = "bad"
    sequence = [13, 24, 3, 18, 3, 21]
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice1h(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 3:
    expected = "bad"
    sequence = [13]
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice1h(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 4:
    expected = 17
    sequence = [20, 12, 133, 11, 9, 13, 3, 99, 20, 4, 200, 17, 3, 5, 7, 11, 13]
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice1h(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 5:
    expected = 5
    sequence = [17, 5, 19]
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice1h(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 6:
    expected = 23
    sequence = [23, 23, 23, 23, 23, 23, 23, 23, 23, 23]
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice1h(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 7:
    expected = 31
    sequence = [23, 23, 23, 23, 23, 23, 23, 23, 23, 31]
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice1h(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 8:
    expected = 23
    sequence = [23, 23, 23, 23, 23, 23, 23, 23, 31]
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice1h(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Tests 9 and following:  Tests that use many random permutations
    number_of_tests = 100000
    numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

    random.seed(42)  # To make the tests reproducible
    for k in range(number_of_tests):
        random.shuffle(numbers)
        # A fancy solution (not available to students since MAX is prohibited):
        candidates = [x for x in numbers[1:len(numbers):2] if is_prime(x)]
        expected = "bad" if len(candidates) == 0 else max(candidates)
        actual = practice1h(numbers)
        if actual != expected:
            print()
            print("Test {}:".format(9 + k))
            print("  This test case calls   practice1h   on:")
            print("    ", numbers)
            print("  Expected:", expected)
            print("  Actual:  ", actual)
            print("  *** FAILED the above test. ***", color="red")
            test_results = [test_results[0], test_results[1] + 1]
            break

    # SUMMARY of test results:
    print_summary_of_test_results(test_results)


# IMPORTANT: You may NOT use the builtin   max   function
#   in your solution to the following problem.
def practice1h(numbers):
    """
    What comes in:
      A sequence of integers that are all >= 2.
    What goes out:
      Returns the largest of the numbers that:
        -- are prime, AND
        -- are at ODD INDICES of the sequence.
      Returns the string "bad" if there are NO such numbers in the sequence.
    Side effects: None.
    Examples:
      If the sequence is:
          [20, 12, 133, 11, 9, 13, 3, 99, 20, 5, 200]
      then the numbers at ODD indices are those at indices 1, 3, 5, 7, and 9:
           12     11     13     99     5
      and of these, only the following are prime:
           11     13     5
      and the largest of those is 13.
      So the function returns 13 in this example.

      If the sequence is:
          [13, 24, 3, 18, 3, 21]
      then the function returns the string "bad"
      since the numbers at ODD indices are those at indices 1, 3, and 5, namely:
          24    18    21
      and none of those numbers are prime.

      If the sequence is:
          [13]
      then the function returns the string "bad"
      since there are no items at odd indices in the sequence.

    Type hints:
      :type numbers: list[int] | tuple[int]
    """
    # -------------------------------------------------------------------------
    # TODO: 12. Implement and test this function.
    #     The testing code is already written for you (above).
    #  _
    #  IMPORTANT: You may NOT use the builtin   max   function
    #   in your solution to this problem.
    #  _
    #  ASK YOURSELF:
    #    1. Which of the following pattern(s) does this problem fit?
    #        COUNT-SUM-EXAMINE-ITEMS?
    #        FIND-ITEM?
    #        FIND-BEST?
    #        TWO-PLACES-AT-EACH-ITERATION?
    #        TWO-SEQUENCES-AT-EACH-ITERATION?
    #    2. Should the RANGE iterate through all of the sequence,
    #         or just part of it?  Forwards or backwards?
    #    3. Does the problem require building up a list? A string?
    #    4. Does it need just one loop, or more loop(s) after the first?
    #  ------------------------------------------------------------------------
    #  DIFFICULTY AND TIME RATINGS (see top of this file for explanation)
    #    DIFFICULTY:      7
    #    TIME ESTIMATE:   15 minutes.
    # -------------------------------------------------------------------------


def run_test_practice1i():
    """ Tests the    practice1i    function. """
    print()
    print("------------------------------------")
    print("Testing the   practice1i   function:")
    print("------------------------------------")

    format_string = "    practice1i( {} )"
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    expected = True
    sequence = [12, 33, 18, 'hello', 9, 13, 3, 9]
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice1i(sequence)
    print_actual_result_of_test(expected, actual, test_results)
    if actual == "True":
        print("  You returned the STRING 'True' instead of", color="red")
        print("  the boolean value True.", color="red")

    # Test 2:
    expected = False
    sequence = [12, 12, 33, 'hello', 5, 33, 5, 9]
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice1i(sequence)
    print_actual_result_of_test(expected, actual, test_results)
    if actual == "False":
        print("  You returned the STRING 'False' instead of", color="red")
        print("  the boolean value False.", color="red")

    # Test 3:
    expected = True
    sequence = (77, 112, 33, 'hello', 0, 43, 5, 77)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice1i(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 4:
    expected = False
    sequence = [1, 1, 1, 1, 1, 1, 2]
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice1i(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 5:
    expected = False
    sequence = ['aa', 'a']
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice1i(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 6:
    expected = True
    sequence = 'aaa'
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice1i(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 7:
    expected = True
    sequence = ['aa', 'a', 'b', 'a', 'b', 'a']
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice1i(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 8:
    expected = False
    sequence = [9]
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice1i(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 9:
    expected = True
    sequence = [12, 33, 18, 'hello', 9, 13, 3, 9]
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice1i(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 10:
    expected = False
    sequence = ['hello there', 'he', 'lo', 'hello']
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice1i(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 11:
    expected = False
    sequence = ((8,), '8', (4 + 4, 4 + 4), [8, 8], 7, 8)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice1i(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 12:
    expected = True
    sequence = [(8,), '8', [4 + 4, 4 + 4], (8, 8), 7, [8, 8]]
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice1i(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 13:
    expected = False
    sequence = [(8,), '8', [4 + 4, 4 + 4], [8, 8], 7, (8, 8)]
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice1i(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # SUMMARY of test results:
    print_summary_of_test_results(test_results)


def practice1i(sequence):
    """
    What comes in: A non-empty sequence.
    What goes out: Returns True if the last item of the sequence
      appears again somewhere else in the sequence.  Returns False otherwise.
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
      :type: sequence: list | tuple | str
    """
    # -------------------------------------------------------------------------
    # TODO: 13. Implement and test this function.
    #     The testing code is already written for you (above).
    #  _
    #  IMPLEMENTATION REQUIREMENT:  You are NOT allowed to use the
    #    'count' or 'index' methods for sequences in this problem
    #    (because here we want you to demonstrate your ability
    #    to use explicit looping).
    #  ------------------------------------------------------------------------
    #  ASK YOURSELF:
    #    1. Which of the following pattern(s) does this problem fit?
    #        COUNT-SUM-EXAMINE-ITEMS?
    #        FIND-ITEM?
    #        FIND-BEST?
    #        TWO-PLACES-AT-EACH-ITERATION?
    #        TWO-SEQUENCES-AT-EACH-ITERATION?
    #    2. Should the RANGE iterate through all of the sequence,
    #         or just part of it?  Forwards or backwards?
    #    3. Does the problem require building up a list? A string?
    #    4. Does it need just one loop, or more loop(s) after the first?
    #  ------------------------------------------------------------------------
    #  DIFFICULTY AND TIME RATINGS (see top of this file for explanation)
    #    DIFFICULTY:      5
    #    TIME ESTIMATE:   8 minutes.
    # -------------------------------------------------------------------------


def run_test_practice1j():
    """ Tests the   practice1j  function. """
    print()
    print("------------------------------------")
    print("Testing the   practice1j   function:")
    print("------------------------------------")

    format_string = "    practice1j( {} )"
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    expected = 'hBo'
    strings = ('hello', 'Bye', 'ok joe')
    print_expected_result_of_test([strings], expected, test_results,
                                  format_string)
    actual = practice1j(strings)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 2:
    expected = 'ABCD'
    strings = ('Alice', 'Bob', 'Carson', 'Devi')
    print_expected_result_of_test([strings], expected, test_results,
                                  format_string)
    actual = practice1j(strings)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 3:
    expected = 'to!'
    strings = ('', 'tricky', '', 'one, no?', '!')
    print_expected_result_of_test([strings], expected, test_results,
                                  format_string)
    actual = practice1j(strings)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 4:
    expected = 'mom'
    strings = ('my very long string', 'ok', 'mmmm')
    print_expected_result_of_test([strings], expected, test_results,
                                  format_string)
    actual = practice1j(strings)
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
    actual = practice1j(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # SUMMARY of test results:
    print_summary_of_test_results(test_results)


def practice1j(strings):
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
      :type strings: list[str] | tuple[str]
    """
    # -------------------------------------------------------------------------
    # TODO: 14. Implement and test this function.
    #     The testing code is already written for you (above).
    #  ASK YOURSELF:
    #    1. Which of the following pattern(s) does this problem fit?
    #        COUNT-SUM-EXAMINE-ITEMS?
    #        FIND-ITEM?
    #        FIND-BEST?
    #        TWO-PLACES-AT-EACH-ITERATION?
    #        TWO-SEQUENCES-AT-EACH-ITERATION?
    #    2. Should the RANGE iterate through all of the sequence,
    #         or just part of it?  Forwards or backwards?
    #    3. Does the problem require building up a list? A string?
    #    4. Does it need just one loop, or more loop(s) after the first?
    #  ------------------------------------------------------------------------
    #  DIFFICULTY AND TIME RATINGS (see top of this file for explanation)
    #    DIFFICULTY:      7
    #    TIME ESTIMATE:   10 minutes.
    # -------------------------------------------------------------------------


def run_test_practice1k():
    """ Tests the   practice1k  function. """
    print()
    print("------------------------------------")
    print("Testing the   practice1k   function:")
    print("------------------------------------")

    format_string = "    practice1k( {}, {} )"
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    expected = 4 * 8 * 4 * 1  # which is 128
    numbers = [5, 9, 4, 6, 1, 8, 2, 3, 4, 3, 2, 1, 8]
    start = 2
    print_expected_result_of_test([numbers, start], expected, test_results,
                                  format_string)
    actual = practice1k(numbers, start)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 2:
    expected = 1 * 3 * 2  # which is 6
    numbers = [5, 9, 4, 6, 1, 8, 2, 3, 4, 3, 2, 1, 8]
    start = 4
    print_expected_result_of_test([numbers, start], expected, test_results,
                                  format_string)
    actual = practice1k(numbers, start)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 3:
    expected = 5 * 6  # which is 30
    numbers = [5, 9, 4, 6]
    start = 0
    print_expected_result_of_test([numbers, start], expected, test_results,
                                  format_string)
    actual = practice1k(numbers, start)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 4:
    expected = 9
    numbers = [5, 9, 4, 6]
    start = 1
    print_expected_result_of_test([numbers, start], expected, test_results,
                                  format_string)
    actual = practice1k(numbers, start)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 5:
    expected = 1
    numbers = [5, 9, 4, 6]
    start = 4
    print_expected_result_of_test([numbers, start], expected, test_results,
                                  format_string)
    actual = practice1k(numbers, start)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 6:
    expected = 1
    numbers = []
    start = 0
    print_expected_result_of_test([numbers, start], expected, test_results,
                                  format_string)
    actual = practice1k(numbers, start)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 7:
    expected = 0
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
    start = 0
    print_expected_result_of_test([numbers, start], expected, test_results,
                                  format_string)
    actual = practice1k(numbers, start)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 8:
    expected = 1 * 4 * 7 * 10 * 13 * 16  # which is 58240
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
    start = 1
    print_expected_result_of_test([numbers, start], expected, test_results,
                                  format_string)
    actual = practice1k(numbers, start)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 9:
    expected = 12 * 15 * 18  # which is 3240
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
    start = 12
    print_expected_result_of_test([numbers, start], expected, test_results,
                                  format_string)
    actual = practice1k(numbers, start)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 10:
    expected = 13 * 16  # which is 208
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
    start = 13
    print_expected_result_of_test([numbers, start], expected, test_results,
                                  format_string)
    actual = practice1k(numbers, start)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 11:
    expected = 14 * 17  # which is 238
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
    start = 14
    print_expected_result_of_test([numbers, start], expected, test_results,
                                  format_string)
    actual = practice1k(numbers, start)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 12:
    expected = 15 * 18  # which is 270
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
    start = 15
    print_expected_result_of_test([numbers, start], expected, test_results,
                                  format_string)
    actual = practice1k(numbers, start)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 13:
    expected = 16
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
    start = 16
    print_expected_result_of_test([numbers, start], expected, test_results,
                                  format_string)
    actual = practice1k(numbers, start)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 14:
    expected = 17
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
    start = 17
    print_expected_result_of_test([numbers, start], expected, test_results,
                                  format_string)
    actual = practice1k(numbers, start)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 15:
    expected = 18
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
    start = 18
    print_expected_result_of_test([numbers, start], expected, test_results,
                                  format_string)
    actual = practice1k(numbers, start)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 16:
    expected = 1
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
    start = 19
    print_expected_result_of_test([numbers, start], expected, test_results,
                                  format_string)
    actual = practice1k(numbers, start)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 17:
    expected = 0
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    start = 9
    print_expected_result_of_test([numbers, start], expected, test_results,
                                  format_string)
    actual = practice1k(numbers, start)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 18:
    expected = 1 * 4 * 7 * 0  # which is 0
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    start = 0
    print_expected_result_of_test([numbers, start], expected, test_results,
                                  format_string)
    actual = practice1k(numbers, start)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 19:
    expected = 2 * 5 * 8  # which is 80
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    start = 1
    print_expected_result_of_test([numbers, start], expected, test_results,
                                  format_string)
    actual = practice1k(numbers, start)
    print_actual_result_of_test(expected, actual, test_results)

    # SUMMARY of test results:
    print_summary_of_test_results(test_results)


def practice1k(numbers, start):
    """
    What comes in:
      -- A sequence of numbers, plus a non-negative integer "start"
    What goes out:
      -- Returns the product of every 3rd number in the sequence,
           starting at the number at index "start".
      -- Returns 1 if the length of the list is less than or equal to "start".
    Side effects: None.
    Examples:
       practice1k( [5, 9, 4, 6, 1, 8, 2, 3, 4, 3, 2, 1, 8], 2 )
         starts at index 2 (i.e., the number 4] and does every 3rd from there,
         so returns  4 x 8 x 4 x 1, which is 128
       practice1k( [5, 9, 4, 6, 1, 8, 2, 3, 4, 3, 2, 1, 8], 4 )
         returns  1 x 3 x 2, which is 6
       practice1k( [5, 9, 4, 6], 0 )  returns  5 x 6, which is 30
       practice1k( [5, 9, 4, 6], 1 )  returns  9
       practice1k( [5, 9, 4, 6], 4 )  returns  1
    Type hints:
      :type numbers: list[int]
      :type start: int
    """
    # -------------------------------------------------------------------------
    # TODO: 15. Implement and test this function.
    #     The testing code is already written for you (above).
    #  ASK YOURSELF:
    #    1. Which of the following pattern(s) does this problem fit?
    #        COUNT-SUM-EXAMINE-ITEMS?
    #        FIND-ITEM?
    #        FIND-BEST?
    #        TWO-PLACES-AT-EACH-ITERATION?
    #        TWO-SEQUENCES-AT-EACH-ITERATION?
    #    2. Should the RANGE iterate through all of the sequence,
    #         or just part of it?  Forwards or backwards?
    #    3. Does the problem require building up a list? A string?
    #    4. Does it need just one loop, or more loop(s) after the first?
    #  ------------------------------------------------------------------------
    #  DIFFICULTY AND TIME RATINGS (see top of this file for explanation)
    #    DIFFICULTY:      4
    #    TIME ESTIMATE:   5 minutes.
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
