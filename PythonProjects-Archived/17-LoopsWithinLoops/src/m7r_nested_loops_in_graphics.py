"""
This project demonstrates NESTED LOOPS (i.e., loops within loops)
in the context of TWO-DIMENSIONAL GRAPHICS.

Authors: David Mutchler, Vibha Alangar, Dave Fisher, Matt Boutell, Mark Hays,
         Mohammed Noureddine, Sana Ebrahimi, Sriram Mohan, their colleagues and
         PUT_YOUR_NAME_HERE.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


# -----------------------------------------------------------------------------
# TODO: 2.
#  *** Unless your instructor directs you otherwise,
#      IF YOU HAVE NOT ALREADY WATCHED THE VIDEO
#          nested_loops_in_GRAPHICS.mp4
#      in the PREPARATION for this session
#          do so ** NOW **
#      As the video proceeds, LOOK AT THE CODE BELOW.
#      It is the same as in the video.
#  __
#  *** USE THE VIDEO to understand the TECHNIQUES used in BOTH examples.
#  __
#   AFTER you have watched the video, asking questions as needed,
#   and you feel that you understand the TECHNIQUES it presents, THEN:
#  __
#     *** Change the _TODO_ above to DONE. ***
# -----------------------------------------------------------------------------


def main():
    """ Calls the other functions to demonstrate them. """
    nested_loops_in_graphics_example()


def nested_loops_in_graphics_example():
    """
    Demonstrates nested loops in a TWO-DIMENSIONAL GRAPHICS example.
    """
    width = 800
    height = 600
    title = "Rectangles and Triangles of Circles"
    window = rg.RoseWindow(width, height, title)

    window.continue_on_mouse_click("Click to run Example 1.")

    # -------------------------------------------------------------------------
    starting_point = rg.Point(50, 50)
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # First set of circles
    # -------------------------------------------------------------------------
    radius = 20
    starting_circle = rg.Circle(starting_point, radius)

    rectangle_of_circles(window, starting_circle.clone(), 4, 12)
    window.continue_on_mouse_click("Click to run Example 2.")

    # -------------------------------------------------------------------------
    # Second set of circles
    # -------------------------------------------------------------------------
    starting_circle.move_by(180, 400)

    rectangle_of_circles(window, starting_circle.clone(), 14, 2)
    window.continue_on_mouse_click("Click to run Example 3.")

    # -------------------------------------------------------------------------
    # Third and last set of circles
    # -------------------------------------------------------------------------
    starting_circle.move_by(200, -400)

    triangle_of_circles(window, starting_circle.clone(), 8)
    window.close_on_mouse_click()


def rectangle_of_circles(window, circle, m, n):
    """
    Draws an m x n rectangle of circles (i.e. m columns and n rows)
    on the given rg.RoseWindow.  The given rg.Circle specifies:
      - The position of the upper-left circle drawn and also
      - The radius that all the circles have.
    After drawing each circle, pauses briefly (0.1 second).

    Preconditions:
      :type window: rg.RoseWindow
      :type circle: rg.Circle
      :type m: int
      :type n: int
    and m and n are small, positive integers.
    """
    original_x = circle.center.x
    original_y = circle.center.y
    radius = circle.radius

    x = original_x
    y = original_y
    for i in range(n):  # Loop through the rows
        for j in range(m):  # Loop through the columns
            new_circle = rg.Circle(rg.Point(x, y), radius)
            new_circle.attach_to(window)
            window.render(0.1)

            x = x + (2 * radius)  # Move x to the right, for next circle

        y = y + 2 * radius  # Move y down, for the next row of circles
        x = original_x  # Reset x to the left-edge, for the next row


def triangle_of_circles(window, circle, n):
    """
    Draws an n x n right-triangle of circles
    (1 circle in the top row, 2 in the next row, etc., until n rows)
    on the given rg.RoseWindow.  The given rg.Circle specifies:
      - The position of the upper-left circle drawn and also
      - The radius that all the circles have.
    After drawing each circle, pauses briefly (0.1 second).

    Preconditions:
      :type window: rg.RoseWindow
      :type circle: rg.Circle
      :type n: int
    and m is a small, positive integer.
    """
    # -------------------------------------------------------------------------
    # NOTE: The solution below is IDENTICAL to the rectangle_of_circles
    #       solution except that the INNER loop has  j+1  instead of m.
    # Make sure you understand why this works!
    # -------------------------------------------------------------------------
    original_x = circle.center.x
    original_y = circle.center.y
    radius = circle.radius

    x = original_x
    y = original_y
    for j in range(n):  # Loop through the rows
        for _ in range(j + 1):  # Loop through the columns
            new_circle = rg.Circle(rg.Point(x, y), radius)
            new_circle.attach_to(window.initial_canvas)
            window.render(0.1)

            x = x + (2 * radius)  # Move x to the right, for next circle

        y = y + 2 * radius  # Move y down, for the next row of circles
        x = original_x  # Reset x to the left-edge, for the next row


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
