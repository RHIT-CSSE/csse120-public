"""
This project lets you practice NESTED LOOPS (i.e., loops within loops)
in the context of SEQUENCES OF SUB-SEQUENCES.

Authors: David Mutchler, Vibha Alangar, Dave Fisher, Matt Boutell, Mark Hays,
         Mohammed Noureddine, Sana Ebrahimi, Sriram Mohan, their colleagues and
         PUT_YOUR_NAME_HERE.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

import time
import testing_helper


def main():
    """ Calls the other functions to test them. """
    print("-----------------------------------------------")
    print("Un-comment each of the following TEST functions")
    print("as you implement the functions that they test.")
    print("-----------------------------------------------")

    # run_test_sum_numbers()
    # run_test_multiply_by_c()


def run_test_sum_numbers():
    """ Tests the    sum_numbers    function. """
    # -------------------------------------------------------------------------
    # TODO: 2. Implement this TEST function.
    #   It TESTS the  sum_numbers  function defined below.
    #   Include at least **   4   ** tests (we wrote 3 for you).
    # -------------------------------------------------------------------------
    print()
    print("--------------------------------------------------")
    print("Testing the   sum_numbers   function:")
    print("--------------------------------------------------")

    format_string = "    sum_numbers( {} )"
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    expected = 38
    print_expected_result_of_test([[(3, 1, 4), (10, 10), [1, 2, 3, 4]]],
                                  expected, test_results, format_string)
    actual = sum_numbers([(3, 1, 4),
                          (10, 10),
                          [1, 2, 3, 4]])
    print_actual_result_of_test(expected, actual, test_results)

    # Test 2:
    expected = 5
    print_expected_result_of_test([([], [5], [])],
                                  expected, test_results, format_string)
    actual = sum_numbers(([], [5], []))
    print_actual_result_of_test(expected, actual, test_results)

    # Test 3:
    expected = 105
    print_expected_result_of_test([[(5, 0, 4), (10,), (), (8, 3, 2, 10, 10),
                                    (3, 5), (1, 2, 3, 4, 5, 6, 7, 8, 9)]],
                                  expected, test_results, format_string)
    actual = sum_numbers([(5, 0, 4),
                          (10,),
                          (),
                          (8, 3, 2, 10, 10),
                          (3, 5),
                          (1, 2, 3, 4, 5, 6, 7, 8, 9)])
    print_actual_result_of_test(expected, actual, test_results)

    # -------------------------------------------------------------------------
    # TODO: 2 (continued): Add your ADDITIONAL test here:
    # -------------------------------------------------------------------------

    # SUMMARY of test results:
    print_summary_of_test_results(test_results)


def sum_numbers(seq_seq):
    """
    Returns the sum of the numbers in the given sequence
    of subsequences.  For example, if the given argument is:
        [(3, 1, 4), (10, 10), [1, 2, 3, 4]]
    then this function returns    38
    (which is 3 + 1 + 4 + 10 + 10 + 1 + 2 + 3 + 4).
    Preconditions:  the given argument is a sequences of sequences,
                    and each item in the subsequences is a number.
    """
    # -------------------------------------------------------------------------
    # TODO: 3. Implement and test this function.
    #   Note that you should write its TEST function first (above).
    #  __
    #  NOTE: This is a classic SEQUENCE of SEQUENCES problem:
    #        -- Each loop is simply the pattern you have seen many times.
    #        -- But INSIDE the OUTER loop and BEFORE the INNER loop,
    #             you can "extract" the current (OUTER loop) SUB-list
    #             to loop through it in the INNER loop.
    #        -- See   m2r_nested_loops_in_sequences   as needed.
    # -------------------------------------------------------------------------


def run_test_multiply_by_c():
    """ Tests the   multiply_by_c   function. """
    # -------------------------------------------------------------------------
    # We have supplied tests for you. No additional tests are required,
    # although you are welcome to supply more tests if you choose.
    # -------------------------------------------------------------------------
    print()
    print("------------------------------------------------------")
    print("Testing the   multiply_by_c   function:")
    print("------------------------------------------------------")

    format_string = "    multiply_by_c( {}, {} )"
    test_results = [0, 0]  # Number of tests passed, failed.

    # -------------------------------------------------------------------------
    # Test 1: Tests whether the function MUTATES the sub-lists correctly.
    seq_of_lists = ([10, 3, 101], [8, 0])
    c = 3  # Each number in each sub-list should be multiplied by this
    # After the function call, seq_of_lists should be as follows:
    expected = ([30, 9, 303], [24, 0])
    print_expected_result_of_test([c, seq_of_lists], expected,
                                  test_results, format_string)
    actual = multiply_by_c(c,
                           seq_of_lists)
    print_actual_result_of_test(expected, seq_of_lists, test_results)
    print("The above is for  seq_of_lists  (whose lists should be MUTATED.")

    # Test 2: (a continuation of Test 1)
    #   Tests whether the function does not RETURN a value (i.e., returns None)
    print_expected_result_of_test([c, seq_of_lists], None,
                                  test_results, format_string)
    print_actual_result_of_test(None, actual, test_results)
    print("The above is for the RETURNED VALUE, which should be")
    print("the constant None, NOT the STRING \"None\".")
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # Test 3: Tests whether the function MUTATES the sub-lists correctly.
    seq_of_lists = ([4, 2, 1], [8, 0], [1, 2, 3, 4, 5], [], [101])
    c = 2  # Each number in each sub-list should be multiplied by this
    # After the function call, seq_of_lists should be as follows:
    expected = ([8, 4, 2], [16, 0], [2, 4, 6, 8, 10], [], [202])
    print_expected_result_of_test([c, seq_of_lists], expected,
                                  test_results, format_string)
    actual = multiply_by_c(c,
                           seq_of_lists)
    print_actual_result_of_test(expected, seq_of_lists, test_results)
    print("The above is for  seq_of_lists  (whose lists should be MUTATED.")

    # Test 4: (a continuation of Test 3)
    #   Tests whether the function does not RETURN a value (i.e., returns None)
    print_expected_result_of_test([c, seq_of_lists], None,
                                  test_results, format_string)
    print_actual_result_of_test(None, actual, test_results)
    print("The above is for the RETURNED VALUE, which should be")
    print("the constant None, NOT the STRING \"None\".")
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # Test 5: Tests whether the function MUTATES the sub-lists correctly.
    seq_of_lists = [[], [1], [20, 2, 30, 4, 100, 8, 2, 2, 2], [], [300],
                    [5, 5], [], [-10, 4]]
    c = 100  # Each number in each sub-list should be multiplied by this
    # After the function call, seq_of_lists should be as follows:
    expected = [[], [100], [2000, 200, 3000, 400, 10000, 800, 200, 200, 200],
                [], [30000], [500, 500], [], [-1000, 400]]
    print_expected_result_of_test([c, seq_of_lists], expected,
                                  test_results, format_string)
    actual = multiply_by_c(c,
                           seq_of_lists)
    print_actual_result_of_test(expected, seq_of_lists, test_results)
    print("The above is for  seq_of_lists  (whose lists should be MUTATED.")

    # Test 6: (a continuation of Test 5)
    #   Tests whether the function does not RETURN a value (i.e., returns None)
    print_expected_result_of_test([c, seq_of_lists], None,
                                  test_results, format_string)
    print_actual_result_of_test(None, actual, test_results)
    print("The above is for the RETURNED VALUE, which should be")
    print("the constant None, NOT the STRING \"None\".")
    # -------------------------------------------------------------------------

    # SUMMARY of test results:
    print_summary_of_test_results(test_results)


def multiply_by_c(c, sequence_of_lists):
    """
     What comes in:
       -- a number c
       -- a sequence of lists, with each item in the lists being a number
     What goes out: Nothing (i.e. None).
     Side effects: MUTATES the given lists by multiplying
       each item in the lists by the given number c.
       For example, consider the following code:
          seq_of_lists = ([4, 2, 1], [8, 0], [1, 2, 3, 4, 5], [], [101])
          v = multiply_by_c(2,
                            seq_of_lists)
       After the above code runs,
          v (the returned value) should be None
          and  seq_of_lists  should be:
                       ([8, 4, 2], [16, 0], [2, 4, 6, 8, 10], [], [202]).
     Type hints:
       :type: c: float
       :type sequence_of_lists:  sequence of lists of numbers
       """
    # -------------------------------------------------------------------------
    # TODO: 4. Implement and test this function.
    #  ** READ THE TESTS that have been written for you (ABOVE).
    #  ** ASK QUESTIONS if you do not understand the TESTS (ABOVE).
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
