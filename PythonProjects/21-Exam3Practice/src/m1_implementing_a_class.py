"""
PRACTICE Exam 3.

This problem provides practice at:  *** IMPLEMENTING CLASSES. ***

Authors: David Mutchler, Vibha Alangar, Dave Fisher, Matt Boutell, Mark Hays,
         Mohammed Noureddine, Sana Ebrahimi, Sriram Mohan, their colleagues and
         PUT_YOUR_NAME_HERE.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

###############################################################################
# TODO: 2.
#  Students:
#  __
#  These problems have DIFFICULTY and TIME ratings:
#    DIFFICULTY rating:  1 to 10, where:
#       1 is very easy
#       3 is an "easy" Exam 3 question.
#       5 is a "typical" Exam 3 question.
#       7 is a "hard" Exam 3 question.
#      10 is an EXTREMELY hard problem (too hard for a Exam 3 question)
#  __
#    TIME ratings: A ROUGH estimate of the number of minutes that we
#       would expect a well-prepared student to take on the problem.
#  __
#    IMPORTANT: For ALL the problems in this module,
#      if you reach the time estimate and are NOT close to a solution,
#      STOP working on that problem and ASK YOUR INSTRUCTOR FOR HELP on it,
#      in class or via Piazza.
#  __
#  After you read (and understand) the above, change this _TODO_ to DONE.
###############################################################################

import math
import time
from numbers import Number
from typing import List
import testing_helper


###############################################################################
# TODO: 3.  READ the   Point   class defined below.
#  Note especially its methods:
#      clone
#      distance_from
#  For full credit, you must use (call) these as appropriate in your code.
#  After you UNDERSTAND the Point class, change the above _TODO_ to DONE.
###############################################################################
class Point:
    """ Represents a point in 2-dimensional space. """

    def __init__(self, x, y):
        """ Sets instance variables  x  and  y  to the given coordinates. """
        self.x = x
        self.y = y

    def __repr__(self):
        """
        Returns a string representation of this Point.
        For each coordinate (x and y), the representation:
          - Uses no decimal points if the number is close to an integer,
          - Else it uses 2 decimal places after the decimal point.
        Examples:
           Point(10, 3.14)
           Point(3.01, 2.99)
        """
        decimal_places = 2  # Use 2 places after the decimal point

        formats = []
        numbers = []
        for coordinate in (self.x, self.y):
            if abs(coordinate - round(coordinate)) < (10 ** -decimal_places):
                # Treat it as an integer:
                formats.append('{}')
                numbers.append(round(coordinate))
            else:
                # Treat it as a float to decimal_places decimal places:
                formats.append('{:.' + str(decimal_places) + 'f}')
                numbers.append(round(coordinate, decimal_places))

        format_string = 'Point(' + formats[0] + ', ' + formats[1] + ')'
        return format_string.format(numbers[0], numbers[1])

    def __eq__(self, p2):
        """
        Defines == for Points:  a == b   is equivalent to  a.__eq__(b).
        Treats two numbers as "equal" if they are within 6 decimal
        places of each other for both x and y coordinates.
        """
        return (round(self.x, 6) == round(p2.x, 6) and
                round(self.y, 6) == round(p2.y, 6))

    def clone(self):
        """ Returns a Point whose x and y are the same as this Point's. """
        return Point(self.x, self.y)

    def distance_from(self, p2):
        """ Returns the distance this Point is from the given Point. """
        dx_squared = (self.x - p2.x) ** 2
        dy_squared = (self.y - p2.y) ** 2
        return math.sqrt(dx_squared + dy_squared)


###############################################################################
# The  main  function, which calls the tests.
###############################################################################
def main():
    """ Calls the   TEST   functions in this module. """
    # -------------------------------------------------------------------------
    # Uncomment the following calls to the testing functions one at a time
    # as you work the problems.
    # -------------------------------------------------------------------------
    print()
    print('Un-comment the calls in MAIN one by one')
    print(' to run the testing code as you complete the TODOs.')

    # run_test_init()
    # run_test_multiply_me()
    # run_test_make_child()
    # run_test_get_point()
    # run_test_get_distance()
    # run_test_swap_colors()
    # run_test_get_recent_color()
    # run_test_get_bigger_size_color()


