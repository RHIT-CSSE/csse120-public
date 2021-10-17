"""
PRACTICE Exam 3.

This problem provides practice at:
  ***  MUTATING  and  RETURNING-NEW  LISTS.  ***

Authors: David Mutchler, Vibha Alangar, Dave Fisher, Matt Boutell, Mark Hays,
         Mohammed Noureddine, Sana Ebrahimi, Sriram Mohan, their colleagues and
         PUT_YOUR_NAME_HERE.
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
    print()
    print("Un-comment and re-comment calls in MAIN one by one as you work.")

    # run_test_doubler_1()
    # run_test_doubler_2()
    # run_test_zero_changer()


def run_test_doubler_1():
    """ Tests the    doubler_1    function. """
    # -------------------------------------------------------------------------
    # TODO: 3.  Note that this is   run_test_doubler_1.
    #           The   doubler_1  function is further down in this module.
    #  _
    #  (a) READ the SPECIFICATION of the  doubler_1  function further down
    #        in this module.
    #  _
    #  (b) For each of the TESTS below (in THIS function, run_test_doubler_1):
    #      1. READ the test.
    #      2. BY HAND, compute how, if at all, the   doubler_1   function should
    #         mutate its argument and what, if anything, it should return.
    #         VERIFY that your by-hand computation agrees with the TEST.
    #  _
    #     These tests use the same form as the tests that you saw in
    #     19-Mutation, module m3r_mutation_vs_copy_return.
    #     ** ASK QUESTIONS if you do not understand this testing framework. **
    #  _
    #     Once you UNDERSTAND the tests that we supplied,
    #  _
    #  (c) In this function, ADD ANOTHER ** GOOD ** TEST of your own
    #      for the  doubler_1  function,
    #      using the same style for testing as we did.
    #  _
    #   Try to choose a test that might expose errors in your code!
    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------
    # DIFFICULTY AND TIME RATINGS (see top of this file for explanation)
    #    DIFFICULTY:      3
    #    TIME ESTIMATE:   < 10 minutes.
    # -------------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   doubler_1   function:')
    print('--------------------------------------------------')

    # -------------------------------------------------------------------------
    # Test 1:
    # -------------------------------------------------------------------------
    test_number = 1
    original_argument = \
        ([10, 3, 101],
         [8, 0],
         [-20, 5, 1, 2, 3, 4, 5],
         [])
    correct_argument_value_after_function_call = \
        ([20, 6, 202],
         [16, 0],
         [-40, 10, 2, 4, 6, 8, 10],
         [])
    correct_returned_value = None

    run_test(doubler_1,
             original_argument,
             test_number,
             correct_returned_value,
             correct_argument_value_after_function_call)

    # -------------------------------------------------------------------------
    # Test 2:
    # -------------------------------------------------------------------------
    test_number = 2
    original_argument = \
        ([10], [200], [3], [4, 7], [], [9], [1, 0, 2], [1])
    correct_argument_value_after_function_call = \
        ([20], [400], [6], [8, 14], [], [18], [2, 0, 4], [2])
    correct_returned_value = None

    run_test(doubler_1,
             original_argument,
             test_number,
             correct_returned_value,
             correct_argument_value_after_function_call)

    # -------------------------------------------------------------------------
    # Test 3:
    # -------------------------------------------------------------------------
    test_number = 3
    original_argument = \
        [[], [1], [20, 2, 30, 4, 100, 8, 2, 2, 2], [], [300], [5, 5], [],
         [-10, 4]]
    correct_argument_value_after_function_call = \
        [[], [2], [40, 4, 60, 8, 200, 16, 4, 4, 4], [], [600], [10, 10], [],
         [-20, 8]]
    correct_returned_value = None

    run_test(doubler_1,
             original_argument,
             test_number,
             correct_returned_value,
             correct_argument_value_after_function_call)

    # -------------------------------------------------------------------------
    # TODO: 3 (continued). Write at least ** 1 GOOD ** additional test for the
    #    doubler_1  function, following the style we used for the above tests.
    #
    # Test 4:  (PUT YOUR TEST BELOW THIS)
    # -------------------------------------------------------------------------


def doubler_1(seq_of_lists):
    """
    What comes in:  A sequence of LISTs,
                    where the interior lists contain only integers.
    What goes out:  Nothing (i.e., None is returned by default)
    Side effects:  MUTATES each number in each sub-list of the argument
           by doubling each number in the sub-list.
    Example:
      If the given sequence of lists is:
          ([10, 3, 101],
           [8, 0],
           [-20, 5, 1, 2, 3, 4, 5],
           [])
    then this method MUTATES the sub-lists so that the sequence of lists
    after the function call is:
          ([20, 6, 202],
           [16, 0],
           [-40, 10, 2, 4, 6, 8, 10],
           [])
    Type hints:
      :type seq_of_lists: list[list] | tuple[list]
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


