"""
This project lets you practice NESTED LOOPS (i.e., loops within loops)
in the context of PRINTING on the CONSOLE.

Authors: David Mutchler, Vibha Alangar, Dave Fisher, Matt Boutell, Mark Hays,
         Mohammed Noureddine, Sana Ebrahimi, Sriram Mohan, their colleagues and
         PUT_YOUR_NAME_HERE.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.


def main():
    """ Calls the other functions to test them. """
    print("-----------------------------------------------")
    print("Un-comment each of the following TEST functions")
    print("as you implement the functions that they test.")
    print("-----------------------------------------------")

    # run_test_alternating_brackets()
    # run_test_triangle_same_number_in_each_row()
    # run_test_triangle_all_numbers_in_each_row()


def run_test_alternating_brackets():
    """ Tests the    alternating_brackets    function. """
    print()
    print("----------------------------------------------------------")
    print("Testing the   ALTERNATING_BRACKETS   function:")
    print("----------------------------------------------------------")

    print("Test 1 of alternating_brackets: (5, 2)")
    alternating_brackets(5, 2)

    print("Test 2 of alternating_brackets: (3, 1)")
    alternating_brackets(3, 1)

    print("Test 3 of alternating_brackets: (4, 4)")
    alternating_brackets(4, 4)

    print("Test 4 of alternating_brackets: (8, 6)")
    alternating_brackets(8, 6)


def alternating_brackets(m, n):
    """
    Prints alternating left/right square brackets:  m on the first row,
    m-1 on the next row, m-2 on the next, etc, until n on the last row.
    For example, when m = 5 and n = 2:
       [][][
       [][]
       [][
       []
    Precondition:  m and n are positive integers with m >= n.
    """
    # -------------------------------------------------------------------------
    # TODO: 2. Implement and test this function.
    #          Some tests are already written for you (above).
    #  IMPLEMENTATION RESTRICTION: ** You may NOT use string multiplication **.
    # -------------------------------------------------------------------------


def run_test_triangle_same_number_in_each_row():
    """ Tests the    triangle_same_number_in_each_row    function. """
    print()
    print("----------------------------------------------------------")
    print("Testing the   TRIANGLE_SAME_NUMBER_IN_EACH_ROW   function:")
    print("----------------------------------------------------------")

    print("Test 1 of triangle_same_number_in_each_row: (5)")
    triangle_same_number_in_each_row(5)

    print("Test 2 of triangle_same_number_in_each_row: (1)")
    triangle_same_number_in_each_row(1)

    print("Test 3 of triangle_same_number_in_each_row: (3)")
    triangle_same_number_in_each_row(3)

    print("Test 4 of triangle_same_number_in_each_row: (6)")
    triangle_same_number_in_each_row(6)


def triangle_same_number_in_each_row(r):
    """
    Prints a triangle of numbers, with r rows.
    The first row is 1, the 2nd is 22, the 3rd is 333, etc.
    For example, when r = 5:
       1
       22
       333
       4444
       55555
    Precondition:  r is a non-negative integer.
    """
    # -------------------------------------------------------------------------
    # TODO: 3. Implement and test this function.
    #          Some tests are already written for you (above).
    #  IMPLEMENTATION RESTRICTION: ** You may NOT use string multiplication **.
    # -------------------------------------------------------------------------


def run_test_triangle_all_numbers_in_each_row():
    """ Tests the    triangle_all_numbers_in_each_row    function. """
    print()
    print("----------------------------------------------------------")
    print("Testing the   TRIANGLE_ALL_NUMBERS_IN_EACH_ROW   function:")
    print("----------------------------------------------------------")

    print("Test 1 of triangle_all_numbers_in_each_row: (5)")
    triangle_all_numbers_in_each_row(5)

    print("Test 2 of triangle_all_numbers_in_each_row: (1)")
    triangle_all_numbers_in_each_row(1)

    print("Test 3 of triangle_all_numbers_in_each_row: (3)")
    triangle_all_numbers_in_each_row(3)

    print("Test 4 of triangle_all_numbers_in_each_row: (6)")
    triangle_all_numbers_in_each_row(6)


def triangle_all_numbers_in_each_row(r):
    """
    Prints a triangle of numbers, with r rows.
    The first row is 1, the 2nd is 12, the 3rd is 123, etc.
    For example, when r = 5:
       1
       12
       123
       1234
       12345
    Precondition:  r is a non-negative integer.
    """
    # -------------------------------------------------------------------------
    # TODO: 4. Implement and test this function.
    #          Some tests are already written for you (above).
    #  IMPLEMENTATION RESTRICTION: ** You may NOT use string multiplication **.
    # -------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