###############################################################################
# The   Blob   class (and its methods) begins here.
###############################################################################
# -----------------------------------------------------------------------------
# DIFFICULTY AND TIME RATINGS (see top of this file for explanation)
#    DIFFICULTY for the methods in this class: the first several are 3-5,
#       the last two are 5-6.
#    TIME ESTIMATE for implementing the ENTIRE class:   35 to 45 minutes.
# -----------------------------------------------------------------------------

class Blob:

    def __init__(self, c, n):
        """
        What comes in:
          -- self
          -- a string that represents a color
          -- a positive number
        What goes out: Nothing (i.e., None).
        Side effects:
           Sets instance variables to the given arguments, naming them:
             -- self.color
             -- self.size
           Also, sets other instance variables as needed by other Blob methods.
        Type hints:
          :type c: str
          :type n: float
        """
        # ---------------------------------------------------------------------
        # TODO: 4.
        #  a. READ specifications of this method (above).
        #       Also READ its tests (below) if you need additional
        #       clarification of the specification of this method.
        #  b. Implement and test this method.
        # ---------------------------------------------------------------------

    def multiply_me(self):
        """
        What comes in:
          -- self
        What goes out: Nothing (i.e., None).
        Side effects:
           Mutates this Blob by multiplying its size by 10.
        """
        # ---------------------------------------------------------------------
        # TODO: 5.
        #  a. READ specifications of this method (above).
        #       Also READ its tests (below) if you need additional
        #       clarification of the specification of this method.
        #  b. Implement and test this method.
        # ---------------------------------------------------------------------

    def make_child(self, other_blob):
        """
        What comes in:
          -- self
          -- other_blob:  Another Blob
        What goes out:
          Returns a new Blob object whose:
             -- color is the same as this Blob's color
             -- size is the same as the given other_blob's size
        Side effects: None.
        Type hints:
          :type other_blob: Blob
          :rtype: Blob
        """
        # ---------------------------------------------------------------------
        # TODO: 6.
        #  a. READ specifications of this method (above).
        #       Also READ its tests (below) if you need additional
        #       clarification of the specification of this method.
        #  b. Implement and test this method.
        # ---------------------------------------------------------------------

    def get_point(self, blob2):
        """
        What comes in:
          -- self
          -- blob2:  Another Blob
        What goes out:
          Returns a Point whose
            -- x-coordinate is this Blob's size
            -- y-coordinate is the given blob2's size.
        Side effects: None.
        Type hints:
          :type blob2: Blob
          :rtype: Point
        """
        # ---------------------------------------------------------------------
        # TODO: 7.
        #  a. READ specifications of this method (above).
        #       Also READ its tests (below) if you need additional
        #       clarification of the specification of this method.
        #  b. Implement and test this method.
        # ---------------------------------------------------------------------

    def get_distance(self, other_blob):
        """
        What comes in:
          -- self
          -- other_blob:  Another Blob
        What goes out:
          Returns the distance between the following two Points:
            -- the Point obtained by calling  get_point  (above) on this Blob
                 with argument the given other_blob
            -- the Point obtained by calling  get_point  on the given other_blob
                 with argument this Blob

        For credit, you:
           MUST call the  get_point      method in this Blob class!!!
           MUST call the  distance_from  method in the Point class!!!

        Side effects: None.
        Type hints:
          :type other_blob: Blob
          :rtype: float
        """
        # ---------------------------------------------------------------------
        # TODO: 8.
        #  a. READ specifications of this method (above).
        #       Also READ its tests (below) if you need additional
        #       clarification of the specification of this method.
        #  b. Implement and test this method.
        # ---------------------------------------------------------------------

    def swap_colors(self, blob2):
        """
        What comes in:
          -- self
          -- blob2:  Another Blob
        What goes out: Nothing (i.e., None)
        Side effects:
          Swaps this Blob's color with the given blob2's color.
        Type hints:
          :type blob2: Blob
        """
        # ---------------------------------------------------------------------
        # TODO: 9.
        #  a. READ specifications of this method (above).
        #       Also READ its tests (below) if you need additional
        #       clarification of the specification of this method.
        #  b. Implement and test this method.
        # ---------------------------------------------------------------------

    def get_recent_color(self):
        """
        Returns the color of the Blob that this Blob's  make_child  method
        has most recently returned.  If this Blob's  make_child  method
        has not yet been called, returns None.
        """
        # ---------------------------------------------------------------------
        # TODO: 10.
        #  a. READ specifications of this method (above).
        #       Also READ its tests (below) if you need additional
        #       clarification of the specification of this method.
        #  b. Implement and test this method.
        # ---------------------------------------------------------------------

    def get_bigger_size_color(self, more_blobs):
        """
        What comes in:
          -- self
          -- a sequence of Blob objects
        What goes out:
          Returns the color of the first (i.e., lowest-index) Blob in the given
          sequence of Blob objects whose size is greater than this Blob's size.
          Returns "no color" (spelled just like that) if no Blob objects in the
          given sequence of Blob objects have size greater than this Blob's
          size.
        Side effects: None.
        Type hints:
          :type more_blobs: list[Blob]
          :rtype: str
        """
        # ---------------------------------------------------------------------
        # TODO: 11.
        #  a. READ specifications of this method (above).
        #       Also READ its tests (below) if you need additional
        #       clarification of the specification of this method.
        #  b. Implement and test this method.
        # ---------------------------------------------------------------------


