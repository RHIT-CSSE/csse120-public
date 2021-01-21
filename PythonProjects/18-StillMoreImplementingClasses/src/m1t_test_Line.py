"""
TESTS the   Line   class in module   m1_Line.

Authors: David Mutchler, Sana Ebrahimi, Mohammed Noureddine, Vibha Alangar,
         Matt Boutell, Dave Fisher, Mark Hays, and their colleagues.
"""

import sys
import time
import inspect
import math
import re
import m1_Line as m1


def main():
    """ Calls the   TEST   functions in this module. """
    run_test_init()
    run_test_clone()
    run_test_reverse()
    run_test_slope()
    run_test_length()
    run_test_get_number_of_clones()
    run_test_line_plus()
    run_test_line_minus()
    run_test_midpoint()
    run_test_is_parallel()
    run_test_reset()

    # These other methods used to exist or were planned at one point.


#     run_test_rotate()
#     run_test_get_number_of_rotations()
#     run_test_projection()
#     run_test_intersection()


def evaluate_test(expected, actual, run_test_title=None, flush_time=0.05):
    """
    Prints the (optional) run_test_title,
    then prints the expected and actual results for the test.
    If the test FAILED, also prints a failure message in red.
    """
    print()
    if run_test_title:
        print(run_test_title)
    print('Expected:', expected)
    print('Actual:  ', actual, flush=True)

    time.sleep(flush_time)

    # If expected is a NUMBER, then actual must also be a number,
    # and their values, rounded to 6 decimal places, must be the same.
    # both in type and in value.  If expected is NOT a number,
    # then actual must match in in both type and value.
    if is_a_number(expected):
        passes_test = (is_a_number(actual) and
                       round(actual, 6) == round(expected, 6))
    else:
        passes_test = (type(actual) is type(expected) and
                       actual == expected)

    if not passes_test:
        print_failure(flush_time=flush_time)


def is_a_number(x):
    """ Returns True if x is an int or a float. """
    return (type(x) is int) or (type(x) is float)


def print_failure(message='  *** FAILED the above test. ***',
                  flush_time=0.05):
    """ Prints a message onto stderr, hence in RED. """
    print(message,
          file=sys.stderr, flush=True)
    time.sleep(flush_time)


def is_implemented(line_method, expected_lines=2):
    """ True if the given Line method is not yet implemented. """
    # There is probably a better way to do this...
    method = getattr(m1.Line, line_method)
    source = inspect.getsource(method)
    doc_string = method.__doc__
    if doc_string:
        expected = source.replace(doc_string, '')
    else:
        line1 = "** Your code in {} is above the method's doc string."
        line2 = "** The doc string should always be at the top of the method."
        line3 = "** Consider moving your code BELOW the doc string within {}."
        print()
        print(line1.format(line_method))
        print(line2)
        print(line3.format(line_method))
        print()
        expected = re.sub(r'""".*"""', '', source,
                          flags=re.DOTALL)  # @UndefinedVariable
        expected = re.sub(r'^\\n', '', expected,
                          flags=re.MULTILINE)  # @UndefinedVariable
    lines_left = expected.splitlines()

    return len(lines_left) > expected_lines


def start_test(method_name):
    print()
    print('-----------------------------------------------------------')
    print('Testing the   {}   method of the  Line  class:'.format(method_name))
    print('-----------------------------------------------------------')
    if not is_implemented(method_name):
        return False

    print('The following are OUR tests (from m1t_run_test_Line):')
    return True


def end_test():
    print('\nHere is the test(s) in YOUR module (from the Example):\n')


