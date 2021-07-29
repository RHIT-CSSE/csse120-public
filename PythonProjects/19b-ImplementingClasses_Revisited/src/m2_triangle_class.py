"""
More practice implementing classes.
You are GIVEN a Point class and IMPLEMENT a Triangle class.

Authors: David Mutchler, Vibha Alangar, Dave Fisher, Matt Boutell, Mark Hays,
         Mohammed Noureddine, Sana Ebrahimi, Sriram Mohan, their colleagues and
         PUT_YOUR_NAME_HERE.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

import math
import time
from numbers import Number
import testing_helper


###############################################################################
# TODO: 2.  READ the   Point   class defined below.
#  Note especially its methods:
#    clone
#    distance_from
#  For full credit, you must use (call) these as appropriate in your code.
#  After you UNDERSTAND the SPECIFICATIONS of the methods and instance
#  variables (but not necessarily all of the code) of the Point class,
#  change the above _TODO_ to DONE.
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
        """ Returns a Point whose x and y are the same as this Point's."""
        return Point(self.x, self.y)

    def distance_from(self, p2):
        """ Returns the distance this Point is from the given Point. """
        dx_squared = (self.x - p2.x) ** 2
        dy_squared = (self.y - p2.y) ** 2
        return math.sqrt(dx_squared + dy_squared)


###############################################################################
# The  main  function and the TODOs for you are after this:
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
    # run_test_area()
    # run_test_bigger_triangle()
    # run_test_shrink_or_expand()
    # run_test_return_doubled_triangle()
    # run_test_get_largest_area()


