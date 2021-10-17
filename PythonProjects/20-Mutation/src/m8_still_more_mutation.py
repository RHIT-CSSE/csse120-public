"""
This module lets you practice   MUTATION   of lists.

Authors: David Mutchler, Vibha Alangar, Dave Fisher, Matt Boutell, Mark Hays,
         Mohammed Noureddine, Sana Ebrahimi, Sriram Mohan, their colleagues and
         PUT_YOUR_NAME_HERE.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

# -----------------------------------------------------------------------------
# TODO: 2. Have you completed the   m3r_mutation_vs_copy_return   module,
#   with its associated FOLLOW-ME video?  Do you understand the code therein?
#   If NOT, go back and do the FOLLOW-ME video again, getting help as needed.
#  _
#   Once you understand the code in the   m3r_mutation_vs_copy_return   module,
#   change this _TODO_ to DONE.
# -----------------------------------------------------------------------------

import time
import testing_helper


def main():
    """ Calls the other functions to test them. """
    print()
    print("Un-comment and re-comment calls in MAIN one by one as you work.")

    # run_test_RETURN_delete_negatives()
    # run_test_MUTATE_delete_negatives()


# -----------------------------------------------------------------------------
# Note: Here are the PROBLEMS.  The TESTS are further down in this module.
# -----------------------------------------------------------------------------
def RETURN_delete_negatives(numbers):
    """
    Returns a NEW list that is the same as the given list of numbers,
    but with each negative number in the list DELETED from the list.

    For example, if the given list is [-30.2, 50, 12.5, -1, -5, 8, 0].
    then the returned list is the NEW list [50, 12.5, 8, 0].

    This function must NOT mutate the given list.

    Precondition:
      :type numbers: list
    where the list is a list of numbers.
    """
    # -------------------------------------------------------------------------
    # TODO: 3. Implement and test this function.
    #   Some tests are already written for you (below).  Those tests use
    #   the same form as the tests that you saw in m3r_mutation_vs_copy_return.
    # -------------------------------------------------------------------------


def MUTATE_delete_negatives(numbers):
    """
    MUTATES the given list of numbers so that each negative number
    in the list is DELETED from the list.

    For example, if the given list is [-30.2, 50, 12.5, -1, -5, 8, 0].
    then that list is MUTATED to become [50, 12.5, 8, 0].

    This function MAY use ONE additional list beyond the given list
    (but see if you can solve the problem WITHOUT any additional lists).
    The function must NOT return anything (other than the default None).

    Precondition: The argument is a list of numbers.
    """
    # -------------------------------------------------------------------------
    # TODO: 4. Implement and test this function.
    #   Some tests are already written for you (below).  Those tests use
    #   the same form as the tests that you saw in m3r_mutation_vs_copy_return.
    #  _
    #   HINT #1: This problem is MUCH harder than it would appear,
    #       for various quite-subtle reasons.
    #       Take a stab at this problem,
    #       then ask for help as needed (perhaps using Piazza).
    #       There are quite a few different ways to solve this problem!
    #   HINT #2: Why might it be wise to start at the end
    #       and work backwards through the list to the beginning?
    # -------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# Note: Here are the TESTS.  The PROBLEMS are further up in this module.
# -----------------------------------------------------------------------------
def run_test_RETURN_delete_negatives():
    """ Tests the   RETURN_delete_negatives   function. """
    print()
    print('--------------------------------')
    print('Testing RETURN_delete_negatives:')
    print('--------------------------------')

    # -------------------------------------------------------------------------
    # Test 1:
    # -------------------------------------------------------------------------
    test_number = 1
    original_argument = [-30.2, 50, 12.5, -1, -5, 8, 0]
    correct_argument_value_after_function_call = original_argument.copy()
    correct_returned_value = [50, 12.5, 8, 0]

    run_test(RETURN_delete_negatives,
             original_argument,
             test_number,
             correct_returned_value,
             correct_argument_value_after_function_call)

    # -------------------------------------------------------------------------
    # Test 2:
    # -------------------------------------------------------------------------
    test_number = 2
    original_argument = [2, 0, -9, 1, -30]
    correct_argument_value_after_function_call = original_argument.copy()
    correct_returned_value = [2, 0, 1]

    run_test(RETURN_delete_negatives,
             original_argument,
             test_number,
             correct_returned_value,
             correct_argument_value_after_function_call)


def run_test_MUTATE_delete_negatives():
    """ Tests the   MUTATE_delete_negatives   function. """
    print()
    print('--------------------------------')
    print('Testing MUTATE_delete_negatives:')
    print('--------------------------------')

    # -------------------------------------------------------------------------
    # Test 1:
    # -------------------------------------------------------------------------
    test_number = 1
    original_argument = [-30.2, 50, 12.5, -1, -5, 8, 0]
    correct_argument_value_after_function_call = [50, 12.5, 8, 0]
    correct_returned_value = None

    run_test(MUTATE_delete_negatives,
             original_argument,
             test_number,
             correct_returned_value,
             correct_argument_value_after_function_call)

    # -------------------------------------------------------------------------
    # Test 2:
    # -------------------------------------------------------------------------
    test_number = 2
    original_argument = [2, 0, -9, 1, -30]
    correct_argument_value_after_function_call = [2, 0, 1]
    correct_returned_value = None

    run_test(MUTATE_delete_negatives,
             original_argument,
             test_number,
             correct_returned_value,
             correct_argument_value_after_function_call)


###############################################################################
# Our tests use the following to print error messages in red.
# Do NOT change it.  You do NOT have to do anything with it.
###############################################################################

def run_test(function_to_test, argument, run_test_number,
             correct_returned_value,
             correct_argument_value_after_function_call):
    """
    Runs a test, by calling the given function on the given argument.
    The function should return the given correct_returned_value.
    After the function call, the argument should equal the given
    correct_argument_value_after_function_call.
    Prints messages to indicate whether the test passed or failed.
    """
    print()
    print('Running TEST {}:'.format(run_test_number, run_test_number))

    actual_returned_value = function_to_test(argument)

    passed_check1 = check_returned_value(actual_returned_value,
                                         correct_returned_value)
    passed_check2 = check_argument(argument,
                                   correct_argument_value_after_function_call)

    if passed_check1 and passed_check2:
        print('  Your code PASSES Test {}.'.format(run_test_number),
              color="blue")


def check_returned_value(actual_returned_value, correct_returned_value):
    """
    Checks whether the two given returned-values are equal.
    If so, returns True.
    If not, prints an appropriate message and returns False.
    """
    if actual_returned_value == correct_returned_value:
        return True
    else:
        print("  Your code FAILS this test", color="red")
        print("    because it returns the wrong value:", color="red")
        print("      -- The correct returned value is:")
        print("         ", correct_returned_value)
        print("      -- Your code returned this value:")
        print("         ", actual_returned_value)

        return False


def check_argument(actual_argument_value, correct_argument_value):
    """
    Checks whether the two given argument-values are equal.
    If so, returns True.
    If not, prints an appropriate message and returns False.
    """
    if actual_argument_value == correct_argument_value:
        return True
    else:
        print("  Your code FAILS this test because the argument", color="red")
        print("    has the wrong value after the function call:", color="red")
        print("      -- The correct value after the function call is:")
        print("         ", correct_argument_value)
        print("      -- Your actual value after the function call is:")
        print("         ", actual_argument_value)

        return False


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