###############################################################################
# The TEST functions for the  Line  class begin here.
###############################################################################
def run_test_init():
    """ Tests the   __init__   method of the Line class. """
    if not start_test('__init__'):
        return

    # -------------------------------------------------------------------------
    # Tests using one line:
    # -------------------------------------------------------------------------
    start = m1.Point(12, 88)
    end = m1.Point(40, 33)
    start_clone = start.clone()
    end_clone = end.clone()

    line = m1.Line(start, end)  # Causes __init__ to run

    # Test whether  start  is set correctly.
    expected = start_clone
    actual = line.start
    evaluate_test(expected, actual, 'Testing START:')

    # Test whether  end  is set correctly.
    expected = end_clone
    actual = line.end
    evaluate_test(expected, actual, 'Testing END:')

    # Testing whether __init__ CLONED its arguments:
    message = '\n  *** ERROR: FAILED to CLONE the {} argument. ***'
    if line.start is start:
        print_failure(message.format('START'))
    if line.end is end:
        print_failure(message.format('END'))

    # -------------------------------------------------------------------------
    # Tests using another line:
    # -------------------------------------------------------------------------
    start = m1.Point(-10, 111)
    end = m1.Point(222, -20)
    start_clone = start.clone()
    end_clone = end.clone()

    line = m1.Line(start, end)  # Causes __init__ to run

    # Test whether  start  is set correctly.
    expected = start_clone
    actual = line.start
    evaluate_test(expected, actual, 'Testing START:')

    # Test whether  end  is set correctly.
    expected = end_clone
    actual = line.end
    evaluate_test(expected, actual, 'Testing END:')

    # Testing whether __init__ CLONED its arguments:
    message = '\n  *** ERROR: FAILED to CLONE the {} argument. ***'
    if line.start is start:
        print_failure(message.format('START'))
    if line.end is end:
        print_failure(message.format('END'))

    end_test()


def run_test_clone():
    """ Tests the   clone   method of the Line class. """
    if not start_test('clone'):
        return

    # -------------------------------------------------------------------------
    # Tests using one line:
    # -------------------------------------------------------------------------
    start = m1.Point(12, 88)
    end = m1.Point(40, 33)
    start_clone = start.clone()
    end_clone = end.clone()

    line = m1.Line(start, end)
    clone = line.clone()

    # Test that the clone is a clone (copy), not just a 2nd reference.
    expected = True
    actual = (line == clone)
    evaluate_test(expected, actual, 'Testing that (line == clone):')

    expected = False
    actual = (line is clone)
    title = 'Testing that the line and clone are NOT the same object:'
    evaluate_test(expected, actual, title)

    expected = False
    actual = (line.start is clone.start)
    title = 'Testing that their START points are NOT the same object:'
    evaluate_test(expected, actual, title)

    expected = False
    actual = (line.end is clone.end)
    title = 'Testing that their END points are NOT the same object:'
    evaluate_test(expected, actual, title)

    # Change both line and clone.  Neither should affect the other.
    new_start = m1.Point(100, 200)
    new_end = m1.Point(300, 400)
    line.start = new_start
    clone.end = new_end

    # Test the clone:
    expected = start_clone
    actual = clone.start
    evaluate_test(expected, actual, 'Testing START for the clone:')

    expected = new_end
    actual = clone.end
    evaluate_test(expected, actual, 'Testing END for the clone:')

    # Test the line:
    expected = new_start
    actual = line.start
    evaluate_test(expected, actual, 'Testing START for the line:')

    expected = end_clone
    actual = line.end
    evaluate_test(expected, actual, 'Testing END for the line:')

    # -------------------------------------------------------------------------
    # Tests using another line:
    # -------------------------------------------------------------------------
    start = m1.Point(55, 66)
    end = m1.Point(77, 88)

    line = m1.Line(start, end)
    clone = line.clone()

    # Test that the clone is a clone (copy), not just a 2nd reference.
    expected = True
    actual = (line == clone)
    evaluate_test(expected, actual, 'Testing that (line == clone):')

    expected = False
    actual = (line is clone)
    title = 'Testing that the line and clone are NOT the same object:'
    evaluate_test(expected, actual, title)

    end_test()


