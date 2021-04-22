"""
This project lets you practice NESTED LOOPS (i.e., loops within loops)
in the context of PRINTING on the CONSOLE.

Authors: David Mutchler, Vibha Alangar, Dave Fisher, Matt Boutell, Mark Hays,
         Mohammed Noureddine, Sana Ebrahimi, Sriram Mohan, their colleagues and
         PUT_YOUR_NAME_HERE.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.


def main():
    """ Calls the other functions to test them. """
    print()
    print("Un-comment and re-comment calls in MAIN one by one as you work.")

    # run_test_triangle_right_justified()
    # run_test_triangle_upside_down()
    # run_test_vee()
    # run_test_numbers_constant_forward()
    # run_test_numbers_constant_backwards()
    # run_test_numbers_increasing_forward()


def run_test_triangle_right_justified():
    """ Tests the    triangle_right_justified    function. """
    print()
    print("--------------------------------------------------")
    print("Testing the   TRIANGLE_RIGHT_JUSTIFIED   function:")
    print("--------------------------------------------------")

    print("Test 1 of triangle_right_justified: (5)")
    triangle_right_justified(5)

    print("Test 2 of triangle_right_justified: (1)")
    triangle_right_justified(1)

    print("Test 3 of triangle_right_justified: (3)")
    triangle_right_justified(3)

    print("Test 4 of triangle_right_justified: (6)")
    triangle_right_justified(6)


def triangle_right_justified(r):
    """
    Prints a triangle of numbers, with r rows.
    It looks the same as a previous example, but right-justified.
    So the first row has some spaces, then a 1,
    the 2nd row has some spaces, then a 12,
    the 3rd row has some spaces, then a 123,
    and so forth, in such a way that the rightmost numbers line up.
    For example, when r = 5:
           1
          12
         123
        1234
       12345
    Precondition:  r is a non-negative integer.
    For purposes of "lining up", assume r is a single digit.
    """
    # -------------------------------------------------------------------------
    # TODO: 2. Implement and test this function.
    #          Some tests are already written for you (above).
    #  __
    #  HINT: Do the following problem FIRST, then convert x's to spaces:
    #          xxxx1
    #          xxx12
    #          xx123
    #          x1234
    #          12345
    #  __
    #  HINT: One way to solve this problem is to have TWO inner loops,
    #        one after the other.
    #  __
    #  IMPLEMENTATION RESTRICTION:
    #    ** You may NOT use string multiplication **
    #    in this or the other problems in this module, as doing so would
    #    defeat the goal of providing practice at loops within loops.
    # -------------------------------------------------------------------------


def run_test_triangle_upside_down():
    """ Tests the    triangle_upside_down    function. """
    print()
    print("----------------------------------------------")
    print("Testing the   TRIANGLE_UPSIDE_DOWN   function:")
    print("----------------------------------------------")

    print("Test 1 of triangle_upside_down: (5)")
    triangle_upside_down(5)

    print("Test 2 of triangle_upside_down: (1)")
    triangle_upside_down(1)

    print("Test 3 of triangle_upside_down: (3)")
    triangle_upside_down(3)

    print("Test 4 of triangle_upside_down: (6)")
    triangle_upside_down(6)


def triangle_upside_down(r):
    """
    Prints a triangle of numbers, with r rows.
    It looks the same as the previous problem,
    but with rows in reversed order.  For example, when r = 5:
       12345
        1234
         123
          12
           1
    Precondition:  r is a non-negative integer.
    For purposes of "lining up", assume r is a single digit.
    """
    # -------------------------------------------------------------------------
    # TODO: 3. Implement and test this function.
    #          Some tests are already written for you (above).
    #  IMPLEMENTATION RESTRICTION: ** You may NOT use string multiplication **.
    # -------------------------------------------------------------------------


def run_test_vee():
    """ Tests the    vee    function. """
    print()
    print("----------------------------------------------")
    print("Testing the   VEE   function:")
    print("----------------------------------------------")

    print("Test 1 of vee: (5)")
    vee(5)

    print("Test 2 of vee: (1)")
    vee(1)

    print("Test 3 of vee: (3)")
    vee(3)

    print("Test 4 of vee: (6)")
    vee(6)


def vee(r):
    """
    Prints a "V" of numbers, with r rows.
    It looks like this example, when r = 5:
        12345-54321
         1234-4321
          123-321
           12-21
            1-1

    Note the single dash ("-") in each row.

    Here is another example, when r = 3:
         123-321
          12-21
           1-1

    Precondition:  r is a non-negative integer.
    For purposes of "lining up", assume r is a single digit.
    """
    # -------------------------------------------------------------------------
    # TODO: 4. Implement and test this function.
    #          Some tests are already written for you (above).
    #  IMPLEMENTATION RESTRICTION: ** You may NOT use string multiplication **.
    # -------------------------------------------------------------------------


def run_test_numbers_constant_forward():
    """ Tests the    numbers_constant_forward    function. """
    print()
    print("--------------------------------------------------")
    print("Testing the   NUMBERS_CONSTANT_FORWARD   function:")
    print("--------------------------------------------------")

    print("Test 1 of numbers_constant_forward: (4, 7, 3)")
    numbers_constant_forward(4, 7, 3)

    print("Test 2 of numbers_constant_forward: (3, 5, 8)")
    numbers_constant_forward(3, 5, 8)

    print("Test 3 of numbers_constant_forward: (1, 5, 4)")
    numbers_constant_forward(1, 5, 4)

    print("Test 4 of numbers_constant_forward: (7, 3, 4)")
    numbers_constant_forward(7, 3, 4)


def numbers_constant_forward(r, maxnum, n):
    """
    Prints a rectangle of numbers, with r rows.
    Each row has n 1s, then a space, then n 2s,
    then a space, then n 3s, etc. up to n maxnum's.
    (It is easiest to include a space after the last
    set of digits on each row, but you don't have to.)

    For example, when r = 4, maxnum = 7 and n = 3:
       111 222 333 444 555 666 777
       111 222 333 444 555 666 777
       111 222 333 444 555 666 777
       111 222 333 444 555 666 777
    Notice that there were r = 4 rows;
    each row had numbers that went from 1 to maxnum = 7; and
    there were n occurrences of each number on each row.

    Here is another example,
    when r = 3, maxnum = 5 and n = 8:
       11111111 22222222 33333333 44444444 55555555
       11111111 22222222 33333333 44444444 55555555
       11111111 22222222 33333333 44444444 55555555

    Preconditions:  r, maxnum and n are positive integers.
    """
    # -------------------------------------------------------------------------
    # TODO: 5. Implement and test this function.
    #          Some tests are already written for you (above).
    #  __
    #  HINT: What loop structure do you need for this problem?
    #  __
    #  IMPLEMENTATION RESTRICTION: ** You may NOT use string multiplication **.
    # -------------------------------------------------------------------------


def run_test_numbers_constant_backwards():
    """ Tests the    numbers_constant_backwards    function. """
    print()
    print("----------------------------------------------------")
    print("Testing the   NUMBERS_CONSTANT_BACKWARDS   function:")
    print("----------------------------------------------------")

    print("Test 1 of numbers_constant_backwards: (4, 7, 3)")
    numbers_constant_backwards(4, 7, 3)

    print("Test 2 of numbers_constant_backwards: (3, 5, 8)")
    numbers_constant_backwards(3, 5, 8)

    print("Test 3 of numbers_constant_backwards: (1, 5, 4)")
    numbers_constant_backwards(1, 5, 4)

    print("Test 4 of numbers_constant_backwards: (7, 3, 4)")
    numbers_constant_backwards(7, 3, 4)


def numbers_constant_backwards(r, maxnum, n):
    """
    Prints a rectangle of numbers, with r rows.
    It looks the same as the previous problem, but with
    numbers reversed. For example, when r = 4, maxnum = 7 and n = 3:
       777 666 555 444 333 222 111
       777 666 555 444 333 222 111
       777 666 555 444 333 222 111
       777 666 555 444 333 222 111
    Preconditions:  r, maxnum and n are positive integers.
    """
    # -------------------------------------------------------------------------
    # TODO: 6. Implement and test this function.
    #          Some tests are already written for you (above).
    #  __
    #  HINT: What loop structure do you need for this problem?
    #  __
    #  IMPLEMENTATION RESTRICTION: ** You may NOT use string multiplication **.
    # -------------------------------------------------------------------------


def run_test_numbers_increasing_forward():
    """ Tests the    numbers_increasing_forward    function. """
    print()
    print("----------------------------------------------------")
    print("Testing the   NUMBERS_INCREASING_FORWARD   function:")
    print("----------------------------------------------------")

    print("Test 1 of numbers_increasing_forward: (4, 3)")
    numbers_increasing_forward(4, 3)

    print("Test 2 of numbers_increasing_forward: (2, 7)")
    numbers_increasing_forward(2, 7)

    print("Test 3 of numbers_increasing_forward: (5, 6)")
    numbers_increasing_forward(5, 6)

    print("Test 4 of numbers_increasing_forward: (1, 7)")
    numbers_increasing_forward(1, 7)

    print("Test 5 of numbers_increasing_forward: (2, 1)")
    numbers_increasing_forward(2, 1)


def numbers_increasing_forward(r, maxnum):
    """
    Prints a rectangle of numbers, with r rows, as in the previous
    two problems.  But now each row has one 1, two 2s, three 3s,
    four 4s, etc. up to the given maxnum.

    For example, when r = 4 and maxnum = 3:
       1 22 333
       1 22 333
       1 22 333
       1 22 333

    Another example, when r = 2 and maxnum = 7:
       1 22 333 4444 55555 666666 7777777
       1 22 333 4444 55555 666666 7777777

    Preconditions:  r and maxnum are positive integers.
    """
    # -------------------------------------------------------------------------
    # TODO: 7. Implement and test this function.
    #          Some tests are already written for you (above).
    #  __
    #  HINT: What loop structure do you need for this problem?
    #  __
    #  IMPLEMENTATION RESTRICTION: ** You may NOT use string multiplication **.
    # -------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
