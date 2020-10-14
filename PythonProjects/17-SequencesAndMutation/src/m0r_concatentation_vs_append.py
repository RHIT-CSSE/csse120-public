"""
This module compares two ways of appending items to a list:
    r = r + [item]
    r.append(item)
Run this module to see which is faster, and how much so!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Mark Hays, Amanda Stouder, Derek Whitley, their colleagues,
         and PUT_YOUR_NAME_HERE.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

# -----------------------------------------------------------------------------
# TODO: 2. With your instructor, read the code below, where you will see
#  two functions each of which produces the list [1, 2, 3, ... n],
#  for any given n.  Run this module, then answer these questions:
#    Which runs faster:
#       the CONCATENATION approach or the APPEND approach?
#    The slower approach takes about how times as many seconds
#    as the faster approach,
#        for a list of size 10,000?
#        for a list of size 20,000?
#        for a list of size 40,000?
#        for a list of size 80,000?
#    Do not RUN the code but take a wild guess at:
#        for a list of size 1,000,000?
# -----------------------------------------------------------------------------

import time


def main():
    size = 10000

    # Run and time the CONCATENATION approach:
    start_time = time.time()
    r_concatenation = using_concatenation_to_construct_a_list(size)
    seconds_for_concatenation = time.time() - start_time

    # Run and time the APPEND approach:
    start_time = time.time()
    r_append = using_append_to_construct_a_list(size)
    seconds_for_append = time.time() - start_time

    # Print the results:
    print('The two approaches produce the same result,')
    print('as you can see by:')
    print('   r_concatenation == r_append:', r_concatenation == r_append)
    print()

    print('To construct a list of size {}:'.format(size))
    print('The   concatenation   approach took {:8.4f} seconds.'.format(
        seconds_for_concatenation))
    print('The   append          approach took {:8.4f} seconds.'.format(
        seconds_for_append))
    print('The former is about {:6.1f} times the latter'.format(
        seconds_for_concatenation / seconds_for_append))


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