def run_test_reverse():
    """ Tests the   reverse   method of the Line class. """
    if not start_test('reverse'):
        return

    # -------------------------------------------------------------------------
    # Tests using one line:
    # -------------------------------------------------------------------------
    line = m1.Line(m1.Point(12, 88),
                   m1.Point(40, 33))

    original_start = line.start
    original_end = line.end
    line_clone = m1.Line(m1.Point(12, 88),
                         m1.Point(40, 33))

    # -------------------------------------------------------------------------
    # Reverse the first time:
    # -------------------------------------------------------------------------
    line.reverse()

    expected = original_end
    actual = line.start
    evaluate_test(expected, actual, 'Testing START after 1st reverse:')
    if (expected == actual) and (expected is not actual):
        print_failure()
        print_failure('      START is a CLONE of the original END')
        print_failure('      instead of the original END itself.')

    expected = original_start
    actual = line.end
    evaluate_test(expected, actual, 'Testing END after 1st reverse:')
    if (expected == actual) and (expected is not actual):
        print_failure()
        print_failure('      END is a CLONE of the original START')
        print_failure('      instead of the original START itself.')

    # -------------------------------------------------------------------------
    # After another reverse, line should be back to the original line.
    # -------------------------------------------------------------------------
    line.reverse()

    expected = line_clone
    actual = line
    evaluate_test(expected, actual, 'Testing after the 2nd reverse:')

    end_test()


def run_test_slope():
    """ Tests the   slope   method of the Line class. """
    if not start_test('slope'):
        return

    line1 = m1.Line(m1.Point(2, 25),
                    m1.Point(7, 10))  # Slope is -3

    line2 = m1.Line(m1.Point(-30, 10),
                    m1.Point(-10, 20))  # Slope is 0.5

    line3 = m1.Line(m1.Point(-100, 20),
                    m1.Point(300, 20))  # Slope is 0

    line4 = m1.Line(m1.Point(30, 40),
                    m1.Point(30, 100))  # Slope is math.inf

    expected = -3.0
    actual = line1.slope()
    evaluate_test(expected, actual, 'Testing a negative slope:')

    expected = 0.5
    actual = line2.slope()
    evaluate_test(expected, actual, 'Testing a fractional slope:')

    expected = 0.0
    actual = line3.slope()
    if actual == -0.0:
        expected = -0.0  # Both positive and negative zero are correct.
    evaluate_test(expected, actual, 'Testing a horizontal line')

    expected = math.inf
    actual = line4.slope()
    evaluate_test(expected, actual, 'Testing a vertical line:')

    end_test()


def run_test_length():
    """ Tests the   length   method of the Line class. """
    if not start_test('length'):
        return

    line1 = m1.Line(m1.Point(25, 2),
                    m1.Point(10, 7))  # Length is 15.8113883

    line2 = m1.Line(m1.Point(-30, 10),
                    m1.Point(-10, 20))  # Length is 22.3606798

    line3 = m1.Line(m1.Point(-100, 20),
                    m1.Point(300, 20))  # Horizontal line, length is 400

    line4 = m1.Line(m1.Point(30, 40),
                    m1.Point(30, 100))  # Vertical line, length is 60

    line5 = m1.Line(m1.Point(100, 200),
                    m1.Point(100, 200))  # Length is 0

    # These tests round all numbers to 6 decimal places before
    # doing the test for equality.  This is necessary since here we
    # are dealing with floating point numbers that may be computed
    # slightly differently (but with both ways correct).

    # ACTUALLY, I think that __eq__ in the Point class now takes
    # care of the floating-point roundoff.

    expected = round(15.8113883, 6)
    actual = round(line1.length(), 6)
    evaluate_test(expected, actual, 'Testing a negative-slope line:')

    expected = round(22.3606798, 6)
    actual = round(line2.length(), 6)
    evaluate_test(expected, actual, 'Testing a fractional-slope line:')

    expected = round(400.0, 6)
    actual = round(line3.length(), 6)
    evaluate_test(expected, actual, 'Testing a horizontal line')

    expected = round(60.0, 6)
    actual = round(line4.length(), 6)
    evaluate_test(expected, actual, 'Testing a vertical line:')

    expected = round(0.0, 6)
    actual = round(line5.length(), 6)
    evaluate_test(expected, actual, 'Testing a length-zero line:')

    end_test()


