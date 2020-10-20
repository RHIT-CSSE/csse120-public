"""
PRACTICE Exam 3.

This problem provides practice at:
  ***  MUTATING  and  RETURNING-NEW  LISTS.  ***

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Mark Hays, Amanda Stouder, Derek Whitley, their colleagues,
         and PUT_YOUR_NAME_HERE.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

###############################################################################
# TODO: 2.  [Note: same _TODO_ as its matching one in module m1.]
#  Students:
#  __
#  These problems have DIFFICULTY and TIME ratings:
#    DIFFICULTY rating:  1 to 10, where:
#       1 is very easy
#       3 is an "easy" Exam 3 question.
#       5 is a "typical" Exam 3 question.
#       7 is a "hard" Exam 3 question.
#      10 is an EXTREMELY hard problem (too hard for a Exam 3 question)
#  __
#    TIME ratings: A ROUGH estimate of the number of minutes that we
#       would expect a well-prepared student to take on the problem.
#  __
#    IMPORTANT: For ALL the problems in this module,
#      if you reach the time estimate and are NOT close to a solution,
#      STOP working on that problem and ASK YOUR INSTRUCTOR FOR HELP on it,
#      in class or via Piazza.
#  __
#  After you read (and understand) the above, change this _TODO_ to DONE.
###############################################################################

import time
import testing_helper


def main():
    """ Calls the   TEST   functions in this module. """
    run_test_doubler()
    run_test_zero_changer()


def run_test_doubler():
    """ Tests the    doubler    function. """
    # -------------------------------------------------------------------------
    # TODO: 3. READ the tests that we supplied in this function, asking
    #  questions as needed.  Once you UNDERSTAND the tests that we supplied,
    #  ADD ANOTHER ** GOOD ** TEST of your own for the  doubler  function,
    #  using the same style for testing as we did.
    #  __
    #   Try to choose a test that might expose errors in your code!
    #  __
    #   As usual, compute the EXPECTED result BY HAND
    #   (not by running your program).
    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------
    # DIFFICULTY AND TIME RATINGS (see top of this file for explanation)
    #    DIFFICULTY:      3
    #    TIME ESTIMATE:   < 10 minutes.
    # -------------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   doubler   function:')
    print('--------------------------------------------------')

    format_string = '    doubler( {} )'
    test_results = [0, 0]  # Number of tests passed, failed.

    # -------------------------------------------------------------------------
    # Test 1:
    # -------------------------------------------------------------------------
    seq_of_lists = ([10, 3, 101], [8, 0], [-20, 5, 1, 2, 3, 4, 5], [])

    # After the function call,  seq_of_lists  should be mutated to:
    expected_mutated = ([20, 6, 202], [16, 0], [-40, 10, 2, 4, 6, 8, 10], [])

    print_function_call_of_test([seq_of_lists], test_results, format_string)

    print()
    print("For the MUTATION of the argument:")  # Testing MUTATION
    print("  Expected:", expected_mutated)

    actual = doubler(seq_of_lists)

    print_actual_result_of_test(expected_mutated, seq_of_lists, test_results)

    print()
    print("For the RETURNED VALUE:")  # Nothing (i.e., None) should be returned
    print("  Expected:", None)
    print_actual_result_of_test(None, actual, test_results)

    # -------------------------------------------------------------------------
    # Test 2:
    # -------------------------------------------------------------------------
    seq_of_lists = ([10], [200], [3], [4, 7], [], [9], [1, 0, 2], [1])

    # After the function call,  seq_of_lists  should be mutated to:
    expected_mutated = ([20], [400], [6], [8, 14], [], [18], [2, 0, 4], [2])

    print_function_call_of_test([seq_of_lists], test_results, format_string)

    print()
    print("For the MUTATION of the argument:")  # Testing MUTATION
    print("  Expected:", expected_mutated)

    actual = doubler(seq_of_lists)

    print_actual_result_of_test(expected_mutated, seq_of_lists, test_results)

    print()
    print("For the RETURNED VALUE:")  # Nothing (i.e., None) should be returned
    print("  Expected:", None)
    print_actual_result_of_test(None, actual, test_results)

    # -------------------------------------------------------------------------
    # Test 3:
    # -------------------------------------------------------------------------
    seq_of_lists = [[], [1], [20, 2, 30, 4, 100, 8, 2, 2, 2], [], [300],
                    [5, 5], [], [-10, 4]]

    # After the function call,  seq_of_lists  should be mutated to:
    expected_mutated = [[], [2], [40, 4, 60, 8, 200, 16, 4, 4, 4], [], [600],
                        [10, 10], [], [-20, 8]]

    print_function_call_of_test([seq_of_lists], test_results, format_string)

    print()
    print("For the MUTATION of the argument:")  # Testing MUTATION
    print("  Expected:", expected_mutated)

    actual = doubler(seq_of_lists)

    print_actual_result_of_test(expected_mutated, seq_of_lists, test_results)

    print()
    print("For the RETURNED VALUE:")  # Nothing (i.e., None) should be returned
    print("  Expected:", None)
    print_actual_result_of_test(None, actual, test_results)

    # -------------------------------------------------------------------------
    # TODO: 3 (continued). Write at least ** 1 GOOD ** additional test for the
    #    doubler  function, following the style we used for the above tests.
    #
    # Test 4:  (PUT YOUR TEST BELOW THIS)
    # -------------------------------------------------------------------------

    # SUMMARY of test results:
    print_summary_of_test_results(test_results)


def doubler(seq_of_lists):
    """
    What comes in:  A sequence of LISTs,
                    where the interior lists contain only integers.
    What goes out:  Nothing (i.e., none)
    Side effects:  MUTATES each number in each sub-list of the argument
           by doubling each number in the sub-list
    Example:
      If the given sequence of lists is:
          ([10, 3, 101], [8, 0], [-20, 5, 1, 2, 3, 4, 5], [])
    then this method MUTATES the sub-lists so that the sequence of lists
    after the function call is:
         ([20, 6, 202], [16, 0], [-40, 10, 2, 4, 6, 8, 10], [])
    Type hints:
      :type seq_of_lists: sequence of lists
    """
    # -------------------------------------------------------------------------
    # TODO: 4. Implement and test this function.
    #          Note that you should write its TEST function first (above).
    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------
    # DIFFICULTY AND TIME RATINGS (see top of this file for explanation)
    #    DIFFICULTY:      4
    #    TIME ESTIMATE:   5 minutes.
    # -------------------------------------------------------------------------


def run_test_zero_changer():
    """ Tests the    zero_changer    function. """
    # -------------------------------------------------------------------------
    # TODO: 5. READ the tests that we supplied in this function, asking
    #  questions as needed.  Once you UNDERSTAND the tests that we supplied,
    #  ADD ANOTHER ** GOOD ** TEST of your own for the  zero_changer  function,
    #  using the same style for testing as we did.
    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------
    # DIFFICULTY AND TIME RATINGS (see top of this file for explanation)
    #    DIFFICULTY:      3
    #    TIME ESTIMATE:   < 10 minutes.
    # -------------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   zero_changer   function:')
    print('--------------------------------------------------')

    format_string = '    zero_changer( {} )'
    test_results = [0, 0]  # Number of tests passed, failed.

    # -------------------------------------------------------------------------
    # Test 1:
    # -------------------------------------------------------------------------
    tuple_of_lists = (
        [8, 4, 0, 9], [77, 0, 0, 11, 15, 0], [0, 0, 0], [4, 0, 4])

    # After the function call,  tuple_of_lists  should be mutated to:
    expected_mutated = (
        [8, 4, 1, 9], [77, 2, 3, 11, 15, 4], [5, 6, 7], [4, 8, 4])

    print_function_call_of_test([tuple_of_lists], test_results, format_string)

    print()
    print("For the MUTATION of the argument:")  # Testing MUTATION
    print("  Expected:", expected_mutated)

    actual = zero_changer(tuple_of_lists)

    print_actual_result_of_test(expected_mutated, tuple_of_lists, test_results)

    print()
    print("For the RETURNED VALUE:")  # Nothing (i.e., None) should be returned
    print("  Expected:", None)
    print_actual_result_of_test(None, actual, test_results)

    # -------------------------------------------------------------------------
    # Test 2:
    # -------------------------------------------------------------------------
    tuple_of_lists = ([0, 0, 0, 0, 0, 0, 0, 0, 0], [], [1, 2, 3], [0])

    # After the function call,  tuple_of_lists  should be mutated to:
    expected_mutated = ([1, 2, 3, 4, 5, 6, 7, 8, 9], [], [1, 2, 3], [10])

    print_function_call_of_test([tuple_of_lists], test_results, format_string)

    print()
    print("For the MUTATION of the argument:")  # Testing MUTATION
    print("  Expected:", expected_mutated)

    actual = zero_changer(tuple_of_lists)

    print_actual_result_of_test(expected_mutated, tuple_of_lists, test_results)

    print()
    print("For the RETURNED VALUE:")  # Nothing (i.e., None) should be returned
    print("  Expected:", None)
    print_actual_result_of_test(None, actual, test_results)

    # -------------------------------------------------------------------------
    # Test 3:
    # -------------------------------------------------------------------------
    tuple_of_lists = ([], [], [1, 2, 3, 4, 5, 1, 2, 3, 4, 5], [-1], [-1, -2])

    # After the function call,  tuple_of_lists  should be mutated to:
    expected_mutated = ([], [], [1, 2, 3, 4, 5, 1, 2, 3, 4, 5], [-1], [-1, -2])

    print_function_call_of_test([tuple_of_lists], test_results, format_string)

    print()
    print("For the MUTATION of the argument:")  # Testing MUTATION
    print("  Expected:", expected_mutated)

    actual = zero_changer(tuple_of_lists)

    print_actual_result_of_test(expected_mutated, tuple_of_lists, test_results)

    print()
    print("For the RETURNED VALUE:")  # Nothing (i.e., None) should be returned
    print("  Expected:", None)
    print_actual_result_of_test(None, actual, test_results)

    # -------------------------------------------------------------------------
    # Test 4:
    # -------------------------------------------------------------------------
    tuple_of_lists = ()

    # After the function call,  tuple_of_lists  should be mutated to:
    expected_mutated = ()

    print_function_call_of_test([tuple_of_lists], test_results, format_string)

    print()
    print("For the MUTATION of the argument:")  # Testing MUTATION
    print("  Expected:", expected_mutated)

    actual = zero_changer(tuple_of_lists)

    print_actual_result_of_test(expected_mutated, tuple_of_lists, test_results)

    print()
    print("For the RETURNED VALUE:")  # Nothing (i.e., None) should be returned
    print("  Expected:", None)
    print_actual_result_of_test(None, actual, test_results)

    # -------------------------------------------------------------------------
    # TODO: 5 (continued). Write at least ** 1 GOOD ** additional test for the
    #  zero_changer  function, following the style we used for the above tests.
    #
    # Test 5:  (PUT YOUR TEST BELOW THIS)
    # -------------------------------------------------------------------------

    # SUMMARY of test results:
    print_summary_of_test_results(test_results)


def zero_changer(tuple_of_lists):
    """
    What comes in:  A tuple of LISTs,
                    where the interior lists contain only integers.
    What goes out:  Nothing (i.e., none)
    Side effects:  The argument is MUTATED so that:
      -- the 1st 0 in the given tuple of lists is changed to 1.
      -- the 2nd 0 in the given tuple of lists is changed to 2.
      -- the 3rd 0 in the given tuple of lists is changed to 3.
           etc.
    Example:
      If the given tuple of lists is:
          ([8, 4, 0, 9], [77, 0, 0, 11, 15, 0], [0, 0, 0], [4, 0, 4])
      this function MUTATES the sub-lists so that after the function call is
      the tuple of lists is:
          ([8, 4, 1, 9], [77, 2, 3, 11, 15, 4], [5, 6, 7], [4, 8, 4])
      Note that:
        -- If there are no zeros in the given sequence of lists,
             then this function does nothing.
        -- After this function call, the sequence of lists IN THE CALLER
             should contain no zeros.
    Type hints:
      :type tuple_of_lists: tuple of list[int]
    """
    # -------------------------------------------------------------------------
    # TODO: 6. Implement and test this function.
    #          Note that you should write its TEST function first (above).
    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------
    # DIFFICULTY AND TIME RATINGS (see top of this file for explanation)
    #    DIFFICULTY:      7
    #    TIME ESTIMATE:  10 to 15 minutes.
    # -------------------------------------------------------------------------


###############################################################################
# Our tests use the following to print error messages in red.
# Do NOT change it.  You do NOT have to do anything with it.
###############################################################################

def print_function_call_of_test(arguments, test_results, format_string):
    testing_helper.print_function_call_of_test(arguments, test_results,
                                               format_string)


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
