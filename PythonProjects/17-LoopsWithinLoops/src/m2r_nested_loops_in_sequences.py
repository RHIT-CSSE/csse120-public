"""
This project demonstrates NESTED LOOPS (i.e., loops within loops)
in the context of SEQUENCES OF SUB-SEQUENCES.

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Mark Hays, Amanda Stouder, Derek Whitley, their colleagues,
         many others before them, and now PUT_YOUR_NAME_HERE.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

###############################################################################
# TODO: 2.  Read and run this program, examining the code and the output.
#           Then answer the questions below, writing answers in this comment.
#  __
#   1. Which feels more clear to you?
#        -- classic_example_1, or
#        -- classic_example_2
#   Note: reasonable people could disagree on the answer to this question.
#  __
#   2. Do you understand why the final example crashes?
#        Yes or No?     [If No, ASK FOR HELP NOW!]
#  __
#   3. Do you believe that you can you READ and TRACE BY HAND
#      simple nested loops like the examples in this module?
#        Yes or No?     [If No, ASK FOR HELP NOW!]
#  __
#  After you have completed the above, change the above _TODO_ to DONE.
#  As always,  *** GET HELP AS NEEDED.  ***
###############################################################################

import time
import testing_helper


def main():
    """ Calls the other functions to demonstrate them. """
    list_of_lists = [[4, 0, 100],
                     [1, 2, 3],
                     [100, 100, 20, 30, 20, 1]]

    tuple_of_lists = ([10, 5],
                      [5, 10, 5, 8, 20],
                      ["a", "b", "c", 8],
                      ["the", "rain", "in spain", 5, "falls"],
                      ["mainly on the plain."])

    list_of_strings = ["hello", "how", "are", "you?"]

    # -------------------------------------------------------------------------
    # Calls  classic_example_1   to PRINT all the sub-items.
    # -------------------------------------------------------------------------
    classic_example_1(list_of_lists)
    classic_example_1(tuple_of_lists)
    classic_example_1(list_of_strings)

    # -------------------------------------------------------------------------
    # Calls  classic_example_2   to show the equivalent [][] notation.
    # -------------------------------------------------------------------------
    classic_example_2(list_of_lists)
    classic_example_2(tuple_of_lists)
    classic_example_2(list_of_strings)

    # -------------------------------------------------------------------------
    # Calls  classic_example_3   to show mutating a sequence of lists.
    # The final example shows that attempting to mutate a STRING fails.
    # -------------------------------------------------------------------------
    count = classic_example_3(list_of_lists, 100, "oops")
    print("Number of occurrences of {} is {}.".format(100, count))
    print("The mutated list of lists is:")
    print(list_of_lists)

    count = classic_example_3(tuple_of_lists, 5, "five")
    print("Number of occurrences of {} is {}.".format(5, count))
    print("The mutated tuple of lists is:")
    print(tuple_of_lists)

    # The next example will throw a TypeError (and crash) with this message:
    #   TypeError: 'str' object does not support item assignment
    count = classic_example_3(list_of_strings, "o", "x")
    print("Number of occurrences of {} is {}.".format("o", count))
    print("The mutated list of STRINGS is:")
    print(list_of_strings)


def classic_example_1(sequence_of_sequences):
    """ Prints the items in the sequence of sequences. """
    print()
    print("------------------------------------------------")
    print("Classic example 1 on this sequence of sequences:")
    print(sequence_of_sequences)
    print("------------------------------------------------")

    for k in range(len(sequence_of_sequences)):
        sequence = sequence_of_sequences[k]
        print("  Beginning inner sequence at outer index", k)
        for j in range(len(sequence)):
            print(sequence[j])
        print("  Ending inner sequence at outer index", k)


def classic_example_2(sequence_of_sequences):
    """ Same as preceding example but using [][] notation. """
    print()
    print("------------------------------------------------")
    print("Classic example 2 on this sequence of sequences:")
    print(sequence_of_sequences)
    print("------------------------------------------------")

    for k in range(len(sequence_of_sequences)):
        print("  Beginning inner sequence at outer index", k)
        for j in range(len(sequence_of_sequences[k])):
            print(sequence_of_sequences[k][j])
        print("  Ending inner sequence at outer index", k)


def classic_example_3(sequence_of_sequences,
                      what_to_count, what_to_mutate_into):
    """
    Shows counting and mutating in a sequence of LISTS.
      -- Counts and returns the number of "what_to_count" occurrences.
      -- Mutates those occurrences into the "what_to_mutate_into".
    """
    print()
    print("------------------------------------------------")
    print("Classic example 3 on this sequence of LISTS:")
    print(sequence_of_sequences)
    print("------------------------------------------------")

    count = 0
    for k in range(len(sequence_of_sequences)):
        sequence = sequence_of_sequences[k]
        for j in range(len(sequence)):
            if sequence[j] == what_to_count:
                count = count + 1
                sequence[j] = what_to_mutate_into
    return count


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# The   try .. except   prevents error messages on the console from being
# intermingled with ordinary output to the console.
# -----------------------------------------------------------------------------
# To allow color-coding the output to the console:
USE_COLORING = True  # Change to False to revert to OLD style coloring

testing_helper.USE_COLORING = USE_COLORING
if USE_COLORING:
    # noinspection PyShadowingBuiltins
    print = testing_helper.print_colored
else:
    # noinspection PyShadowingBuiltins
    print = testing_helper.print_uncolored

try:
    main()
except Exception:
    print("ERROR - While running this test,", color="red")
    print("your code raised the following exception:", color="red")
    print()
    time.sleep(1)
    raise