def run_test_get_number_of_clones():
    """ Tests the   get_number_of_clones   method of the Line class. """
    if not start_test('get_number_of_clones'):
        return

    line1 = m1.Line(m1.Point(500, 20), m1.Point(100, 8))
    line1.reverse()
    line2 = line1.clone()
    line1.reverse()
    line2.reverse()
    line2.x = m1.Point(0, 0)
    line3 = line1.clone()
    line4 = line3.clone()
    line5 = line1.clone()

    expected = 3
    actual = line1.get_number_of_clones()
    evaluate_test(expected, actual, 'Testing line1, cloned 3 times:')

    expected = 0
    actual = line2.get_number_of_clones()
    evaluate_test(expected, actual, 'Testing line2, never cloned:')

    expected = 1
    actual = line3.get_number_of_clones()
    evaluate_test(expected, actual, 'Testing line3, cloned once:')

    expected = 0
    actual = line4.get_number_of_clones()
    evaluate_test(expected, actual, 'Testing line4, never cloned:')

    expected = 0
    actual = line5.get_number_of_clones()
    evaluate_test(expected, actual, 'Testing line5, not yet cloned:')

    line3 = line5.clone()

    expected = 0
    actual = line3.get_number_of_clones()
    evaluate_test(expected, actual, 'Testing line3, now a new Line')

    expected = 1
    actual = line5.get_number_of_clones()
    evaluate_test(expected, actual, 'Testing line5, cloned once:')

    line5 = line1
    expected = 3
    actual = line5.get_number_of_clones()
    evaluate_test(expected, actual, 'Testing line5, now same as line1:')

    end_test()


def run_test_line_plus():
    """ Tests the   line_plus   method of the Line class. """
    if not start_test('line_plus'):
        return

    line1 = m1.Line(m1.Point(500, 20), m1.Point(100, 8))
    line2 = m1.Line(m1.Point(100, 13), m1.Point(400, 8))

    expected = m1.Line(m1.Point(600, 33), m1.Point(500, 16))
    actual = line1.line_plus(line2)
    evaluate_test(expected, actual, 'Testing line1 + line2:')

    expected = m1.Line(m1.Point(600, 33), m1.Point(500, 16))
    actual = line2.line_plus(line1)
    evaluate_test(expected, actual, 'Testing line2 + line1:')

    expected = m1.Line(m1.Point(1100, 53), m1.Point(600, 24))
    actual = line2.line_plus(line1).line_plus(line1)
    evaluate_test(expected, actual, 'Testing line2 + line1 + line1:')

    expected = m1.Line(m1.Point(200, 26), m1.Point(800, 16))
    actual = line2.line_plus(line2)
    evaluate_test(expected, actual, 'Testing line2 + line2:')

    end_test()


def run_test_line_minus():
    """ Tests the   line_minus   method of the Line class. """
    if not start_test('line_minus'):
        return

    line1 = m1.Line(m1.Point(500, 20), m1.Point(100, 8))
    line2 = m1.Line(m1.Point(100, 13), m1.Point(400, 8))

    expected = m1.Line(m1.Point(400, 7), m1.Point(-300, 0))
    actual = line1.line_minus(line2)
    evaluate_test(expected, actual, 'Testing line1 - line2:')

    expected = m1.Line(m1.Point(-400, -7), m1.Point(300, 0))
    actual = line2.line_minus(line1)
    evaluate_test(expected, actual, 'Testing line2 - line1:')

    expected = m1.Line(m1.Point(-900, -27), m1.Point(200, -8))
    actual = line2.line_minus(line1).line_minus(line1)
    evaluate_test(expected, actual, 'Testing line2 - line1 - line1:')

    expected = m1.Line(m1.Point(0, 0), m1.Point(0, 0))
    actual = line2.line_minus(line2)
    evaluate_test(expected, actual, 'Testing line2 - line2:')

    end_test()


def run_test_midpoint():
    """ Tests the   midpoint   method of the Line class. """
    if not start_test('midpoint'):
        return

    line = m1.Line(m1.Point(-10, 50),
                   m1.Point(30, 20))  # midpoint is (10, 35)

    expected = m1.Point(10.0, 35.0)
    actual = line.midpoint()
    evaluate_test(expected, actual, 'Testing the original line:')

    expected = m1.Point(10.0, 35.0)
    actual = line.midpoint()
    evaluate_test(expected, actual, 'Testing the original line again:')

    line.start = m1.Point(30.0, 10.0)
    expected = m1.Point(30.0, 15.0)
    actual = line.midpoint()
    evaluate_test(expected, actual, 'Testing a vertical line:')

    line.end = m1.Point(-30.0, 10.0)
    expected = m1.Point(0.0, 10.0)
    actual = line.midpoint()
    evaluate_test(expected, actual, 'Testing a horizontal line:')

    line.start = line.end
    expected = line.start.clone()
    actual = line.midpoint()
    evaluate_test(expected, actual, 'Testing a zero-length line:')

    end_test()