###############################################################################
# The   Triangle   class (and its methods) begins here.
###############################################################################
class Triangle:
    """ Represents a triangle in 2-dimensional space. """

    # IMPORTANT: Be CERTAIN you understand the Example in the spec below.
    def __init__(self, a, b, c):
        """
        What comes in:
          -- self and three Point objects
               where the three Point objects are to be the initial points
               of this Triangle.
        What goes out: Nothing (i.e., None).
        Side effects:
           Sets instance variables:
             self.a
             self.b
             self.c
           to CLONES of the three Point objects a, b, and c.

           Also, initializes other instance variables as needed
           by other Triangle methods.

        Example:  This   __init__  method runs when one constructs
        a Triangle.  So the fourth of the following statements
        invokes the   __init__   method of this Line class:
            p1 = Point(30, 17)
            p2 = Point(50, 80)
            p3 = Point(35, 15)
            triangle = Triangle(p1, p2, p3)  # Causes __init__ to run

            print(triangle.a)  # Should print Point(30, 17)
            print(triangle.b)  # Should print Point(50, 80)
            print(triangle.c)  # Should print Point(35, 15)
            print(triangle.a == p1)  # Should print True
            print(triangle.a is p1)  # Should print False

        Type hints:
          :type a: Point
          :type b: Point
          :type c: Point
        """
        # ---------------------------------------------------------------------
        # TODO: 3.
        #   a. READ the above specification, including the Example.
        #        ** ASK QUESTIONS AS NEEDED. **
        #        ** Be sure you understand it, ESPECIALLY the Example.
        #   b. Implement and test this method.
        #        The tests are already written (below).
        #        They include the Example in the above doc-string.
        # ---------------------------------------------------------------------

    # IMPORTANT: Read the HINT in the specification below.
    def area(self):
        """
        What comes in:
          -- self
        What goes out: Returns the area of this Triangle.
        Side effects: None.

        HINT: Recall Heron's formula for the area of a triangle:
        Area =   square root of (S
                                 * (S - length of side 1)
                                 * (S - length of side 2)
                                 * (S - length of side 3))

            where S = (1/2) * (length of perimeter of the triangle)

        For example:  if the triangle has endpoints:
            a = Point(15, 35)
            b = Point(15, 50)
            c = Point(35, 45)
        then one can compute (** using the Point distance_from method **) that:
            the length of the side from a to b is (about): 15
            the length of the side from b to c is (about): 20.6
            the length of the side from c to a is (about): 22.4
        and hence S is (about) (1/2) * (15 + 20.6 + 22.4),
        which is about 28.99
        and so the area of the Triangle is (per the formula):
            150.0
        Type hints:
          :rtype: float
        """
        # ---------------------------------------------------------------------
        # TODO: 4.
        #   a. READ the above specification, including the Example AND HINT!
        #   __
        #      ************* READ THE HINT!!!!!!!!! *************
        #   __
        #        ** ASK QUESTIONS AS NEEDED. **
        #        ** Be sure you understand it, ESPECIALLY the Example.
        #   b. Implement and test this method.
        #        The tests are already written (below).
        #        They include the Example in the above doc-string.
        # ---------------------------------------------------------------------

    # IMPORTANT: CALL the   area   method in your solution to the following.
    def bigger_triangle(self, triangle2):
        """
        What comes in:
          -- self
          -- another Triangle object
        What goes out: returns True if this Triangle has a larger area than
            the given Triangle (triangle2). Returns False otherwise.
        Side effects: None.

        Type hints:
          :type: triangle2: Triangle
          :rtype: bool
        """
        # ---------------------------------------------------------------------
        # TODO: 5.
        #   a. READ the above specification, including the Example.
        #        ** ASK QUESTIONS AS NEEDED. **
        #        ** Be sure you understand it, ESPECIALLY the Example.
        #   b. Implement and test this method.
        #        The tests are already written (below).
        #        They include the Example in the above doc-string.
        # ---------------------------------------------------------------------

    # IMPORTANT:  In the function below, do NOT return a Triangle.  Mutate it.
    def shrink_or_expand(self, f):
        """
         What comes in:
           -- self
           -- a positive number f
         What goes out: Nothing.
         Side effects: MUTATES this Triangle object by multiplying
           the x and y coordinates of each of this Triangle's three points
           by the given number f.

         Type hints:
           :type: f: float
        """
        # ---------------------------------------------------------------------
        # TODO: 6.
        #   a. READ the above specification, including the Example.
        #        ** ASK QUESTIONS AS NEEDED. **
        #        ** Be sure you understand it, ESPECIALLY the Example.
        #   b. Implement and test this method.
        #        The tests are already written (below).
        #        They include the Example in the above doc-string.
        # ---------------------------------------------------------------------

    def return_doubled_triangle(self):
        """
        What comes in:
          -- self
        What goes out:
          -- Return a new Triangle object that is the same as this Triangle
             object, except that the x and y coordinates of its a, b, and c
             endpoints are each TWICE the values of this Triangle's a, b and c.
        Side effects: None.

        Type hints:
          :rtype: Triangle:
        """
        # -------------------------------------------------------------------------
        # TODO: 7.
        #   a. READ the above specification, including the Example.
        #        ** ASK QUESTIONS AS NEEDED. **
        #        ** Be sure you understand it, ESPECIALLY the Example.
        #   b. Implement and test this method.
        #        The tests are already written (below).
        #        They include the Example in the above doc-string.
        # -------------------------------------------------------------------------

    def get_largest_area(self):
        """
        What comes in:
          -- self
        What goes out:
          -- Returns the area of the Triangle when it was the largest
             during any   shrink_or_expand   operations.
             Returns the initial area of the Triangle if there have
             been no shrink_or_expand operations so far.
        Side effects: None.

        Type hints:
          :rtype: float:
        """
        # ---------------------------------------------------------------------
        # TODO: 8.
        #   a. READ the above specification, including the Example.
        #        ** ASK QUESTIONS AS NEEDED. **
        #        ** Be sure you understand it, ESPECIALLY the Example.
        #   b. Implement and test this method.
        #        The tests are already written (below).
        #        They include the Example in the above doc-string.
        # ---------------------------------------------------------------------


