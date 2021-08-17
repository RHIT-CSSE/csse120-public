"""
This module lets you practice various patterns
for ITERATING through SEQUENCES, including selections from:
  -- Beginning to end
  -- Other ranges (e.g., backwards and every-3rd-item)
  -- The COUNT/SUM/etc pattern
  -- The FIND pattern (via LINEAR SEARCH)
  -- The MAX/MIN pattern
  -- Looking two places in the sequence at once
  -- Looking at two sequences in parallel
plus practice at:
  -- BUILDING a LIST via a loop
  -- BUILDING a STRING via a loop

Authors: David Mutchler, Vibha Alangar, Dave Fisher, Matt Boutell, Mark Hays,
         Mohammed Noureddine, Sana Ebrahimi, Sriram Mohan, their colleagues and
         PUT_YOUR_NAME_HERE.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

import testing_helper
import time
import rosegraphics as rg
import math


def main():
    """ Calls the   TEST   functions in this module. """

    # -------------------------------------------------------------------------
    # STUDENTS: Do the work in this module as follows.
    #   Otherwise, you will be overwhelmed by the output.
    #
    #   For each function that you implement:
    #     1. Locate the statements just below this comment
    #          that call TEST functions.
    #     2. UN-comment only one test at a time.
    #     3. Implement that function per its _TODO_.
    #     4. When satisfied with your work, move onto the next test,
    #        RE-commenting out the previous test to reduce the output.
    # -------------------------------------------------------------------------

    print("-----------------------------------------------")
    print("Un-comment each of the following TEST functions")
    print("as you implement the functions that they test.")
    print("-----------------------------------------------")
    # run_test_sum_at_even()
    # run_test_smallest_index_where_zero()
    # run_test_multiply_x_coordinates()
    # run_test_count_same()
    # run_test_has_stutters()
    # run_test_shortest_string()
    # run_test_is_palindrome()
    # run_test_make_even_numbers()
    # run_test_make_concatenation()


def run_test_sum_at_even():
    """ Tests the    sum_at_even    function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   sum_at_even  function:')
    print('--------------------------------------------------')

    format_string = '    sum_at_even( {} )'
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    expected = 161
    sequence = (12, 33, 18, 9, 13, 3, 99, 20, 19, 20)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = sum_at_even(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 2:
    expected = 29
    sequence = (3, 12, 10, 8, 8, 9, 8, 11)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = sum_at_even(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 3:
    expected = -9999999999
    sequence = (-9999999999, 8888888888)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = sum_at_even(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 4:
    expected = 8888888888
    sequence = (8888888888, -9999999999)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = sum_at_even(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 5:
    expected = -176
    sequence = (-77, 20000, -33, 40000, -55, 60000, -11)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = sum_at_even(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 6:
    expected = 0
    sequence = ()
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = sum_at_even(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 7:
    expected = 0
    sequence = []
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = sum_at_even(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 8:
    expected = 8
    sequence = [8]
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = sum_at_even(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 9:
    expected = -77
    sequence = (-77, 8)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = sum_at_even(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 10:
    expected = 0
    sequence = (-77, 8, 77)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = sum_at_even(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 11:
    expected = 1
    sequence = (-77, 8, 78)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = sum_at_even(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 12:
    expected = 1
    sequence = (-77, 8, 78, 100)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = sum_at_even(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # SUMMARY of test results:
    print_summary_of_test_results(test_results)


def sum_at_even(sequence):
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
    # TODO: 2. Implement and test this function.
    #     The testing code is already written for you (above).
    # -------------------------------------------------------------------------


def run_test_smallest_index_where_zero():
    """ Tests the    smallest_index_where_zero    function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   smallest_index_where_zero  function:')
    print('--------------------------------------------------')

    format_string = '    smallest_index_where_zero( {} )'
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    expected = 1
    sequence = (9, 0, 8, 0, 0, 4, 4, 0)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = smallest_index_where_zero(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 2:
    expected = 4
    sequence = (9, 9, 9, 9, 0, 9, 9, 9)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = smallest_index_where_zero(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 3:
    expected = -1
    sequence = (4, 5, 4, 5, 4, 5, 4)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = smallest_index_where_zero(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 4:
    expected = 0
    sequence = [0, 0, 0]
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = smallest_index_where_zero(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 5:
    expected = 0
    sequence = [0, 0]
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = smallest_index_where_zero(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 6:
    expected = 0
    sequence = [0, 77]
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = smallest_index_where_zero(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 7:
    expected = 1
    sequence = [-40, 0]
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = smallest_index_where_zero(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 8:
    expected = -1
    sequence = [-40, 67]
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = smallest_index_where_zero(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 9:
    expected = 1
    sequence = (1, 0, 2, 0, 0, 0, 0, 6, 9, 0, 0, 12)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = smallest_index_where_zero(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # SUMMARY of test results:
    print_summary_of_test_results(test_results)


def smallest_index_where_zero(sequence):
    """
    What comes in: A sequence of integers.
    What goes out: Returns the first (leftmost) place (index)
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


def run_test_multiply_x_coordinates():
    """ Tests the    multiply_x_coordinates    function. """
    print()
    print("--------------------------------------------------")
    print("Testing the   multiply_x_coordinates  function:")
    print("--------------------------------------------------")

    format_string = "    multiply_x_coordinates( {} )"
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    expected = 5 * 2 * 7 * 10 * 2  # which is 1400
    circles = (rg.Circle(rg.Point(5, 10), 20),
               rg.Circle(rg.Point(2, 20), 20),
               rg.Circle(rg.Point(7, 30), 10),
               rg.Circle(rg.Point(10, 40), 20),
               rg.Circle(rg.Point(2, 50), 10))
    print_expected_result_of_test([circles], expected, test_results,
                                  format_string)
    actual = multiply_x_coordinates(circles)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 2:
    expected = 58
    circles = (rg.Circle(rg.Point(58, 10), 20),)
    print_expected_result_of_test([circles], expected, test_results,
                                  format_string)
    actual = multiply_x_coordinates(circles)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 3:
    expected = 84 * 28 * 10005  # which is 23531760
    circles = (rg.Circle(rg.Point(84, 100), 200),
               rg.Circle(rg.Point(28, 200), 200),
               rg.Circle(rg.Point(10005, 300), 100))
    print_expected_result_of_test([circles], expected, test_results,
                                  format_string)
    actual = multiply_x_coordinates(circles)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 4:
    expected = 1
    circles = ()
    print_expected_result_of_test([circles], expected, test_results,
                                  format_string)
    actual = multiply_x_coordinates(circles)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 5:
    expected = 5 * 0 * 7 * 10 * 2  # which is 0
    circles = (rg.Circle(rg.Point(5, 10), 20),
               rg.Circle(rg.Point(0, 20), 20),
               rg.Circle(rg.Point(7, 30), 10),
               rg.Circle(rg.Point(10, 40), 20),
               rg.Circle(rg.Point(2, 50), 10))

    print_expected_result_of_test([circles], expected, test_results,
                                  format_string)
    actual = multiply_x_coordinates(circles)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 6:
    circles = ()
    for k in range(1, 101):
        circles = circles + (rg.Circle(rg.Point(k, k + 20), 5 * k),)
    expected = math.factorial(100)
    print_expected_result_of_test([circles], expected, test_results,
                                  format_string)
    actual = multiply_x_coordinates(circles)
    print_actual_result_of_test(expected, actual, test_results)

    # SUMMARY of test results:
    print_summary_of_test_results(test_results)


def multiply_x_coordinates(circles):
    """
    What comes in:  A sequence of rg.Circles.
    What goes out:  Returns the product of the x-coordinates
      of the centers of the rg.Circles.
      Returns 1 if the given sequence is empty.
    Side effects: None.
    Examples:
      If the sequence is a list containing these 5 rg.Circles:
        rg.Circle(rg.Point(5, 10), 20)
        rg.Circle(rg.Point(2, 20), 20)
        rg.Circle(rg.Point(7, 30), 10)
        rg.Circle(rg.Point(10, 40), 20)
        rg.Circle(rg.Point(2, 50), 10)
      then this function returns:
        5 x 2 x 7 x 10 x 2, which is 1400.
    Type hints:
      :type circles: tuple[rg.Circle]
    """
    # -------------------------------------------------------------------------
    # TODO: 4. Implement and test this function.
    #     The testing code is already written for you (above).
    #  ------------------------------------------------------------------------


def run_test_count_same():
    """ Tests the   count_same   function. """
    print()
    print("--------------------------------------------------")
    print("Testing the   count_same   function:")
    print("--------------------------------------------------")

    format_string = "    count_same ( {} )"
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    expected = 3
    sequence1 = (11, 33, 83, 18, 30, 55)
    sequence2 = (99, 33, 83, 19, 30, 44)
    print_expected_result_of_test([sequence1, sequence2], expected,
                                  test_results, format_string)
    actual = count_same(sequence1, sequence2)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 2:
    expected = 8
    sequence1 = "how are you today?"
    sequence2 = "HOW? r ex u tiday?"
    print_expected_result_of_test([sequence1, sequence2], expected,
                                  test_results, format_string)
    actual = count_same(sequence1, sequence2)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 3:
    expected = 1
    sequence1 = [1, 44, 55]
    sequence2 = [0, 44, 77]
    print_expected_result_of_test([sequence1, sequence2], expected,
                                  test_results, format_string)
    actual = count_same(sequence1, sequence2)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 4:
    expected = 2
    sequence1 = (1, 44, 55, 88, 44, 88)
    sequence2 = (1, 55, 44, 55, 88, 88)
    print_expected_result_of_test([sequence1, sequence2], expected,
                                  test_results, format_string)
    actual = count_same(sequence1, sequence2)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 5:
    expected = 0
    sequence1 = [1, 44, 55, 88, 44]
    sequence2 = [0, 43, 77, 8, 4]
    print_expected_result_of_test([sequence1, sequence2], expected,
                                  test_results, format_string)
    actual = count_same(sequence1, sequence2)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 6:
    expected = 0
    sequence1 = []
    sequence2 = []
    print_expected_result_of_test([sequence1, sequence2], expected,
                                  test_results, format_string)
    actual = count_same(sequence1, sequence2)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 7:
    expected = 2
    sequence1 = "ok"
    sequence2 = "ok"
    print_expected_result_of_test([sequence1, sequence2], expected,
                                  test_results, format_string)
    actual = count_same(sequence1, sequence2)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 8:
    expected = 1
    sequence1 = "ox"
    sequence2 = "ok"
    print_expected_result_of_test([sequence1, sequence2], expected,
                                  test_results, format_string)
    actual = count_same(sequence1, sequence2)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 9:
    expected = 1
    sequence1 = "ok"
    sequence2 = "xk"
    print_expected_result_of_test([sequence1, sequence2], expected,
                                  test_results, format_string)
    actual = count_same(sequence1, sequence2)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 10:
    expected = 1
    sequence1 = "o"
    sequence2 = "o"
    print_expected_result_of_test([sequence1, sequence2], expected,
                                  test_results, format_string)
    actual = count_same(sequence1, sequence2)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 11:
    expected = 0
    sequence1 = "y"
    sequence2 = "n"
    print_expected_result_of_test([sequence1, sequence2], expected,
                                  test_results, format_string)
    actual = count_same(sequence1, sequence2)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 12:
    expected = 20
    sequence1 = "12345678901234567890"
    sequence2 = "12345678901234567890"
    print_expected_result_of_test([sequence1, sequence2], expected,
                                  test_results, format_string)
    actual = count_same(sequence1, sequence2)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 13:
    expected = 19
    sequence1 = "12345678901234567890"
    sequence2 = "1234567890123456789z"
    print_expected_result_of_test([sequence1, sequence2], expected,
                                  test_results, format_string)
    actual = count_same(sequence1, sequence2)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 14:
    expected = 18
    sequence1 = "12345678901234567890"
    sequence2 = "z234567890123456789z"
    print_expected_result_of_test([sequence1, sequence2], expected,
                                  test_results, format_string)
    actual = count_same(sequence1, sequence2)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 15:
    expected = 0
    sequence1 = "12345678901234567890"
    sequence2 = "23456789012345678901"
    print_expected_result_of_test([sequence1, sequence2], expected,
                                  test_results, format_string)
    actual = count_same(sequence1, sequence2)
    print_actual_result_of_test(expected, actual, test_results)

    # SUMMARY of test results:
    print_summary_of_test_results(test_results)


def count_same(sequence1, sequence2):
    """
    What comes in:
      -- two sequences that have the same length
    What goes out: Returns the number of indices at which the two
      given sequences have the same item at that index.
    Side effects: None.
    Examples:
      If the sequences are:
          (11, 33, 83, 18, 30, 55)
          (99, 33, 83, 19, 30, 44)
      then this function returns  3
      since the two sequences have the same item at:
        -- index 1 (both are 33)
        -- index 2 (both are 83)
        -- index 4 (both are 30)

      Another example:  if the sequences are:
          "how are you today?"
          "HOW? r ex u tiday?"
      then this function returns  8  since the sequences are the same
      at indices 5 (both are "r"), 10 (both are "u"), 11 (both are " "),
      12 (both are "t"), 14 (both are "d"), 15 (both are "a"),
      16 (both are "y") and 17 (both are "?") -- 8 indices.
    Type hints:
      type: sequence1: tuple or list or string
      type: sequence2: tuple or list or string
    """
    # -------------------------------------------------------------------------
    # TODO: 5. Implement and test this function.
    #     The testing code is already written for you (above).
    # -------------------------------------------------------------------------


def run_test_has_stutters():
    """ Tests the   has_stutters   function. """
    print()
    print("--------------------------------------------------")
    print("Testing the   has_stutters   function:")
    print("--------------------------------------------------")

    format_string = "    has_stutters ( {} )"
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    expected = True
    sequence = "xhhbrrs"
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = has_stutters(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 2:
    expected = True
    sequence = "xxxx"
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = has_stutters(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 3:
    expected = False
    sequence = "xaxaxa"
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = has_stutters(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 4:
    expected = True
    sequence = "xxx yyy xxxx"
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = has_stutters(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 5:
    expected = True
    sequence = "xxx xxx xxxx"
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = has_stutters(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 6:
    expected = True
    sequence = "xxxyyyxxxx"
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = has_stutters(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 7:
    expected = False
    sequence = ""
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = has_stutters(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 8:
    expected = False
    sequence = "x x x x x x x x x x x x"
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = has_stutters(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 9:
    expected = True
    sequence = "x x x x x x x x x x x xx"
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = has_stutters(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 10:
    expected = True
    sequence = "xx x x x x x x x x x x x"
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = has_stutters(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 11:
    expected = True
    sequence = "x x x xx x x x x x x x x"
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = has_stutters(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 12:
    expected = False
    sequence = "ababcabcdabcde"
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = has_stutters(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 13:
    expected = False
    sequence = "a"
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = has_stutters(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 14:
    expected = False
    sequence = "ba"
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = has_stutters(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 15:
    expected = False
    sequence = "bab"
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = has_stutters(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # SUMMARY of test results:
    print_summary_of_test_results(test_results)


def has_stutters(s):
    """
    What comes in:
      -- a string s
    What goes out: Returns True if a letter is repeated
      twice-in-a-row in the given string s, else returns False.
    Side effects: None.
    Examples:
      -- has_stutters("xhhbrrs")  returns True
      -- has_stutters("xxxx")     returns True
      -- has_stutters("xaxaxa")   returns False
      -- has_stutters("xxx yyy xxxx")  returns True
      -- has_stutters("xxxyyyxxxx")    returns True
      -- has_stutters("")  returns False
    Type hints:
       :type s: str
    """
    # -------------------------------------------------------------------------
    # TODO: 6. Implement and test this function.
    #     The testing code is already written for you (above).
    # -------------------------------------------------------------------------


def run_test_shortest_string():
    """ Tests the   shortest_string   function. """
    print()
    print("--------------------------------------------------")
    print("Testing the   shortest_string   function:")
    print("--------------------------------------------------")

    format_string = "    shortest_string ( {} )"
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    expected = "a"
    sequence = ("all", "we", "are", "saying",
                "is", "give", "peace", "a", "chance")
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = shortest_string(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 2:
    expected = "we"
    sequence = ("all", "we", "are", "saying",
                "is", "give", "peace", "a chance")
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = shortest_string(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 3:
    expected = "is"
    sequence = ("all we", "are saying",
                "is", "give", "peace", "a chance")
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = shortest_string(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 4:
    expected = "all we are saying is give peace a chance"
    sequence = ("all we are saying is give peace a chance",)
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = shortest_string(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 5:
    expected = "a"
    sequence = ("a", "c", "b")
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = shortest_string(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 6:
    expected = "c"
    sequence = ("ab", "c", "b")
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = shortest_string(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 7:
    expected = "b"
    sequence = ("ab", "cd", "b")
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = shortest_string(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 8:
    expected = "a"
    sequence = ("a", "c", "b")
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = shortest_string(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 9:
    expected = ""
    sequence = ("a", "b", "")
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = shortest_string(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 10:
    expected = "bb"
    sequence = ("00000", "aaa", "bb", "cccccc", "dddd", "eee")
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = shortest_string(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 11:
    expected = "11"
    sequence = ("00000", "aaa", "11", "cccccc", "dddd", "eee", "bb")
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = shortest_string(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # SUMMARY of test results:
    print_summary_of_test_results(test_results)


def shortest_string(strings):
    """
    What comes in:
      -- a non-empty sequence of strings
    What goes out: Returns the shortest string in the given sequence
    of strings.  If there is a tie for shortest string, returns the one
    (among the ties) whose index is smallest.
    Side effects: None.
    Examples:
      If the argument is:
        ["all", "we",  "are saying", "is", "give", "peace", "a chance"]
      then this function returns  "we"

      If the argument is:
        ["all we",  "are saying", "is give", "peace", "a chance"]
      then this function returns  "peace"

      If the argument is:
        ["all we are saying", "is give", "peace a chance"]
      then this function returns  "is give"

      If the argument is ["abc"], then this function returns  "abc".
    Type hints:
      :type strings: list[str]   or tuple(str)
    """
    # -------------------------------------------------------------------------
    # TODO: 7. Implement and test this function.
    #     The testing code is already written for you (above).
    # -------------------------------------------------------------------------


def run_test_is_palindrome():
    """ Tests the   is_palindrome   function. """
    print()
    print("--------------------------------------------------")
    print("Testing the   is_palindrome   function:")
    print("--------------------------------------------------")

    format_string = "    is_palindrome ( {} )"
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    expected = True
    sequence = "abba"
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = is_palindrome(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 2:
    expected = False
    sequence = "abbz"
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = is_palindrome(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 3:
    expected = True
    sequence = "abcdexxedcba"
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = is_palindrome(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 4:
    expected = False
    sequence = "abcdexyedcba"
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = is_palindrome(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 5:
    expected = True
    sequence = "bob"
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = is_palindrome(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 6:
    expected = True
    sequence = "obbo"
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = is_palindrome(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 7:
    expected = True
    sequence = "obbo"
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = is_palindrome(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 8:
    expected = False
    sequence = "nope"
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = is_palindrome(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 9:
    expected = False
    sequence = "almosttxomla"
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = is_palindrome(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 10:
    expected = False
    sequence = "abcxa"
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = is_palindrome(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 11:
    expected = False
    sequence = "abccxa"
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = is_palindrome(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 12:
    expected = False
    sequence = "aaaabcccccxaaaa"
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = is_palindrome(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 13:
    # This one would normally be written:
    #      Murder for a jar of red rum
    # It IS a palindrome (ignoring spaces and punctuation).
    expected = True
    sequence = "murderforajarofredrum"
    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = is_palindrome(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # SUMMARY of test results:
    print_summary_of_test_results(test_results)


def is_palindrome(s):
    """
    What comes in:
      -- a string s that (in this simple version of the palindrome
           problem) contains only lower-case letters
           (no spaces, no punctuation, no upper-case characters)
    What goes out: Returns  True  if the given string s is a palindrome,
      i.e., reads the same backwards as forwards.
      Returns  False  if the given string s is not a palindrome.
    Side effects: None.
    Examples:
       abba  reads backwards as   abba   so it IS a palindrome
    but
       abbz  reads backwards as   zbba   so it is NOT a palindrome

    Here are two more examples:  (Note: I have put spaces into the
    strings for readability; the real problem is the string WITHOUT
    the spaces.)
       a b c d e x x e d c b a  reads backwards as
       a b c d e x x e d c b a
         so it IS a palindrome
     but
       a b c d e x y e d c b a  reads backwards as
       a b c d e y x e d c b a
         so it is NOT a palindrome
    Type hints:
      :type s: str
    """
    # -------------------------------------------------------------------------
    # TODO: 8. Implement and test this function.
    #     The testing code is already written for you (above).
    #  ___
    #  ########################################################################
    #   IMPORTANT:  As with ALL problems, work a concrete example BY HAND
    #   to figure out how to solve this problem.  The last two examples
    #   above are particularly good examples to work by hand.
    #  ########################################################################
    # -------------------------------------------------------------------------


def run_test_make_even_numbers():
    """ Tests the   make_even_numbers   function. """
    print()
    print("--------------------------------------------------")
    print("Testing the   make_even_numbers   function:")
    print("--------------------------------------------------")

    format_string = "    make_even_numbers ( {} )"
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    expected = [2, 4, 6, 8]
    print_expected_result_of_test([4], expected, test_results, format_string)
    actual = make_even_numbers(4)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 2:
    expected = [2, 4, 6, 8, 10, 12, 14]
    print_expected_result_of_test([7], expected, test_results, format_string)
    actual = make_even_numbers(7)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 3:
    expected = []
    print_expected_result_of_test([0], expected, test_results, format_string)
    actual = make_even_numbers(0)
    print_actual_result_of_test(expected, actual, test_results)

    print_summary_of_test_results(test_results)

    # Test 4:
    expected = [2]
    print_expected_result_of_test([1], expected, test_results, format_string)
    actual = make_even_numbers(1)
    print_actual_result_of_test(expected, actual, test_results)

    print_summary_of_test_results(test_results)


def make_even_numbers(n):
    """
    What comes in:  A non-negative integer n.
    What goes out: Returns the list   [2, 4, 6, 8, 10, 12, ... 2n]
      for the given n.
    Side effects: None.
    Examples:
      -- make_even_numbers(4) returns the list:  [2, 4, 6, 8]
      -- make_even_numbers(7) returns the list:  [2, 4, 6, 8, 10, 12, 14]
      -- make_even_numbers(0) returns the list:  []  (the empty list)
    Type hints:
      :type n: int
    """
    # -------------------------------------------------------------------------
    # TODO: 9. Implement and test this function.
    #     The testing code is already written for you (above).
    # -------------------------------------------------------------------------


def run_test_make_concatenation():
    """ Tests the   make_concatenation   function. """
    print()
    print("--------------------------------------------------")
    print("Testing the   make_concatenation   function:")
    print("--------------------------------------------------")

    format_string = "    make_concatenation ( {} )"
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    expected = "GivePeaceAChance"
    strings = ["Give", "Peace", "A", "Chance"]
    print_expected_result_of_test([strings], expected, test_results,
                                  format_string)
    actual = make_concatenation(strings)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 2:
    expected = "HelloGoodbyeHere andThere"
    strings = ["Hello", "Goodbye", "Here and", "There"]
    print_expected_result_of_test([strings], expected, test_results,
                                  format_string)
    actual = make_concatenation(strings)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 3:
    expected = "I love that hat."
    strings = ["I ", "love ", "that hat."]
    print_expected_result_of_test([strings], expected, test_results,
                                  format_string)
    actual = make_concatenation(strings)
    print_actual_result_of_test(expected, actual, test_results)

    print_summary_of_test_results(test_results)

    # Test 4:
    expected = ""
    strings = []
    print_expected_result_of_test([strings], expected, test_results,
                                  format_string)
    actual = make_concatenation(strings)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 5:
    expected = ""
    strings = ["", "", ""]
    print_expected_result_of_test([strings], expected, test_results,
                                  format_string)
    actual = make_concatenation(strings)
    print_actual_result_of_test(expected, actual, test_results)

    # SUMMARY of test results:
    print_summary_of_test_results(test_results)


def make_concatenation(strings):
    """
    What comes in: A sequence of strings.
    What goes out: Returns the "concatenation" of all the strings,
      that is, returns a single string that is all of the strings
      "stiched together".  See examples.
    Side effects: None.
    Examples:
      -- make_concatenation(["Give",
                             "Peace",
                             "A",
                             "Chance"])
             returns "GivePeaceAChance"
      -- make_concatenation(["Hello", "Goodbye", "Here and", "There"])
            returns    "HelloGoodbyeHere andThere"
      -- make_concatenation(["I ", "love ", "that hat."])
            returns    "I love that hat."
      -- make_concatenation([])   returns  ""  (the empty string)
      -- make_concatenation(["", "", ""])   returns   ""  (the empty string)
    Type hints:
      :type strings: list[str]
    """
    # -------------------------------------------------------------------------
    # TODO: 10. Implement and test this function.
    #     The testing code is already written for you (above).
    #   HINT: The   +    operator concatenates ("stiches together")
    #   any two strings.
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