def run_test_doubler_2():
    """ Tests the    doubler_2    function. """
    # -------------------------------------------------------------------------
    # TODO: 5.  Note that this is   run_test_doubler_2.
    #           The   doubler_2  function is further down in this module.
    #  _
    #  (a) READ the SPECIFICATION of the  doubler_2  function further down
    #        in this module.
    #  _
    #  (b) For each of the TESTS below (in THIS function, run_test_doubler_2):
    #      1. READ the test.
    #      2. BY HAND, compute how, if at all, the   doubler_2   function should
    #         mutate its argument and what, if anything, it should return.
    #         VERIFY that your by-hand computation agrees with the TEST.
    #  _
    #     These tests use the same form as the tests that you saw in
    #     19-Mutation, module m3r_mutation_vs_copy_return.
    #     ** ASK QUESTIONS if you do not understand this testing framework. **
    #  _
    #     Once you UNDERSTAND the tests that we supplied,
    #  _
    #  (c) In this function, ADD ANOTHER ** GOOD ** TEST of your own
    #      for the  doubler_2  function,
    #      using the same style for testing as we did.
    #  _
    #   Try to choose a test that might expose errors in your code!
    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------
    # DIFFICULTY AND TIME RATINGS (see top of this file for explanation)
    #    DIFFICULTY:      3
    #    TIME ESTIMATE:   < 10 minutes.
    # -------------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   doubler_2   function:')
    print('--------------------------------------------------')

    # -------------------------------------------------------------------------
    # Test 1:
    # -------------------------------------------------------------------------
    test_number = 1
    original_argument = \
        ([10, 3, 101],
         [8, 0],
         [-20, 5, 1, 2, 3, 4, 5],
         [])
    correct_argument_value_after_function_call = \
        ([10, 3, 101],
         [8, 0],
         [-20, 5, 1, 2, 3, 4, 5],
         [])  # i.e., unchanged
    correct_returned_value = \
        ([20, 6, 202],
         [16, 0],
         [-40, 10, 2, 4, 6, 8, 10],
         [])

    run_test(doubler_2,
             original_argument,
             test_number,
             correct_returned_value,
             correct_argument_value_after_function_call)

    # -------------------------------------------------------------------------
    # Test 2:
    # -------------------------------------------------------------------------
    test_number = 2
    original_argument = \
        ([10], [200], [3], [4, 7], [], [9], [1, 0, 2], [1])
    correct_argument_value_after_function_call = \
        ([10], [200], [3], [4, 7], [], [9], [1, 0, 2], [1])  # i.e., unchanged
    correct_returned_value = \
        ([20], [400], [6], [8, 14], [], [18], [2, 0, 4], [2])

    run_test(doubler_2,
             original_argument,
             test_number,
             correct_returned_value,
             correct_argument_value_after_function_call)

    # -------------------------------------------------------------------------
    # Test 3:
    # -------------------------------------------------------------------------
    test_number = 3
    original_argument = \
        ([], [1], [20, 2, 30, 4, 100, 8, 2, 2, 2], [], [300], [5, 5], [],
         [-10, 4])
    correct_argument_value_after_function_call = \
        ([], [1], [20, 2, 30, 4, 100, 8, 2, 2, 2], [], [300], [5, 5], [],
         [-10, 4])
    correct_returned_value = \
        ([], [2], [40, 4, 60, 8, 200, 16, 4, 4, 4], [], [600], [10, 10], [],
         [-20, 8])

    run_test(doubler_2,
             original_argument,
             test_number,
             correct_returned_value,
             correct_argument_value_after_function_call)

    # -------------------------------------------------------------------------
    # TODO: 5 (continued). Write at least ** 1 GOOD ** additional test for the
    #    doubler_2  function, following the style we used for the above tests.
    #
    # Test 4:  (PUT YOUR TEST BELOW THIS)
    # -------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# See the IMPORTANT note and HINT in the _TODO_ for the following problem.
# -----------------------------------------------------------------------------
def doubler_2(seq_of_lists):
    """
    What comes in:  A TUPLE of LISTs,
                    where the interior lists contain only integers.
    What goes out:  Returns a TUPLE of LISTS, where each sublist has
      the same numbers as the given sublists, but with each number doubled.
    Side effects:  None.
    Example:
      If the given tuple of lists is:
          ([10, 3, 101],
           [8, 0],
           [-20, 5, 1, 2, 3, 4, 5],
           [])
    then this method RETURNS a NEW tuple of sublists that is:
          ([20, 6, 202],
           [16, 0],
           [-40, 10, 2, 4, 6, 8, 10],
           [])
    (and does NOT mutate the argument).
    Type hints:
      :type seq_of_lists: tuple[list]
    """
    # -------------------------------------------------------------------------
    # TODO: 6. Implement and test this function.
    #          Note that you should write its TEST function first (above).
    #  IMPORTANT: You should use APPEND ** where appropriate ** in your code.
    #  HINT: A tuple with ONE item in it is written as per this example: (9,)
    #        Note the comma.
    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------
    # DIFFICULTY AND TIME RATINGS (see top of this file for explanation)
    #    DIFFICULTY:      6
    #    TIME ESTIMATE:   5 minutes.
    # -------------------------------------------------------------------------


