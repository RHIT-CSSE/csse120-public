"""
This module shows two ways for a function to send information back
to the caller via a list:
  1. Functions that MUTATE their list argument.
  2. Functions that make a COPY of their list argument and return the copy.

Authors: David Mutchler, Vibha Alangar, Dave Fisher, Matt Boutell, Mark Hays,
         Mohammed Noureddine, Sana Ebrahimi, Sriram Mohan, their colleagues and
         PUT_YOUR_NAME_HERE.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

# -----------------------------------------------------------------------------
# TODO: 2.  *** There is a FOLLOW-ME VIDEO associated with this module. ***
#  Start running that video and follow along with it.  Change this _TODO_
#  to DONE after you have started the associated follow-me video.
# -----------------------------------------------------------------------------

import time
import testing_helper


def main():
    run_test_example1_mutate()
    run_test_example1_copy()

    run_test_example2_mutate()
    run_test_example2_copy()


# -----------------------------------------------------------------------------
# Note: Here are the EXAMPLES.  The TESTS are further down in this module.
# -----------------------------------------------------------------------------
def example1_mutate(numbers):
    """ Mutates the given list by incrementing each number in the list. """
    for k in range(len(numbers)):
        numbers[k] = numbers[k] + 1


def example1_copy(numbers):
    """ Returns a copy of the given list with each number incremented. """
    new = []
    for k in range(len(numbers)):
        new.append(numbers[k] + 1)  # Better than: new = new + [numbers[k] + 1]
    return new


def example2_mutate(numbers):
    """ Mutates the given list by incrementing the LAST number in the list. """
    if len(numbers) > 0:
        numbers[-1] = numbers[-1] + 1


def example2_copy(numbers):
    """ Returns a copy of the given list with the LAST number incremented. """
    new = []
    for k in range(len(numbers)):
        new.append(numbers[k])  # Better than: new = new + [numbers[k] + 1]
    new[-1] = new[-1] + 1
    return new


# -------------------------------------------------------------------------
# TODO: 2.
#  READ the four function definitions directly above this _TODO_.
#  All four send information back to the caller via a list.
#   a. Make sure that you understand all 4 functions.  ASK QUESTIONS as needed!
#   b. The  example1_copy  does NOT mutate the  numbers  argument.
#      Does it mutate the  new  list while it is building up that list?
#         (Answer: YES!  Be sure that you see why!)
#  Make sure that you completely UNDERSTAND how one writes:
#    -- code that MUTATES an argument, versus
#    -- code that COPIES an argument and returns the copy.
#    ** ASK QUESTIONS
#    AS NEEDED. **
#  Then change the above _TODO_ to DONE.
# -------------------------------------------------------------------------

# -------------------------------------------------------------------------
# TODO: 3. With your instructor, read the two TESTING functions below,
#  just enough that you see how they test BOTH the returned value AND
#  the mutation (or non-mutation) of the argument.
#  _
#  Then, with your instructor, make changes to the four functions above
#  so that they have errors in:
#    -- what they return, and
#    -- whether they mutate the argument correctly (or don't mutate it at all).
#   Run the code as needed to see how the tests catch these errors.
#     ** ASK QUESTIONS AS NEEDED. **
#  Then change the above _TODO_ to DONE.
# -------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# Note: Here are the TESTS.  The EXAMPLES are further up in this module.
# -----------------------------------------------------------------------------
def run_test_example1_mutate():
    """ Tests the   example1_mutate   function. """
    print()
    print('------------------------------------------')
    print('Testing example1_mutate:')
    print('------------------------------------------')

    # -------------------------------------------------------------------------
    # Test 1:
    # -------------------------------------------------------------------------
    test_number = 1
    original_argument = [50, 12.5, -1, -5, 8, 0]
    correct_argument_value_after_function_call = [51, 13.5, 0, -4, 9, 1]
    correct_returned_value = None

    run_test(example1_mutate,
             original_argument,
             test_number,
             correct_returned_value,
             correct_argument_value_after_function_call)

    # -------------------------------------------------------------------------
    # Test 2:
    # -------------------------------------------------------------------------
    test_number = 2
    original_argument = [2, 0, -9, 1, 30]
    correct_argument_value_after_function_call = [3, 1, -8, 2, 31]
    correct_returned_value = None

    run_test(example1_mutate,
             original_argument,
             test_number,
             correct_returned_value,
             correct_argument_value_after_function_call)


def run_test_example1_copy():
    """ Tests the   example1_copy   function. """
    print()
    print('------------------------------------------')
    print('Testing example1_copy:')
    print('------------------------------------------')

    # -------------------------------------------------------------------------
    # Test 1:
    # -------------------------------------------------------------------------
    test_number = 1
    original_argument = [50, 12.5, -1, -5, 8, 0]
    correct_returned_value = [51, 13.5, 0, -4, 9, 1]

    # The following makes what is called a "shallow" copy.
    # It clones each of the items, but does NOT clone any sub-items.
    correct_argument_value_after_function_call = original_argument.copy()

    run_test(example1_copy,
             original_argument,
             test_number,
             correct_returned_value,
             correct_argument_value_after_function_call)

    # -------------------------------------------------------------------------
    # Test 2:
    # -------------------------------------------------------------------------
    test_number = 2
    original_argument = [2, 0, -9, 1, 30]
    correct_returned_value = [3, 1, -8, 2, 31]
    correct_argument_value_after_function_call = original_argument.copy()

    run_test(example1_copy,
             original_argument,
             test_number,
             correct_returned_value,
             correct_argument_value_after_function_call)


def run_test_example2_mutate():
    """ Tests the   example2_mutate   function. """
    print()
    print('------------------------------------------')
    print('Testing example2_mutate:')
    print('------------------------------------------')

    # -------------------------------------------------------------------------
    # Test 1:
    # -------------------------------------------------------------------------
    test_number = 1
    original_argument = [50, 12.5, -1, -5, 8, 0]
    correct_argument_value_after_function_call = [50, 12.5, -1, -5, 8, 1]
    correct_returned_value = None

    run_test(example2_mutate,
             original_argument,
             test_number,
             correct_returned_value,
             correct_argument_value_after_function_call)

    # -------------------------------------------------------------------------
    # Test 2:
    # -------------------------------------------------------------------------
    test_number = 2
    original_argument = [2, 0, -9, 1, 30]
    correct_argument_value_after_function_call = [2, 0, -9, 1, 31]
    correct_returned_value = None

    run_test(example2_mutate,
             original_argument,
             test_number,
             correct_returned_value,
             correct_argument_value_after_function_call)


def run_test_example2_copy():
    """ Tests the   example2_copy   function. """
    print()
    print('------------------------------------------')
    print('Testing example2_copy:')
    print('------------------------------------------')

    # -------------------------------------------------------------------------
    # Test 1:
    # -------------------------------------------------------------------------
    test_number = 1
    original_argument = [50, 12.5, -1, -5, 8, 0]
    correct_returned_value = [50, 12.5, -1, -5, 8, 1]

    # The following makes what is called a "shallow" copy.
    # It clones each of the items, but does NOT clone any sub-items.
    correct_argument_value_after_function_call = original_argument.copy()

    run_test(example2_copy,
             original_argument,
             test_number,
             correct_returned_value,
             correct_argument_value_after_function_call)

    # -------------------------------------------------------------------------
    # Test 2:
    # -------------------------------------------------------------------------
    test_number = 2
    original_argument = [2, 0, -9, 1, 30]
    correct_returned_value = [2, 0, -9, 1, 31]
    correct_argument_value_after_function_call = original_argument.copy()

    run_test(example2_copy,
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