def run_test_is_parallel():
    """ Tests the   is_parallel   method of the Line class. """
    if not start_test('is_parallel'):
        return

    # -------------------------------------------------------------------------
    # Tests using one pair of lines.  Each has slope -5.
    # -------------------------------------------------------------------------
    line1 = m1.Line(m1.Point(24, 10),
                    m1.Point(20, 30))
    line2 = m1.Line(m1.Point(60, -110),
                    m1.Point(68, -150))  # These both have slope -5

    expected = True
    actual = line1.is_parallel(line2)
    evaluate_test(expected, actual, 'Testing parallel lines:')

    expected = True
    actual = line2.is_parallel(line1)
    evaluate_test(expected, actual, 'Testing those lines again:')

    line1.reverse()
    expected = True
    actual = line1.is_parallel(line2)
    evaluate_test(expected, actual, 'Testing after reversing one line:')

    expected = True
    actual = line2.is_parallel(line1)
    evaluate_test(expected, actual, 'Testing that again:')

    # -------------------------------------------------------------------------
    # Modifying one of the lines, so that they are no longer parallel:
    # -------------------------------------------------------------------------
    line1.start.x = line1.start.x + 0.000001
    expected = False
    actual = line1.is_parallel(line2)
    evaluate_test(expected, actual, 'Testing lines no longer parallel:')

    expected = False
    actual = line2.is_parallel(line1)
    evaluate_test(expected, actual, 'Testing that again:')

    # -------------------------------------------------------------------------
    # Testing horizontal lines:
    # -------------------------------------------------------------------------
    line1 = m1.Line(m1.Point(88, 50),
                    m1.Point(99, 50))
    line2 = m1.Line(m1.Point(-100, 300),
                    m1.Point(-200, 300))  # These are both horizontal

    expected = True
    actual = line1.is_parallel(line2)
    evaluate_test(expected, actual, 'Testing parallel lines:')

    expected = True
    actual = line2.is_parallel(line1)
    evaluate_test(expected, actual, 'Testing those lines again:')

    line1.reverse()
    expected = True
    actual = line1.is_parallel(line2)
    evaluate_test(expected, actual, 'Testing after reversing one line:')

    expected = True
    actual = line2.is_parallel(line1)
    evaluate_test(expected, actual, 'Testing that again:')

    # Modifying one of the lines, so that they are no longer parallel:
    line2.end.y = line2.end.y + 0.000001
    expected = False
    actual = line1.is_parallel(line2)
    evaluate_test(expected, actual,
                  'Testing lines that are ALMOST parallel:')

    expected = False
    actual = line2.is_parallel(line1)
    evaluate_test(expected, actual, 'Testing that again:')

    # -------------------------------------------------------------------------
    # Testing vertical lines:
    # -------------------------------------------------------------------------
    line1 = m1.Line(m1.Point(77, 66),
                    m1.Point(77, -600))
    line2 = m1.Line(m1.Point(-110, 33),
                    m1.Point(-110, 300))  # These are both vertical

    expected = True
    actual = line1.is_parallel(line2)
    evaluate_test(expected, actual, 'Testing parallel lines:')

    expected = True
    actual = line2.is_parallel(line1)
    evaluate_test(expected, actual, 'Testing those lines again:')

    line1.reverse()
    expected = True
    actual = line1.is_parallel(line2)
    evaluate_test(expected, actual, 'Testing after reversing one line:')

    expected = True
    actual = line2.is_parallel(line1)
    evaluate_test(expected, actual, 'Testing that again:')

    # Modifying one of the lines, so that they are no longer parallel:
    line1.end.x = line1.end.x + 0.000001
    expected = False
    actual = line1.is_parallel(line2)
    evaluate_test(expected, actual,
                  'Testing lines that are ALMOST parallel:')

    expected = False
    actual = line2.is_parallel(line1)
    evaluate_test(expected, actual, 'Testing that again:')

    # -------------------------------------------------------------------------
    # Testing a situation where floating point arithmetic may say
    # that two slopes that are equal (in REAL arithmetic) are NOT equal.
    #
    # The code must ROUND in comparing the two slopes.
    # -------------------------------------------------------------------------
    line1 = m1.Line(m1.Point(24 * math.pi, 10),
                    m1.Point(20 * math.pi, 30))
    line2 = m1.Line(m1.Point(60 * math.pi, -110),
                    m1.Point(68 * math.pi, -150))

    expected = True
    actual = line1.is_parallel(line2)
    message = ('Testing two in-fact PARALLEL lines with slightly'
               + ' different computed slopes from round-off):')
    evaluate_test(expected, actual, message)

    end_test()


