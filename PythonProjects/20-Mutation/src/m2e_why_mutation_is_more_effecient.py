"""
This module demonstrates how MUTATION allows for MORE EFFICIENT
use of TIME and SPACE when a container object repeatedly has its
insides change.

Authors: David Mutchler, Vibha Alangar, Dave Fisher, Matt Boutell, Mark Hays,
         Mohammed Noureddine, Sana Ebrahimi, Sriram Mohan, and their colleagues.
"""
# -----------------------------------------------------------------------------
# Students: Your instructor may ask you to read and run this program, or
#   your instructor may use a different way to show why mutation
#   is more efficient than the alternative (copy/mutate/return).
#
# Students: Read and run this program.
#    Do you see how   MUTATION   made possible
#    the more efficient use of time and space?
# -----------------------------------------------------------------------------

import time


def main():
    """
    This program compares two approaches to sending information
    back to the caller via a list:
      1. Mutate the list.
      2. Copy the list, mutate the copy, and return the copy.
    For each approach, the program does the approach many times
    and prints how long the approach took.
    """
    # -------------------------------------------------------------------------
    # Try changing the variables:
    #    number_of_repetitions
    #    length_of_list
    # to see what happens in larger cases.
    # -------------------------------------------------------------------------
    number_of_repetitions = 1000  # Try 100, 1000, 10000 ...should take 10x time
    length_of_list = 1000  # Try 1000, 2000, 4000, 8000, ...
    print()
    print("Running {} repetitions on a list".format(number_of_repetitions))
    print("whose length is {}.".format(length_of_list))

    list_of_zeros_for_mutation = make_list(length_of_list)
    list_of_zeros_for_copy_return = make_list(length_of_list)

    # -------------------------------------------------------------------------
    # Return information to the caller (increment the last item in the list)
    # by MUTATING the argument.  This should be fast:
    # -------------------------------------------------------------------------
    start_time = time.time()

    for _ in range(number_of_repetitions):
        mutate(list_of_zeros_for_mutation)

    end_time = time.time()

    print("  -- Mutating took {:6.4f} seconds.".format(end_time - start_time))

    # -------------------------------------------------------------------------
    # Return information to the caller (increment the last item in the list)
    # by COPYING the argument, mutating it, and returning the  mutated copy.
    # This should be slow:
    # -------------------------------------------------------------------------
    start_time = time.time()

    for _ in range(number_of_repetitions):
        result = copy_return(list_of_zeros_for_copy_return)

    end_time = time.time()

    print("  -- Copy-returning took {:6.4f} seconds.".format(
        end_time - start_time))


def make_list(n):
    """ Returns a list of   n   zeros, for the given argument n. """
    zeros = []
    for _ in range(n):
        zeros.append(0)  # FWIW, the  append   method uses mutation

    return zeros


def mutate(numbers):
    """ Mutates the given list by making its last item one larger. """
    numbers[len(numbers) - 1] = numbers[len(numbers) - 1] + 1


def copy_return(numbers):
    """
    Returns a copy of the given list, but with the last item in the copy
    being one larger than the last item in the given list.
    """
    copy = []

    for k in range(len(numbers)):
        # The following makes the copy WITHOUT mutating it.  If you think
        # that that is cheating, use the commented-out version instead.
        copy = copy + [numbers[k]]
        # copy.append(numbers[k])  # Still worse than mutation, but less so.

    copy[len(copy) - 1] = copy[(len(copy) - 1)] + 1
    return copy


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
