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

    # run_test_multiply_numbers()
    # run_test_print_characters()
    # run_test_print_characters_slanted()


def run_test_multiply_numbers():
    """ Tests the   multiply_numbers   function. """
    # -------------------------------------------------------------------------
    # We have supplied tests for you. No additional tests are required,
    # although you are welcome to supply more tests if you choose.
    # -------------------------------------------------------------------------
    print()
    print("------------------------------------------------------")
    print("Testing the   multiply_numbers   function:")
    print("------------------------------------------------------")

    format_string = "    multiply_numbers( {} )"
    test_results = [0, 0]  # Number of tests passed, failed.

    # -------------------------------------------------------------------------
    # Test 1: Tests whether the function MUTATES the sub-lists correctly.
    seq_of_lists = ([4, 2, 1],
                    [8, 0],
                    [1, 2, 3, 4, 5],
                    [],
                    [101])
    # After the function call, seq_of_lists should be as follows:
    seq_of_lists_after_multiply = ([4, 2, 1],
                                   [16, 0],
                                   [3, 6, 9, 12, 15],
                                   [],
                                   [505])
    print_expected_result_of_test([seq_of_lists],
                                  seq_of_lists_after_multiply,
                                  test_results, format_string)
    actual = multiply_numbers(seq_of_lists)
    print_actual_result_of_test(seq_of_lists_after_multiply, seq_of_lists,
                                test_results)
    print("The above is for  seq_of_lists  (whose lists should be MUTATED.")

    # Test 2: (a continuation of Test 1)
    #   Tests whether the function does not RETURN a value (i.e., returns None)
    print_expected_result_of_test([seq_of_lists], None,
                                  test_results, format_string)
    print_actual_result_of_test(None, actual, test_results)
    print("The above is for the RETURNED VALUE, which should be")
    print("the constant None, NOT the STRING \"None\".")
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # Test 3: Tests whether the function MUTATES the sub-lists correctly.
    seq_of_lists = ([4, 0, 100],
                    [1, 2, 3],
                    [100, 100, 20, 30])
    # After the function call, seq_of_lists should be as follows:
    seq_of_lists_after_multiply = ([4, 0, 100],
                                   [2, 4, 6],
                                   [300, 300, 60, 90])
    print_expected_result_of_test([seq_of_lists],
                                  seq_of_lists_after_multiply,
                                  test_results, format_string)
    actual = multiply_numbers(seq_of_lists)
    print_actual_result_of_test(seq_of_lists_after_multiply, seq_of_lists,
                                test_results)
    print("The above is for  seq_of_lists  (whose lists should be MUTATED.")

    # Test 4: (a continuation of Test 3)
    #   Tests whether the function does not RETURN a value (i.e., returns None)
    print_expected_result_of_test([seq_of_lists], None,
                                  test_results, format_string)
    print_actual_result_of_test(None, actual, test_results)
    print("The above is for the RETURNED VALUE, which should be")
    print("the constant None, NOT the STRING \"None\".")
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # Test 5: Tests whether the function MUTATES the sub-lists correctly.
    seq_of_lists = (["the ", "rain "],
                    ["in spain ", "falls ", "mainly on the "],
                    ["plain."])
    # After the function call, seq_of_lists should be as follows:
    seq_of_lists_after_multiply = (["the ", "rain "],
                                   ["in spain in spain ",
                                    "falls falls ",
                                    "mainly on the mainly on the "],
                                   ["plain.plain.plain."])
    print_expected_result_of_test([seq_of_lists],
                                  seq_of_lists_after_multiply,
                                  test_results, format_string)
    actual = multiply_numbers(seq_of_lists)
    print_actual_result_of_test(seq_of_lists_after_multiply, seq_of_lists,
                                test_results)
    print("The above is for  seq_of_lists  (whose lists should be MUTATED.")

    # Test 6: (a continuation of Test 5)
    #   Tests whether the function does not RETURN a value (i.e., returns None)
    print_expected_result_of_test([seq_of_lists], None,
                                  test_results, format_string)
    print_actual_result_of_test(None, actual, test_results)
    print("The above is for the RETURNED VALUE, which should be")
    print("the constant None, NOT the STRING \"None\".")
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # Test 7: Tests whether the function MUTATES the sub-lists correctly.
    seq_of_lists = [[10, 5],
                    [10, 5, 5, 8, 20],
                    ["a", "b", "c"],
                    ["d"],
                    ["e", "f"],
                    [100, 0, "z"]]
    # After the function call, seq_of_lists should be as follows:
    seq_of_lists_after_multiply = [[10, 5],
                                   [20, 10, 10, 16, 40],
                                   ["aaa", "bbb", "ccc"],
                                   ["dddd"],
                                   ["eeeee", "fffff"],
                                   [600, 0, "zzzzzz"]]
    print_expected_result_of_test([seq_of_lists],
                                  seq_of_lists_after_multiply,
                                  test_results, format_string)
    actual = multiply_numbers(seq_of_lists)
    print_actual_result_of_test(seq_of_lists_after_multiply, seq_of_lists,
                                test_results)
    print("The above is for  seq_of_lists  (whose lists should be MUTATED.")

    # Test 8: (a continuation of Test 7)
    #   Tests whether the function does not RETURN a value (i.e., returns None)
    print_expected_result_of_test([seq_of_lists], None,
                                  test_results, format_string)
    print_actual_result_of_test(None, actual, test_results)
    print("The above is for the RETURNED VALUE, which should be")
    print("the constant None, NOT the STRING \"None\".")
    # -------------------------------------------------------------------------

    # SUMMARY of test results:
    print_summary_of_test_results(test_results)