def run_test_zero_changer():
    """ Tests the    zero_changer    function. """
    # -------------------------------------------------------------------------
    # TODO: 7.  Note that this is   run_test_zero_changer.
    #           The   zero_changer  function is further down in this module.
    #  _
    #  (a) READ the SPECIFICATION of the  zero_changer  function further down
    #        in this module.
    #  _
    #  (b) For each of the TESTS below (in THIS function, run_test_zero_changer)
    #      1. READ the test.
    #      2. BY HAND, compute how, if at all, the   zero_changer   function
    #         should mutate its argument and what, if anything, it should
    #         return. VERIFY that your by-hand computation agrees with the TEST.
    #  _
    #     These tests use the same form as the tests that you saw in
    #     19-Mutation, module m3r_mutation_vs_copy_return.
    #     ** ASK QUESTIONS if you do not understand this testing framework. **
    #  _
    #     Once you UNDERSTAND the tests that we supplied,
    #  _
    #  (c) In this function, ADD ANOTHER ** GOOD ** TEST of your own
    #      for the  zero_changer  function,
    #      using the same style for testing as we did.
    #  _
    #   Try to choose a test that might expose errors in your code!
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

    # -------------------------------------------------------------------------
    # Test 1:
    # -------------------------------------------------------------------------
    test_number = 1
    original_argument = \
        ([8, 4, 0, 9], [77, 0, 0, 11, 15, 0], [0, 0, 0], [4, 0, 4])
    correct_argument_value_after_function_call = \
        ([8, 4, 1, 9], [77, 2, 3, 11, 15, 4], [5, 6, 7], [4, 8, 4])
    correct_returned_value = None

    run_test(zero_changer,
             original_argument,
             test_number,
             correct_returned_value,
             correct_argument_value_after_function_call)

    # -------------------------------------------------------------------------
    # Test 2:
    # -------------------------------------------------------------------------
    test_number = 2
    original_argument = \
        ([0, 0, 0, 0, 0, 0, 0, 0, 0], [], [1, 2, 3], [0])
    correct_argument_value_after_function_call = \
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], [], [1, 2, 3], [10])
    correct_returned_value = None

    run_test(zero_changer,
             original_argument,
             test_number,
             correct_returned_value,
             correct_argument_value_after_function_call)

    # -------------------------------------------------------------------------
    # Test 3:
    # -------------------------------------------------------------------------
    test_number = 3
    original_argument = \
        ([], [], [1, 2, 3, 4, 5, 1, 2, 3, 4, 5], [-1], [-1, -2])
    correct_argument_value_after_function_call = \
        ([], [], [1, 2, 3, 4, 5, 1, 2, 3, 4, 5], [-1], [-1, -2])
    correct_returned_value = None

    run_test(zero_changer,
             original_argument,
             test_number,
             correct_returned_value,
             correct_argument_value_after_function_call)

    # -------------------------------------------------------------------------
    # Test 4:
    # -------------------------------------------------------------------------
    test_number = 4
    original_argument = ()
    correct_argument_value_after_function_call = ()
    correct_returned_value = None

    run_test(zero_changer,
             original_argument,
             test_number,
             correct_returned_value,
             correct_argument_value_after_function_call)

    # -------------------------------------------------------------------------
    # Test 5:
    # -------------------------------------------------------------------------
    test_number = 5
    original_argument = ([0],)
    correct_argument_value_after_function_call = ([1],)
    correct_returned_value = None

    run_test(zero_changer,
             original_argument,
             test_number,
             correct_returned_value,
             correct_argument_value_after_function_call)

    # -------------------------------------------------------------------------
    # Test 6:
    # -------------------------------------------------------------------------
    test_number = 6
    original_argument = \
        ([], [1, 0, 2], [0, 8, 0], [0], [1, 2])
    correct_argument_value_after_function_call = \
        ([], [1, 1, 2], [2, 8, 3], [4], [1, 2])
    correct_returned_value = None

    run_test(zero_changer,
             original_argument,
             test_number,
             correct_returned_value,
             correct_argument_value_after_function_call)

    # -------------------------------------------------------------------------
    # TODO: 5 (continued). Write at least ** 1 GOOD ** additional test for the
    #  zero_changer  function, following the style we used for the above tests.
    #
    # Test 5:  (PUT YOUR TEST BELOW THIS)
    # -------------------------------------------------------------------------


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
                  ^           ^  ^          ^    ^  ^  ^       ^
      where the   ^    symbols are just to help you see the items that changed.
      Note that:
        -- If there are no zeros in the given sequence of lists,
             then this function does nothing.
        -- After this function call, the sequence of lists IN THE CALLER
             should contain no zeros.
    Type hints:
      :type tuple_of_lists: tuple[list[int]]
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
    print_function_call_of_test(function_to_test, argument)
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


def print_function_call_of_test(function_to_test, argument):
    print("  This test case calls: {}".format(function_to_test.__name__))
    print("  with argument:")
    print(" ", argument)


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