###############################################################################
# The TEST functions for the  Blob  class begin here.
###############################################################################
def run_test_init():
    """ Tests the   __init__   method of the Blob class. """

    print()
    print('-----------------------------------------------------------')
    print('Testing the   __init__   method of the Blob class.')
    print('-----------------------------------------------------------')

    # Test 1
    print('\nTest 1:')
    blob_1 = Blob("red", 50)
    run_test_instance_variables(blob_1, "red", 50)

    # Test 2
    print('\nTest 2:')
    blob_2 = Blob("blue", 88)
    run_test_instance_variables(blob_2, "blue", 88)

    # Test 3
    print('\nTest 3:')
    blob_1.color = "green"
    run_test_instance_variables(blob_1, "green", 50)


def run_test_multiply_me():
    """ Tests the   multiply_me   method of the Blob class. """

    print()
    print('-----------------------------------------------------------')
    print('Testing the  multiply_me  method of the Blob class.')
    print('-----------------------------------------------------------')

    # Test 1
    print('\nTest 1:')
    blob_1 = Blob("red", 50)
    blob_1.multiply_me()
    run_test_instance_variables(blob_1, "red", 500)

    # Test 2
    print('\nTest 2:')
    blob_2 = Blob("blue", 88)
    blob_2.multiply_me()
    blob_2.multiply_me()
    run_test_instance_variables(blob_2, "blue", 8800)

    # Test 3
    print('\nTest 3:')
    blob_1.color = "green"
    blob_1.multiply_me()
    run_test_instance_variables(blob_1, "green", 5000)

    # Test 4
    print('\nTest 3:')
    blob_1.color = "black"
    blob_1.size = 7
    blob_1.multiply_me()
    run_test_instance_variables(blob_1, "black", 70)


def run_test_make_child():
    """ Tests the   make_child   method of the Blob class. """

    print()
    print('-----------------------------------------------------------')
    print('Testing the   make_child   method of the Blob class.')
    print('-----------------------------------------------------------')

    # Test 1
    print('\nTest 1:')
    blob_1 = Blob("red", 50)
    blob_2 = Blob("blue", 88)
    blob_3 = blob_1.make_child(blob_2)

    print()
    print("For the RETURNED Blob:")
    run_test_instance_variables(blob_3, "red", 88)

    print()
    print("The Blob acted upon should not have changed:")
    run_test_instance_variables(blob_1, "red", 50)

    print()
    print("The Blob argument should not have changed:")
    run_test_instance_variables(blob_2, "blue", 88)

    # Test 2
    print('\nTest 2:')
    blob_1 = Blob("white", 500)
    blob_2 = Blob("black", 888)
    blob_3 = blob_2.make_child(blob_1)

    print()
    print("For the RETURNED Blob:")
    run_test_instance_variables(blob_3, "black", 500)

    print()
    print("The Blob acted upon should not have changed:")
    run_test_instance_variables(blob_1, "white", 500)

    print()
    print("The Blob argument should not have changed:")
    run_test_instance_variables(blob_2, "black", 888)

    # Test 3
    print('\nTest 3:')
    blob_1.color = "green"
    blob_2.size = 777
    blob_3 = blob_1.make_child(blob_2)

    print()
    print("For the RETURNED Blob:")
    run_test_instance_variables(blob_3, "green", 777)

    print()
    print("The Blob acted upon should not have changed:")
    run_test_instance_variables(blob_1, "green", 500)

    print()
    print("The Blob argument should not have changed:")
    run_test_instance_variables(blob_2, "black", 777)


