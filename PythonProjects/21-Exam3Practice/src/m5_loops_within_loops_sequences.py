"""
PRACTICE Exam 3.

This problem provides practice at:
  ***  LOOPS WITHIN LOOPS in SEQUENCE of SEQUENCES problems.  ***

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
    run_test_integers()
    run_test_big_letters()
    run_test_problem2a()
    run_test_problem2b()


def run_test_integers():
    """ Tests the    integers    function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   integers   function:')
    print('--------------------------------------------------')

    format_string = '    integers( {} )'
    test_results = [0, 0]  # Number of tests passed, failed.

    # -------------------------------------------------------------------------
    # Test 1:
    # -------------------------------------------------------------------------
    sequence_of_sequences = [(3, 1, 4),
                             (10, 'hi', 10),
                             [1, 2.5, 3, 4],
                             'hello',
                             [],
                             ['oops'],
                             [[55], [44]],
                             [30, -4]
                             ]
    expected = [3, 1, 4, 10, 10, 1, 3, 4, 30, -4]
    print_expected_result_of_test([sequence_of_sequences], expected,
                                  test_results, format_string)
    actual = integers(sequence_of_sequences)
    print_actual_result_of_test(expected, actual, test_results)

    # -------------------------------------------------------------------------
    # Test 2:
    # -------------------------------------------------------------------------
    sequence_of_sequences = [(3, 1, 4, 'hmmm', [3, 1, 4], 55555555555),
                             'this is a string',
                             'ok',
                             [],
                             ['oops'],
                             [[55], 5555, [44], 4444, (4, 5), 4, 5],
                             (),
                             [1, 2, 3, 4, 5, 1, 2, 3, 4, 5],
                             [1000],
                             (1, 2, 3, 4, 5, 1, 2, 3, 4, 5),
                             (1000,)
                             ]
    expected = [3, 1, 4, 55555555555, 5555, 4444, 4, 5, 1, 2, 3, 4, 5,
                1, 2, 3, 4, 5, 1000, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1000]
    print_expected_result_of_test([sequence_of_sequences], expected,
                                  test_results, format_string)
    actual = integers(sequence_of_sequences)
    print_actual_result_of_test(expected, actual, test_results)

    # SUMMARY of test results:
    print_summary_of_test_results(test_results)


def integers(sequence_of_sequences):
    """
    Returns a new list that contains all the integers in the subsequences
    of the given sequence, in the order that they appear in the subsequences.
    For example, if the argument is:
        [(3, 1, 4),
         (10, 'hi', 10),
         [1, 2.5, 3, 4],
         'hello',
         [],
         ['oops'],
         [[55], [44]],
         [30, -4]
        ]
    then this function returns:
        [3, 1, 4, 10, 10, 1, 3, 4, 30, -4]

    Type hints:
      :type sequence_of_sequences: (list|tuple) of (list|tuple|string)
      :rtype: list of int
    """
    # -------------------------------------------------------------------------
    # TODO: 3. Implement and test this function.
    #          Tests have been written for you (above).
    #  ########################################################################
    #  HINT: The
    #           type
    #       function can be used to determine the type of
    #       its argument (and hence to see if it is an integer).
    #       For example, you can write expressions like:
    #         -- if type(34) is int: ...
    #         -- if type(4.6) is float: ...
    #         -- if type('three') is str: ...
    #         -- if type([1, 2, 3]) is list: ...
    #       Note that the returned values do NOT have quotes.
    #       Also, the   is   operator tests for equality (like ==)
    #       but is more appropriate than == in this situation.
    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------
    # DIFFICULTY AND TIME RATINGS (see top of this file for explanation)
    #    DIFFICULTY:      5
    #    TIME ESTIMATE:  10 minutes.
    # -------------------------------------------------------------------------