# def run_test_rotate():
#     """ Tests the   rotate   method of the Line class. """
#     print()
#     print('-----------------------------------------------------------')
#     print('Testing the   rotate   method of the   Line   class:')
#     print('-----------------------------------------------------------')
#     if not is_implemented('rotate'):
#         return
#
#     print('The following are OUR tests (from m1t_run_test_Line):')
#
#     # ------------------------------------------------------------------
#     # Tests using a vertical Line whose center is (60, 300)
#     # and whose length is 400.
#     # ------------------------------------------------------------------
#     p1 = m1.Point(60, 100)
#     p2 = m1.Point(60, 500)
#     center = m1.Point(60, 300)
#     length = 400
#     line1 = m1.Line(p1.clone(), p2.clone())
#
#     line1.rotate(90)  # The line is now horizontal
#     expected = m1.Line(m1.Point(p1.x + (length / 2), center.y),
#                        m1.Point(p2.x - (length / 2), center.y))
#     actual = line1
#     evaluate_test(expected, actual,
#                   'Testing a vertical line after 90 rotation:')
#
#     line1.rotate(-180)
#     expected = m1.Line(m1.Point(p2.x - (length / 2), center.y),
#                        m1.Point(p1.x + (length / 2), center.y))
#     actual = line1
#     evaluate_test(expected, actual,
#                   'Testing after an additional -180 rotation:')
#
#     line1.rotate(90)
#     expected = m1.Line(p1, p2)
#     actual = line1
#     evaluate_test(expected, actual,
#                   'Then testing after an additional 90 rotation:')
#
#     # ------------------------------------------------------------------
#     # Tests using a horizontal Line whose center is (50, -100)
#     # and whose length is 40.
#     # ------------------------------------------------------------------
#     p1 = m1.Point(30, -100)
#     p2 = m1.Point(70, -100)
#     center = m1.Point(50, -100)
#     length = 40
#     line2 = m1.Line(p1.clone(), p2.clone())
#
#     line2.rotate(30)  # The line is now at 30 degree angle
#     delta_x = math.cos(math.pi / 6) * (length / 2)
#     delta_y = math.sin(math.pi / 6) * (length / 2)
#     if p1.x > p2.x:
#         direction = 1
#     else:
#         direction = -1
#     expected = m1.Line(m1.Point(center.x + (direction * delta_x),
#                                 center.y + (direction * delta_y)),
#                        m1.Point(center.x - (direction * delta_x),
#                                 center.y - (direction * delta_y)))
#     actual = line2
#     evaluate_test(expected, actual,
#                   'Testing a horizontal line after 30 rotation:')
#
#     # Same as previous test, but with start and end reversed:
#     line2 = m1.Line(p2.clone(), p1.clone())
#
#     line2.rotate(30)  # The line is now at 30 degree angle
#     delta_x = math.cos(math.pi / 6) * (length / 2)
#     delta_y = math.sin(math.pi / 6) * (length / 2)
#     if p1.x > p2.x:
#         direction = 1
#     else:
#         direction = -1
#     expected = m1.Line(m1.Point(center.x - (direction * delta_x),
#                                 center.y - (direction * delta_y)),
#                        m1.Point(center.x + (direction * delta_x),
#                                 center.y + (direction * delta_y)))
#     actual = line2
#     evaluate_test(expected, actual,
#                   'Testing same line, reversed, after 30 rotation:')
#
#     print('\nHere is YOUR test (that YOU wrote in m1_Line):')
#     print()
#
#
# def run_test_rotations():
#     """ Tests the   rotations   method of the Line class. """
#     print()
#     print('-----------------------------------------------------------')
#     print('Testing the   rotations   method of the   Line   class:')
#     print('-----------------------------------------------------------')
#     if not is_implemented('rotations'):
#         return
#
#     print('The following are OUR tests (from m1t_run_test_Line):')
#
#     line1 = m1.Line(m1.Point(88, 99), m1.Point(77, 66))
#     line2 = m1.Line(m1.Point(0, 0), m1.Point(10, 30))
#
#     # Various actions with 5 calls to ROTATE of line1 among them
#     # and 2 calls to ROTATE of line2 among them.
#     line1.clone()
#     line1.rotate(55)
#     line1.reverse()
#     line1.slope()
#     line2.rotate(44)
#     line1.length()
#     line1.rotate(33)
#     line1.is_parallel(line2)
#     line2.rotate(22)
#     line1.rotate(11)
#     line1.rotate(-33)
#     line1.reverse()
#     line1.rotate(-0.0003)
#     line1.clone()
#
#     expected = 5
#     actual = line1.rotations()
#     evaluate_test(expected, actual,
#                   'Testing various actions with 5 line1 rotations:')
#
#     expected = 2
#     actual = line2.rotations()
#     evaluate_test(expected, actual,
#                   'Testing various actions with 2 line2 rotations:')
#
#     # Testing repeated calls to ROTATE.
#     line3 = m1.Line(m1.Point(0, 0), m1.Point(0, 0))
#     result = 'PASSED'
#     for k in range(100):
#         line3.rotate(33)
#         line3.rotations()  # Should not change anything
#         r = line3.rotations()
#         if r != k + 1:
#             result = 'FAILED'
#             break
#
#     expected = 'PASSED'
#     actual = result
#     evaluate_test(expected, actual, 'Testing up to 100 more rotations:')
#
#     print('\nHere is YOUR test (that YOU wrote in m1_Line):')
#     print()


