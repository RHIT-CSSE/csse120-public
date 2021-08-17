"""
PRACTICE Exam 1, problem 4.

Authors: David Mutchler, Vibha Alangar, Dave Fisher, Matt Boutell, Mark Hays,
         Mohammed Noureddine, Sana Ebrahimi, Sriram Mohan, their colleagues and
         PUT_YOUR_NAME_HERE.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.


###############################################################################
# Students:
#
# These problems have DIFFICULTY and TIME ratings:
#  DIFFICULTY rating:  1 to 10, where:
#     1 is very easy
#     3 is an "easy" Test 1 question.
#     5 is a "typical" Test 1 question.
#     7 is a "hard" Test 1 question.
#    10 is an EXTREMELY hard problem (too hard for a Test 1 question)
#
#  TIME ratings: A ROUGH estimate of the number of minutes that we
#     would expect a well-prepared student to take on the problem.
#
#  IMPORTANT: For ALL the problems in this module,
#    if you reach the time estimate and are NOT close to a solution,
#    STOP working on that problem and ASK YOUR INSTRUCTOR FOR HELP
#    on it, in class or via Piazza.
###############################################################################


def main():
    """ Calls the   TEST   functions in this module. """
    test_factor_sum()


def test_factor_sum():
    """ Tests the   factor_sum   function. """
    ###########################################################################
    # TODO: 2. Implement this TEST function, as follows:
    #  _
    #   1. Read the  doc-string of the   factor_sum   function defined below.
    #  _
    #   2. Add to THIS function at least ** 5 ** tests that, taken together,
    #      would form a    ** REASONABLY GOOD test set **
    #      for testing the   factor_sum   function defined below.
    #  _
    #    Use the usual format:
    #     # Test NNN:
    #     expected = XXX
    #     actual = problem1b(YYY, ZZZ)
    #     print()
    #     print("Expected:", expected)
    #     print("Actual:  ", actual)
    #  _
    #  IMPORTANT:
    #  The function that you are TESTING is PURPOSELY implemented INCORRECTLY
    #  (it just returns 0).  Do NOT implement the   factor_sum   function.
    #  Just write these TESTS of that function after reading its doc-string.
    #  ------------------------------------------------------------------------
    #  DIFFICULTY AND TIME RATINGS (see top of this file for explanation)
    #    DIFFICULTY:      3
    #    TIME ESTIMATE:   10 minutes.
    ###########################################################################
    print()
    print("---------------------------------------------------------")
    print("Testing the   factor_sum   function:")
    print("---------------------------------------------------------")

    ###########################################################################
    # WRITE YOUR TESTS BELOW HERE:
    ###########################################################################


def factor_sum(n):
    """
    Given a positive integer n,
    returns the sum of the digits of the sum of the distinct factors of n,
    where a FACTOR of n is an integer that divides evenly into n.

    For example, if n is 28, this function returns 11, because:
      -- the distinct factors of n are:
             1  2  4  7  14  28
      -- and the sum of those numbers is   1 + 2 + 4 + 7 + 14 + 28,
             which is 56
      -- and the sum of the digits of 56 is 11,
    so this function returns 11 when n is 28.

    As another example, if n is 25, this function returns 4, because:
    -- the distinct factors of n are:
             1  5  25
      -- and the sum of those numbers is   1 + 5 + 25,
             which is 31
      -- and the sum of the digits of 31 is 4,
    so this function returns 4 when n is 28.

       *** ASK FOR AN EXPLANATION IF YOU DO NOT UNDERSTAND THE ABOVE. ***
    """
    ###########################################################################
    #  This function is PURPOSELY implemented INCORRECTLY (it just returns 0).
    #  DO NOT IMPLEMENT  factor_sum.  Just leave it as it is (returning 0).
    ###########################################################################
    return 0
    ###########################################################################
    # DO NOT modify the above line of code!
    ###########################################################################
