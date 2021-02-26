import rosegraphics as rg
import traceback
import turtle


def main():
    """ Demonstrates some of the features of RoseGraphics. """
    turtles()
#     shapes()


def turtles():
    # ----------------------------------------------------------------------
    # Next two lines set up a Screen object for animation:
    # ----------------------------------------------------------------------
    window = turtle.Screen()
    window.delay(50)  # Bigger numbers mean slower animation.

    # ----------------------------------------------------------------------
    # Next two lines make two Turtle objects:
    # ----------------------------------------------------------------------
    nadia = rg.SimpleTurtle()
    akil = rg.SimpleTurtle('turtle')

    # ----------------------------------------------------------------------
    # Next lines ask the Turtle objects to do things:
    # ----------------------------------------------------------------------
    nadia.forward(100)
    nadia.left(90)
    nadia.forward(200)

    akil.right(45)
    akil.backward(50)
    akil.right(60)

    nadia.pen_up()
    nadia.forward(50)
    nadia.pen_down()
    nadia.left(135)
    nadia.backward(40)
#
#     # ----------------------------------------------------------------------
#     # Next lines set characteristics of the Turtle objects:
#     # ----------------------------------------------------------------------
#     nadia._newLine()  # Makes new pen characteristics NOT be retroactive.
#     nadia._pencolor = 'blue'
#     nadia._pensize = 10
#     nadia._speed = 10
#
#     akil._pencolor = 'red'
#     akil._pensize = 30
#     akil._speed = 1
#
#     akil.backward(100)
#     nadia.forward(100)
#
#     nadia.left(60)
#     nadia.forward(500)

    # ----------------------------------------------------------------------
    # Next line keeps the window open until the user clicks in the window:
    # ----------------------------------------------------------------------
    window.exitonclick()


def shapes():
    print("rg.Point.x=5 should give an error")
    try:
        rg.Point.x = 5
    except:
        print("Got the error!")
        traceback.print_exc()
        # raise

    # Demonstrates/tests the __repr__ methods:
    point1 = rg.Point(100, 200)
    point2 = rg.Point(300, 400)
    circle = rg.Circle(point1, 50)
    rectangle = rg.Rectangle(point1, point2)
    square = rg.Square(point1, 40)
    line = rg.Line(point1, point2)
    for shape in (point1, point2, circle, rectangle, square, line):
        print(shape)

    for shape in (circle, rectangle, square):
        shape.fill_color = 'red'
        shape.outline_color = 'blue'
        shape.outline_thickness = 5
    line.color = 'green'
    line.thickness = 10

    for shape in (point1, point2, circle, rectangle, square, line):
        print(shape)

    w = rg.RoseWindow(500, 300, 'hello')
    w.close_on_mouse_click()
    window1 = rg.RoseWindow(title='An empty window',
                            make_initial_canvas=False)

    window1.close_on_mouse_click()

    window2 = rg.RoseWindow(500, 300, 'Blue window with yellow canvas',
                            # window_color='blue', # Mark: I assume most students
                            # won't use this.
                            canvas_color='yellow')

    center = rg.Point(300, 100)
    circle = rg.Circle(center, 40)
    circle.attach_to(window2.initial_canvas)
    circle.fill_color = 'red'
    window2.render(1)
    circle.fill_color = ''
    print("Emptied the fill color.")
    print(window2.width, window2.height)
    window2.render()
    window2.get_next_mouse_click()

    center.move_by(-200, -50)
    circle = rg.Circle(center, 70)
    circle.attach_to(window2.initial_canvas)
    circle.fill_color = None

    print(window2.width, window2.height)
    window2.render()
    window2.close_on_mouse_click()

    window3 = rg.RoseWindow()

    p1 = rg.Point(100, 50)
    p2 = rg.Point(200, 90)

    rect = rg.Rectangle(p1, p2)
# rect.attach_to(window2.initial_canvas) # DCM: Two windows open,
# confusing.
    rect.attach_to(window3.initial_canvas)

    window3.render(1)

    rect.fill_color = 'red'
    center.attach_to(window3.initial_canvas)
    window3.render(1)

    center.move_by(50, 0)
    window3.render()

    window3.close_on_mouse_click()

main()