# def run_test_intersection():
#     """ Tests the   intersection   method of the Line class. """
#     print()
#     print('-----------------------------------------------------------')
#     print('Testing the   intersection   method of the   Line   class:')
#     print('-----------------------------------------------------------')
#     if not is_implemented('intersection'):
#         return
#
#     print('The following are OUR tests (from m1t_run_test_Line):')
#
#     line1 = m1.Line(m1.Point(10, 4),
#                     m1.Point(24, 4))
#     line2 = m1.Line(m1.Point(18, 20),
#                     m1.Point(18, -5))
#     line3 = m1.Line(m1.Point(19, 6),
#                     m1.Point(14, 1))
#     line4 = m1.Line(m1.Point(21, 5),
#                     m1.Point(11, 0))
#
#     expected = m1.Point(18.0, 4.0)
#     actual = line1.intersection(line2)
#     evaluate_test(expected, actual,
#                   'Testing horizontal line crossed by vertical line')
#
#     expected = m1.Point(18.0, 4.0)
#     actual = line2.intersection(line1)
#     evaluate_test(expected, actual,
#                   'Testing the same, in the other order')
#
#     expected = m1.Point(17.0, 4.0)
#     actual = line1.intersection(line3)
#     evaluate_test(expected, actual,
#                   'Testing horizontal line crossed by slanted line')
#
#     expected = m1.Point(18.0, 4.0)
#     actual = line2.intersection(line1)
#     evaluate_test(expected, actual,
#                   'Testing the same, in the other order')
#
#     expected = m1.Point(15.0, 2.0)
#     actual = line3.intersection(line4)
#     evaluate_test(expected, actual,
#                   'Testing slanted line crossed by slanted line')
#
#     line5 = m1.Line(m1.Point(10, 4),
#                     m1.Point(18, 4))
#
#     expected = m1.Point(18.0, 4.0)
#     actual = line5.intersection(line2)
#     evaluate_test(expected, actual,
#                   'Testing two lines that barely cross')
#
#     line6 = m1.Line(m1.Point(10, 4),
#                     m1.Point(17.99, 4))
#
#     expected = None
#     actual = line6.intersection(line2)
#     evaluate_test(expected, actual,
#                   'Testing two lines that just miss crossing')
#
#     line7 = m1.Line(m1.Point(24 * math.pi, 10),
#                     m1.Point(20 * math.pi, 30))
#     line8 = m1.Line(m1.Point(60 * math.pi, -110),
#                     m1.Point(68 * math.pi, -150))
#
#     expected = None
#     actual = line7.intersection(line8)
#     evaluate_test(expected, actual, 'Testing two parallel lines')
#
#     end_test()


