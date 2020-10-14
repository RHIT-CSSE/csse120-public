"""
This module lets you practice   MUTATION   of lists.
In this module, you mutate by CHANGING elements of a list.

Authors: David Mutchler, Sana Ebrahimi, Mohammed Noureddine, Vibha Alangar,
         Matt Boutell, Dave Fisher, Mark Hays, their colleagues, and
         PUT_YOUR_NAME_HERE.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

# -----------------------------------------------------------------------------
# STUDENTS:
#  Be sure to READ and RUN the examples in the preceding files.
#  Be sure to understand those examples BEFORE doing these exercises!
# -----------------------------------------------------------------------------


def main():
    run_test_RETURN_replace_negatives_by_zeros()
    run_test_MUTATE_replace_negatives_by_zeros()


def run_test_RETURN_replace_negatives_by_zeros():
    """ Tests the   RETURN_replace_negatives_by_zeros   function. """
    print()
    print('------------------------------------------')
    print('Testing RETURN_replace_negatives_by_zeros:')
    print('------------------------------------------')

    # -------------------------------------------------------------------------
    # Test 1:
    # -------------------------------------------------------------------------
    run_test_number = 1
    original_argument = [-30.2, 50, 12.5, -1, -5, 8, 0]
    correct_argument_value_after_function_call = original_argument.copy()
    correct_returned_value = [0, 50, 12.5, 0, 0, 8, 0]

    run_test(RETURN_replace_negatives_by_zeros,
             original_argument,
             run_test_number,
             correct_returned_value,
             correct_argument_value_after_function_call)

    # -------------------------------------------------------------------------
    # Test 2:
    # -------------------------------------------------------------------------
    run_test_number = 2
    original_argument = [2, 0, -9, 1, -30]
    correct_argument_value_after_function_call = original_argument.copy()
    correct_returned_value = [2, 0, 0, 1, 0]

    run_test(RETURN_replace_negatives_by_zeros,
             original_argument,
             run_test_number,
             correct_returned_value,
             correct_argument_value_after_function_call)


def run_test(function_to_test, argument, run_test_number,
             correct_returned_value,
             correct_argument_value_after_function_call):
    """
    Runs a test, by sending the given function the given argument.
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
        print('  Your code PASSES Test {}.'.format(run_test_number))


def check_returned_value(actual_returned_value, correct_returned_value):
    """
    Checks whether the two given returned-values are equal.
    If so, returns True.
    If not, prints an appropriate message and returns False.
    """
    if actual_returned_value == correct_returned_value:
        return True
    else:
        print('  Your code FAILS this test')
        print('    because it returns the wrong value:')
        print('      -- The correct returned value is:',
              correct_returned_value)
        print('      -- Your code returned this value:',
              actual_returned_value)

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
        print('  Your code FAILS this test because the argument')
        print('    has the wrong value after the function call:')
        print('      -- The correct value after the function call is:',
              correct_argument_value)
        print('      -- Your actual value after the function call is:',
              actual_argument_value)

        return False


def RETURN_replace_negatives_by_zeros(numbers):
    """
    RETURNs a NEW list that is the same as the given list of numbers,
    but with each negative number in the list replaced by zero.

    For example, if the given list is [-30.2, 50, 12.5, -1, -5, 8, 0].
    then the returned list is the NEW list [0, 50, 12.5, 0, 0, 8, 0].

    This function must NOT mutate the given list.

    Precondition: The argument is a list of numbers.
    """
    # -------------------------------------------------------------------------
    # TODO: 2. First, READ THE ABOVE TEST CODE.
    #          Make sure that you understand it.
    #          Then, IMPLEMENT and test THIS FUNCTION
    #          (using the above code for testing).
    # -------------------------------------------------------------------------


def run_test_MUTATE_replace_negatives_by_zeros():
    """ Tests the   MUTATE_replace_negatives_by_zeros   function. """
    print()
    print('------------------------------------------')
    print('Testing MUTATE_replace_negatives_by_zeros:')
    print('------------------------------------------')

    # -------------------------------------------------------------------------
    # Test 1:
    # -------------------------------------------------------------------------
    run_test_number = 1
    original_argument = [-30.2, 50, 12.5, -1, -5, 8, 0]
    correct_argument_value_after_function_call = [0, 50, 12.5, 0, 0, 8, 0]
    correct_returned_value = None

    run_test(MUTATE_replace_negatives_by_zeros,
             original_argument,
             run_test_number,
             correct_returned_value,
             correct_argument_value_after_function_call)

    # -------------------------------------------------------------------------
    # Test 2:
    # -------------------------------------------------------------------------
    run_test_number = 2
    original_argument = [2, 0, -9, 1, -30]
    correct_argument_value_after_function_call = [2, 0, 0, 1, 0]
    correct_returned_value = None

    run_test(MUTATE_replace_negatives_by_zeros,
             original_argument,
             run_test_number,
             correct_returned_value,
             correct_argument_value_after_function_call)


def MUTATE_replace_negatives_by_zeros(numbers):
    """
    MUTATES the given list of numbers so that
    each negative number in the list is replaced by zero
    (and non-negative numbers are left unchanged).

    For example, if the given list is [-30.2, 50, 12.5, -1, -5, 8, 0].
    then that list is MUTATED to become [0, 50, 12.5, 0, 0, 8, 0].

    This function must NOT use any additional lists beyond the given
    list and must NOT return anything (other than the default None).

    Precondition: The argument is a list of numbers.
    """
    # -------------------------------------------------------------------------
    # TODO: 3. First, READ THE ABOVE TEST CODE.
    #          Make sure that you understand it.
    #          Then, IMPLEMENT and test THIS FUNCTION
    #          (using the above code for testing).
    # -------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
