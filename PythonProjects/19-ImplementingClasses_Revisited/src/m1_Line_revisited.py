"""
This module   REVISITS  the simple   Line   class that you implemented 
previously.  Note that:
  1. This is NOT rosegraphics -- it is your OWN Line class.
  2. We supply (below) a Point class that you should use in implementing
       your Line class.  YOU will implement PART of the Point class.

The learning objective of this exercise is to review QUICKLY the key ideas
of implementing classes, by RE-DOING work that you did previously, but doing
it in a BETTER way, by following along with your instructor.

The KEY IDEAS are:
  1. The notation for implementing a class called (say) Blah is:
        class Blah:
            def __init__(self, ...):
                ...
            def other_methods(self, ...):
                ...
                     
  2. When one constructs an instance of class Blah, e.g.:
            b = Blah(...)
     ** the  __init__  method in Blah's class definition runs, **
     with   self   referring to a NEW place in memory for
         ** Blah object being constructed **
     and the remaining arguments referring to the values in the parentheses.
     
  3. When one calls a method on an instance of class Blah, e.g.:
            b.other_method(...)
     the   other_method   method in Blah's class definition runs,
     with   self   referring to
         ** the object in front of the DOT **
     and the remaining arguments referring to the values in the parentheses.
  
  4. INSIDE a class definition, one uses exactly the SAME NOTATION as one uses
     OUTSIDE a class definition.  For example, inside the Blah class,
     one constructs a Blah object by:   b = Blah(...)
     
     Just remember that SELF refers to an instance of the class being defined. 

  5. If an instance of the class needs to REMEMBER (store) information in
     order for you to implement a method, add YOUR OWN instance variable
     for that purpose to __init__.  Choose a meaningful name for it, then
     use that instance variable as needed in other methods.
     
Authors: David Mutchler, Vibha Alangar, Dave Fisher, Matt Boutell, Mark Hays,
         Mohammed Noureddine, Sana Ebrahimi, Sriram Mohan, their colleagues and
         Groucho.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import math
import m1t_test_Line as m1t


###############################################################################
# IMPORTANT:
#   Your instructor will lead you through this exercise.
###############################################################################
# -----------------------------------------------------------------------------
# DONE: 2.  Right-click on the  src  folder and
#               Mark Directory as ... Sources Root,
#           if you have not already done so.
# -----------------------------------------------------------------------------

###############################################################################
# The   Point   class (and its methods) begins here.
###############################################################################
class Point:
    """ Represents a point in 2-dimensional space. """

    def __init__(self, x, y):
        """ Sets instance variables  x  and  y  to the given coordinates. """
        # DONE: 3. What is SELF here?
        #   the Point being constructed
        #  Implement the above spec, using instance variables named x and y.
        self.x = x
        self.y = y

    def __repr__(self):
        """ Returns a fancy string representation of this Point. """
        # DONE: 4. Read the above spec.  (Ignore the details of the code below.)
        #  What function that you use a LOT calls the __repr__ method?
        #   print
        decimal_places = 2  # Use 2 places after the decimal point

        formats = []
        numbers = []
        for coordinate in (self.x, self.y):
            if abs(coordinate - round(coordinate)) < (10 ** -decimal_places):
                # Treat it as an integer:
                formats.append("{}")
                numbers.append(round(coordinate))
            else:
                # Treat it as a float to decimal_places decimal places:
                formats.append("{:." + str(decimal_places) + "f}")
                numbers.append(round(coordinate, decimal_places))

        format_string = "Point(" + formats[0] + ", " + formats[1] + ")"
        return format_string.format(numbers[0], numbers[1])

    def __eq__(self, p2):
        """
        Defines == for Points:  a == b   is equivalent to  a.__eq__(b).
        Treats two numbers as "equal" if they are within 6 decimal
        places of each other for both x and y coordinates.
        """
        # DONE: 5. Read the above spec.  What would go wrong if we did NOT
        #  define __eq__ for a Point. That is, why would we WANT to define EQ?
        #   Then two Points like   a = Point(10, 5) and b = Point(10, 5)
        #   would NOT be treated as equal, that is,   a == b would be FALSE.
        return (round(self.x, 6) == round(p2.x, 6) and
                round(self.y, 6) == round(p2.y, 6))

    def clone(self):
        """  Returns a new Point at the same (x, y) as this Point. """
        # TODO: 6.  What is SELF here?  Implement the above spec.
        #    SELF is the Point being cloned, that is, the Point
        #    in front of the dot in the caller, e.g.,   a.clone()
        #  Concepts illustrated:
        #    -- constructing an instance of a class and
        #    -- accessing instance variables
        #  Note: SAME NOTATION as when NOT inside a class definition!
        return Point(self.x, self.y)

    def distance_from(self, p2):
        """ Returns the distance this Point is from the given Point. """
        # DONE: 7.  What is SELF here?  What is p2 here?  Read the code below.
        #   SELF is the Point in front of the dot in the caller, p2 is the Point
        #   inside the parentheses:    a.distance_from(b)
        #  Which feels better: the multi-line solution or the one-line solution?
        #  Note (again): SAME NOTATION as when NOT inside a class definition!

        dx_squared = (self.x - p2.x) ** 2
        dy_squared = (self.y - p2.y) ** 2

        return math.sqrt(dx_squared + dy_squared)

        # Alternative solution:
        return ((self.x - p2.x) ** 2 + (self.y - p2.y) ** 2) ** 0.5

    def halfway_to(self, p2):
        """ Returns a new Point half-way between this Point and given Point. """
        # TODO: 8.  What are SELF and p2 here?  Implement the above spec.
        #  SELF is the Point in front of the dot in the caller, p2 is the Point
        #         #   inside the parentheses:    a.halfway_to(b)
        #   Geometry hint: Average the x-coordinates and average the
        #   y-coordinates to get the coordinates of the halfway-between Point.
        #   (No subtraction!  Although there is a formula for halfway that
        #   uses subtraction, the formula for the average is simpler!)
        return Point((self.x + p2.x) / 2, (self.y + p2.y) / 2)

    def plus(self, p2):
        """
        Returns a Point whose coordinates are those of this Point
        PLUS the given Point.  For example:
            p1 = Point(500, 20)
            p2 = Point(100, 13)
            p3 = p1.plus(p2)
            print(p3)
        would print:   Point(600, 33)
        """
        # DONE: 9.  What are SELF and p2 here?  Implement the above spec.
        return Point(self.x + p2.x, self.y + p2.y)

    def minus(self, p2):
        """
        Returns a Point whose coordinates are those of this Point
        MINUS the given Point.  For example:
            p1 = Point(500, 20)
            p2 = Point(100, 13)
            p3 = p1.minus(p2)
            print(p3)
        would print:   Point(400, 7)
        """
        # DONE: 10.  What are SELF and p2 here?  Implement the above spec.
        return Point(self.x - p2.x, self.y - p2.y)


def main():
    """
    Calls the   TEST   functions in this module, but ONLY if the method
    to be tested has at least a partial implementation.  That is,
    a  TEST   function will not be called until you begin work
    on the code that it is testing.
    """
    if m1t.is_implemented("__init__"):
        run_test_init()
    if m1t.is_implemented("clone"):
        run_test_clone()
    if m1t.is_implemented("reverse"):
        run_test_reverse()
    if m1t.is_implemented("slope"):
        run_test_slope()
    if m1t.is_implemented("length"):
        run_test_length()
    if m1t.is_implemented("get_number_of_clones"):
        run_test_get_number_of_clones()
    if m1t.is_implemented("line_plus"):
        run_test_line_plus()
    if m1t.is_implemented("line_minus"):
        run_test_line_minus()
    if m1t.is_implemented("midpoint"):
        run_test_midpoint()
    if m1t.is_implemented("is_parallel"):
        run_test_is_parallel()
    if m1t.is_implemented("reset"):
        run_test_reset()


###############################################################################
# The   Line   class (and its methods) begins here.
###############################################################################
class Line(object):
    """ Represents a line segment in 2-dimensional space. """

    def __init__(self, start, end):
        """
        What comes in:
          -- self
          -- a Point object named  start
          -- a Point object named  end
        where the two Points are to be the initial start and end points,
        respectively, of this Line.
        Side effects: MUTATEs this Line by setting instance variables named:
          -- start
          -- end
        to CLONES of the two Point arguments, respectively.

        Type hints:
          :type start: Point
          :type end:   Point
        """
        # DONE: 11.  What is SELF?  What TYPE of objects are start and end?
        #  SELF is the LINE being constructed.  Start and end are Points.
        #  What does putting the "Type hints" accomplish?
        #  Implement the above spec.  Use the Point class  clone  method!
        #  Why is it wise to CLONE start and end?  (See to_clone_or_not.pdf)
        self.start = start.clone()
        self.end = end.clone()

        self.number_of_times_cloned = 0
        self.original_start = self.start.clone()
        self.original_end = self.end.clone()

        # In reset:
        self.start = self.original_start
        self.end = self.original_end

    def __repr__(self):
        """ Returns a string representation of this Line. """
        # TODO: 12. Read the above spec.
        #  What function that you use a LOT calls the __repr__ method?
        #   PRINT
        start = repr(self.start).replace("Point", "")
        end = repr(self.end).replace("Point", "")
        return "Line[{}, {}]".format(start, end)

    def __eq__(self, line2):
        """
        Defines == for Lines:  a == b   is equivalent to  a.__eq__(b).
        """
        # DONE: 13. Read the above spec.  Why would we WANT to define == ?
        #  Then mark this _TODO_ as DONE.
        #   What it means for two Lines to be "equal"
        return (self.start == line2.start) and (self.end == line2.end)

    def clone(self):
        """
        What comes in:
          -- self
        What goes out: Returns a new Line whose START is a clone of
          this Line's START and whose END is a clone of this Line's END.
        """
        # DONE: 14.  What is SELF?  Implement the above spec.
        #   The Line being cloned, ie., the one in front of the dot
        #   in    a.clone()
        #  Use the Point class  clone  method!
        self.number_of_times_cloned = self.number_of_times_cloned + 1
        return Line(self.start.clone(), self.end.clone())

    def reverse(self):
        """
        What comes in:
          -- self
        Side effects: MUTATES this Line so that its direction is reversed
        (that is, its start and end points are swapped).
        ** Must NOT mutate its start and end points -- just SWAP them. **
        """
        # TODO: 15.  What is SELF?  Implement the above spec.
        #  What is the SWAP pattern?  (Hint: temp variable, 3 lines, think Z.)
        temp = self.start
        self.start = self.end
        self.end = temp

    def slope(self):
        """
        What comes in:
          -- self
        What goes out: Returns the slope of this Line, or
           math.inf
        if the line is vertical (i.e., has "infinite" slope).
        """
        # DONE: 16.  What is SELF?  Implement the above spec.
        #  Geometry hint:  slope = dy / dx.  Guard against division by zero!
        dx = self.start.x - self.end.x
        dy = self.start.y - self.end.y

        if dx == 0:
            return math.inf
        return dy / dx

    def length(self):
        """
        What comes in:
          -- self
        What goes out: Returns the length of this Line.
        """
        # DONE: 17.  What is SELF?  Implement the above spec.
        #   The Line whose length we want, ie, distance from
        #   self.start to self.end.
        #  Geometry hint:  length of a line is the distance from its start
        #  point to its end point.  Use the Point class  distance_from   method!
        return self.start.distance_from(self.end)

    def get_number_of_clones(self):
        """
        What comes in:
          -- self
        What goes out:
          -- Returns the number of times that this Line has been cloned
               (via the   clone   method).
        """
        # TODO: 18.  Do you see that you MUST introduce an instance variable
        #  to STORE with the Line the number of times clone has been called?
        #  Implement the above spec.
        #    (Hint:  add a new instance variable to __init__ and ...)
        return self.number_of_times_cloned

    def line_plus(self, other_line):
        """
        What comes in:
          -- self
          -- another Line object
        What goes out:
          -- Returns a Line whose:
              -- start is the sum of this Line's start (a Point)
                   and the other_line's start (another Point).
              -- end is the sum of this Line's end (a Point)
                   and the other_line's end (another Point).
        Type hints:
          :type  other_line: Line
        """
        # DONE: 19.  What is SELF?  other_line?  Implement this method.
        #  Use methods from the Point class!
        return Line(self.start.plus(other_line.start),
                    self.end.plus(other_line.end))

    def line_minus(self, other_line):
        """
        What comes in:
          -- self
          -- another Line object
        What goes out:
          -- Returns a Line whose:
              -- start is this Line's start (a Point)
                   minus the other_line's start (another Point).
              -- end is this Line's end (a Point)
                   minus the other_line's end (another Point).
        Type hints:
          :type  other_line: Line
        """
        # TODO: 20.  What is SELF?  other_line?  Implement this method.
        #   SELF is the Line in front of the dot.  Other_line is the Line
        # inside the parentheses.    a.line_minus(b)
        #  Use methods from the Point class!
        return Line(self.start.minus(other_line.start),
                    self.end.minus(other_line.end))

    def midpoint(self):
        """
        What comes in:
          -- self
        What goes out: returns a Point at the midpoint of this Line.
        """
        # TODO: 21.  What is SELF?  Implement this method.
        #  Use a method from the Point class!
        return self.start.halfway_to(self.end)

    def is_parallel(self, line2):
        """
        What comes in:
          -- self
          -- another Line object (line2)
        What goes out: Returns  True  if this Line is parallel to the
          given Line (line2).  Returns  False  otherwise.
            *** SEE THE IMPORTANT NOTE BELOW, re ROUNDING numbers.
        Type hints:
          :type  line2: Line
        """
        # TODO: 22.  What is SELF?  line2?  Implement this method.
        #  IMPORTANT NOTE:
        #  Use the  slope  method, but round to 12 decimal places.
        return round(self.slope(), 12) == round(line2.slope(), 12)

    def reset(self):
        """
        What comes in:
          -- self
        Side effects: MUTATES this Line so that its start and end points
          revert to what they were when this Line was constructed.
        """
        # TODO: 23.  Do you see that you MUST introduce an instance variable
        #  to STORE the original  start  and  end  Point objects
        #  and that you CANNOT use SELF for that purpose?
        #  Implement the above spec.
        #     (Hint:  add a new instance variable to __init__ and ...)
        self.start = self.original_start
        self.end = self.original_end


###############################################################################
# The TEST functions for the  Line  class begin here.
#
# We have already written the TEST functions.  They all take the form:
#   -- m1t.run_test_BLAH()  # This runs OUR tests.
#   -- One more test (or set of tests) that came directly from the Example
#        in the specification.
###############################################################################
def run_test_init():
    """ Tests the   __init__   method of the Line class. """
    m1t.run_test_init()  # This runs OUR tests.
    # -------------------------------------------------------------------------
    # One ADDITIONAL test (or set of tests).
    # -------------------------------------------------------------------------
    p1 = Point(30, 17)
    p2 = Point(50, 80)
    line = Line(p1, p2)  # Causes __init__ to run

    print(line.start)  # Should print Point(30, 17)
    print(line.end)  # Should print Point(50, 80)
    print(line.start == p1)  # Should print True
    print(line.start is p1)  # Should print False

    print("The above should print:")
    print("  Point(30, 17)")
    print("  Point(50, 80)")
    print("  True")
    print("  False")


def run_test_clone():
    """ Tests the   clone   method of the Line class. """
    m1t.run_test_clone()  # This runs OUR tests.
    # -------------------------------------------------------------------------
    # One ADDITIONAL test (or set of tests).
    # -------------------------------------------------------------------------
    p1 = Point(30, 17)
    p2 = Point(50, 80)
    line1 = Line(p1, p2)
    line2 = line1.clone()

    print(line1)  # Should print: Line[(30, 17), (50, 80)]
    print(line2)  # Should print: Line[(30, 17), (50, 80)]
    print(line1 == line2)  # Should print: True
    print(line1 is line2)  # Should print: False
    print(line1.start is line2.start)  # Should print: False
    print(line1.end is line2.end)  # Should print: False

    line1.start = Point(11, 12)
    print(line1)  # Should print: Line[(11, 12), (50, 80)]
    print(line2)  # Should print: Line[(30, 17), (50, 80)]
    print(line1 == line2)  # Should now print: False

    print("The above should print:")
    print("  Line[(30, 17), (50, 80)]")
    print("  Line[(30, 17), (50, 80)]")
    print("  True")
    print("  False")
    print("  False")
    print("  False")
    print("  Line[(11, 12), (50, 80)]")
    print("  Line[(30, 17), (50, 80)")
    print("  False")


def run_test_reverse():
    """ Tests the   reverse   method of the Line class. """
    m1t.run_test_reverse()  # This runs OUR tests.
    # -------------------------------------------------------------------------
    # One ADDITIONAL test (or set of tests).
    # -------------------------------------------------------------------------
    p1 = Point(30, 17)
    p2 = Point(50, 80)
    line1 = Line(p1, p2)
    line2 = line1.clone()

    print(line1)  # Should print: Line[(30, 17), (50, 80)]

    line1.reverse()
    print(line1)  # Should print: Line[(50, 80), (30, 17)]
    print(line1 == line2)  # Should print: False

    line1.reverse()
    print(line1 == line2)  # Should now print: True

    print("The above should print:")
    print("  Line[(30, 17), (50, 80)]")
    print("  Line[(50, 80), (30, 17)")
    print("  False")
    print("  True")


def run_test_slope():
    """ Tests the   slope   method of the Line class. """
    m1t.run_test_slope()  # This runs OUR tests.
    # -------------------------------------------------------------------------
    # One ADDITIONAL test (or set of tests).
    # -------------------------------------------------------------------------
    p1 = Point(30, 3)
    p2 = Point(50, 8)
    line1 = Line(p1, p2)

    # Since the slope is (8 - 3) / (50 - 30) , which is 0.25:
    print(line1.slope())  # Should print [approximately]: 0.25

    line2 = Line(Point(10, 10), Point(10, 5))
    print(line2.slope())  # Should print:  inf

    # math.inf is NOT the STRING "inf", so:
    print(line2.slope() == "inf")  # Should print False

    print("The above should print:")
    print("  0.25 (approximately)")
    print("  inf")
    print("  False")


def run_test_length():
    """ Tests the   length   method of the Line class. """
    m1t.run_test_length()  # This runs OUR tests.
    # -------------------------------------------------------------------------
    # One ADDITIONAL test (or set of tests).
    # -------------------------------------------------------------------------
    p1 = Point(166, 10)
    p2 = Point(100, 10)
    line1 = Line(p1, p2)

    # Since the distance from p1 to p2 is 66:
    print(line1.length())  # Should print: 66.0

    p3 = Point(0, 0)
    p4 = Point(3, 4)
    line2 = Line(p3, p4)
    print(line2.length())  # Should print about 5.0

    print("The above should print:")
    print("  66.0")
    print("  5.0 (approximately)")


def run_test_get_number_of_clones():
    """ Tests the   get_number_of_clones   method of the Line class. """
    m1t.run_test_get_number_of_clones()  # This runs OUR tests.
    # -------------------------------------------------------------------------
    # One ADDITIONAL test (or set of tests).
    # -------------------------------------------------------------------------
    line1 = Line(Point(500, 20), Point(100, 8))
    line2 = line1.clone()
    line3 = line1.clone()
    line4 = line3.clone()
    line5 = line1.clone()
    print(line1.get_number_of_clones())
    print(line2.get_number_of_clones())
    print(line3.get_number_of_clones())
    print(line4.get_number_of_clones())
    print(line5.get_number_of_clones())
    print("The above should print 3, then 0, then 1, then 0, then 0.")


def run_test_line_plus():
    """ Tests the   line_plus   method of the Line class. """
    m1t.run_test_line_plus()  # This runs OUR tests.
    # -------------------------------------------------------------------------
    # One ADDITIONAL test (or set of tests).
    # -------------------------------------------------------------------------
    line1 = Line(Point(500, 20), Point(100, 8))
    line2 = Line(Point(100, 13), Point(400, 8))
    line3 = line1.line_plus(line2)
    print(line3)
    print("The above should print:  Line[(600, 33), (500, 16)]")


def run_test_line_minus():
    """ Tests the   line_minus   method of the Line class. """
    m1t.run_test_line_minus()  # This runs OUR tests.
    # -------------------------------------------------------------------------
    # One ADDITIONAL test (or set of tests).
    # -------------------------------------------------------------------------
    line1 = Line(Point(500, 20), Point(100, 8))
    line2 = Line(Point(100, 13), Point(400, 8))
    line3 = line1.line_minus(line2)
    print(line3)
    print("The above should print:  Line[(400, 7), (-300, 0)]")


def run_test_midpoint():
    """ Tests the   midpoint   method of the Line class. """
    m1t.run_test_midpoint()  # This runs OUR tests.
    # -------------------------------------------------------------------------
    # One ADDITIONAL test (or set of tests).
    # -------------------------------------------------------------------------
    p1 = Point(3, 10)
    p2 = Point(9, 20)
    line1 = Line(p1, p2)

    print(line1.midpoint())  # Should print: Point(6, 15)

    print("The above should print:  Point(6, 15)")


def run_test_is_parallel():
    """ Tests the   is_parallel   method of the Line class. """
    m1t.run_test_is_parallel()  # This runs OUR tests.
    # -------------------------------------------------------------------------
    # One ADDITIONAL test (or set of tests).
    # -------------------------------------------------------------------------
    line1 = Line(Point(15, 30), Point(17, 50))  # slope is 10.0
    line2 = Line(Point(10, 10), Point(15, 60))  # slope is 10.0
    line3 = Line(Point(10, 10), Point(80, 80))  # slope is  7.0
    line4 = Line(Point(10, 10), Point(10, 20))  # slope is inf

    print(line1.is_parallel(line2))  # Should print: True
    print(line2.is_parallel(line1))  # Should print: True
    print(line1.is_parallel(line3))  # Should print: False
    print(line1.is_parallel(line4))  # Should print: False
    print(line1.is_parallel(line1))  # Should print: True
    print(line4.is_parallel(line4))  # Should print: True

    print("The above should print:")
    print("  True,  True,  False,  False,  True,  True")


def run_test_reset():
    """ Tests the   reset   method of the Line class. """
    m1t.run_test_reset()  # This runs OUR tests.
    # -------------------------------------------------------------------------
    # One ADDITIONAL test (or set of tests).
    # -------------------------------------------------------------------------
    p1 = Point(-3, -4)
    p2 = Point(3, 4)
    line1 = Line(p1, p2)
    line2 = Line(Point(0, 1), Point(10, 20))

    line1.start = Point(100, 300)
    line2.end = Point(99, 4)
    line1.reverse()

    # Should print: Line[(x1, y1), (x2, y2)] where (x1, y1) and
    # (x2, y2) are the CURRENT coordinates of line1's endpoints.
    print(line1)
    print(line2)  # Similarly for line2

    line1.reset()
    line2.reset()
    print(line1)  # Should print: Line[(-3, -4), (3, 4)]
    print(line2)  # Should print: Line[(0, 1), (10, 20)]

    print("The above should print:")
    print("  Line[(3, 4), (100, 300)]")
    print("  Line[(0, 1), (99, 4)]")
    print("  Line[(-3, -4), (3, 4)]")
    print("  Line[(0, 1), (10, 20)]")


# -----------------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the "main" function.
# It is necessary here to enable the automatic testing in m1t_test_Line.py.
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    main()
