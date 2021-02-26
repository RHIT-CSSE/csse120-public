"""
Test 3, problem 2.

Authors: Mark Hays, Amanda Stouder, their colleagues,
         and Zachary Bergstedt.  January 2015.
"""  # TODO: PUT YOUR NAME IN THE ABOVE LINE.


import rosegraphics as rg

class Polygon(object):
    """
    The Polygon class represents a polygon that is drawn on the screen with RoseGraphics.
    
    The Polygon constructor takes a list (points) that contains some number of rg.Points.
    The constructor creates rg.Lines between the points in the order they're given.
    The last line should go from the last point to the first point given.
    
    The Polygon must have at least these two instance variables:
    - points: the list of points defining the polygon.
    - lines: the list of lines between the points.
    
    The Polygon must have at least these three methods:
    - set_outline_color(color): sets the color of each line to the given color.
    - attach_to(window): attaches the lines to the given window.
    - sub_polygon(): returns a smaller polygon with the same number of sides as this polygon,
         whose points are the midpoints of each side of this polygon.
    """
    # TODO: implement the methods of this class below
    #
    # NOTE: USE this class in the NEXT file, problem3.py.
    #         You do NOT need to write test cases for THIS file, problem2.py.

    def __init__(self, list_of_points):
        self.list_of_points = list_of_points
        self.get_lines()

    def get_lines(self):
        self.list_of_lines = []
        for a in range(len(self.list_of_points) - 1):
            line = rg.Line(self.list_of_points[a], self.list_of_points[a + 1])
            self.list_of_lines.append(line)
        line = rg.Line(self.list_of_points[len(self.list_of_points) - 1], self.list_of_points[0])
        self.list_of_lines.append(line)

    def set_outline_color(self, color):
        for a in range(len(self.list_of_lines)):
            self.list_of_lines[a].color = color

    def attach_to(self, window):
        for a in range(len(self.list_of_lines)):
            self.list_of_lines[a].attach_to(window)

    def sub_polygon(self):
        list_of_points = []
        for a in range(len(self.list_of_lines)):
            list_of_points.append(self.list_of_lines[a].get_midpoint())
        newPolygon = Polygon(list_of_points)
        return newPolygon



