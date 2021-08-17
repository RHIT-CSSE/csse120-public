"""
This module lets you practice  ** using objects **, including:
  -- CONSTRUCTING objects,
  -- applying METHODS to them, and
  -- accessing their DATA via INSTANCE VARIABLES

Authors: David Mutchler, Vibha Alangar, Dave Fisher, Matt Boutell, Mark Hays,
         Mohammed Noureddine, Sana Ebrahimi, Sriram Mohan, their colleagues and
         PUT_YOUR_NAME_HERE.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the other functions to demonstrate and/or test them. """
    # Test your functions by putting calls to them here:


def two_circles():
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws two rg.Circle objects on the window
         such that:
           -- They fit in the window and are easily visible.
           -- They have different radii.
           -- One is filled with some color and one is not filled.
    -- Waits for the user to press the mouse, then closes the window.
    """
    # -------------------------------------------------------------------------
    # TODO: 2. Implement this function, per its green doc-string above.
    #     -- ANY two rg.Circle objects that meet the criteria are fine.
    #     -- File  COLORS.txt  lists all legal color-names.
    #   Put a statement in   main   to test this function
    #    (by calling this function).
    #   HINT: Module  m2r_using_rosegraphics  has helpful examples for this.
    # -------------------------------------------------------------------------


def lines():
    """
    -- Constructs a rg.RoseWindow.
    -- Constructs and draws on the window two rg.Lines such that:
          -- They both fit in the window and are easily visible.
          -- One rg.Line has the default thickness.
          -- The other rg.Line is thicker (i.e., has a bigger width).
    -- Uses a rg.Line method to get the midpoint (center) of the
         thicker rg.Line.
    -- Then prints (on the console, on SEPARATE lines, for the thicker Line):
         -- the midpoint itself
         -- the x-coordinate of the midpoint
         -- the y-coordinate of the midpoint

       Here is an example of the output on the console, if the two
       endpoints of the thicker line are at (100, 100) and (121, 200):
            Point(110.5, 150.0)
            110.5
            150.0

    -- Waits for the user to press the mouse, then closes the window.
    """
    # -------------------------------------------------------------------------
    # TODO: 3. Implement this function, per its green doc-string above.
    #    -- ANY lines that meet the criteria are fine.
    #  Put a statement in   main   to test this function
    #    (by calling this function).
    #   HINT: Module  m2r_using_rosegraphics  has helpful examples for this.
    #  ___
    #  IMPORTANT: Use the DOT TRICK to guess the name of the relevant method
    #    and instance variables.
    # -------------------------------------------------------------------------


def circle_and_rectangle():
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws a rg.Circle and rg.Rectangle
       on the window such that:
          -- They fit in the window and are easily visible.
          -- The rg.Circle is filled with 'blue'
    -- Prints (on the console, on SEPARATE lines) the following data
         associated with your rg.Circle (using its INSTANCE VARIABLES):
          -- Its outline thickness.
          -- Its fill color.
          -- Its center.
          -- Its center's x coordinate.
          -- Its center's y coordinate.
    -- Prints (on the console, on SEPARATE lines) the same data
         but for your rg.Rectangle.  (Hint: For this, you'll need to use
         a METHOD that begins with "get".)
    -- Waits for the user to press the mouse, then closes the window.

    Here is an example of the output on the console,
    for one particular circle and rectangle:
           1
           blue
           Point(180.0, 115.0)
           180
           115
           1
           None
           Point(75.0, 150.0)
           75.0
           150.0
    """
    # -------------------------------------------------------------------------
    # TODO: 4. Implement this function, per its green doc-string above.
    #    -- ANY objects that meet the criteria are fine.
    #  Put a statement in   main   to test this function
    #    (by calling this function).
    #   HINT: Module  m2r_using_rosegraphics  has helpful examples for this.
    #  ___
    #  IMPORTANT: Use the DOT TRICK to guess the names of the relevant
    #       instance variables for outline thickness, etc.
    # -------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
