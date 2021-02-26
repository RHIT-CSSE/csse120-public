'''
Created on Nov 29, 2012

@author: mutchler
'''
import unittest
import rosegraphics as rg


class ShapeTest(unittest.TestCase):
    """
    Tests a Shape class that is determined by the class variable
      start_shape
    which the subclass should set (overriding its setting to None here).
    """
    # TODO: Make these real tests (not just draws and prints).
    start_shape = None
    speed = 1  # bigger numbers mean render with less wait

    shapes_to_draw = 5
    colors = ('red', None, 'blue', 'white', 'black')
    arrow_values = (None, 'last', 'first', 'both', None)

    def test(self):
        if not self.start_shape:
            return

        title = 'Testing {}'.format(self.start_shape.__class__.__name__)
        window = rg.RoseWindow(800, 600, title=title)

        shapes = self.simple_shapes(window)

        this_class = self.start_shape.__class__

        if issubclass(this_class, rg._ShapeWithCenter):
            self.move_centers(shapes, window)

        if issubclass(this_class, rg._ShapeWithOutline):
            self.fills_and_outlines(shapes, window)
        elif issubclass(this_class, rg._ShapeWithThickness):
            self.colors_and_thicknesses(shapes, window)
        elif issubclass(this_class, rg._ShapeWithText):
            self.text_attributes(shapes, window)

        if issubclass(this_class, rg._RectangularShape):
            self.rectangular_getters(shapes)

    def simple_shapes(self, window):
        shapes = []
        shape = self.start_shape
        for _ in range(self.shapes_to_draw):
            print(shape)
            shape.attach_to(window)
            shapes.append(shape)
            window.render(0.5 / self.speed)

            shape = shape.clone()
            shape.move_by(100, 50)

        window.continue_on_mouse_click()

        for shape in shapes:
            shape.detach_from(window)
            window.render(0.5 / self.speed)

        window.continue_on_mouse_click()

        return shapes

    def move_centers(self, shapes, window):
        for k in range(len(shapes)):
            shapes[k].attach_to(window)
            window.render(2.0 / self.speed)
            new_center = shapes[k].center.clone()
            new_center.move_by(50, 20)
            shapes[k].move_center_to(new_center.x, new_center.y)
            window.render(0.5 / self.speed)

        window.continue_on_mouse_click()

        for shape in shapes:
            shape.detach_from(window)
            window.render(0.5 / self.speed)

        window.continue_on_mouse_click()

        return shapes

    def fills_and_outlines(self, shapes, window):
        for k in range(self.shapes_to_draw):
            shapes[k].fill_color = self.colors[k % len(self.colors)]
            shapes[k].attach_to(window)
            window.render(0.2 / self.speed)

        window.continue_on_mouse_click()

        for k in range(self.shapes_to_draw):
            shapes[k].fill_color = None
            shapes[k].outline_color = self.colors[k % len(self.colors)]
            shapes[k].outline_thickness = (k + 1) * 3
            window.render(0.2 / self.speed)

        window.close_on_mouse_click()

    def colors_and_thicknesses(self, shapes, window):
        for k in range(self.shapes_to_draw):
            shapes[k].color = self.colors[k % len(self.colors)]
            shapes[k].attach_to(window)
            window.render(0.2 / self.speed)

        window.continue_on_mouse_click()

        for k in range(self.shapes_to_draw):
            shapes[k].color = self.colors[k % len(self.colors)]
            shapes[k].thickness = (k + 1) * 5
            window.render(0.2 / self.speed)

        window.continue_on_mouse_click()

        for k in range(self.shapes_to_draw):
            shapes[k].thickness = 5
            shapes[k].arrow = self.arrow_values[k % len(self.arrow_values)]
            window.render(0.2 / self.speed)

        window.continue_on_mouse_click()

        for k in range(self.shapes_to_draw):
            temp = shapes[k].start.clone()
            shapes[k].start = shapes[k].end.clone()
            shapes[k].end = temp
            shapes[k].thickness = 5
            shapes[k].arrow = self.arrow_values[k % len(self.arrow_values)]
            window.render(0.2 / self.speed)

        window.close_on_mouse_click()

    def text_attributes(self, shapes, window):
        """ Not yet implemented. """
        pass

    def rectangular_getters(self, shapes):
        for shape in shapes:
            print()
            print(shape)
            print('upper-left corner: ', shape.get_upper_left_corner())
            print('lower-left corner: ', shape.get_lower_left_corner())
            print('upper-right corner:', shape.get_upper_right_corner())
            print('lower-right corner:', shape.get_lower_right_corner())
            print('center:            ', shape.get_center())
            print('width:  ', shape.get_width())
            print('height: ', shape.get_height())
            print('bounding box:')
            print(shape.get_bounding_box())


class ShapesTest(unittest.TestCase):
    """
    Runs tests for the Shapes specified in the class variable
      shapes
    below.
    """
    shapes = (rg.Rectangle(rg.Point(50, 100), rg.Point(70, 140)),
              rg.Ellipse(rg.Point(50, 100), rg.Point(70, 140)),
              rg.Circle(rg.Point(50, 100), 30),
              rg.Square(rg.Point(50, 100), 30),
              rg.Point(50, 100),
              rg.Line(rg.Point(50, 100), rg.Point(70, 140)))
    speed = 10

    def test(self):
        testcase = ShapeTest()
        testcase.speed = ShapesTest.speed
        for shape in ShapesTest.shapes:
            testcase.start_shape = shape
            testcase.test()


# class CircleTest(ShapeTest):
#     start_shape = rg.Circle(rg.Point(50, 100), 30)
#     speed = 10
#
#
# class EllipseTest(ShapeTest):
#     start_shape = rg.Ellipse(rg.Point(50, 100), 20, 40)
#     speed = 10
#
#
# class LineTest(ShapeTest):
#     start_shape = rg.Line(rg.Point(50, 100), rg.Point(70, 140))
#
#
# class PointTest(ShapeTest):
#     start_shape = rg.Point(50, 100)
#     speed = 1
#
#
# class SquareTest(ShapeTest):
#     start_shape = rg.Square(rg.Point(50, 100), 30)
#     speed = 10
#
#
# class RectangleTest(ShapeTest):
#     start_shape = rg.Rectangle(rg.Point(50, 100), 20, 40)
#     speed = 10

if __name__ == '__main__':
    unittest.main()