def run_test_get_point():
    """ Tests the   get_point   method of the Blob class. """

    print()
    print('-----------------------------------------------------------')
    print('Testing the   get_point   method of the Blob class.')
    print('-----------------------------------------------------------')

    # Test 1
    print('\nTest 1:')
    blob_1 = Blob("red", 50)
    blob_2 = Blob("blue", 88)
    p1 = blob_1.get_point(blob_2)

    print()
    print("For the RETURNED Point:")
    print('Expected: ', Point(50, 88))
    print('Actual:   ', p1)
    print_result_of_test(Point(50, 88), p1)

    print()
    print("The Blob acted upon should not have changed:")
    run_test_instance_variables(blob_1, "red", 50)

    print()
    print("The Blob argument should not have changed:")
    run_test_instance_variables(blob_2, "blue", 88)

    # Test 2
    print('\nTest 2:')
    blob_1 = Blob("white", 33)
    blob_2 = Blob("black", 44)
    p1 = blob_1.get_point(blob_2)

    print()
    print("For the RETURNED Point:")
    print('Expected: ', Point(33, 44))
    print('Actual:   ', p1)
    print_result_of_test(Point(33, 44), p1)

    print()
    print("The Blob acted upon should not have changed:")
    run_test_instance_variables(blob_1, "white", 33)

    print()
    print("The Blob argument should not have changed:")
    run_test_instance_variables(blob_2, "black", 44)

    # Test 3
    blob_1.color = "green"
    blob_2.size = 99
    p2 = blob_2.get_point(blob_1)

    print()
    print("For the RETURNED Point:")
    print('Expected: ', Point(99, 33))
    print('Actual:   ', p1)
    print_result_of_test(Point(99, 33), p2)

    print()
    print("The Blob acted upon should not have changed:")
    run_test_instance_variables(blob_1, "green", 33)

    print()
    print("The Blob argument should not have changed:")
    run_test_instance_variables(blob_2, "black", 99)


def run_test_get_distance():
    """ Tests the    get_distance    method of the Blob class. """
    print()
    print('-----------------------------------------------------------')
    print('Testing the   get_distance   method of the Blob class.')
    print('-----------------------------------------------------------')

    # Test 1
    print('\nTest 1:')
    blob_1 = Blob("red", 10)
    blob_2 = Blob("blue", 20)
    p1 = Point(10, 20)
    p2 = Point(20, 10)
    distance = blob_1.get_distance(blob_2)

    print()
    print("For the RETURNED distance:")
    print('Expected: ', p1.distance_from(p2))
    print('Actual:   ', distance)
    print_result_of_test(p1.distance_from(p2), distance)

    print()
    print("The Blob acted upon should not have changed:")
    run_test_instance_variables(blob_1, "red", 10)

    print()
    print("The Blob argument should not have changed:")
    run_test_instance_variables(blob_2, "blue", 20)

    # Test 2
    print('\nTest 2:')
    blob_1 = Blob("cyan", 123)
    blob_2 = Blob("green", 456)
    p1 = Point(123, 456)
    p2 = Point(456, 123)
    distance = blob_1.get_distance(blob_2)

    print()
    print("For the RETURNED distance:")
    print('Expected: ', p1.distance_from(p2))
    print('Actual:   ', distance)
    print_result_of_test(p1.distance_from(p2), distance)

    print()
    print("The Blob acted upon should not have changed:")
    run_test_instance_variables(blob_1, "cyan", 123)

    print()
    print("The Blob argument should not have changed:")
    run_test_instance_variables(blob_2, "green", 456)

    # Test 3
    print('\nTest 3:')
    distance = blob_2.get_distance(blob_1)

    print()
    print("For the RETURNED distance:")
    print('Expected: ', p1.distance_from(p2))
    print('Actual:   ', distance)
    print_result_of_test(p1.distance_from(p2), distance)

    print()
    print("The Blob acted upon should not have changed:")
    run_test_instance_variables(blob_1, "cyan", 123)

    print()
    print("The Blob argument should not have changed:")
    run_test_instance_variables(blob_2, "green", 456)


