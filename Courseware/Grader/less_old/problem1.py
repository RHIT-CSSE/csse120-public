"""
Test 1, problem 1.

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Yuankai Wang.  September 2016.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

def main():
    """ Calls the   TEST   functions in this module. """
    test_problem1a()
    test_problem1b()
    test_problem1c()


def is_perfect(n):
    """
    What comes in:  A positive integer n.
    What goes out:
      A number is "perfect" if it equals the sum of all its factors,
      excluding itself.  (See examples below.)
      This  is_perfect  function returns True if the given number n
      is perfect. It returns False if the given number n is not perfect.
    Side effects: None.
    Examples:
      -- 496 is perfect because its factors (excluding 496 itself) are:
           1   2   5   8   16   31   62   124   248
         and
           1 + 2 + 4 + 8 + 16 + 31 + 62 + 124 + 248 = 496
         So is_perfect(496) returns True.

      -- 18 is NOT perfect because its factors (excluding itself) are
           1   2   3   6   9
         and
           1 + 2 + 3 + 6 + 9 = 21, and 21 is NOT equal to 18.
         So is_perfect(18) returns False.
    Type hints:
      :type n: int
    """
    # ------------------------------------------------------------------
    # Students:
    #   Do NOT touch the above  is_perfect  function - it has no TODO.
    #   Do NOT copy code from this function.
    #
    # Instead, ** CALL ** this function as needed in the problems below.
    # ------------------------------------------------------------------
    total = 0
    for k in range(1, n):
        if n % k == 0:
            total = total + k

    return (total == n)


def reverse_number(num):
    """
    What comes in:  A positive integer num.
    What goes out:
      The number "reversed" (see examples below).
    Side effects: None.
    Examples:
      -- If num is 123, this function returns 321.
      -- If num is 17397, this function returns 79371.
      -- If num is 559002, this function returns 200955.
      -- If num is 30100, this function returns 103,
           since the reverse of 30100 is 00103 and integers drop
           any leading zeros.
    Type hints:
      :type num: int
    """
    # ------------------------------------------------------------------
    # Students:
    #   Do NOT touch the above  reverse_number  function - it has no TODO.
    #   Do NOT copy code from this function.
    #
    # Instead, ** CALL ** this function as needed in the problems below.
    # ------------------------------------------------------------------
    numstring = ''
    instring = str(num)
    for i in range(len(instring)):
        numstring = instring[i] + numstring
    return int(numstring)


def test_problem1a():
    print()
    print('--------------------------------------------------')
    print('Testing the   problem1a   function:')
    print('--------------------------------------------------')

    # Test 1:
    expected = 0
    answer = problem1a(8, 20)
    print()
    print('Test 1 expected:', expected)
    print('       actual:  ', answer)

    # Test 2:
    expected = 1
    answer = problem1a(5, 10)
    print()
    print('Test 2 expected:', expected)
    print('       actual:  ', answer)

    # Test 3:
    expected = 1
    answer = problem1a(6, 6)
    print()
    print('Test 3 expected:', expected)
    print('       actual:  ', answer)

    # Test 4:
    expected = 2
    answer = problem1a(6, 28)
    print()
    print('Test 4 expected:', expected)
    print('       actual:  ', answer)

    # Test 5:
    expected = 3
    answer = problem1a(2, 2000)
    print()
    print('Test 5 expected:', expected)
    print('       actual:  ', answer)

    # Test 6:
    expected = 3
    answer = problem1a(6, 496)
    print()
    print('Test 6 expected:', expected)
    print('       actual:  ', answer)

    # Test 7:
    expected = 1
    answer = problem1a(8000, 8200)
    print()
    print('Test 7 expected:', expected)
    print('       actual:  ', answer)

    # Test 8:
    expected = 0
    answer = problem1a(8129, 8200)
    print()
    print('Test 8 expected:', expected)
    print('       actual:  ', answer)


def problem1a(m, n):
    """
    What comes in: Two positive integers, m and n, where m <= n.
    What goes out: Returns the number of "perfect" numbers
        from m to n inclusive.
        [See  is_perfect  above for what "perfect" means.]
    Side effects: None
    Examples:
        If m is 8 and n is 20, this function should return 0,
        as there are no perfect numbers between 8 and 20.

        If m is 5 and n is 10, this function should return 1,
        as 6 is the sole perfect number between 5 and 10.
    Type hints:
      :type m: int
      :type n: int
    """
    # ------------------------------------------------------------------
    # DONE: 2. Implement and test this function.
    #          Tests have been written for you (above).
    #
    ####################################################################
    # IMPORTANT:
    #    **  For full credit you must appropriately use (call)
    #    **  the   is_perfect   function that is DEFINED ABOVE.
    ####################################################################

    number = 0
    for k in range (n - m + 1):
        if is_perfect(k + m):
            number = number + 1
    return number


def test_problem1b():
    print()
    print('--------------------------------------------------')
    print('Testing the   problem1b   function:')
    print('--------------------------------------------------')

    # Test 1:
    expected = 1
    answer = problem1b(20)
    print()
    print('Test 1 expected:', expected)
    print('       actual:  ', answer)

    # Test 2:
    expected = 3
    answer = problem1b(496)
    print()
    print('Test 2 expected:', expected)
    print('       actual:  ', answer)

    # Test 3:
    expected = 2
    answer = problem1b(495)
    print()
    print('Test 3 expected:', expected)
    print('       actual:  ', answer)

    # Test 4:
    expected = 3
    answer = problem1b(497)
    print()
    print('Test 4 expected:', expected)
    print('       actual:  ', answer)

    # Test 5:
    expected = 0
    answer = problem1b(5)
    print()
    print('Test 5 expected:', expected)
    print('       actual:  ', answer)

    # Test 6:
    expected = 0
    answer = problem1b(1)
    print()
    print('Test 6 expected:', expected)
    print('       actual:  ', answer)


def problem1b(num):
    """
    What comes in: A positive integer  num.
    What goes out: Returns the number of perfect numbers
        from 1 to num, inclusive.
    Side effects: None
    Examples:
        If  num  is 20, this function should return 1,
        as 6 is the sole perfect number between 1 and 20.

        If  num  is 496, this function should return 3,
        as there are 3 perfect numbers (namely, 6, 28 and 496)
        between 1 and 496.
    Type hints:
      :type num: int
    """
    # ------------------------------------------------------------------
    # DONE: 2. Implement and test this function.
    #          Tests have been written for you (above).
    #
    ####################################################################
    # IMPORTANT:
    #    **  This problem is only a small number of points.
    #    **  For any credit on it, you must appropriately use (call)
    #    **  the relevant function(s) that are DEFINED ABOVE.
    ####################################################################

    number2 = 0
    for k in range(num):
        if is_perfect(k + 1):
            number2 = number2 + 1
    return number2


def test_problem1c():
    # ------------------------------------------------------------------
    # DONE: 3. Implement this TEST function.
    #   It TESTS the  problem1c  function defined below.
    #   Include at least **   6   ** tests (we wrote 4 for you).
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   problem1c   function:')
    print('--------------------------------------------------')

    # Test 1:
    expected = 262
    answer = problem1c(2, 4)
    print()
    print('Test 1 expected:', expected)
    print('       actual:  ', answer)

    # Test 2:
    expected = 10
    answer = problem1c(4, 1)
    print()
    print('Test 2 expected:', expected)
    print('       actual:  ', answer)

    # Test 3:
    expected = 15291
    answer = problem1c(5, 3)
    print()
    print('Test 3 expected:', expected)
    print('       actual:  ', answer)

    # Test 4:
    expected = 454545454546
    answer = problem1c(10, 6)
    print()
    print('Test 4 expected:', expected)
    print('       actual:  ', answer)

    # ------------------------------------------------------------------
    # DONE: 3 (continued).
    # Below this comment, add 2 more test cases of your own choosing.
    # ------------------------------------------------------------------

    # Test 5:
    expected = 73593
    answer = problem1c(3, 5)
    print()
    print('Test 5 expected:', expected)
    print('       actual:  ', answer)

    # Test 6:
    expected = 94509996309
    answer = problem1c(6, 7)
    print()
    print('Test 6 expected:', expected)
    print('       actual:  ', answer)


def problem1c(m, p):
    """
    What comes in: Two positive integers, m and p.
    What goes out: Returns the sum of the "reverses" of all the
        integers from 1 to m ** p, inclusive.
        [See  reverse_number  above for what "reverses" means.]
    Side effects: None
    Example:
      -- If m is 2 and p is 4, then this function returns
           1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 1 + 11 + 21 + 31 + 41 + 51 + 61
        which is 262.
        Note that the above simply "reverses" each of the numbers from
        1 to 16 and adds up those reversed numbers.
          -- The reverse of any single-digit number is that number.
          -- The reverse of 10 is 1.
          -- The reverse of 11 is 11.
          -- The reverse of 12 is 21.
          -- The reverse of 13 is 31.
          -- The reverse of 14 is 41.
          -- The reverse of 15 is 51.
          -- The reverse of 16 is 61.
        Don't forget that there is a function  reverse_number
        above that reverses any number that you give it.
    Type hints:
      :type m: int
      :type p: int
    """
    # ------------------------------------------------------------------
    # DONE: 4. Implement and test this function.
    #   Note that you should write its TEST function first (above).
    #
    ####################################################################
    # IMPORTANT:
    #    **  For full credit you must appropriately use (call)
    #    **  the   reverse_number   function that is DEFINED ABOVE.
    ####################################################################

    sum1 = 0
    for k in range(m ** p):
        a = reverse_number(k + 1)
        sum1 = sum1 + a
    return sum1


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
#main()
