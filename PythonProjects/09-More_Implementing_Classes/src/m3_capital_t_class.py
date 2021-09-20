"""
A   CapitalT   class and functions that use/test it.

Authors: David Mutchler, Yiji Zhang, Mark Hays, Derek Whitley, Vibha Alangar,
         Matt Boutell, Dave Fisher, Sriram Mohan, Mohammed Noureddine,
         Amanda Stouder, Curt Clifton, Valerie Galluzzi, their colleagues and
         PUT_YOUR_NAME_HERE.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


# -----------------------------------------------------------------------------
# TODO: 2.
#   Skim this module, noting:
#     -- You must un-comment the calls to the testing functions as you go.
#     -- We supplied the tests, each of which has an associated PDF.
#     -- You will be implementing a CapitalT class per the specification
#          that is at the ** NEXT **  _TODO_.
#   After skimming the module per the above,
#   OPEN the file   03a-dimensions.pdf    that is included with this project
#   and KEEP IT OPEN as you continue to the next _TODO_.
#   After you have done the above, mark this _TODO_ as DONE.
# -----------------------------------------------------------------------------


def main():
    """
    Calls the test functions.
    As you implement CapitalT methods, uncomment the appropriate tests.
    """
    # -------------------------------------------------------------------------
    #   Uncomment only 1 test at a time as you develop your code.
    # -------------------------------------------------------------------------
    print("Un-comment the calls in MAIN one by one")
    print(" to run the testing code as you complete the TODOs.")

    # run_test_simple_t()
    # run_test_set_colors()
    # run_test_move_by()
    # run_test_clone()


def run_test_simple_t():
    """
    Tests for the   __init__   method and   attach_to   method.
    Implement BOTH of them before running this test.
    See   03b-simple_t.pdf  for the expected output.
    """
    print()
    print("--------------------------------------------------")
    print("Testing    __init__    and    attach_to ")
    print("--------------------------------------------------")
    window = rg.RoseWindow(600, 400, "Test 1 - Simple Ts")
    t1 = CapitalT(rg.Point(300, 50), 100, 200, 20)
    print("Expected: Point(250.0, 40.0) Point(350.0, 60.0)")
    print("Actual:  ", t1.h_rect.get_upper_left_corner(),
          t1.h_rect.get_lower_right_corner())
    print("Expected: Point(290.0, 40.0) Point(310.0, 240.0)")
    print("Actual:  ", t1.v_rect.get_upper_left_corner(),
          t1.v_rect.get_lower_right_corner())
    t1.attach_to(window)
    t2 = CapitalT(rg.Point(150, 150), 100, 150, 40)
    t2.attach_to(window)
    t3 = CapitalT(rg.Point(450, 150), 10, 15, 4)
    t3.attach_to(window)
    window.render()
    print("See graphics window and compare to the 03b-simple_t PDF")
    window.close_on_mouse_click()

    if len(vars(t1).keys()) > 2:
        print()
        print("ERROR: You appear to have used extra instance variables.")
        print("See the   IMPORTANT RESTRICTION   in the specification.")
        print("You must do this problem with ONLY  h_rect  and   v_rect.")


def run_test_set_colors():
    """
    Tests for the   set_colors   method.
    See the  03c-set_colors.pdf   for the expected output.
    """
    window = rg.RoseWindow(600, 400, "Test 2 - Colorful Ts")
    t1 = CapitalT(rg.Point(300, 50), 100, 200, 20)
    t1.set_colors("red", "magenta")
    t1.attach_to(window)
    t2 = CapitalT(rg.Point(150, 150), 100, 150, 40)
    t2.set_colors("green", "purple")
    t2.attach_to(window)
    t3 = CapitalT(rg.Point(450, 150), 10, 15, 4)
    t3.set_colors("blue", "gray")
    t3.attach_to(window)
    window.render()
    window.close_on_mouse_click()


def run_test_move_by():
    """
    Tests for the   move_by   method.
    See the   03d-move_by.pdf   for the expected output.
    """
    window = rg.RoseWindow(600, 400, "Test 3 - Moving T")
    little_red_t = CapitalT(rg.Point(300, 50), 60, 80, 5)
    little_red_t.set_colors("red", "gray")
    little_red_t.attach_to(window)
    window.render(0.5)
    little_red_t.move_by(0, 100)
    window.render(0.5)
    little_red_t.move_by(0, 100)
    window.render(0.5)
    for k in range(40):
        little_red_t.move_by(5, -2)
        window.render(0.05)
    window.close_on_mouse_click()


def run_test_clone():
    """
    Tests for the   clone   method.
    See the   03e-clone.pdf   for the expected output.
    """
    window = rg.RoseWindow(650, 400, "Test 4 - Cloning Ts")
    first_t = CapitalT(rg.Point(75, 50), 80, 80, 40)
    first_t.set_colors("blue", "cyan")
    for k in range(6):
        t = first_t.clone()
        if k < 2:
            t.set_colors("white", "black")
        t.move_by(100 * k, 20 * k)
        t.attach_to(window)
    first_t.move_by(0, 200)
    first_t.attach_to(window)
    window.render()
    window.close_on_mouse_click()


###############################################################################
# The   CapitalT   class (and its methods) begins here.
###############################################################################
class CapitalT(object):
    """
    Manages a CapitalT graphics object which is made up of two rectangles.
    *** See the PDFs, especially
            03a-dimensions.pdf
        to help you understand this specification.
    """

    def __init__(self, intersection_center, width, height, letter_thickness):
        """
        *** See   03a-dimensions.pdf   to understand the following! ***

        What comes in:
           -- self
           -- an rg.Point for the intersection center of the CapitalT
              -- This point is also center of the horizontal rectangle.
           -- a int for the width of the CapitalT
                 (that is, the width of the horizontal rectangle)
           -- a int for the height of the CapitalT
                 (that is, the height of the vertical rectangle)
           -- a int for the CapitalT's thickness, that is,
                 the height of the horizontal rectangle and also
                 the width of the vertical rectangle.
        What goes out:  Nothing (i.e., None).
        Side effects: Sets two instance variables named:
          -- h_rect  (to represent the horizontal rectangle in the T,
                      that is, the top bar)
          -- v_rect  (to represent the vertical rectangle in the T,
                      that is, the | part of the T)

           *** See   03a-dimensions.pdf   to understand the above! ***

        Each rectangle is an rg.Rectangle.

        IMPORTANT RESTRICTION:  Unlike prior modules you are NOT allowed
            to make any other instance variables than h_rect and v_rect.
            You must figure out how to do the problem with ONLY
            those two instance variables.

        Example:
            t1 = CapitalT(rg.Point(300, 50), 100, 200, 20)
                -- t1.h_rect would have an upper left corner of (250, 40)
                -- t1.h_rect would have an lower right corner of (350, 60)
                -- t1.v_rect would have an upper left corner of (290, 40)
                -- t1.v_rect would have an lower right corner of (310, 240)

            *** Make sure that you understand this example before     ***
            *** proceeding. See    03a-dimensions.pdf   to understand it! ***

        Type hints:
          :type intersection_center: rg.Point
          :type width:               int
          :type height:              int
          :type letter_thickness:    int
        """
        # ---------------------------------------------------------------------
        # TODO: 3.
        #   READ the above specification, including the Example.
        #   Implement this method, using the instance variables
        #      h_rect
        #      v_rect
        #   and *** NO OTHER INSTANCE VARIABLES. ***
        #   Note: Implement   attach_to   before testing this __init__ method.
        # ---------------------------------------------------------------------

    def attach_to(self, window):
        """
        What comes in:
           -- self
           -- an rg.RoseWindow
        What goes out:  Nothing (i.e., None).
        Side effects:
          -- Attaches both instance-variable rectangles to the given window.
          -- Hint: Attach  h_rect  second to make it draw in front of  v_rect.

        Example:
            window = rg.RoseWindow()
            t1 = CapitalT(rg.Point(300, 50), 100, 200, 20)
            t1.attach_to(window)

        Type hints:
          :type window: rg.RoseWindow
        """
        # ---------------------------------------------------------------------
        # TODO: 4.
        #   READ the above specification, including the Example.
        #   Implement this method, then TEST it by:
        #     a. Un-comment the call to its test function, in main.  Run.
        #     b. Look at the Console output.  Does it indicate any errors?
        #     c. Compare the graphics window to the pictures in
        #           03b-simple_t.pdf.
        #        Your window should look exactly like the pictures in the PDF.
        # ---------------------------------------------------------------------

    def set_colors(self, fill_color, outline_color):
        """
        What comes in:
          -- self
          -- a string that represents a valid rosegraphics color
          -- a string that represents a valid rosegraphics color
        What goes out:  Nothing (i.e., None).
        Side effects:
          -- Sets the fill_color of both instance-variable rectangles
               to the given fill color.
          -- Sets the outline_color of both instance-variable rectangles
               to the given outline color.

        Example:
            window = rg.RoseWindow()
            t1 = CapitalT(rg.Point(300, 50), 100, 200, 20)
            t1.set_color("red", "blue")

        Type hints:
          :type fill_color:    str
          :type outline_color: str
        """
        # ---------------------------------------------------------------------
        # TODO: 5.
        #   READ the above specification, including the Example.
        #   Implement this method, then TEST it by:
        #     a. Un-comment the call to its test function, in main.  Run.
        #     b. Look at the Console output.  Does it indicate any errors?
        #     c. Compare the graphics window to the pictures in
        #           03c-set_colors.pdf.
        #        Your window should look exactly like the pictures in the PDF.
        # ---------------------------------------------------------------------

    # See the IMPORTANT HINT in the TODO below!
    def move_by(self, dx, dy):
        """
        What comes in:
           -- self
           -- an int amount to move in the x direction
           -- an int amount to move in the y direction
        What goes out:  Nothing (i.e., None).
        Side effects:
          -- Moves both instance-variable rectangles the specified distances
               in the x and y directions, respectively.

        Example:
            window = rg.RoseWindow()
            t1 = CapitalT(rg.Point(300, 50), 100, 200, 20)
            t1.attach_to(window)
            window.render(0.5)
            t1.move_by(100, 200) # Moves the T 100 pixels right and 200 down.
            window.render()  # necessary to see the change

        Type hints:
          :type dx: int
          :type dy: int
        """
        # ---------------------------------------------------------------------
        # TODO: 6.
        #   READ the above specification, including the Example.
        #   Implement this method, then TEST it by:
        #     a. Un-comment the call to its test function, in main.  Run.
        #     b. Look at the Console output.  Does it indicate any errors?
        #     c. Compare the graphics window to the picture in
        #           03d-move_by.pdf.
        #        Your window should look exactly like the pictures in the PDF.
        #   ___
        #   Note: the 03d-move_by.pdf shows the different locations that
        #         the T moves through, but there is only one T at any moment.
        #   _
        #   IMPORTANT HINT:  rg.Rectangle objects have their OWN move_by method.
        #   Using that makes the implementation of this method VERY short!!!
        # ---------------------------------------------------------------------

    def clone(self):
        """
        What comes in:
          -- self
        What goes out:
          -- Returns a new CapitalT that is located at the same position
               as this CapitalT and has the same colors for its
               instance-variable rectangles.
        Side effects:
          -- None

        Example:
            window = rg.RoseWindow()
            t1 = CapitalT(rg.Point(300, 50), 100, 200, 20)
            t1.set_color("red", "blue")
            t2 = t1.clone() # t2 is at the same location WITH THE SAME COLORS

        Type hints:
          :rtype: CapitalT
        """
        # ---------------------------------------------------------------------
        # TODO: 7.
        #   READ the above specification, including the Example.
        #   Implement this method, then TEST it by:
        #     a. Un-comment the call to its test function, in main.  Run.
        #     b. Look at the Console output.  Does it indicate any errors?
        #     c. Compare the graphics window to the pictures in
        #           03e-clone.pdf   pictures.
        #        Your window should look exactly like the pictures in the PDF.
        #  ####################################################################
        #  IMPORTANT RESTRICTION: You are NOT permitted to add any instance
        #  variables beyond  h_rect  and  v_rect, at any point of this exercise.
        #######################################################################


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
