"""
This module demonstrates how MUTATION allows for MORE EFFICIENT
use of TIME and SPACE when a container object repeatedly has its
insides change.

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Mark Hays, Amanda Stouder, Derek Whitley, and their colleagues.
"""
# -----------------------------------------------------------------------------
# Students: Read and run this program.
#           Do you see how   MUTATION   made the more efficient use
#           of time and space possible?
# -----------------------------------------------------------------------------

import time


def main():
    # -------------------------------------------------------------------------
    # Try changing the variables:
    #    number_of_mutations_to_perform
    #    number_of_copy_and_changes_to_perform
    # to see what happens in larger cases.
    # -------------------------------------------------------------------------
    number_of_mutations_to_perform = 1000
    number_of_copy_and_changes_to_perform = 1000

    zeros1 = make_list(number_of_mutations_to_perform)
    zeros2 = make_list(number_of_copy_and_changes_to_perform)

    # -------------------------------------------------------------------------
    # This changes the list by mutating the list.
    # This should be fast:
    # -------------------------------------------------------------------------
    start_time = time.time()

    for _ in range(number_of_mutations_to_perform):
        mutate_list(zeros1)

    end_time = time.time()

    format_string = 'Mutating the list {} times took {:6.4f} seconds.'
    print(format_string.format(number_of_mutations_to_perform,
                               end_time - start_time))

    # -------------------------------------------------------------------------
    # This changes the list by copying-and-changing the list;
    # no mutation.
    # This should be slow:
    # -------------------------------------------------------------------------
    start_time = time.time()

    for _ in range(number_of_copy_and_changes_to_perform):
        zeros2 = copy_and_change_list(zeros2)

    end_time = time.time()

    format_string = 'Copy-and-changing the list {} times took {:6.4f} seconds.'
    print(format_string.format(number_of_copy_and_changes_to_perform,
                               end_time - start_time))


def make_list(n):
    """ Returns a list of   n   zeros, for the given argument n. """
    zeros = []
    for _ in range(n):
        zeros.append(0)  # FWIW, the  append   method uses mutation

    return zeros


def mutate_list(numbers):
    """ Mutates the given list by making its last item one larger. """
    numbers[len(numbers) - 1] = numbers[len(numbers) - 1] + 1


def copy_and_change_list(numbers):
    """
    Returns a copy of the given list, but with the last item in the copy
    being one larger than the last item in the given list.
    """
    copy = []

    for k in range(len(numbers)):
        copy = copy + [numbers[k]]

    copy[len(copy) - 1] = copy[(len(copy) - 1)] + 1
    return copy


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