def multiply_numbers(sequence_of_lists):
    """
    What comes in:
       -- a sequence of lists, with each item in the lists being something
          that can be multiplied by an integer
     What goes out: Nothing (i.e. None).
     Side effects: MUTATES the given lists by:
      -- multiplies each item of the first list by 1,
      -- multiplies each item of the second list by 2,
      -- multiplies each item of the third list by 3,
      -- and so forth.
      For example, consider the following code:
          seq_of_lists = ([4, 2, 1],
                          [8, 0],
                          [1, 2, 3, 4, 5],
                          [],
                          [101])
          v = multiply_numbers(seq_of_lists)
      After the above code runs,
          v (the returned value) should be None
          and  seq_of_lists  should be:
                       ([4, 2, 1],
                        [16, 0],
                        [3, 6, 9, 12, 15],
                        [],
                        [505])
    Type hints:
       :type sequence_of_lists:  sequence of lists, with each item
       in the lists being something that can be multiplied by an integer
       [FYI: The "can be multiplied ..." is an example of DUCK TYPING.]
    """
    # -------------------------------------------------------------------------
    # TODO: 2. Implement and test this function.
    #  ** READ THE TESTS that have been written for you (ABOVE).
    #  ** ASK QUESTIONS if you do not understand the TESTS (ABOVE).
    # -------------------------------------------------------------------------


def run_test_print_characters():
    """ Tests the    print_characters    function. """
    # -------------------------------------------------------------------------
    # We have supplied tests for you. No additional tests are required,
    # although you are welcome to supply more tests if you choose.
    # -------------------------------------------------------------------------
    print()
    print("------------------------------------------")
    print("Testing the   PRINT_CHARACTERS   function:")
    print("------------------------------------------")

    # Test 1:
    print()
    print("The following should be:")
    print("  h")
    print("  i")
    print("  b")
    print("  y")
    print("  e")
    print("  a")
    print("   ")
    print("  t")
    print("  i")
    print("  e")
    print("  !")
    print("but without the leading spaces:")
    print_characters(["hi", "bye", "a tie!"])

    # Test 2:
    print()
    print("The following should be:")
    print("  9876abc67 89z")
    print("but printed in a COLUMN, one character per line:")
    print_characters(["9876", "abc", "", "67 89", "z"])


def print_characters(sequence_of_strings):
    """
    Prints all the characters in the sequence of strings,
    but each character on ITS OWN LINE.  For example,
    if the given argument is ["hi", "bye", "a tie!"],
    then this function prints:
       h
       i
       b
       y
       e
       a

       t
       i
       e
       !
    Precondition:  the given argument is a sequence of strings.
    """
    # -------------------------------------------------------------------------
    # TODO: 3. Implement and test this function.
    #  ** READ THE TESTS that have been written for you (ABOVE).
    #  ** ASK QUESTIONS if you do not understand the TESTS (ABOVE).
    # -------------------------------------------------------------------------


def run_test_print_characters_slanted():
    """ Tests the    print_characters_slanted    function. """
    # -------------------------------------------------------------------------
    # We have supplied tests for you. No additional tests are required,
    # although you are welcome to supply more tests if you choose.
    # -------------------------------------------------------------------------
    print()
    print("--------------------------------------------------")
    print("Testing the   PRINT_CHARACTERS_SLANTED   function:")
    print("--------------------------------------------------")

    # Test 1:
    print()
    print("The following should be:")
    print("h")
    print(" i")
    print("b")
    print(" y")
    print("  e")
    print("a")
    print(" _")
    print("  t")
    print("   i")
    print("    e")
    print("     !")
    print("Actual result:")
    print_characters_slanted(["hi", "bye", "a_tie!"])

    # Test 2:
    print()
    print("The following should be:")
    print("a")
    print(" b")
    print("  c")
    print("   d")
    print("    e")
    print("x")
    print("y")
    print("z")
    print(" z")
    print("  z")
    print("1")
    print(" 2")
    print("  3")
    print("   4")
    print("Actual result:")
    print_characters_slanted(["abcde", "x", "y", "zzz", "1234"])


def print_characters_slanted(sequence_of_strings):
    """
    Same as the previous problem, but each string "slants".
    For example, if the given argument is ["hi", "bye", "a_tie!"],
    then this function prints:
       h
        i
       b
        y
         e
       a
        _
         t
          i
           e
            !
    Precondition:  the given argument is a sequence of strings.
    """
    # -------------------------------------------------------------------------
    # TODO: 4. Implement and test this function.
    #  ** READ THE TESTS that have been written for you (ABOVE).
    #  ** ASK QUESTIONS if you do not understand the TESTS (ABOVE).
    #  __
    #  ** HINT: ** Consider using string multiplication for the spaces
    #              and string addition to stitch the spaces to the character.
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