def run_test_big_letters():
    """ Tests the    big_letters    function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   big_letters   function:')
    print('--------------------------------------------------')

    format_string = '    big_letters( {} )'
    test_results = [0, 0]  # Number of tests passed, failed.

    # -------------------------------------------------------------------------
    # Test 1:
    # -------------------------------------------------------------------------
    sequence_of_sequences = [(3, 1, 4),  # not a string
                             'wHAS what?',  # HAS
                             ['oops'],  # not a string
                             'oops',  #
                             ['OOPS'],  # not a string
                             '1 THIS !',  # THIS
                             ]
    expected = 'HASTHIS'
    print_expected_result_of_test([sequence_of_sequences], expected,
                                  test_results, format_string)
    actual = big_letters(sequence_of_sequences)
    print_actual_result_of_test(expected, actual, test_results)

    # -------------------------------------------------------------------------
    # Test 2:
    # -------------------------------------------------------------------------
    sequence_of_sequences = [(3, 1, 4),  # not a string
                             'Ok what is ThiSSS?',  # OTSSS
                             (10, 'Ok what is ThiSSS?', 10),  # not a string
                             [],  # not a string
                             ['oops'],  # not a string
                             'oops',  #
                             ['OOPS'],  # not a string
                             '1 OOPS !',  # OOPS
                             'A',  # A
                             'ooPS $$&*#%&&',  # PS
                             'B',  # B
                             'oOpS',  # OS
                             'C',  # C
                             'OoPs'  # OP
                             'D',  # D
                             'OOps'  # OO
                             ]
    expected = 'OTSSSOOPSAPSBOSCOPDOO'
    print_expected_result_of_test([sequence_of_sequences], expected,
                                  test_results, format_string)
    actual = big_letters(sequence_of_sequences)
    print_actual_result_of_test(expected, actual, test_results)

    # SUMMARY of test results:
    print_summary_of_test_results(test_results)


def big_letters(sequence_of_sequences):
    """
    Returns a new STRING that contains all the upper-case letters
    in the subsequences of the given sequence that are strings,
    in the order that they appear in the subsequences.
    For example, if the argument is:
        [(3, 1, 4),                          # not a string
        'Ok what is ThiSSS?',                # OTSSS
        (10, 'Ok what is ThiSSS?', 10),      # not a string
        [],                                  # not a string
        ['oops'],                            # not a string
        'oops',                              #
        ['OOPS'],                            # not a string
        '1 OOPS !',                          # OOPS
        'A',                                 # A
        'ooPS $$&*#%&&',                     # PS
        'B',                                 # B
        'oOpS',                              # OS
        'C',                                 # C
        'OoPs'                               # OP
        'D',                                 # D
        'OOps'                               # OO
         ]
    then this function returns:
        'OTSSSOOPSAPSBOSCOPDOO'

    Precondition:  the given argument is a sequence of sequences.
    """
    # -------------------------------------------------------------------------
    # TODO: 4. Implement and test this function.
    #          Tests have been written for you (above).
    #  ########################################################################
    #  HINTS: The  type   function can be used to identify strings,
    #         per the HINT in the previous problem.
    #  ALSO:
    #   There is a STRING METHOD that determines whether or not
    #   a string contains upper-case letters.  To find that method,
    #   somewhere in this file type:
    #           "".
    #   and pause after the dot.
    #   That will display ALL the STRING methods.
    #  __
    #   Look for a method whose name begins with
    #           is
    #   e.g. isalnum()  isdigit() ... [but find the one for upper-case letters]
    ###########################################################################
    # -------------------------------------------------------------------------
    # DIFFICULTY AND TIME RATINGS (see top of this file for explanation)
    #    DIFFICULTY:      7
    #    TIME ESTIMATE:  12 minutes.
    # -------------------------------------------------------------------------


def run_test_problem2a():
    """ Tests the   problem2a   function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   problem2a  function:')
    print('--------------------------------------------------')

    format_string = '    problem2a( {} )'
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    numbers = ([5, 1],
               [0, 3, 4],
               [6, 3])
    expected = [5, 3, 4, 6]
    print_expected_result_of_test([numbers],
                                  expected, test_results, format_string)
    actual = problem2a(numbers)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 2:
    numbers = ([5, 1, 1, 1, 1],
               [1, 4, 4, 1, 1, 1, 1],
               [6, 3, 2, 3, 4, 5, 6, 7, 8, 9],
               [1, 2, 3, 4, 5])
    expected = [5, 4, 4, 6]
    print_expected_result_of_test([numbers],
                                  expected, test_results, format_string)
    actual = problem2a(numbers)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 3:
    numbers = ([5, 1, 1, 1, 1],
               [1, 6, 5, 1, 1, 1, 1],
               [6, 3, 2, 3, 4, 5, 6, 7, 8, 9],
               [1, 2, 3, 4, 5],
               [5, 6, 7, 8, 9, 10, 11, 12])
    expected = [5, 6, 5, 6, 5, 6, 7, 8, 9, 10, 11, 12]
    print_expected_result_of_test([numbers],
                                  expected, test_results, format_string)
    actual = problem2a(numbers)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 4:
    numbers = ([1, 2, 1, 1, 1],
               [1, 6, 5, 1, 1, 1, 1],
               [6, 3, 2, 3, 4, 5, 6, 7, 8, 9],
               [1, 2, 3, 4, 5],
               [5, 6, 7, 8, 9, 10, 11, 12])
    expected = [1, 2, 6, 5, 6, 5, 6, 7, 8, 9, 10, 11, 12]
    print_expected_result_of_test([numbers],
                                  expected, test_results, format_string)
    actual = problem2a(numbers)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 5:
    numbers = ([100, 200, 1, 1, 1],
               [1, 6, 5, 1, 1, 1, 1],
               [6, 3, 2, 3, 4, 5, 6, 7, 8, 9],
               [1, 2, 3, 4, 5],
               [5],
               [5, 6, 7, 8, 9, 10, 11, 12])
    expected = [100, 200, 6, 5, 6, 5]
    print_expected_result_of_test([numbers],
                                  expected, test_results, format_string)
    actual = problem2a(numbers)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 6:
    numbers = ([100, 200, 99],
               [300])
    expected = [100, 200, 99, 300]
    print_expected_result_of_test([numbers],
                                  expected, test_results, format_string)
    actual = problem2a(numbers)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 7:
    numbers = ([98, 200, 99],
               [300])
    expected = [98, 200, 99, 300]
    print_expected_result_of_test([numbers],
                                  expected, test_results, format_string)
    actual = problem2a(numbers)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 8:
    numbers = ([100, 200, 99],
               [1, 3])
    expected = [100, 200, 99, 3]
    print_expected_result_of_test([numbers],
                                  expected, test_results, format_string)
    actual = problem2a(numbers)
    print_actual_result_of_test(expected, actual, test_results)

    # SUMMARY of test results:
    print_summary_of_test_results(test_results)