def run_test_reset():
    """ Tests the   reset   method of the Line class. """
    if not start_test('reset'):
        return

    p1 = m1.Point(55, 66)
    p2 = m1.Point(77, 88)
    p3 = m1.Point(0, 0)
    p4 = m1.Point(-100, -2)
    line1 = m1.Line(p1.clone(), p2.clone())
    line2 = m1.Line(p3.clone(), p4.clone())
    line3 = m1.Line(p1.clone(), p3.clone())

    line1.start = m1.Point(100, 300)
    line2.end = m1.Point(99, 4)
    line1.reverse()
    line1.reverse()
    line2.reverse()
    line3.reverse()

    # -------------------------------------------------------------------------
    # Testing line1 BEFORE the reset, then AFTER the reset.
    # -------------------------------------------------------------------------
    expected = False
    actual = (line1 == m1.Line(p1, p2))
    evaluate_test(expected, actual, 'Testing line1 BEFORE the reset:')

    line1.reset()

    expected = m1.Line(p1, p2)
    actual = line1
    evaluate_test(expected, actual, 'Testing line1 AFTER the reset:')

    # -------------------------------------------------------------------------
    # Testing line2 BEFORE the reset, then AFTER the reset.
    # -------------------------------------------------------------------------
    expected = False
    actual = (line2 == m1.Line(p3, p4))
    evaluate_test(expected, actual, 'Testing line2 BEFORE the reset:')

    line2.reset()

    expected = m1.Line(p3, p4)
    actual = line2
    evaluate_test(expected, actual, 'Testing line2 AFTER the reset:')

    # -------------------------------------------------------------------------
    # Testing line3 BEFORE the reset, then AFTER the reset.
    # -------------------------------------------------------------------------
    expected = False
    actual = (line3 == m1.Line(p1, p3))
    evaluate_test(expected, actual, 'Testing line3 BEFORE the reset:')

    line3.reset()

    expected = m1.Line(p1, p3)
    actual = line3
    evaluate_test(expected, actual, 'Testing line3 AFTER the reset:')

    # -------------------------------------------------------------------------
    # Testing MANY resets, then ONLY resets.
    # -------------------------------------------------------------------------
    for _ in range(99):
        line1.reverse()
        line1.reset()

    expected = m1.Line(p1, p2)
    actual = line1
    evaluate_test(expected, actual, 'Testing line1 after MANY resets')

    line3 = m1.Line(p1.clone(), p4.clone())
    for _ in range(1001):
        line3.reset()

    expected = m1.Line(p1, p4)
    actual = line3
    evaluate_test(expected, actual, 'Testing line3 after ONLY resets')

    # -------------------------------------------------------------------------
    # Testing whether the code CLONED when it stored the original Points
    # for retrieval by reset.
    # -------------------------------------------------------------------------
    line4 = m1.Line(m1.Point(66, 77),
                    m1.Point(88, 99))
    line4.start.x = 100
    line4.reset()

    expected = m1.Line(m1.Point(66, 77),
                       m1.Point(88, 99))
    actual = line4
    title = 'Testing whether the code CLONED when it stored the Points'
    evaluate_test(expected, actual, title)

    end_test()


# def run_test_projection():
#     """ Tests the   projection   method of the Line class. """
#     print()
#     print('-----------------------------------------------------------')
#     print('Testing the   projection   method of the   Line   class:')
#     print('-----------------------------------------------------------')
#     if not is_implemented('projection'):
#         return
#
#     print('The following are OUR tests (from m1t_run_test_Line):')
#
#     print('\nHere is YOUR test (that YOU wrote in m1_Line):')
#     print()

# -----------------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# -----------------------------------------------------------------------------
if __name__ == '__main__':
    main()
