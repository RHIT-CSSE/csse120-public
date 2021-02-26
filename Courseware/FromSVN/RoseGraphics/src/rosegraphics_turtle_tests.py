"""
Tests the Turtle classes (in their various forms) in Rosegraphics.

Authors: David Mutchler, November 2015.
"""

import rosegraphics as rg
import unittest


class TurtleTest(unittest.TestCase):

    def setUp(self):
        self.window = rg.TurtleWindow()
        self.window.delay(10)  # Bigger numbers mean slower animation.

        self.turtle1 = rg.SimpleTurtle()
        self.turtle1.pen = rg.Pen('red', 5)
        self.turtle2 = rg.SimpleTurtle(shape='turtle')

    def tearDown(self):
        self.window.close_on_mouse_click()

#     def testMovement(self):
#         """ Should draw squares and triangles. """
#         self.turtle2.go_to(rg.Point(-50, 50))
#
#         # Squares by turtle1 and turtle2.
#         for t in (self.turtle1, self.turtle2):
#             for _ in range(4):
#                 t.forward(100)
#                 t.left(90)
#
#         # Triangles by turtle1 and turtle2, taking turns with their movements.
#         for _ in range(3):
#             self.turtle1.right(120)
#             self.turtle2.left(-120)
#             self.turtle1.forward(-300)
#             self.turtle2.backward(300)
#
#     def testPen(self):
#         """ Should draw a thick blue line, followed by a thin red one. """
#         self.turtle1.pen = rg.Pen('blue', 10)
#         self.turtle1.forward(100)
#         self.turtle1.pen = rg.Pen('red', 1)
#         self.turtle1.forward(100)
#
#     def testPenUpDown(self):
#         """ Should draw a blue line, then continue, then a red line. """
#         self.turtle1.pen = rg.Pen('blue', 10)
#         self.turtle1.forward(100)
#         self.turtle1.pen_up()
#         self.turtle1.forward(100)
#         self.turtle1.pen_down()
#         self.turtle1.pen = rg.Pen('red', 1)
#         self.turtle1.forward(100)
#
#     def testPaintBucket(self):
#         """ Should draw a blue line, red filled square, blue line. """
#         self.turtle1.pen = rg.Pen('blue', 3)
#         self.turtle1.paint_bucket = rg.PaintBucket('red')
#         self.turtle1.forward(100)
#         self.turtle1.begin_fill()
#         for _ in range(4):
#             self.turtle1.left(90)
#             self.turtle1.forward(50)
#         self.turtle1.end_fill()
#
#         self.turtle1.right(90)
#         self.turtle1.forward(100)
#
#     def testDelay(self):
#         self.window.delay(1)
#         self.testMovement()
#         self.window.delay(10)
#         self.testMovement()

    def testSpeed(self):
        self.turtle1.speed = 1
        for _ in range(4):
            self.turtle1.left(90)
            self.turtle1.forward(50)

        self.turtle1.speed = 10
        self.turtle1.forward(100)
        for _ in range(4):
            self.turtle1.left(90)
            self.turtle1.forward(50)

        self.turtle1.speed = 5
        self.turtle1.forward(100)
        for _ in range(4):
            self.turtle1.left(90)
            self.turtle1.forward(50)

if __name__ == '__main__':
    unittest.main()
