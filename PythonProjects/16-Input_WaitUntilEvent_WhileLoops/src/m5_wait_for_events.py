"""
This module lets you practice the WAIT-FOR-EVENT pattern, using:
     while True:
       ...
       if <event has occurred>:
           break
       ...

If you wish to use the    while <condition>:    form, that is OK too,
but we reserve the right to offer help only if you use the   while True:  form,
since many people find it easier to write correct code in that form.

Authors: David Mutchler, Vibha Alangar, Dave Fisher, Matt Boutell, Mark Hays,
         Mohammed Noureddine, Sana Ebrahimi, Sriram Mohan, their colleagues and
         PUT_YOUR_NAME_HERE.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

import math
import testing_helper
import time


def main():
    """ Calls the   TEST   functions in this module. """
    print()
    print("Un-comment and re-comment calls in MAIN one by one as you work.")
    print()

    # run_test_sum_until_prime_input()
    # run_test_next_prime()
    # run_test_sum_to_next_prime()
    # run_test_prime_gap()
    # run_test_wait_for_sum_of_cubes()


def is_prime(n):
    """
    What comes in:  An integer n >= 2.
    What goes out:  Returns True if the given integer is prime,
       else returns False.
    Side effects:   None.
    Examples:
      -- is_prime(11) returns  True
      -- is_prime(12) returns  False
      -- is_prime(2)  returns  True
    Note: The algorithm used here is simple and clear but slow.
    Type hints:
      :type n:  int
      :rtype:   bool
    """
    for k in range(2, int(math.sqrt(n) + 0.1) + 1):
        if n % k == 0:
            return False

    return True
    # -------------------------------------------------------------------------
    # Students:
    #   Do NOT touch the above  is_prime  function - it has no TO DO.
    #   Do NOT copy code from this function.
    #
    # Instead, ** CALL ** this function as needed in the problems below.
    # -------------------------------------------------------------------------


def run_test_sum_until_prime_input():
    """ Tests the   wait_for_prime_input   function by calling it. """
    print()
    print("--------------------------------------------------")
    print("Testing the   sum_until_prime_input   function:")
    print("--------------------------------------------------")

    sum_until_prime_input()


def sum_until_prime_input():
    """
    What comes in:  Nothing.
    What goes out: Nothing (i.e., None).
    Side effects:
      -- Repeatedly prompts the user for and inputs an integer
            that is at least 2.
      -- Stops when the input integer is prime.
      -- Prints the sum of the input integers (including the prime one).
    Example:
    Here is a sample run, where the user input is to the right
    of the colons:
         Enter an integer greater than 1: 6
         Enter an integer greater than 1: 100
         Enter an integer greater than 1: 50
         Enter an integer greater than 1: 11
         The sum of the input integers is: 167
    """
    # -------------------------------------------------------------------------
    # TODO: 2. Implement and test this function.
    #   The testing code is already written for you (above).
    # -------------------------------------------------------------------------


def run_test_next_prime():
    """ Tests the   next_prime    function. """
    # -------------------------------------------------------------------------
    # TODO: 3. Implement this TEST function.
    #   It TESTS the  wait_for_prime  function defined below.
    #   Include at least  ** 13 **  tests. (We supplied 12 tests for you.)
    #  __
    #   As usual, include both EXPECTED and ACTUAL results in your test
    #   and compute the latter BY HAND (not by running your program).
    # -------------------------------------------------------------------------
    print()
    print("--------------------------------------------------")
    print("Testing the   next_prime   function:")
    print("--------------------------------------------------")

    format_string = "    next_prime( {} )"
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    print()
    print("TEST STARTED!  Has it ended?")
    expected = 7
    print_expected_result_of_test([6], expected, test_results, format_string)
    actual = next_prime(6)
    print_actual_result_of_test(expected, actual, test_results)
    print("TEST ENDED!")

    # Test 2:
    print()
    print("TEST STARTED!  Has it ended?")
    expected = 11
    print_expected_result_of_test([7], expected, test_results, format_string)
    actual = next_prime(7)
    print_actual_result_of_test(expected, actual, test_results)
    print("TEST ENDED!")

    # Test 3:
    print()
    print("TEST STARTED!  Has it ended?")
    expected = 83
    print_expected_result_of_test([80], expected, test_results, format_string)
    actual = next_prime(80)
    print_actual_result_of_test(expected, actual, test_results)
    print("TEST ENDED!")

    # Test 4:
    print()
    print("TEST STARTED!  Has it ended?")
    expected = 156007
    print_expected_result_of_test([155922], expected, test_results,
                                  format_string)
    actual = next_prime(155922)
    print_actual_result_of_test(expected, actual, test_results)
    print("TEST ENDED!")

    # Test 5:
    print()
    print("TEST STARTED!  Has it ended?")
    expected = 156007
    print_expected_result_of_test([155921], expected, test_results,
                                  format_string)
    actual = next_prime(155921)
    print_actual_result_of_test(expected, actual, test_results)
    print("TEST ENDED!")

    # Test 6:
    print()
    print("TEST STARTED!  Has it ended?")
    expected = 156007
    print_expected_result_of_test([156003], expected, test_results,
                                  format_string)
    actual = next_prime(156003)
    print_actual_result_of_test(expected, actual, test_results)
    print("TEST ENDED!")

    # Test 7:
    print()
    print("TEST STARTED!  Has it ended?")
    expected = 156007
    print_expected_result_of_test([156006], expected, test_results,
                                  format_string)
    actual = next_prime(156006)
    print_actual_result_of_test(expected, actual, test_results)
    print("TEST ENDED!")

    # Test 8:
    print()
    print("TEST STARTED!  Has it ended?")
    expected = 156011
    print_expected_result_of_test([156007], expected, test_results,
                                  format_string)
    actual = next_prime(156007)
    print_actual_result_of_test(expected, actual, test_results)
    print("TEST ENDED!")

    # Test 9:
    print()
    print("TEST STARTED!  Has it ended?")
    expected = 156011
    print_expected_result_of_test([156009], expected, test_results,
                                  format_string)
    actual = next_prime(156009)
    print_actual_result_of_test(expected, actual, test_results)
    print("TEST ENDED!")

    # Test 10:
    print()
    print("TEST STARTED!  Has it ended?")
    expected = 156011
    print_expected_result_of_test([156010], expected, test_results,
                                  format_string)
    actual = next_prime(156010)
    print_actual_result_of_test(expected, actual, test_results)
    print("TEST ENDED!")

    # Test 11:
    print()
    print("TEST STARTED!  Has it ended?")
    expected = 156019
    print_expected_result_of_test([156011], expected, test_results,
                                  format_string)
    actual = next_prime(156011)
    print_actual_result_of_test(expected, actual, test_results)
    print("TEST ENDED!")

    # Test 12:
    print()
    print("TEST STARTED!  Has it ended?")
    expected = 3
    print_expected_result_of_test([2], expected, test_results, format_string)
    actual = next_prime(2)
    print_actual_result_of_test(expected, actual, test_results)
    print("TEST ENDED!")

    # -------------------------------------------------------------------------
    # TODO: 3 (continued):
    #   PUT YOUR TEST   ** IN THE SPACE BETWEEN **   the
    #   print("TEST STARTED!" ...) and print("TEST ENDED") lines below.
    # -------------------------------------------------------------------------
    # Test 13:
    print()
    print("TEST STARTED!  Has it ended?")

    print("TEST ENDED!")

    # SUMMARY of test results:
    print_summary_of_test_results(test_results)


def next_prime(m):
    """
    What comes in:  An integer   m   that is at least 2.
    What goes out:  Returns the smallest prime number strictly greater than m.
    Side effects:   None.
    Examples:
      -- next_prime(6)   returns   7
      -- next_prime(7)   returns  11
      -- next_prime(80)  returns  83
      -- next_prime(155921)  returns  156007  [trust me!]
    Type hints:
      :type m: int
    """
    # -------------------------------------------------------------------------
    # TODO: 4. Implement and test this function.
    #   Note that you should write its TEST function first (above).
    #  __
    #  HINT: do NOT re-assign the parameter m.
    #  Instead, use an AUXILIARY variable (e.g., maybe_prime)
    #  for incrementing the number that you check for primality.
    #  __
    #  IMPLEMENTATION REQUIREMENT:
    #    -- Use (call) the   is_prime   function above appropriately.
    # -------------------------------------------------------------------------


def run_test_sum_to_next_prime():
    """ Tests the   sum_to_next_prime    function. """
    # -------------------------------------------------------------------------
    # TODO: 5. Implement this TEST function.
    #   It TESTS the  sum_to_next_prime  function defined below.
    #   Include at least  ** 13 **  tests. (We supplied 12 tests for you.)
    #  __
    #   As usual, include both EXPECTED and ACTUAL results in your test
    #   and compute the latter BY HAND (not by running your program).
    # -------------------------------------------------------------------------
    print()
    print("--------------------------------------------------")
    print("Testing the   sum_to_next_prime   function:")
    print("--------------------------------------------------")

    format_string = "    sum_to_next_prime( {} )"
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    print()
    print("TEST STARTED!  Has it ended?")
    expected = 6 + 7  # which is 13
    print_expected_result_of_test([6], expected, test_results, format_string)
    actual = sum_to_next_prime(6)
    print_actual_result_of_test(expected, actual, test_results)
    print("TEST ENDED!")

    # Test 2:
    print()
    print("TEST STARTED!  Has it ended?")
    expected = 7 + 8 + 9 + 10 + 11  # which is 45
    print_expected_result_of_test([7], expected, test_results, format_string)
    actual = sum_to_next_prime(7)
    print_actual_result_of_test(expected, actual, test_results)
    print("TEST ENDED!")

    # Test 3:
    print()
    print("TEST STARTED!  Has it ended?")
    expected = 80 + 81 + 82 + 83  # which is 326
    print_expected_result_of_test([80], expected, test_results, format_string)
    actual = sum_to_next_prime(80)
    print_actual_result_of_test(expected, actual, test_results)
    print("TEST ENDED!")

    # Test 4:
    print()
    print("TEST STARTED!  Has it ended?")
    expected = 13412947
    print_expected_result_of_test([155922], expected, test_results,
                                  format_string)
    actual = sum_to_next_prime(155922)
    print_actual_result_of_test(expected, actual, test_results)
    print("TEST ENDED!")

    # Test 5:
    print()
    print("TEST STARTED!  Has it ended?")
    expected = 13568868
    print_expected_result_of_test([155921], expected, test_results,
                                  format_string)
    actual = sum_to_next_prime(155921)
    print_actual_result_of_test(expected, actual, test_results)
    print("TEST ENDED!")

    # Test 6:
    print()
    print("TEST STARTED!  Has it ended?")
    expected = 780025
    print_expected_result_of_test([156003], expected, test_results,
                                  format_string)
    actual = sum_to_next_prime(156003)
    print_actual_result_of_test(expected, actual, test_results)
    print("TEST ENDED!")

    # Test 7:
    print()
    print("TEST STARTED!  Has it ended?")
    expected = 156006 + 156007  # which is 312013
    print_expected_result_of_test([156006], expected, test_results,
                                  format_string)
    actual = sum_to_next_prime(156006)
    print_actual_result_of_test(expected, actual, test_results)
    print("TEST ENDED!")

    # Test 8:
    print()
    print("TEST STARTED!  Has it ended?")
    expected = 780045
    print_expected_result_of_test([156007], expected, test_results,
                                  format_string)
    actual = sum_to_next_prime(156007)
    print_actual_result_of_test(expected, actual, test_results)
    print("TEST ENDED!")

    # Test 9:
    print()
    print("TEST STARTED!  Has it ended?")
    expected = 468030
    print_expected_result_of_test([156009], expected, test_results,
                                  format_string)
    actual = sum_to_next_prime(156009)
    print_actual_result_of_test(expected, actual, test_results)
    print("TEST ENDED!")

    # Test 10:
    print()
    print("TEST STARTED!  Has it ended?")
    expected = 156010 + 156011  # which is 312021
    print_expected_result_of_test([156010], expected, test_results,
                                  format_string)
    actual = sum_to_next_prime(156010)
    print_actual_result_of_test(expected, actual, test_results)
    print("TEST ENDED!")

    # Test 11:
    print()
    print("TEST STARTED!  Has it ended?")
    expected = 1404135
    print_expected_result_of_test([156011], expected, test_results,
                                  format_string)
    actual = sum_to_next_prime(156011)
    print_actual_result_of_test(expected, actual, test_results)
    print("TEST ENDED!")

    # Test 12:
    print()
    print("TEST STARTED!  Has it ended?")
    expected = 2 + 3  # which is 5
    print_expected_result_of_test([2], expected, test_results, format_string)
    actual = sum_to_next_prime(2)
    print_actual_result_of_test(expected, actual, test_results)
    print("TEST ENDED!")

    # -------------------------------------------------------------------------
    # TODO: 5 (continued):
    #   PUT YOUR TEST   ** IN THE SPACE BETWEEN **   the
    #   print("TEST STARTED!" ...) and print("TEST ENDED") lines below.
    # -------------------------------------------------------------------------
    # Test 13:
    print()
    print("TEST STARTED!  Has it ended?")

    print("TEST ENDED!")

    # SUMMARY of test results:
    print_summary_of_test_results(test_results)


def sum_to_next_prime(m):
    """
    What comes in:  An integer   m   that is at least 2.
    What goes out:  Returns the sum of all the numbers from m
      to the smallest prime number strictly greater than m, inclusive.
    Side effects:   None.
    Examples:
      -- next_prime(6)   returns   6 + 7                  which is 13
      -- next_prime(7)   returns   7 + 8 + 9 + 10 + 11    which is 45
      -- next_prime(80)  returns  80 + 81 + 82 + 83       which is 326
      -- next_prime(155921)  returns  13568868  [trust me!]
    Type hints:
      :type m: int
    """
    # -------------------------------------------------------------------------
    # TODO: 6. Implement and test this function.
    #   Note that you should write its TEST function first (above).
    #  __
    #  HINT: do NOT re-assign the parameter m.
    #  Instead, use an AUXILIARY variable (e.g., maybe_prime)
    #  for incrementing the number that you check for primality.
    #  __
    #  IMPLEMENTATION REQUIREMENT:
    #    -- Use (call) the   is_prime   function above appropriately.
    #    -- While you COULD solve this problem by first calling next_prime
    #         and then doing appropriate summing, do NOT use that solution
    #         (so that you get more practice at the  wait-until  pattern).
    # -------------------------------------------------------------------------


def run_test_prime_gap():
    """ Tests the   prime_gap    function. """
    print()
    print("--------------------------------------------------")
    print("Testing the   prime_gap   function:")
    print("--------------------------------------------------")

    format_string = "    prime_gap( {} )"
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    print()
    print("TEST STARTED!  Has it ended?")
    expected = 2
    print_expected_result_of_test([1], expected, test_results, format_string)
    actual = prime_gap(1)
    print_actual_result_of_test(expected, actual, test_results)
    print("TEST ENDED!")

    # Test 2:
    print()
    print("TEST STARTED!  Has it ended?")
    expected = 3
    print_expected_result_of_test([2], expected, test_results, format_string)
    actual = prime_gap(2)
    print_actual_result_of_test(expected, actual, test_results)
    print("TEST ENDED!")

    # Test 3:
    print()
    print("TEST STARTED!  Has it ended?")
    expected = 7
    print_expected_result_of_test([3], expected, test_results, format_string)
    actual = prime_gap(3)
    print_actual_result_of_test(expected, actual, test_results)
    print("TEST ENDED!")

    # Test 4:
    print()
    print("TEST STARTED!  Has it ended?")
    expected = 7
    print_expected_result_of_test([4], expected, test_results, format_string)
    actual = prime_gap(4)
    print_actual_result_of_test(expected, actual, test_results)
    print("TEST ENDED!")

    # Test 5:
    print()
    print("TEST STARTED!  Has it ended?")
    expected = 23
    print_expected_result_of_test([5], expected, test_results, format_string)
    actual = prime_gap(5)
    print_actual_result_of_test(expected, actual, test_results)
    print("TEST ENDED!")

    # Test 6:
    print()
    print("TEST STARTED!  Has it ended?")
    expected = 23
    print_expected_result_of_test([6], expected, test_results, format_string)
    actual = prime_gap(6)
    print_actual_result_of_test(expected, actual, test_results)
    print("TEST ENDED!")

    # Test 7:
    print()
    print("TEST STARTED!  Has it ended?")
    expected = 89
    print_expected_result_of_test([8], expected, test_results, format_string)
    actual = prime_gap(8)
    print_actual_result_of_test(expected, actual, test_results)
    print("TEST ENDED!")

    # Test 8:
    print()
    print("TEST STARTED!  Has it ended?")
    expected = 89
    print_expected_result_of_test([7], expected, test_results, format_string)
    actual = prime_gap(7)
    print_actual_result_of_test(expected, actual, test_results)
    print("TEST ENDED!")

    # Test 9:
    print()
    print("TEST STARTED!  Has it ended?")
    expected = 113
    print_expected_result_of_test([10], expected, test_results, format_string)
    actual = prime_gap(10)
    print_actual_result_of_test(expected, actual, test_results)
    print("TEST ENDED!")

    # Test 10:
    print()
    print("TEST STARTED!  Has it ended?")
    expected = 19609
    print_expected_result_of_test([45], expected, test_results, format_string)
    actual = prime_gap(45)
    print_actual_result_of_test(expected, actual, test_results)
    print("TEST ENDED!")

    # Test 11:
    print()
    print("TEST STARTED!  Has it ended?")
    expected = 19609
    print_expected_result_of_test([50], expected, test_results, format_string)
    actual = prime_gap(50)
    print_actual_result_of_test(expected, actual, test_results)
    print("TEST ENDED!")

    # Test 12:
    print()
    print("TEST STARTED!  Has it ended?")
    expected = 19609
    print_expected_result_of_test([52], expected, test_results, format_string)
    actual = prime_gap(52)
    print_actual_result_of_test(expected, actual, test_results)
    print("TEST ENDED!")

    # Test 13:
    print()
    print("TEST STARTED!  Has it ended?")
    expected = 31397
    print_expected_result_of_test([54], expected, test_results, format_string)
    actual = prime_gap(54)
    print_actual_result_of_test(expected, actual, test_results)
    print("TEST ENDED!")

    # Test 14:
    print()
    print("TEST STARTED!  Has it ended?")
    expected = 31397
    print_expected_result_of_test([56], expected, test_results, format_string)
    actual = prime_gap(56)
    print_actual_result_of_test(expected, actual, test_results)
    print("TEST ENDED!")

    # Test 15:
    print()
    print("TEST STARTED!  Has it ended?")
    expected = 31397
    print_expected_result_of_test([58], expected, test_results, format_string)
    actual = prime_gap(58)
    print_actual_result_of_test(expected, actual, test_results)
    print("TEST ENDED!")

    # Test 16:
    print()
    print("TEST STARTED!  Has it ended?")
    expected = 31397
    print_expected_result_of_test([60], expected, test_results, format_string)
    actual = prime_gap(60)
    print_actual_result_of_test(expected, actual, test_results)
    print("TEST ENDED!")

    # Test 17:
    print()
    print("TEST STARTED!  Has it ended?")
    expected = 31397
    print_expected_result_of_test([62], expected, test_results, format_string)
    actual = prime_gap(62)
    print_actual_result_of_test(expected, actual, test_results)
    print("TEST ENDED!")

    # Test 18:
    print()
    print("TEST STARTED!  Has it ended?")
    expected = 31397
    print_expected_result_of_test([64], expected, test_results, format_string)
    actual = prime_gap(64)
    print_actual_result_of_test(expected, actual, test_results)
    print("TEST ENDED!")

    # Test 19:
    print()
    print("TEST STARTED!  Has it ended?")
    expected = 31397
    print_expected_result_of_test([66], expected, test_results, format_string)
    actual = prime_gap(66)
    print_actual_result_of_test(expected, actual, test_results)
    print("TEST ENDED!")

    # Test 20:
    print()
    print("TEST STARTED!  Has it ended?")
    expected = 31397
    print_expected_result_of_test([68], expected, test_results, format_string)
    actual = prime_gap(68)
    print_actual_result_of_test(expected, actual, test_results)
    print("TEST ENDED!")

    # Test 21:
    print()
    print("TEST STARTED!  Has it ended?")
    expected = 31397
    print_expected_result_of_test([70], expected, test_results, format_string)
    actual = prime_gap(70)
    print_actual_result_of_test(expected, actual, test_results)
    print("TEST ENDED!")

    # Test 22:
    print()
    print("TEST STARTED!  Has it ended?")
    expected = 31397
    print_expected_result_of_test([72], expected, test_results, format_string)
    actual = prime_gap(72)
    print_actual_result_of_test(expected, actual, test_results)
    print("TEST ENDED!")

    # Test 23:
    print()
    print("TEST STARTED!  Has it ended?")
    expected = 155921
    print_expected_result_of_test([74], expected, test_results, format_string)
    actual = prime_gap(74)
    print_actual_result_of_test(expected, actual, test_results)
    print("TEST ENDED!")

    # Test 24:
    print()
    print("TEST STARTED!  Has it ended?")
    expected = 155921
    print_expected_result_of_test([80], expected, test_results, format_string)
    actual = prime_gap(80)
    print_actual_result_of_test(expected, actual, test_results)
    print("TEST ENDED!")

    # Test 25:
    print()
    print("TEST STARTED!  Has it ended?")
    expected = 370261
    print_expected_result_of_test([100], expected, test_results, format_string)
    actual = prime_gap(100)
    print_actual_result_of_test(expected, actual, test_results)
    print("TEST ENDED!")

    # Test 26:
    print()
    print("TEST STARTED!  Has it ended?")
    expected = 1357201
    print_expected_result_of_test([120], expected, test_results, format_string)
    actual = prime_gap(120)
    print_actual_result_of_test(expected, actual, test_results)
    print("TEST ENDED!")

    # Test 27:
    print()
    print("TEST STARTED!  Has it ended?")
    expected = 4652353
    print_expected_result_of_test([150], expected, test_results, format_string)
    actual = prime_gap(150)
    print_actual_result_of_test(expected, actual, test_results)
    print("TEST ENDED!")

    # SUMMARY of test results:
    print_summary_of_test_results(test_results)


def prime_gap(gap):
    """
    What comes in:  An integer   gap   that is at least 1.
    What goes out:
       Returns the smallest prime number whose "gap" is at least the given gap,
       where the "gap" of a prime number is the difference between
       that prime number and the next-smallest prime number.
    Side effects:   None.
    Examples:
      -- prime_gap(1) returns 2, because the next prime after 2 is 3,
           and so the gap for 2 is 3 - 2 = 1,
           and 2 is the smallest (and in fact, ONLY) prime with gap 1.
      -- prime_gap(2) returns 3, because the next prime after 3 is 5,
           and so the gap for 3 is 5 - 3 = 2,
           and 3 is the smallest prime with gap 2.
      -- prime_gap(3) returns 7, because the next prime after 7 is 11,
           and so the gap for 7 is 11 - 7 = 4,
           and 7 is the smallest prime with gap 3 or more.
           (Note: There are no primes except 2 that have a gap that is odd.)
      -- prime_gap(4) returns 7 for similar reasons.
      -- prime_gap(6) returns 23, because the next prime after 23 is 29,
           and so the gap for 23 is 29 - 23 = 6,
           and 23 is the smallest prime with gap 6.
      -- prime_gap(8) returns 89, because the next prime after 89 is 97,
           and so the gap for 89 is 97 - 89 = 8,
           and 89 is the smallest prime with gap 8.
      -- prime_gap(52)  returns  19609  [trust me!]
    Type hints:
      :type gap: int
      :rtype:    int
    """
    # -------------------------------------------------------------------------
    # TODO: 7. Implement and test this function.
    #   The testing code is already written for you (above).
    #  __
    #  IMPLEMENTATION REQUIREMENT:
    #    -- Use (call) the   *** next_prime ***   function
    #       (that you implemented above) appropriately.
    #  HINT:  The last few tests may take up to a minute or two, depending
    #         on your computer.  If they take longer (or never complete),
    #         then you are probably not using   next_prime   correctly.
    # -------------------------------------------------------------------------


def run_test_wait_for_sum_of_cubes():
    """ Tests the   wait_for_sum_of_cubes    function. """
    # -------------------------------------------------------------------------
    # TODO: 8. Implement this TEST function.
    #   It TESTS the  wait_for_sum_of_cubes  function defined below.
    #   Include at least  ** 20 **  tests. (We supplied 18 tests for you.)
    #  __
    #   As usual, include both EXPECTED and ACTUAL results in your test
    #   and compute the latter BY HAND (not by running your program).
    # -------------------------------------------------------------------------
    print()
    print("--------------------------------------------------")
    print("Testing the   wait_for_sum_of_cubes   function:")
    print("--------------------------------------------------")

    format_string = "    wait_for_sum_of_cubes( {} )"
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    print()
    print("TEST STARTED!  Has it ended?")
    expected = 2
    print_expected_result_of_test([4.3], expected, test_results, format_string)
    actual = wait_for_sum_of_cubes(4.3)
    print_actual_result_of_test(expected, actual, test_results)
    print("TEST ENDED!")

    # Test 2:
    print()
    print("TEST STARTED!  Has it ended?")
    expected = 1
    print_expected_result_of_test([1], expected, test_results, format_string)
    actual = wait_for_sum_of_cubes(1)
    print_actual_result_of_test(expected, actual, test_results)
    print("TEST ENDED!")

    # Test 3:
    print()
    print("TEST STARTED!  Has it ended?")
    expected = 2
    print_expected_result_of_test([1.000000000001], expected, test_results,
                                  format_string)
    actual = wait_for_sum_of_cubes(1.000000000001)
    print_actual_result_of_test(expected, actual, test_results)
    print("TEST ENDED!")

    # Test 4:
    print()
    print("TEST STARTED!  Has it ended?")
    expected = 2
    print_expected_result_of_test([9], expected, test_results, format_string)
    actual = wait_for_sum_of_cubes(9)
    print_actual_result_of_test(expected, actual, test_results)
    print("TEST ENDED!")

    # Test 5:
    print()
    print("TEST STARTED!  Has it ended?")
    expected = 3
    print_expected_result_of_test([9.000000000001], expected, test_results,
                                  format_string)
    actual = wait_for_sum_of_cubes(9.000000000001)
    print_actual_result_of_test(expected, actual, test_results)
    print("TEST ENDED!")

    # Test 6:
    print()
    print("TEST STARTED!  Has it ended?")
    expected = 3
    print_expected_result_of_test([35.9999999999999], expected, test_results,
                                  format_string)
    actual = wait_for_sum_of_cubes(35.9999999999999)
    print_actual_result_of_test(expected, actual, test_results)
    print("TEST ENDED!")

    # Test 7:
    print()
    print("TEST STARTED!  Has it ended?")
    expected = 3
    print_expected_result_of_test([36], expected, test_results, format_string)
    actual = wait_for_sum_of_cubes(36)
    print_actual_result_of_test(expected, actual, test_results)
    print("TEST ENDED!")

    # Test 8:
    print()
    print("TEST STARTED!  Has it ended?")
    expected = 4
    print_expected_result_of_test([36.0000001], expected, test_results,
                                  format_string)
    actual = wait_for_sum_of_cubes(36.0000001)
    print_actual_result_of_test(expected, actual, test_results)
    print("TEST ENDED!")

    # Test 9:
    print()
    print("TEST STARTED!  Has it ended?")
    expected = 4
    print_expected_result_of_test([58], expected, test_results, format_string)
    actual = wait_for_sum_of_cubes(58)
    print_actual_result_of_test(expected, actual, test_results)
    print("TEST ENDED!")

    # Test 10:
    print()
    print("TEST STARTED!  Has it ended?")
    expected = 4
    print_expected_result_of_test([100], expected, test_results, format_string)
    actual = wait_for_sum_of_cubes(100)
    print_actual_result_of_test(expected, actual, test_results)
    print("TEST ENDED!")

    # Test 11:
    print()
    print("TEST STARTED!  Has it ended?")
    expected = 5
    print_expected_result_of_test([100.00000001], expected, test_results,
                                  format_string)
    actual = wait_for_sum_of_cubes(100.00000001)
    print_actual_result_of_test(expected, actual, test_results)
    print("TEST ENDED!")

    # Test 12:
    print()
    print("TEST STARTED!  Has it ended?")
    expected = 8
    print_expected_result_of_test([1000], expected, test_results,
                                  format_string)
    actual = wait_for_sum_of_cubes(1000)
    print_actual_result_of_test(expected, actual, test_results)
    print("TEST ENDED!")

    # Test 13:
    print()
    print("TEST STARTED!  Has it ended?")
    expected = 1
    print_expected_result_of_test([-4.2], expected, test_results,
                                  format_string)
    actual = wait_for_sum_of_cubes(-4.2)
    print_actual_result_of_test(expected, actual, test_results)
    print("TEST ENDED!")

    # Test 14:
    print()
    print("TEST STARTED!  Has it ended?")
    expected = 8
    print_expected_result_of_test([1296], expected, test_results,
                                  format_string)
    actual = wait_for_sum_of_cubes(1296)
    print_actual_result_of_test(expected, actual, test_results)
    print("TEST ENDED!")

    # Test 15:
    print()
    print("TEST STARTED!  Has it ended?")
    expected = 9
    print_expected_result_of_test([1296.00000001], expected, test_results,
                                  format_string)
    actual = wait_for_sum_of_cubes(1296.00000001)
    print_actual_result_of_test(expected, actual, test_results)
    print("TEST ENDED!")

    # Test 16:
    print()
    print("TEST STARTED!  Has it ended?")
    expected = 25
    print_expected_result_of_test([100000], expected, test_results,
                                  format_string)
    actual = wait_for_sum_of_cubes(100000)
    print_actual_result_of_test(expected, actual, test_results)
    print("TEST ENDED!")

    # Test 17:
    print()
    print("TEST STARTED!  Has it ended?")
    expected = 38
    print_expected_result_of_test([500000], expected, test_results,
                                  format_string)
    actual = wait_for_sum_of_cubes(500000)
    print_actual_result_of_test(expected, actual, test_results)
    print("TEST ENDED!")

    # Test 18:
    print()
    print("TEST STARTED!  Has it ended?")
    expected = 251
    print_expected_result_of_test([1000000000], expected, test_results,
                                  format_string)
    actual = wait_for_sum_of_cubes(1000000000)
    print_actual_result_of_test(expected, actual, test_results)
    print("TEST ENDED!")

    # -------------------------------------------------------------------------
    # TODO: 8 (continued):
    #   PUT YOUR TEST   ** IN THE SPACE BETWEEN **   the
    #   print("TEST STARTED!" ...) and print("TEST ENDED") lines below.
    #  __
    #  *** Use   wait_for_sum_of_cubes(30.33)   as your test here.
    #  Compute the expected answer BY HAND, as always.
    # -------------------------------------------------------------------------
    # Test 19:
    print()
    print("TEST STARTED!  Has it ended?")

    print("TEST ENDED!")

    # -------------------------------------------------------------------------
    # TODO: 8 (continued):
    #   PUT YOUR TEST   ** IN THE SPACE BETWEEN **  the
    #   print("TEST STARTED!" ...) and print("TEST ENDED") lines below.
    # -------------------------------------------------------------------------
    # Test 20:
    print()
    print("TEST STARTED!  Has it ended?")

    print("TEST ENDED!")

    # SUMMARY of test results:
    print_summary_of_test_results(test_results)


def wait_for_sum_of_cubes(x):
    """
    What comes in:  A number x.
    What goes out:  Returns the smallest positive integer n
      such that the sum
           1 cubed  +  2 cubed  +  3 cubed  +  ...  + n cubed
      is greater than or equal to x.
    Side effects:   None.
    Examples:
      -- If x is 4.3, this function returns   2   because:
            1 cubed = 1 which is less than 4.3
         but
            1 cubed + 2 cubed = 9 which is greater than or equal to 4.3
      -- For similar reasons, if x is any number in the range (1, 9]
         (that is, numbers greater than 1 but less than or equal to 9),
         this function returns 2.
      -- If x is 58, this function returns   4   because:
            1 cubed + 2 cubed + 3 cubed = 36   which is less than 58
         but
            1 cubed + 2 cubed + 3 cubed + 4 cubed = 100
              which is greater than or equal to 58
      -- For similar reasons, if x is any number in the range (36, 100],
         this function returns 4.
      -- If x is 1000, this function returns 8 because:
              1 + 8 + 27 + 64 + ... + (7**3) = 784
            but
              1 + 8 + 27 + 64 + ... + (8**3) = 1296
      -- For similar reasons, f x is 1296, this function returns 8.
      -- if x is -5.2 (or any number less than or equal to 1),
           this function returns 1.
    Type hints:
      :type x: float  [or an int]
    """
    # -------------------------------------------------------------------------
    # TODO: 9. Implement and test this function.
    #   Note that you should write its TEST function first (above).
    #  __
    #  IMPLEMENTATION REQUIREMENT:
    #   -- Solve this using the   wait-until-event   pattern.
    #  __
    #  Note for the mathematically inclined:  One could figure out
    #  (or look up) a formula that would allow a faster computation.
    #  But no fair using any such approach in this implementation.
    # -------------------------------------------------------------------------


###############################################################################
# Our tests use the following to print error messages in red.
# Do NOT change it.  You do NOT have to do anything with it.
###############################################################################

def print_expected_result_of_test(arguments, expected,
                                  test_results, format_string, suffix=""):
    testing_helper.print_expected_result_of_test(arguments, expected,
                                                 test_results, format_string,
                                                 suffix)


def print_actual_result_of_test(expected, actual, test_results,
                                precision=None):
    testing_helper.print_actual_result_of_test(expected, actual,
                                               test_results, precision)


def print_summary_of_test_results(test_results):
    testing_helper.print_summary_of_test_results(test_results)


# To allow color-coding the output to the console:
USE_COLORING = True  # Change to False to revert to OLD style coloring

testing_helper.USE_COLORING = USE_COLORING
if USE_COLORING:
    # noinspection PyShadowingBuiltins
    print = testing_helper.print_colored
else:
    # noinspection PyShadowingBuiltins
    print = testing_helper.print_uncolored

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# The   try .. except   prevents error messages on the console from being
# intermingled with ordinary output to the console.
# -----------------------------------------------------------------------------
try:
    main()
except Exception:
    print("ERROR - While running this test,", color="red")
    print("your code raised the following exception:", color="red")
    print()
    time.sleep(1)
    raise
