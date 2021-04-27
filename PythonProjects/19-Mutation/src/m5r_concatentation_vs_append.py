"""
This module compares two ways of appending items to a list:
    r = r + [item]
    r.append(item)
Run this module to see which is faster, and how much so!

Authors: David Mutchler, Vibha Alangar, Dave Fisher, Matt Boutell, Mark Hays,
         Mohammed Noureddine, Sana Ebrahimi, Sriram Mohan, their colleagues and
         PUT_YOUR_NAME_HERE.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

# -----------------------------------------------------------------------------
# TODO: 2. With your instructor, read the code below, where you will see two
#  functions each of which produces the list [1, 2, 3, ... n], for any given n.
#  _
#  Run this module, modifying  main  as needed to answer these questions:
#  _
#    1. Which runs faster:
#         the CONCATENATION approach or the APPEND approach?"
#  _
#    2. In the CONCATENATION approach, if you double the size of the list,
#         about how much does that multiply the time to make the list?
#  _
#    3. The slower approach takes about how times as many seconds
#       as the faster approach,
#          for a list of size 10,000?
#          for a list of size 20,000?
#          for a list of size 40,000?
#          for a list of size 80,000?
#          for a list of size 160,000?  (this may take a while)
#  _
#    4. Do NOT run the code but take a wild guess at how many
#       MINUTES the APPEND approach would take for a list
#       of size 1,000,000,000?
#  _
#    5. Do NOT run the code but take a wild guess at how many
#       YEARS the CONCATENATION approach would take for a list
#       of size 1,000,000,000?
# -----------------------------------------------------------------------------

import time


def main():
    run_append_vs_concatenation(10000)
    run_append(20000)
    run_concatenation(20000)

    # Use the following or not, as you see fit:

    # for k in range(1, 11):
    #     run_append(10000 * (2 ** k))

    # for k in range(5):
    #     run_concatenation(10000 * (2 ** k))


def run_append_vs_concatenation(size):
    append_time, append_result = run_append(size)
    concatenation_time, concatenation_result = run_concatenation(size)

    # Print the results:
    print()
    print("The two approaches produce the same result,")
    print("as you can see by:")
    print("   append_result == concatenation_result:",
          append_result == concatenation_result)

    print()
    print("The CONCATENATION approach took about:")
    print("   {:6.1f} times".format(concatenation_time / append_time))
    print("the APPEND approach")


def run_append(size):
    # Run and time the APPEND approach:
    start_time = time.time()
    append_result = using_append_to_construct_a_list(size)
    seconds_for_append = time.time() - start_time

    # Print and return the results:
    print()
    print("To construct a list of size {}:".format(size))
    print("  the   APPEND    approach took")
    print("  {:8.4f} seconds.".format(seconds_for_append))

    return seconds_for_append, append_result


def run_concatenation(size):
    # Run and time the CONCATENATION approach:
    start_time = time.time()
    concatenation_result = using_concatenation_to_construct_a_list(size)
    seconds_for_concatenation = time.time() - start_time

    # Print and return the results:
    print()
    print("To construct a list of size {}:".format(size))
    print("  the   CONCATENATION    approach took")
    print("  {:8.4f} seconds.".format(seconds_for_concatenation))

    return seconds_for_concatenation, concatenation_result


def using_concatenation_to_construct_a_list(n):
    """ Constructs [1, 2, 3, ... n] by using list concatenation. """
    new = []
    for k in range(1, n + 1):
        new = new + [k]
    return new


def using_append_to_construct_a_list(n):
    """ Constructs [1, 2, 3, ... n] by using the  append  list method. """
    new = []
    for k in range(1, n + 1):
        new.append(k)
    return new


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