def run_test_swap_colors():
    """ Tests the   swap_colors   method of the Blob class. """

    print()
    print('-----------------------------------------------------------')
    print('Testing the  swap_colors  method of the Blob class.')
    print('-----------------------------------------------------------')

    # Test 1
    print('\nTest 1:')
    blob_1 = Blob("red", 55)
    blob_2 = Blob("blue", 66)
    blob_1.swap_colors(blob_2)

    print()
    print("Blob 1 should now be:")
    run_test_instance_variables(blob_1, "blue", 55)

    print()
    print("Blob 2 should now be:")
    run_test_instance_variables(blob_2, "red", 66)

    # Test 2
    print('\nTest 2:')
    blob_1.swap_colors(blob_2)

    print()
    print("Blob 1 should now be:")
    run_test_instance_variables(blob_1, "red", 55)

    print()
    print("Blob 2 should now be:")
    run_test_instance_variables(blob_2, "blue", 66)

    # Test 3
    print('\nTest 3:')
    blob_1.color = "green"
    blob_2.swap_colors(blob_1)

    print()
    print("Blob 1 should now be:")
    run_test_instance_variables(blob_1, "blue", 55)

    print()
    print("Blob 2 should now be:")
    run_test_instance_variables(blob_2, "green", 66)

    # Test 4
    print('\nTest 2:')
    blob_2.size = 999
    blob_1.swap_colors(blob_2)

    print()
    print("Blob 1 should now be:")
    run_test_instance_variables(blob_1, "green", 55)

    print()
    print("Blob 2 should now be:")
    run_test_instance_variables(blob_2, "blue", 999)

    # Test 5
    print('\nTest 2:')
    blob_1 = Blob("black", 101)
    blob_1.swap_colors(blob_1)

    print("Blob 1 should now be:")
    run_test_instance_variables(blob_1, "black", 101)


def run_test_get_recent_color():
    """ Tests the get_recent_color method. """
    print()
    print('-----------------------------------------------------------')
    print('Testing the   get_recent_color   method of the Blob class.')
    print('-----------------------------------------------------------')

    # Test 1
    print('\nTest 1:')
    blob_1 = Blob("red", 10)
    blob_2 = Blob("blue", 20)

    print()
    print("Testing blob_1 before doing make_child on it:")
    print('Expected for returned value: ', None)
    print('Actual:                      ', blob_1.get_recent_color())
    print_result_of_test(None, blob_1.get_recent_color())

    blob_unused = blob_1.make_child(blob_2)

    print()
    print("Testing blob_1 after doing make_child on it:")
    print('Expected for returned value: ', "red")
    print('Actual:                      ', blob_1.get_recent_color())
    print_result_of_test("red", blob_1.get_recent_color())

    print()
    print("Testing that blob_2 did not get affected:")
    print('Expected for returned value: ', None)
    print('Actual:                      ', blob_2.get_recent_color())
    print_result_of_test(None, blob_2.get_recent_color())

    # Test 2
    print('\nTest 2:')
    blob_1 = Blob("red", 10)
    blob_2 = Blob("blue", 20)
    blob_unused = blob_1.make_child(blob_2)
    blob_1.color = "green"
    blob_unused = blob_1.make_child(blob_2)
    blob_2.color = "black"
    blob_unused = blob_2.make_child(blob_1)
    blob_1.color = "white"

    print()
    print("Testing blob_2 after a make_child:")
    print('Expected for returned value: ', "black")
    print('Actual:                      ', blob_2.get_recent_color())
    print_result_of_test("black", blob_2.get_recent_color())