###############################################################################
# The TEST functions for the  Triangle  class begin here.
###############################################################################
def run_test_init():
    """ Tests the   __init__   method of the Triangle class. """

    print()
    print('-----------------------------------------------------------')
    print('Testing the   __init__   method of the Triangle class.')
    print('-----------------------------------------------------------')

    # Test 1
    print('\nTest 1:')
    p1 = Point(0, 0)
    p2 = Point(5, 2)
    p3 = Point(3, 6)
    t1 = Triangle(p1, p2, p3)

    expected_a = Point(0, 0)
    expected_b = Point(5, 2)
    expected_c = Point(3, 6)
    run_test_instance_variables(t1, expected_a, expected_b, expected_c)

    if (p1 is t1.a) or (p2 is t1.b) or (p3 is t1.c):
        print_failure_message(
            '\nFAILED CLONING: You failed to CLONE the arguments.\n'
            + 'See your instructor for help.\n')

    # Test 2
    print('\nTest 2:')
    p1 = Point(10, 10)
    p2 = Point(15, 34)
    p3 = Point(45, 100)
    t2 = Triangle(p1, p2, p3)

    expected_a = Point(10, 10)
    expected_b = Point(15, 34)
    expected_c = Point(45, 100)
    run_test_instance_variables(t2, expected_a, expected_b, expected_c)

    if (p1 is t1.a) or (p2 is t1.b) or (p3 is t1.c):
        print_failure_message(
            '\nFAILED CLONING: You failed to CLONE the arguments.\n'
            + 'See your instructor for help.\n')


def run_test_area():
    """ Tests the    area    method of the Triangle class. """

    print()
    print('-----------------------------------------------------------')
    print('Testing the   area   method of the Triangle class.')
    print('-----------------------------------------------------------')

    p1 = Point(15, 35)
    p2 = Point(15, 50)
    p3 = Point(35, 45)
    t1 = Triangle(p1, p2, p3)
    print()
    print('Expected for area:', 150.0)
    print('Actual:           ', t1.area())
    print_result_of_test(150.0, t1.area())

    p4 = Point(25, 40)
    p5 = Point(15, 50)
    p6 = Point(35, 45)
    t2 = Triangle(p4, p5, p6)
    print()
    print('Expected for area:', 75.0)
    print('Actual:           ', t2.area())
    print_result_of_test(75.0, t2.area())

    p7 = Point(15, 20)
    p8 = Point(25, 10)
    p9 = Point(35, 20)
    t3 = Triangle(p7, p8, p9)
    print()
    print('Expected for area:', 100.0)
    print('Actual:           ', t3.area())
    print_result_of_test(100.0, t3.area())


def run_test_bigger_triangle():
    """ Tests the   bigger_triangle   method of the Triangle class. """
    print()
    print('-----------------------------------------------------------')
    print('Testing the   bigger_triangle   method of the Triangle class.')
    print('-----------------------------------------------------------')
    p1 = Point(15, 35)
    p2 = Point(15, 50)
    p3 = Point(35, 45)
    t1 = Triangle(p1, p2, p3)

    p4 = Point(40, 45)
    t2 = Triangle(p1, p2, p4)

    print()
    print('Expected for bigger_triangle:', True)
    print('                      Actual:', t2.bigger_triangle(t1))
    print_result_of_test(True, t2.bigger_triangle(t1))

    print()
    print('Expected for bigger_triangle:', False)
    print('                      Actual:', t1.bigger_triangle(t2))
    print_result_of_test(False, t1.bigger_triangle(t2))

    print()
    print('Expected for bigger_triangle:', False)
    print('                      Actual:', t1.bigger_triangle(t1))
    print_result_of_test(False, t1.bigger_triangle(t1))

    p5 = Point(15, 20)
    p6 = Point(25, 10)
    p7 = Point(35, 20)
    t3 = Triangle(p5, p6, p7)

    p8 = Point(25, 40)
    p9 = Point(15, 50)
    p10 = Point(35, 45)
    t4 = Triangle(p8, p9, p10)
    print()
    print('Expected for bigger_triangle:', False)
    print('                      Actual:', t4.bigger_triangle(t3))
    print_result_of_test(False, t4.bigger_triangle(t3))

    print()
    print('Expected for bigger_triangle:', True)
    print('                      Actual:', t3.bigger_triangle(t4))
    print_result_of_test(True, t3.bigger_triangle(t4))

    print()
    print('Expected for bigger_triangle:', True)
    print('                      Actual:', t1.bigger_triangle(t3))
    print_result_of_test(True, t1.bigger_triangle(t3))

    print()
    print('Expected for bigger_triangle:', True)
    print('                      Actual:', t1.bigger_triangle(t4))
    print_result_of_test(True, t1.bigger_triangle(t4))


