"""
This module lets you practice DEBUGGING when LOGIC ERRORS occur.

That is, no run-time exception occurs, but the function simply
does not do the right thing.

Authors: David Mutchler, Yiji Zhang, Mark Hays, Derek Whitley, Vibha Alangar,
         Matt Boutell, Dave Fisher, Sriram Mohan, Mohammed Noureddine,
         Amanda Stouder, Curt Clifton, Valerie Galluzzi, their colleagues and
         PUT_YOUR_NAME_HERE.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.


###############################################################################
#
# TODO: 2. READ these instructions, ASKING QUESTIONS as needed.
#
#   This module contains "broken" functions, as in m1 and m2.
#   FOLLOW THE SAME STEPS as in the instructions of m1.py
#   to find and correct the mistakes in these functions.
#
#   The broken functions in here have LOGIC errors.
#   The code does NOT break when you run it,
#   but it does not produce the correct output.
#
#   In THIS module, the mistakes may be ANYWHERE in the module
#   EXCEPT:
#     -- The  is_prime  function below is correct.
#     -- The tests themselves are correct.
#
#   *** IMPORTANT: ***
#       Resist the urge to "fiddle" with the code until you stumble
#       upon something that works.  This exercise will be helpful
#       to you ONLY if you use it as an opportunity to learn
#       what the error messages mean and how to react to them.
#
#   *** ASK QUESTIONS AS NEEDED! ***
#
#   When you believe you understand these instructions,
#   change the above TO DO to DONE.
#
###############################################################################

def main():
    """ Calls the   TEST   functions in this module. """


###############################################################################
# Students:
#   Do NOT touch the following  is_prime  function - it has no _TODO_.
#   Do NOT copy code from the  is_prime  function.
#
#   Instead, ** CALL ** this function as needed in the problems below.
#   There are NO errors in this  is_prime  function.
###############################################################################
def is_prime(n):
    """
    What comes in:  An integer n >= 2.
    What goes out:
      -- Returns True if the given integer is prime,
         else returns False.
    Side effects:   None.
    Examples:
      -- is_prime(11) returns  True
      -- is_prime(12) returns  False
      -- is_prime(2)  returns  True
    Note: The algorithm used here is simple and clear but slow.
    """
    for k in range(2, (n // 2) + 1):
        if n % k == 0:
            return False

    return True


###############################################################################
# Students: Do NOT change any of the TEST functions.
#           There are NO errors in the TESTS.
###############################################################################
def run_test_broken_1():
    """ Tests the  broken_1  function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   broken_1   function:')
    print('--------------------------------------------------')

    expected = 3
    actual = broken_1(3)  # Test 1 of broken_1
    print('Expected:', expected)
    print('Actual:  ', actual)

    expected = 4
    actual = broken_1(10)  # Test 2 of broken_1
    print('Expected:', expected)
    print('Actual:  ', actual)

    expected = 135  # Yes, this is the correct answer
    actual = broken_1(1000)  # Test 3 of broken_1
    print('Expected:', expected)
    print('Actual:  ', actual)


# -----------------------------------------------------------------------------
# TODO: 3. Follow the INSTRUCTIONS AT THE TOP OF THIS MODULE
#          to correct the mistake(s) in the following function.
# -----------------------------------------------------------------------------
def broken_1(m):
    """
    What comes in: a positive integer m that is at least 2.
    What goes out:  Returns the number of prime numbers
      between m and (2m + 1) inclusive.
    Side effects:  None.
    Examples:
      If m is 3, this function returns 3 since there
        are 3 primes between 3 and 7 (namely: 3, 5, and 7).
        
      If m is 10, then this function returns 4 since there
        are 4 primes between 10 and 21 (namely: 11, 13, 17 and 19).

    Type hints:
      :type m: int
    """
    #    **  For full credit you must appropriately
    #    **  use (call) the   is_prime   function that is DEFINED ABOVE.
    count = 0
    for k in range(2 * m):
        if is_prime(m):
            count = count + 1

    # -----------------------------------------------------------------------------
    # Calls  main  to start the ball rolling.
    # -----------------------------------------------------------------------------
    main()