def run_test_get_bigger_size_color():
    """ Tests the    get_bigger_size_color    method of the Blob class. """
    print()
    print('---------------------------------------------------------------')
    print('Testing the   get_bigger_size_color   method of the Blob class.')
    print('---------------------------------------------------------------')

    # Test 1
    print('\nTest 1:')
    blob_1 = Blob("red", 100)
    blobs = [Blob("green", 99),
             Blob("white", 20),
             Blob("yellow", 101),
             Blob("black", 30),
             Blob("blue", 40)]

    color = blob_1.get_bigger_size_color(blobs)
    print("For the RETURNED size:")
    print('Expected: ', "yellow")
    print('Actual:   ', color)
    print_result_of_test("yellow", color)

    # Test 2
    print('\nTest 2:')
    blob_1 = Blob("red", 200)
    blobs = [Blob("green", 202),
             Blob("white", 20),
             Blob("yellow", 201),
             Blob("black", 30),
             Blob("blue", 40)]

    color = blob_1.get_bigger_size_color(blobs)
    print("For the RETURNED size:")
    print('Expected: ', "green")
    print('Actual:   ', color)
    print_result_of_test("green", color)

    # Test 3
    print('\nTest 3:')
    blob_1 = Blob("red", 102)
    blobs = [Blob("green", 99),
             Blob("white", 20),
             Blob("yellow", 101),
             Blob("black", 30),
             Blob("blue", 40)]

    color = blob_1.get_bigger_size_color(blobs)
    print("For the RETURNED size:")
    print('Expected: ', "no color")
    print('Actual:   ', color)
    print_result_of_test("no color", color)


###############################################################################
# The following are HELPER functions that display error messages in RED
# and help make it easier for us to write tests.
# Do NOT change any of the following.
###############################################################################
def run_test_instance_variables(blob, expected_color, expected_size):
    """
    Tests whether the instance variables for the given Blob
    are per the given expected values.
      -- Prints relevant messages.
      -- Returns True if all is OK, else returns False.
    """
    try:
        return (run_test_type_of_object(blob) and
                run_test_types_of_instance_variables(blob) and
                run_test_values_of_instance_variables(
                    blob,
                    expected_color,
                    expected_size))
    except Exception:
        something_unexpected_happened_in_our_testing_code()
        return False


def run_test_values_of_instance_variables(blob, expected_color, expected_size):
    # Print the EXPECTED and ACTUAL values of the instance variables
    format_string = '  {:10} {:>9} {:>6}'
    print('  Testing instance variables:')
    print('                 color   size')
    print('                 -----   ----')
    print(format_string.format('Expected:', str(expected_color),
                               str(expected_size)))
    print(format_string.format('Actual:', blob.color, blob.size))

    # Print a message indicating whether or not
    # the EXPECTED values are equal to the ACTUAL values.
    expected = (expected_color, expected_size)
    actual = (blob.color, blob.size)
    return print_result_of_test(expected, actual)


def something_unexpected_happened_in_our_testing_code():
    print_failure_message()
    explanation = (
            '  Something unexpected has happened in the testing \n' +
            '  code that we supplied.  You should probably\n' +
            '  SEEK HELP FROM YOUR INSTRUCTOR NOW.')
    print_failure_message(explanation)


def run_test_type_of_object(blob):
    """ Returns True if the argument is in fact a Blob object """
    if isinstance(blob, Blob):
        return True
    else:
        explanation = ('  The following object to test:\n' +
                       '     ' + str(blob) + '\n' +
                       '  should be a Blob object,\n' +
                       '  but it is not.  Perhaps your code\n' +
                       '  returned something of the wrong type?')
        print_failure_message()
        print_failure_message(explanation)
        return False