def problem2a(numbers):
    """
    What comes in:  A non-empty sequence of non-empty sequences
      of positive integers.
    What goes out:  Returns a list containing every number in the sub-sequences
      that is bigger than the sum of its indices.
      The numbers in the returned list should appear in the same order
      that the numbers appear in the subsequences.
    Examples:
      Suppose that  numbers  is:
          ([5, 1],
           [0, 3, 4],
           [6, 3])
         Then: problem2a(numbers) examines:
        -- 5: It is at numbers[0][0], so sum of indices is 0,
              so PUT 5 into the list to return.
        -- 1: It is at numbers[0][1], so sum of indices is 1,
              so do NOT put 1 into the list to return.
        -- 0: It is at numbers[1][0], so sum of indices is 1,
              so do NOT put 0 into the list to return.
        -- 3: It is at numbers[1][1], so sum of indices is 2,
              so PUT 3 into the list to return.
        -- 4: It is at numbers[1][2], so sum of indices is 3,
              so PUT 4 into the list to return.
        -- 6: It is at numbers[2][0], so sum of indices is 2,
              so PUT 6 into the list to return.
        -- 3: It is at numbers[2][1], so sum of indices is 3,
              so do NOT put 3 into the list to return.
        So on this example, problem2a returns [5, 3, 4, 6]

      ** ASK YOUR INSTRUCTOR FOR HELP **
      ** if this example and the above specification are not clear to you. **
     """
    ###########################################################################
    # TODO: 5. Implement and test this function.
    #          Tests have been written for you (above).
    ###########################################################################
    # -------------------------------------------------------------------------
    # DIFFICULTY AND TIME RATINGS (see top of this file for explanation)
    #    DIFFICULTY:      6
    #    TIME ESTIMATE:  12 minutes.
    # -------------------------------------------------------------------------