def run_test_shrink_or_expand():
    """ Tests the    shrink_or_expand   method of the Triangle class. """
    print()
    print('-----------------------------------------------------------')
    print('Testing the   shrink_or_expand   method of the Triangle class.')
    print('-----------------------------------------------------------')

    # Test 1
    print('\nTest 1:')
    p1 = Point(10, 20)
    p2 = Point(18, 26)
    p3 = Point(30, 10)
    t1 = Triangle(p1, p2, p3)
    t1.shrink_or_expand(0.5)

    expected_a = Point(5, 10)
    expected_b = Point(9, 13)
    expected_c = Point(15, 5)
    run_test_instance_variables(t1, expected_a, expected_b, expected_c)

    p1 = Point(20, 50)
    p2 = Point(10, 30)
    p3 = Point(5, 60)
    t2 = Triangle(p1, p2, p3)
    t2.shrink_or_expand(3)

    expected_a = Point(60, 150)
    expected_b = Point(30, 90)
    expected_c = Point(15, 180)
    run_test_instance_variables(t2, expected_a, expected_b, expected_c)


def run_test_return_doubled_triangle():
    """ Tests the  return_doubled_triangle   method of the Triangle class. """
    print()
    print('-----------------------------------------------------------')
    print('Testing the  return_doubled_triangle  method of the Triangle class')
    print('-----------------------------------------------------------')

    p1 = Point(30, 75)
    p2 = Point(15, 45)
    p3 = Point(30, 90)
    t1 = Triangle(p1, p2, p3)
    t2 = t1.return_doubled_triangle()

    print()
    print("Testing whether the correct Triangle was returned:")
    expected_a = Point(60, 150)
    expected_b = Point(30, 90)
    expected_c = Point(60, 180)
    run_test_instance_variables(t2, expected_a, expected_b, expected_c)

    print()
    print("Testing that the Triangle itself was not mutated:")
    run_test_instance_variables(t1, p1, p2, p3)


def run_test_get_largest_area():
    """ Tests the  get_largest_area   method of the Triangle class. """
    print()
    print('-----------------------------------------------------------')
    print('Testing the   get_largest_area   method of the Triangle class.')
    print('-----------------------------------------------------------')
    p1 = Point(5, 5)
    p2 = Point(12, 8)
    p3 = Point(5, 9)
    t1 = Triangle(p1, p2, p3)
    area1 = t1.area()

    print()
    print('Expected for get_largest_area:', area1)
    print('                       Actual:', t1.get_largest_area())
    print_result_of_test(area1, t1.get_largest_area())

    t1.shrink_or_expand(6)
    area2 = t1.area()

    print()
    print('Expected for get_largest_area:', area2)
    print('                       Actual:', t1.get_largest_area())
    print_result_of_test(area2, t1.get_largest_area())

    t1.shrink_or_expand(0.1)
    area3 = t1.area()

    print()
    print('Expected for get_largest_area:', area2)
    print('                       Actual:', t1.get_largest_area())
    print_result_of_test(area2, t1.get_largest_area())

    p1 = Point(5, 5)
    p2 = Point(12, 8)
    p3 = Point(5, 9)
    t2 = Triangle(p1, p2, p3)
    area4 = t2.area()

    print()
    print('Expected for get_largest_area:', area4)
    print('                       Actual:', t2.get_largest_area())
    print_result_of_test(area4, t2.get_largest_area())

    print()
    print('Expected for get_largest_area:', area2)
    print('                       Actual:', t1.get_largest_area())
    print_result_of_test(area2, t1.get_largest_area())


