"""
This module lets you study the ACCUMULATOR pattern for SUMMING.

Authors: Many, many people over many, many years.
         David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher, Mark Hays,
         Amanda Stouder, Derek Whitley, and their colleagues wrote this version.
"""
# -----------------------------------------------------------------------------
# Students: Read and run this program.  Just use it as an example.
#
#   There is nothing for you to turn in from this file.
# -----------------------------------------------------------------------------


def main():
    """ Calls the   TEST   functions in this module. """
    run_test_sum_squares()


def run_test_sum_squares():
    """ Tests the   sum_squares   function. """
    print()
    print("--------------------------------------------------")
    print("Testing the   sum_squares   function:")
    print("--------------------------------------------------")

    # Test 1:
    expected = 55
    answer = sum_squares(5)
    print("Test 1 expected:", expected)
    print("       actual:  ", answer)

    # Test 2:
    expected = 91
    answer = sum_squares(6)
    print("Test 2 expected:", expected)
    print("       actual:  ", answer)

    # Test 3:
    expected = 333833500
    answer = sum_squares(1000)
    print("Test 3 expected:", expected)
    print("       actual:  ", answer)


def sum_squares(n):
    """
    What comes in:  A positive integer n.
    What goes out:  Returns the sum of the squares of the integers
       1, 2, 3, ... n, inclusive, for the given n.
    Side effects:   None.
    Example:
      If n is 5,
      this function returns 1 + 4 + 9 + 16 + 25,   which is 55.
    Type hints:
      :type n: int
      :rtype: int
    """
    total = 0
    for k in range(n):
        total = total + ((k + 1) ** 2)

    return total


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