def run_test_problem2b():
    """ Tests the   problem2b   function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   problem2b  function:')
    print('--------------------------------------------------')

    format_string = '    problem2b( {} )'
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    numbers = ([5, 1, 8, 3],
               [0, -3, 7, 8, 1],
               [6, 3, 5, 5, -10, 12])
    expected = 5 + 8 + 7 + 8 + 6 + 5 + 5 + 12  # which is 56 (A = 17/4 = 4.25)
    print_expected_result_of_test([numbers], expected, test_results,
                                  format_string)
    actual = problem2b(numbers)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 2:
    numbers = ([5, 1, 1, 1, 1, 3],
               [1, 4, 4, 1, 1, 1, 1],
               [6, 3, 2, 3, 4, 5, 6, 7, 8, 9],
               [1, 2, 3, 2, 1])
    # so A = 12/6 = 2 and
    expected = 5 + 3 + 4 + 4 + 6 + 3 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 3  # = 70
    print_expected_result_of_test([numbers], expected, test_results,
                                  format_string)
    actual = problem2b(numbers)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 3:
    numbers = ([5, 1, 1, 1, 1],
               [1, 6, 5, 1, 1, 1, 1],
               [6, 3, 2, 3, 4, 5, 6, 7, 8, 9],
               [1, 2, 3, 4, 5],
               [5, 6, 7, 8, 9, 10, 11, 12])
    expected = 151
    print_expected_result_of_test([numbers], expected, test_results,
                                  format_string)
    actual = problem2b(numbers)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 4:
    numbers = ([1, 2, 1, 1, 1],
               [1, 6, 5, 1, 1, 1, 1],
               [6, 3, 2, 3, 4, 5, 6, 7, 8, 9],
               [1, 2, 3, 4, 5],
               [5, 6, 7, 8, 9, 10, 11, 12])
    expected = 148
    print_expected_result_of_test([numbers], expected, test_results,
                                  format_string)
    actual = problem2b(numbers)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 5:
    numbers = ([100, 200, 1, 1, 1],
               [1, 6, 5, 1, 1, 1, 1],
               [6, 3, 2, 3, 4, 5, 6, 7, 8, 9],
               [1, 2, 3, 4, 5],
               [5],
               [5, 6, 7, 8, 9, 10, 11, 12])
    expected = 300
    print_expected_result_of_test([numbers], expected, test_results,
                                  format_string)
    actual = problem2b(numbers)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 6:
    numbers = ([100, 200, 99],
               [300])
    expected = 500
    print_expected_result_of_test([numbers], expected, test_results,
                                  format_string)
    actual = problem2b(numbers)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 7:
    numbers = ([98, 200, 99],
               [300])
    expected = 500
    print_expected_result_of_test([numbers], expected, test_results,
                                  format_string)
    actual = problem2b(numbers)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 8:
    numbers = ([100, 200, 99],
               [50])
    expected = 200
    print_expected_result_of_test([numbers], expected, test_results,
                                  format_string)
    actual = problem2b(numbers)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 9:
    numbers = ([-4],
               [],
               [],
               [-3, 0, 1, 2, 3],
               [-3.99],
               [-4.0000000001])
    expected = -0.99  # from -3 + 0 + 1 + 2 + 3 + (-3.99)
    print_expected_result_of_test([numbers], expected, test_results,
                                  format_string, suffix="(approximately)")
    actual = problem2b(numbers)
    print_actual_result_of_test(expected, actual, test_results, precision=6)

    # Test 10:
    numbers = ([-99999999999],
               [],
               [])
    expected = 0
    print_expected_result_of_test([numbers], expected, test_results,
                                  format_string)
    actual = problem2b(numbers)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 11:
    numbers = ([1, 4],
               [3, 3, 3, 3],
               [],
               [2.49, 2.48, 2.49],
               [])
    expected = 4 + 3 + 3 + 3 + 3  # = 16
    print_expected_result_of_test([numbers], expected, test_results,
                                  format_string)
    actual = problem2b(numbers)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 12:
    numbers = ([1, -1],)
    expected = 1
    print_expected_result_of_test([numbers], expected, test_results,
                                  format_string)
    actual = problem2b(numbers)
    print_actual_result_of_test(expected, actual, test_results)

    # SUMMARY of test results:
    print_summary_of_test_results(test_results)


def problem2b(numbers):
    """
    What comes in:  A non-empty sequence of sequences of numbers,
      with the first sub-sequence being non-empty.
    What goes out:  Returns the sum of all the numbers in the subsequences
      that are bigger than A,
      where A is the average of the numbers in the FIRST sub-sequence.
    Side effects:  None.
    Examples:
      Suppose that  numbers  is:
          ([5, 1, 8, 3],
           [0, -3, 7, 8, 1],
           [6, 3, 5, 5, -10, 12])
      Then: the average of the numbers in the first sub-sequence is
        (5 + 1 + 8 + 3) / 4, which is 17 / 4, which is 4.25, and so
        problem2b(numbers)   returns   (5 + 8 + 7 + 8 + 6 + 5 + 5 + 12),
        which is 56, since the numbers in that sum are the numbers
        in the subsequences that are bigger than 4.25.
      ** ASK YOUR INSTRUCTOR FOR HELP **
      ** if this example and the above specification are not clear to you. **
     """
    ###########################################################################
    # TODO: 6. Implement and test this function.
    #          Tests have been written for you (above).
    ###########################################################################
    ###########################################################################
    # -------------------------------------------------------------------------
    # DIFFICULTY AND TIME RATINGS (see top of this file for explanation)
    #    DIFFICULTY:      7
    #    TIME ESTIMATE:  15 minutes.
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
                                                 test_results,
                                                 format_string,
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