###############################################################################
# The following are HELPER functions that display error messages in RED
# and help make it easier for us to write tests.
# Do NOT change any of the following.
###############################################################################
def run_test_instance_variables(triangle, expected_a, expected_b, expected_c):
    """
    Tests whether the instance variables for the given Triangle
    are per the given expected values.
      -- Prints relevant messages.
      -- Returns True if all is OK, else returns False.
    """
    try:
        return (run_test_type_of_object(triangle) and
                run_test_types_of_instance_variables(triangle) and
                run_test_values_of_instance_variables(
                    triangle,
                    expected_a,
                    expected_b,
                    expected_c))
    except Exception:
        something_unexpected_happened_in_our_testing_code()
        return False


def run_test_values_of_instance_variables(triangle, expected_a, expected_b,
                                          expected_c):
    # Print the EXPECTED and ACTUAL values of the instance variables
    format_string = '  {:9} {:15} {:15} {:15}'
    print('  Testing instance variables:')
    print('              a                b                  c')
    print('            ------           ------            -------')
    print(format_string.format('Expected:', str(expected_a), str(expected_b),
                               str(expected_c)))
    print(format_string.format('Actual:', str(triangle.a), str(triangle.b),
                               str(triangle.c)))

    # Print a message indicating whether or not
    # the EXPECTED values are equal to the ACTUAL values.
    expected = (expected_a, expected_b, expected_c)
    actual = (triangle.a, triangle.b, triangle.c)
    return print_result_of_test(expected, actual)


def something_unexpected_happened_in_our_testing_code():
    print_failure_message()
    explanation = (
            '  Something unexpected has happened in the testing \n' +
            '  code that we supplied.  You should probably\n' +
            '  SEEK HELP FROM YOUR INSTRUCTOR NOW.')
    print_failure_message(explanation)


def run_test_type_of_object(triangle):
    """ Returns True if the argument is in fact a Triangle object """
    if isinstance(triangle, Triangle):
        return True
    else:
        explanation = ('  The following object to test:\n' +
                       '     ' + str(triangle) + '\n' +
                       '  should be a Triangle object,\n' +
                       '  but it is not.  Perhaps your code\n' +
                       '  returned something of the wrong type?')
        print_failure_message()
        print_failure_message(explanation)
        return False


def run_test_types_of_instance_variables(triangle):
    """
    Returns True if the argument has the right instance variables
    and they are all numbers.
    """
    # If NONE of the expected instance variables exist,
    # then perhaps the only "problem" is that the  __init__  method
    # has not yet been implemented.
    attributes = dir(triangle)
    if ('a' not in attributes
            and 'b' not in attributes
            and 'c' not in attributes):
        explanation = (
                '  This object:\n' +
                '     ' + str(triangle) + '\n' +
                '  should have these instance variables:\n' +
                '     self.a\n' +
                '     self.b\n' +
                '     self.c\n' +
                '  but it has NONE of them.\n' +
                '  Perhaps you simply have not yet\n' +
                '  implemented the   __init__   method?\n' +
                '  (If so, implement it now.)')
        print_failure_message()
        print_failure_message(explanation)
        return False

    # If SOME (but not all) of the expected instance variables exist,
    # then perhaps something was misspelled in __init__.
    if not ('a' in attributes
            and 'b' in attributes
            and 'c' in attributes):
        explanation = (
                '  This object:\n' +
                '     ' + str(triangle) + '\n' +
                '  should have these instance variables:\n' +
                '     self.a\n' +
                '     self.b\n' +
                '     self.c\n' +
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
