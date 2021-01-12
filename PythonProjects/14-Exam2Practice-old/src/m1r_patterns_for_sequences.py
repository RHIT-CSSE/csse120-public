"""
This module demonstrates various patterns
for ITERATING through SEQUENCES, including:
  -- Beginning to end
  -- Other ranges (e.g., backwards and every-3rd-item)
  -- The COUNT/SUM/etc pattern
  -- The FIND pattern (via LINEAR SEARCH)
  -- The MAX/MIN pattern
  -- Looking two places in the sequence at once
  -- Looking at two sequences in parallel

Of course, these are not the only patterns, and some problems require
combining these patterns, but this is a good base upon which to build.

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Mark Hays, Amanda Stouder, Derek Whitley, their colleagues,
         and PUT_YOUR_NAME_HERE.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.


# -----------------------------------------------------------------------------
# TODO: 2. SKIM the program below and RUN it.
#   ___
#   Then look more closely at the CODE for:
#     -- find_example1
#     -- find_example2
#     -- find_example3
#     -- min_index
#     -- min_item
#     -- two_places_at_once
#     -- two_sequences_in_parallel
#   ___
#   When you have read them, asking questions as needed,
#   and you feel that you understand (at least mostly)
#   the patterns for:
#     -- FIND
#     -- MIN/MAX
#     -- TWO-PLACES-AT-ONCE, and
#     -- TWO-SEQUENCES-IN-PARALLEL
#   then:
#      change the above _TODO_ to DONE.
# -----------------------------------------------------------------------------

import math


def main():
    """
    Demonstrates some patterns for ITERATING through SEQUENCES.
    These are the CALLS to code that uses the patterns.
    See further below for the CODE ITSELF that uses the pattersn.
    """
    # -------------------------------------------------------------------------
    # Demonstrate the    BEGINNING-TO-END    and   COUNTING   patterns.
    # -------------------------------------------------------------------------
    print()
    print('-----------------------------------------------------------')
    print('Demonstrating the   BEGINNING-TO-END   pattern,')
    print('   along with the   COUNTING   pattern:')
    print('-----------------------------------------------------------')

    sequence = [88, 232, 8.5, -11, 'Grandmother', 22, 4.3, 18 / 2, 7 // 2]
    answer = beginning_to_end(sequence)
    print('The test sequence is:')
    print('  ', sequence)
    print('The number of integers in that sequence is', answer)

    # -------------------------------------------------------------------------
    # Demonstrate the    OTHER-RANGES    pattern.
    # -------------------------------------------------------------------------
    print()
    print('-----------------------------------------------------------')
    print('Demonstrating the   OTHER-RANGES   pattern')
    print('   (backwards, every 3rd item)   in each of THREE FORMS:')
    print('-----------------------------------------------------------')

    sequence = [88, 232, 8.5, -11, 'Grandmother', 22, 4.3, 9.0, 3]
    other_ranges(sequence)

    # -------------------------------------------------------------------------
    # Demonstrate the    FIND    pattern.
    # -------------------------------------------------------------------------
    print()
    print('-----------------------------------------------------------')
    print('Demonstrating the   FIND   pattern, in several variations:')
    print('-----------------------------------------------------------')

    print()
    print('Example: FINDING the first STRING in the sequence.')
    print()
    print('  Case 1:  The item  ** IS **  in the sequence:')
    find([88, 232, 8.5, -11, 'Grandmother', 22, 'mother', 9.0, 3])

    print()
    print('  Case 2:  The item  ** IS NOT **  in the sequence:')
    find([1, 2, 5])

    # -------------------------------------------------------------------------
    # Demonstrate the    MAX/MIN    pattern.
    # -------------------------------------------------------------------------
    print()
    print('-----------------------------------------------------------')
    print('Demonstrating the  MAX/MIN  pattern, in several variations:')
    print('-----------------------------------------------------------')

    sequence = [4, 66, 33, 90, 93, 2, 3, 3, 2, 15]
    max_min(sequence)

    # -------------------------------------------------------------------------
    # Demonstrate the    TWO-PLACES-IN-THE-SEQUENCE-AT-ONCE    pattern.
    # -------------------------------------------------------------------------
    print()
    print('-----------------------------------------------------------')
    print('Demonstrating  TWO-PLACES-IN-THE-SEQUENCE-AT-ONCE  pattern:')
    print('-----------------------------------------------------------')

    sequence = [4, 66, 33, 90, 93, 3, 3, 3, 2, 15]
    print('The sequence is:', sequence)
    answer = two_places_at_once(sequence)
    print('The sequence increments at', answer, 'places.')

    # -------------------------------------------------------------------------
    # Demonstrate the    TWO-SEQUENCES-IN-PARALLEL    pattern.
    # -------------------------------------------------------------------------
    print()
    print('-----------------------------------------------------------')
    print('Demonstrating the   TWO-SEQUENCES-IN-PARALLEL   pattern:')
    print('-----------------------------------------------------------')

    seq1 = [11, 22, 10, 44, 33, 12]
    seq2 = [55, 10, 30, 30, 30, 30]
    print('Sequence 1 is:', seq1)
    print('Sequence 2 is:', seq2)
    answer = two_sequences_in_parallel(seq1, seq2)
    print('The 2nd sequence exceeds the 1st at', answer, 'places.')


# -----------------------------------------------------------------------------
# The   BEGINNING-TO-END   pattern:
# -----------------------------------------------------------------------------
def beginning_to_end(sequence):
    """
    Demonstrates iterating (looping) through a sequence in the most
    typical way:  from BEGINNING TO END.

    This particular example returns the number of items in the sequence
    that are integers. It also prints the index during the looping.
    Type hints:
      :type sequence: list | tuple
    """
    # -------------------------------------------------------------------------
    # The   BEGINNING-TO-END   pattern is:
    #
    #    for k in range(len(sequence)):
    #        ... sequence[k] ...
    #
    # -------------------------------------------------------------------------
    count = 0
    for k in range(len(sequence)):
        if type(sequence[k]) == int:
            count = count + 1
        print(k)

    return count


# -----------------------------------------------------------------------------
# The   OTHER-RANGES   pattern:
# -----------------------------------------------------------------------------
def other_ranges(sequence):
    """
    Demonstrates iterating (looping) through a sequence in a pattern
    OTHER than from beginning to end.

    This particular example prints every 3rd item of the sequence,
    but starting at the END of the list (and going backwards).
    Type hints:
      :type sequence: list | tuple
    """
    # -------------------------------------------------------------------------
    # The   OTHER-RANGES   pattern can be thought of as having
    #   any of three equivalent forms.
    # Choose the form that makes the most sense to you.
    #
    # FORM 1:
    #    for k in range( NUMBER ):
    #        ... sequence[ BLAH_EXPRESSION ] ...
    #
    # where NUMBER is the number of items in the sequence to examine
    # and   BLAH_EXPRESSION   is some formula involving k that is carefully
    #                         crafted to produce exactly the right indices.
    #
    # FORM 2:
    #    for k in range( BLAH_RANGE ):
    #        ... sequence[k] ...
    #
    # where BLAH_RANGE is some range OTHER than one that generates
    #    0, 1, 2, 3, ...
    # and is carefully crafted to produce exactly the right indices.
    #
    # FORM 3:
    #    m = ...
    #    for k in range( NUMBER ):
    #        ... sequence[ m ] ...
    #        m = ...
    #
    # where NUMBER is the number of items in the sequence to examine
    # and     m    is an auxiliary variable that is carefully crafted and
    #                controlled to produce exactly the right indices.
    #
    # FORM 1: Puts all the heavy lifting into figuring out BLAH_EXPRESSION.
    # FORM 2: Puts all the heavy lifting into figure out BLAH_RANGE.
    # FORM 3: Like FORM 1,
    #    but uses an auxiliary variable to simplify figuring out the
    #    index of the sequence at each iteration of the loop.
    # -------------------------------------------------------------------------
    print('Printing backwards, every 3rd item, ONE WAY:')

    # -------------------------------------------------------------------------
    # Solution using FORM 1:
    # -------------------------------------------------------------------------
    last = len(sequence) - 1
    for k in range(len(sequence) // 3):
        print(sequence[last - (k * 3)])

    print('\nANOTHER way:')

    # -------------------------------------------------------------------------
    # Solution using FORM 2:
    # -------------------------------------------------------------------------
    last = len(sequence) - 1
    for k in range(last, -1, -3):
        print(sequence[k])

    print('\nYET ANOTHER way:')

    # -------------------------------------------------------------------------
    # Solution using FORM 3:
    # -------------------------------------------------------------------------
    last = len(sequence) - 1
    m = last
    for k in range(len(sequence) // 3):
        print(sequence[m])
        m = m - 3


# -----------------------------------------------------------------------------
# The   FIND   pattern, in its several variations:
# -----------------------------------------------------------------------------
def find(sequence):
    """
    Demonstrates FINDING an item in a sequence.  Its forms include:
      1. Finding WHETHER a given item is in the given sequence.
      2. Finding whether the sequence contains an item
         with a given property, and returning either of:
           2a. the INDEX of the first such item found
               (or -1 if none was found)
           2b. the ITEM that was found (or None if none was found)

    This particular example finds the first item in the sequence
    that is a string.  The three sub-examples return:
      -- True or False (per item 1 above)
      -- the INDEX of the found item (per 2a above)
      -- the ITEM that was found (per 2b above)
    Type hints:
      :type sequence: list | tuple
    """
    # -------------------------------------------------------------------------
    # The   FIND   pattern is:
    #
    #     for k in range(len(sequence)):
    #         if ... seq[k] ...:
    #             return k
    #
    #     return -1
    #
    # *** NOTE the placement of the TWO   return   statements! ***
    #
    # The above returns the INDEX where the item was found,
    #   or -1 if none was found.
    #
    # Other problems/variations might return  True  if the item
    # was found and  False  otherwise, or might return the item itself
    # that was found (and perhaps  None  if the item was not found).
    #
    # Also, some problems might require you to search through only part
    # of the sequence (not all of it) or to search backwards, or ...
    # -------------------------------------------------------------------------

    answer1 = find_example1(sequence)
    answer2 = find_example2(sequence)
    answer3 = find_example3(sequence)

    print('  Test sequence is:', sequence)
    print('    -- Found (True or False)?', answer1)
    print('    -- Index of found item:', answer2)
    print('    -- Item that was found:', answer3)


def find_example1(sequence):
    """
    Returns True if the given sequence contains a string,
    else returns False.
    Type hints:
      :type sequence: list | tuple
      :rtype: bool
    """
    # Returns True or False
    for k in range(len(sequence)):
        if type(sequence[k]) == str:
            return True

    return False


def find_example2(sequence):
    """
    Returns the INDEX of the first string in the given sequence,
    or -1 if the given sequence contains no strings.
    Type hints:
      :type sequence: list | tuple
      :rtype: int
    """
    # Returns the index (k) or -1
    for k in range(len(sequence)):
        if type(sequence[k]) == str:
            return k

    return -1


def find_example3(sequence):
    """
    Returns the FIRST STRING in the given sequence,
    or None if the sequence contains no strings.
    Type hints:
      :type sequence: list | tuple
      :rtype: str
    """
    # Returns the item ( sequence[k] )  or  None
    for k in range(len(sequence)):
        if type(sequence[k]) == str:
            return sequence[k]

    return None


# -----------------------------------------------------------------------------
# The   MAX/MIN   pattern, in several variations:
# -----------------------------------------------------------------------------
def max_min(sequence):
    """
    Demonstrates determining the item in a sequence whose BLAH
    is SMALLEST (or LARGEST), where BLAH varies from problem to problem.

    The sub-examples of this particular example find,
    for a sequence of numbers:
      -- The index of the smallest number in the sequence
      -- The number at that index
           (i.e., the smallest number in the sequence)
      -- The index of the number in the sequence
           whose cosine is smallest
    Type hints:
      :type sequence: list[int | float] | tuple[int | float]
    """
    # -------------------------------------------------------------------------
    # The   MIN   pattern is as follows (with  MAX  being similar):
    #
    #     index_of_min = 0
    #     for k in range(1, len(sequence)):
    #         if BLAH(sequence[k]) < BLAH(sequence[index_of_min]):
    #             index_of_min = k
    #
    #     return index_of_min
    #
    # The property  BLAH  varies from problem to problem.
    # NOTE the distinction between the SMALLEST item
    #   and the INDEX of that item.
    #
    # The above returns the INDEX where the item was found.
    # Some problems ask for the item itself.
    # -------------------------------------------------------------------------

    print('The sequence is:', sequence)
    answer1 = min_index(sequence)
    answer2 = min_item(sequence)
    answer3 = min_cosine(sequence)

    print()
    print('The index of the smallest item in the sequence is', answer1)

    print()
    print('The smallest item in the sequence is', answer2)

    print()
    print('The index of the item in the sequence')
    print('  whose cosine is smallest is', answer3)
    print('That item is', sequence[answer3])
    print('Its cosine is', math.cos(sequence[answer3]))


def min_index(sequence):
    """
    Returns the index of the smallest item in the given sequence.
    Breaks ties in favor of the smallest index among the ties.

    Type hints:
      :type sequence: list[int | float] | tuple[int | float]
      :rtype: int
    Precondition: the sequence is a non-empty sequence of numbers.
    """
    # -------------------------------------------------------------------------
    # Return the INDEX of the smallest item in the sequence.
    # -------------------------------------------------------------------------
    index_of_min = 0
    for k in range(1, len(sequence)):
        if sequence[k] < sequence[index_of_min]:
            index_of_min = k

    return index_of_min


def min_item(sequence):
    """
    Returns the smallest item in the given sequence.

    Type hints:
      :type sequence: list[int | float] | tuple[int | float]
      :rtype: int | float
    Precondition: the sequence is a non-empty sequence of numbers.
    """
    # -------------------------------------------------------------------------
    # Use the same code as above to find the INDEX of the smallest item.
    # But return the item itself, in this variation.
    # -------------------------------------------------------------------------
    index_of_min = min_index(sequence)
    return sequence[index_of_min]


def min_cosine(sequence):
    """
    Returns the index of the item in the sequence whose cosine
    is smallest.

    Type hints:
      :type sequence: list[int | float] | tuple[int | float]
      :rtype: int
    Precondition: the sequence is a non-empty sequence of numbers.
    """
    # -------------------------------------------------------------------------
    # Very similar to   min_index   above.  Just compare the COSINES
    #   of the numbers instead of the numbers themselves.
    # -------------------------------------------------------------------------
    index_of_min = 0
    for k in range(1, len(sequence)):
        if math.cos(sequence[k]) < math.cos(sequence[index_of_min]):
            index_of_min = k

    return index_of_min


# -----------------------------------------------------------------------------
# The   TWO-PLACES-AT-ONCE   pattern:
# -----------------------------------------------------------------------------
def two_places_at_once(sequence):
    """
    Demonstrates iterating (looping) through a sequence,
    but examining TWO places in the sequence on the SAME ITERATION.

    This particular example returns the number of items in the sequence
    that are bigger than the previous item in the sequence.
    For example, if the sequence is [4, 66, 33, 90, 93, 3, 3, 3, 2, 15],
    then the function returns   4
    since   66 > 4   and   90 > 33   and   93 > 90   and   15 > 2.

    Type hints:
      :type sequence: list[int | float] | tuple[int | float]
      :rtype: int
    """
    # -------------------------------------------------------------------------
    # The   TWO-PLACES-AT-ONCE   pattern is:
    #
    #    for k in range( BLAH ):
    #        ... sequence[ FOO_1 ] ... sequence[ FOO_2 ] ...
    #
    # where BLAH is some range appropriate to the problem,
    #       FOO_1 is some function of k that gives ONE
    #             of the "two places at once" to examine, and
    #       FOO_2 is another function of k that gives the OTHER
    #             of the "two places at once" to examine.
    # Typically, FOO_1 or FOO_2 (but not both) is simply k.
    # -------------------------------------------------------------------------
    count = 0
    for k in range(len(sequence) - 1):
        if sequence[k + 1] > sequence[k]:
            count = count + 1

    return count


# -----------------------------------------------------------------------------
# The   TWO-SEQUENCES-IN-PARALLEL   pattern:
# -----------------------------------------------------------------------------
def two_sequences_in_parallel(sequence1, sequence2):
    """
    Demonstrates iterating (looping) through TWO sequences in PARALLEL.

    This particular example assumes that the two sequences are of equal
    length and returns the number of items in sequence2 that are bigger
    than  their corresponding item in sequence1.  For example,
    if the sequences are:
        [11, 22, 10, 44, 33, 12]
        [55, 10, 30, 30, 30, 30]
    then this function returns 3, since 55 > 11 and 30 > 10 and 30 > 12.

    Type hints:
      :type sequence1: list[int | float] | tuple[int | float]
      :type sequence2: list[int | float] | tuple[int | float]
      :rtype: int
    Precondition:  the two sequences are of equal length.
    """
    # -------------------------------------------------------------------------
    # The TWO-SEQUENCES-IN-PARALLEL pattern is:
    #
    #    for k in range(len(sequence1)):
    #        ... sequence1[k] ... sequence2[k] ...
    #
    # The above assumes that the sequences are of equal length
    # (or that you just want to do the length of sequence1).
    # -------------------------------------------------------------------------
    count = 0
    for k in range(len(sequence1)):
        if sequence1[k] > sequence2[k]:
            count = count + 1

    return count


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
