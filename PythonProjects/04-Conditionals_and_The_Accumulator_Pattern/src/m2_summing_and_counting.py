"""
This module lets you practice the ACCUMULATOR pattern in classic forms:
   SUMMING:    total = total + number
   COUNTING:   count = count + 1

A subsequent module lets you practice the ACCUMULATOR pattern
in another classic form:
   IN GRAPHICS:   x = x + pixels

Authors: David Mutchler, Yiji Zhang, Mark Hays, Derek Whitley, Vibha Alangar,
         Matt Boutell, Dave Fisher, Sriram Mohan, Mohammed Noureddine,
         Amanda Stouder, Curt Clifton, Valerie Galluzzi, their colleagues and
         PUT_YOUR_NAME_HERE.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

# -----------------------------------------------------------------------------
# Students: As you work each of these problems, ask yourself:
#   1. Do I need a loop?
#      If so, HOW MANY LOOPS?
#
#   2. Where I need a loop, what needs to happen:
#        -- BEFORE the loop?
#        -- IN the loop?
#        -- AFTER the loop?
# -----------------------------------------------------------------------------

##############################################################################
# TODO: 2. Read the following, then change its _TODO_ to DONE.
#   Throughout these exercises, you must use  RANGE  statements.
#   At this point of the course, you are restricted to the SINGLE-ARGUMENT
#   form of RANGE statements, like this:
#         range(blah):
#   There is a MULTIPLE-ARGUMENT form of RANGE statements (e.g. range(a, b))
#   but you are NOT permitted to use the MULTIPLE-ARGUMENT form yet, for
#   pedagogical reasons.  Change the above _TODO_ to DONE after reading this.
###############################################################################


def main():
    """ Calls the   TEST   functions in this module. """
    print("-----------------------------------------------")
    print("Un-comment each of the following TEST functions")
    print("as you implement the functions that they test.")
    print("-----------------------------------------------")

    # run_test_sum_more_cosines()
    # run_test_count_sines_from()
    # run_test_count_sines_vs_cosines()


def run_test_sum_more_cosines():
    """ Tests the   sum_more_cosines   function. """
    # -------------------------------------------------------------------------
    # TODO: 3. Implement this TEST function.
    #   It TESTS the  sum_more_cosines  function defined below.
    #   Include at least **   3   ** tests (we wrote one for you).
    #   _
    #   To implement this TEST function, use the same 4 steps as before:
    #   _
    #   Step 1: Read the doc-string of  sum_more_cosines  below.
    #     Understand what that function SHOULD return.
    #   _
    #   Step 2:  Pick a test case:  numbers that you could send as
    #     actual arguments to the  sum_more_cosines  function.
    #   _
    #   Step 3: Figure out (by hand/calculator, or by trusting
    #     a test case that your instructor provided in the doc-string)
    #     the CORRECT (EXPECTED) answer for your test case.
    #   _
    #   Step 4: Write code that prints both the EXPECTED answer
    #     and the ACTUAL answer returned when you call the function.
    #     Follow the same form as in the test case we provided below.
    # -------------------------------------------------------------------------
    print()
    print("--------------------------------------------------")
    print("Testing the   sum_more_cosines   function:")
    print("--------------------------------------------------")

    # Test 1:
    expected = 0.13416  # This is APPROXIMATELY the correct answer.
    answer = sum_more_cosines(0, 3)
    print("Test 1 expected:", expected, "(approximately)")
    if answer is not None:
        print("       actual:  ", round(answer, 5))
    else:
        print("       actual:  ", answer)

    # -------------------------------------------------------------------------
    # TODO: 3 (continued).
    #   Below this comment, add 2 more test cases of your own choosing.
    # -------------------------------------------------------------------------


def sum_more_cosines(m, n):
    """
    What comes in:  Integers m and n, with m <= n.
    What goes out:  Returns the sum
       cos(m) + cos(m+1) + cos(m+2) +  ...  cos(n)
    Side effects:   None.
    Examples:
      -- sum_more_cosines(0, 3)  returns
            cos(0) + cos(1) + cos(2) + cos(3)
         which is approximately 0.13416
      -- sum_more_cosines(-4, 1)  returns
            cos(-4) + cos(-3) + cos(-2) + cos(-1) + cos(0) + cos(1)
         which is approximately 0.02082.
    Type hints:
      :type m: int
      :type n: int
      :rtype:  float
    """
    # -------------------------------------------------------------------------
    # TODO: 4. Implement and test this function.
    #   Note that you should write its TEST function first (above).
    #   That is called TEST-FIRST DEVELOPMENT (TFD).
    #  _
    #  IMPORTANT: In this and all other problems in this session,
    #    you must NOT use the 2 or 3-parameter versions
    #    of the RANGE expression, if you happen to know them.
    #    That is, no fair using   range(m, n)   or anything like that.
    #    Just   range(blah)   where blah is a single variable.
    #    Reason: To ensure that you get more practice using expressions.
    # -------------------------------------------------------------------------


def run_test_count_sines_from():
    """ Tests the   count_sines_from   function. """
    # -------------------------------------------------------------------------
    # TODO: 5. Implement this TEST function.
    #   It TESTS the  count_sines_from  function defined below.
    #   Include at least **   6   ** tests (we wrote one for you).
    #              ** Yes, 6 (six) tests. **
    #     ** Counting problems are harder to test than summing problems. **
    #   Use the same 4-step process as for previous TEST functions.
    # -------------------------------------------------------------------------
    print()
    print("--------------------------------------------------")
    print("Testing the   count_sines_from   function:")
    print("--------------------------------------------------")

    # Test 1:
    expected = 5
    answer = count_sines_from(3, 9)
    print("Test 1 expected:", expected)
    print("       actual:  ", answer)

    # -------------------------------------------------------------------------
    # TODO: 5 (continued).
    #   Below this comment, add 5 more test cases of your own choosing.
    # -------------------------------------------------------------------------


def count_sines_from(m, n):
    """
    What comes in:  Integers m and n, with m <= n.
    What goes out:  Returns the number of integers from m to n,
       inclusive, whose sine is less than 0.5.
    Side effects:   None.
    Examples:
    Since:  sine(3) is about 0.14
            sine(4) is about -0.76
            sine(5) is about -0.96
            sine(6) is about -0.28
            sine(7) is about 0.66
            sine(8) is about 0.99
            sine(9) is about 0.41
      -- count_sines_from(3, 9)  returns  5
      -- count_sines_from(4, 6)  returns  3
      -- count_sines_from(7, 7)  returns  0
      -- count_sines_from(9, 9)  returns  1
    Type hints:
      :type m: int
      :type n: int
      :rtype:  int
    """
    # -------------------------------------------------------------------------
    # TODO: 6. Implement and test this function.
    #   Note that you should write its TEST function first (above).
    #  _
    #  IMPORTANT: As in previous problems in this session,
    #    you must NOT use the 2 or 3-parameter versions
    #    of the RANGE expression, if you happen to know them.
    # -------------------------------------------------------------------------


def run_test_count_sines_vs_cosines():
    """ Tests the   count_sines_vs_cosines   function. """
    # -------------------------------------------------------------------------
    # TODO: 7. Implement this TEST function.
    #   It TESTS the  count_sines_vs_cosines  function defined below.
    #   Include at least **   6   ** tests (we wrote one for you).
    #              ** Yes, 6 (six) tests. **
    #     ** Counting problems are harder to test than summing problems. **
    #   Use the same 4-step process as for previous TEST functions.
    # -------------------------------------------------------------------------
    print()
    print("--------------------------------------------------")
    print("Testing the   count_sines_vs_cosines   function:")
    print("--------------------------------------------------")

    # Test 1:
    expected = 100
    answer = count_sines_vs_cosines(101)
    print("Test 1 expected:", expected)
    print("       actual:  ", answer)

    # -------------------------------------------------------------------------
    # TODO: 7 (continued).
    #   Below this comment, add 5 more test cases of your own choosing.
    # -------------------------------------------------------------------------


def count_sines_vs_cosines(m):
    """
    What comes in:  A non-negative integer m.
    What goes out:  Returns the number of integers from -m to m,
       inclusive, whose sine is greater than its cosine.
    Side effects:   None.
    Examples:
    Since:  sine(-5) is about  0.96  and cosine(-5) is about  0.28
            sine(-4) is about  0.76  and cosine(-4) is about -0.65
            sine(-3) is about -0.14  and cosine(-3) is about -0.99
            sine(-2) is about -0.91  and cosine(-2) is about -0.42
            sine(-1) is about -0.84  and cosine(-1) is about  0.54
            sine(0)  is about  0.00  and  cosine(0) is about  1.00
            sine(1)  is about  0.84  and  cosine(1) is about  0.54
            sine(2)  is about  0.91  and  cosine(2) is about -0.42
            sine(3)  is about  0.14  and  cosine(3) is about -0.99
            sine(4)  is about -0.76  and  cosine(4) is about -0.65
            sine(5)  is about -0.96  and  cosine(5) is about  0.28
      -- count_sines_vs_cosines(5) returns 6 because
           for -5, -4, -3, 1, 2, and 3, their sine is larger than their cosine
      -- count_sines_vs_cosines(3) returns 4
      -- count_sines_vs_cosines(0) returns 0
      -- count_sines_vs_cosines(1) returns 1
      -- Also:  count_sines_vs_cosines(101) returns 100 (trust me!)
    Type hints:
      :type m: int
      :rtype:  int
    """
    # -------------------------------------------------------------------------
    # TODO: 8. Implement and test this function.
    #   Note that you should write its TEST function first (above).
    #  _
    #  IMPORTANT: As in previous problems in this session,
    #    you must NOT use the 2 or 3-parameter versions
    #    of the RANGE expression, if you happen to know them.
    # -------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
