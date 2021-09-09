"""
This module lets you practice DEBUGGING when RUN-TIME EXCEPTIONS occur,
focusing here on AttributeError exceptions:
  'BLAHType' object has no attribute 'FOO'
  
and on TypeError exceptions, in particular those of the form:
  'BLAHType' object is not callable.

Authors: David Mutchler, Yiji Zhang, Mark Hays, Derek Whitley, Vibha Alangar,
         Matt Boutell, Dave Fisher, Sriram Mohan, Mohammed Noureddine,
         Amanda Stouder, Curt Clifton, Valerie Galluzzi, their colleagues and
         PUT_YOUR_NAME_HERE.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


###############################################################################
#
# TODO: 2. READ these instructions, ASKING QUESTIONS as needed.
#
#   This module contains "broken" functions, as in m1.py.
#   FOLLOW THE SAME STEPS as in the instructions of m1.py
#   to find and correct the mistakes in these functions.
#
#   The broken functions herein have the SAME SPECIFICATIONS
#   as those in the  m1  module.  Therefore, you can use the
#   SAME PICTURES (in the file m1_pictures.pdf) as you used
#   for determining whether your corrected code passes the tests.
#
#   *** IMPORTANT: ***
#       Do NOT look back to m1.py to solve THESE problems.
#       That would greatly diminish what you learn from THESE problems.
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
    run_test_all()


###############################################################################
# Students: Do NOT change the following tests.
#           There are NO errors in the TESTS.
###############################################################################
def run_test_all():
    """ Tests ALL the functions in this module. """
    # Test broken_1:
    window = rg.RoseWindow(title='Testing BROKEN_1')
    circle1 = rg.Circle(rg.Point(50, 50), 15)
    circle1.fill_color = 'blue'
    broken_1(circle1, window)  # Test 1 of broken_1

    circle2 = rg.Circle(rg.Point(70, 150), 30)
    circle2.fill_color = 'red'
    broken_1(circle2, window)  # Test 2 of broken_1
    window.close_on_mouse_click()

    # Test broken_2:
    window = rg.RoseWindow(title='Testing BROKEN_2')
    broken_2(50, 75, window)  # Test 1 of broken_2
    broken_2(100, 150, window)  # Test 2 of broken_2
    window.close_on_mouse_click()

    # Test broken_3:
    window = rg.RoseWindow(title='Testing BROKEN_3')
    broken_3(5, rg.Point(100, 50), 80, 20, window)  # Test 1 of broken_3
    broken_3(3, rg.Point(50, 150), 40, 50, window)  # Test 2 of broken_3
    window.close_on_mouse_click()

    # Test broken_4:
    window = rg.RoseWindow(title='Testing BROKEN_4')
    broken_4(50, 75, 40, window)  # Test 1 of broken_4
    broken_4(100, 150, 75, window)  # Test 2 of broken_4
    window.close_on_mouse_click()

    # Test broken_5:
    window = rg.RoseWindow(title='Testing BROKEN_5')
    circle = rg.Circle(rg.Point(100, 50), 30)
    circle.fill_color = 'pink'
    broken_5(circle, window)  # Test 1 of broken_5

    circle = rg.Circle(rg.Point(250, 100), 80)
    circle.fill_color = 'red'
    broken_5(circle, window)  # Test 2 of broken_5
    window.close_on_mouse_click()

    # Test broken_6:
    expected = 1.8333333
    actual = broken_6(3)  # Test 1 of broken_6
    print("Testing BROKEN_6:\n")
    print('Expected for BROKEN_6, Test 1:', expected, '(approximately)')
    print('  Actual for BROKEN_6, Test 1:', actual)

    expected = 5.1873775
    actual = broken_6(100)  # Test 2 of broken_6
    print()
    print('Expected for BROKEN_6, Test 2:', expected, '(approximately)')
    print('  Actual for BROKEN_6, Test 2:', actual)
    print()


# -----------------------------------------------------------------------------
# TODO: 3. Follow the INSTRUCTIONS AT THE TOP OF THIS MODULE
#          to correct the mistake(s) in the following function.
# -----------------------------------------------------------------------------
def broken_1(circle, window):
    """
    What comes in: an rg.Circle and an rg.RoseWindow.
    What goes out:  Nothing (i.e., None).
    Side effects:
      Draws the given rg.Circle on the given rg.RoseWindow,
        then draws another rg.Circle whose RADIUS
        is TWICE that of the given rg.Circle
        and whose center is the same as that of the given rg.Circle.
        
      Must  ** render **     but   ** NOT close **   the window.

    Type hints:
      :type circle: rg.Circle
      :type window: rg.RoseWindow
    """
    circle.attach(window)
    circle2 = rg.Circle(circle.center(), 2 * circle.r)
    circle2.attach(circle)
    circle2.render()


# -----------------------------------------------------------------------------
# TODO: 4. Follow the INSTRUCTIONS AT THE TOP OF THIS MODULE
#          to correct the mistake(s) in the following function.
# -----------------------------------------------------------------------------
def broken_2(x, y, window):
    """
    What comes in: Positive integers x and y, and an rg.RoseWindow.
    What goes out:  Nothing (i.e., None).
    Side effects:
      Draws a rg.Circle with radius 33, centered at (x, y),
        on the given rg.RoseWindow.
      
      Must  ** render **     but   ** NOT close **   the window.
          
    Type hints:
      :type x:      int
      :type y:      int
      :type window: rg.RoseWindow
      """
    circle = rg.Circle(x, y)
    circle.attach_to(window)
    window.render()


# -----------------------------------------------------------------------------
# TODO: 5. Follow the INSTRUCTIONS AT THE TOP OF THIS MODULE
#          to correct the mistake(s) in the following function.
# -----------------------------------------------------------------------------
def broken_3(n, point, length, distance_between_lines, window):
    """
    What comes in: The four arguments are:
      -- A positive integer n.
      -- An rg.Point.
      -- A positive integer length.
      -- An rg.RoseWindow.
    What goes out:  Nothing (i.e., None).
    Side effects:
      Draws  n  vertical rg.Lines on the given rg.RoseWindow,
        where the leftmost rg.Line has the given point as its topmost
        point and all the rg.Lines have the given length
        and they are the given distance apart.
        Each line is drawn with a 0.5 second pause after drawing it.

      Must  ** render **     but   ** NOT close **   the window.

    Type hints:
      :type n:                      int
      :type point:                  rg.Point
      :type length:                 int
      :type distance_between_lines: int
      :type window:                 rg.RoseWindow
    """
    a = rg.Point(point.x, point.y)
    b = rg.Point(point.x, point.y + length)

    for _ in range(n):
        rg.Line(a, b)
        rg.Line.attach_to(window)
        window.render(0.5)
        a = rg.Point(a.x + distance_between_lines, a.y)
        b = rg.Point(b.x + distance_between_lines, b.y)


# -----------------------------------------------------------------------------
# TODO: 6. Follow the INSTRUCTIONS AT THE TOP OF THIS MODULE
#          to correct the mistake(s) in the following function.
# -----------------------------------------------------------------------------
def broken_4(x, y, radius, window):
    """
    What comes in: Positive integers x and y, and an rg.RoseWindow.
    What goes out:  Nothing (i.e., None).
    Side effects:
      Draws a green-filled rg.Circle with the given radius,
        centered at (x, y), on the given rg.RoseWindow
      
      Must  ** render **     but   ** NOT close **   the window.
          
    Type hints:
      :type x:      int
      :type y:      int
      :type radius: int
      :type window: rg.RoseWindow
      """
    line = rg.Line(rg.Point(x, y), radius)
    line.fill_color = 'green'
    line.attach_to(window)
    window.render()


# -----------------------------------------------------------------------------
# TODO: 7. Follow the INSTRUCTIONS AT THE TOP OF THIS MODULE
#          to correct the mistake(s) in the following function.
# -----------------------------------------------------------------------------
def broken_5(circle, window):
    """
    What comes in: an rg.Circle and an rg.RoseWindow.
    What goes out:  Nothing (i.e., None).
    Side effects:
      Draws the given rg.Circle and an rg.Square that circumscribes it,
         both on the given rg.RoseWindow,
         with the rg.Square having the same OUTLINE color
         as the FILL color of the given rg.Circle.
      
      Must  ** render **     but   ** NOT close **   the window.

    Type hints:
      :type circle: rg.Circle
      :type window: rg.RoseWindow
    """
    circle.attach_to(window)
    square = rg.Square(circle.center, 2 * circle.radius)
    square.outlinecolor = circle.fillcolor
    square.attach_to(window)
    window.render()


# -----------------------------------------------------------------------------
# TODO: 8. Follow the INSTRUCTIONS AT THE TOP OF THIS MODULE
#          to correct the mistake(s) in the following function.
# -----------------------------------------------------------------------------
def broken_6(n):
    """
    What comes in:  A positive integer n.
    What goes out:  Returns the sum:
      1 + 1/2 + 1/3 + ... + 1/n.
    Side effects:   None.
    """
    total = 0
    for k in range(n):
        total.x = total.x + (1 / (k + 1))

    return total


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
