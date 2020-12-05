"""
PRACTICE Exam 3.

This problem provides practice at:
  ***  LOOPS WITHIN LOOPS in SEQUENCE of SEQUENCES problems.  ***

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
    run_test_integers()
    run_test_big_letters()


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
    # TODO: 5. Implement and test this function.
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