def run_test_types_of_instance_variables(blob):
    """
    Returns True if the argument has the right instance variables.
    # and they are all numbers.
    """
    # If NONE of the expected instance variables exist,
    # then perhaps the only "problem" is that the  __init__  method
    # has not yet been implemented.
    attributes = dir(blob)
    if ('color' not in attributes
            and 'size' not in attributes):
        explanation = (
                '  This object:\n' +
                '     ' + str(blob) + '\n' +
                '  should have these instance variables:\n' +
                '     self.color\n' +
                '     self.size\n' +
                '  but it has NONE of them.\n' +
                '  Perhaps you simply have not yet\n' +
                '  implemented the   __init__   method?\n' +
                '  (If so, implement it now.)')
        print_failure_message()
        print_failure_message(explanation)
        return False

    # If SOME (but not all) of the expected instance variables exist,
    # then perhaps something was misspelled in __init__.
    if not ('color' in attributes
            and 'size' in attributes):
        explanation = (
                '  This object:\n' +
                '     ' + str(blob) + '\n' +
                '  should have these instance variables:\n' +
                '     self.color\n' +
                '     self.size\n' +
                '  but it is missing some of them.\n' +
                '  Perhaps you misspelled something\n' +
                '  in your   __init__   code?')
        print_failure_message()
        print_failure_message(explanation)
        return False

    # Check that the instance variables are of the right types:
    #     if not isinstance(cloud.capacity, str):
    #         explanation = (
    #             '  This object:\n' +
    #             '     ' + str(cloud) + '\n' +
    #             '  has an instance variable  capacity  with this value:\n' +
    #             '     capacity: ' + str(cloud.capacity) +
    #             '  That value should be a STRING, but is isn\'t.\n')
    #         print_failure_message()
    #         print_failure_message(explanation)
    #         return False
    #
    #     if not isinstance(cloud.water, list):
    #         explanation = (
    #             '  This object:\n' +
    #             '     ' + str(cloud) + '\n' +
    #             '  has an instance variable  water  with this value:\n' +
    #             '     water: ' + str(cloud.water) +
    #             '  That value should be a LIST, but is isn\'t.\n')
    #         print_failure_message()
    #         print_failure_message(explanation)
    #         return False
    #
    #     if not is_list_of_strings(cloud.water):
    #         explanation = (
    #             '  This object:\n' +
    #             '     ' + str(cloud) + '\n' +
    #             '  has an instance variable  water  with this value:\n' +
    #             '     water: ' + str(cloud.water) +
    #             '  That value should be a list of STRINGS, but is isn\'t.\n')
    #         print_failure_message()
    #         print_failure_message(explanation)
    #         return False

    return True


def is_list_of_strings(strings):
    return ((strings == [])
            or (isinstance(strings[0], str)
                and is_list_of_strings(strings[1:])))


def print_result_of_test(expected, actual):
    if are_equal(expected, actual):
        print("  PASSED the above test -- good!", color="blue")
        return True

    print_failure_message()

    if isinstance(expected, list) or isinstance(expected, tuple):
        explanation = (
                '  For at least one of the above, its Expected value\n' +
                '  does not equal its Actual value.')
        #          Note: the printed\n' +
        #             '  values are the actual values ROUNDED to 1 decimal place.')
        print_failure_message(explanation)

    return False


def are_equal(a, b):
    # We will treat two numbers as being "equal" if they are
    # the same when each is rounded to 12 decimal places.
    if isinstance(a, Number) and isinstance(b, Number):
        return (round(a, 12) == round(b, 12))

    # For lists and tuples, their items have to be equal for the
    # lists/tuples to be equal.
    if isinstance(a, list) and isinstance(b, list):
        if len(a) != len(b):
            return False
        for k in range(len(a)):
            if not are_equal(a[k], b[k]):
                return False
        return True  # All the items were equal.

    if isinstance(a, tuple) and isinstance(b, tuple):
        if len(a) != len(b):
            return False
        for k in range(len(a)):
            if not are_equal(a[k], b[k]):
                return False
        return True  # All the items were equal.

    # For all else, they must be equal in the "usual" way:
    return a == b


def print_failure_message(message='  *** FAILED the above test. ***',
                          flush_time=0.5):
    """ Prints a message onto stderr, hence in RED. """
    time.sleep(flush_time)
    print(message, flush=True, color="red")
    time.sleep(flush_time)


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
    print('ERROR - While running this test,', color='red')
    print('your code raised the following exception:', color='red')
    print()
    time.sleep(1)
    raise
