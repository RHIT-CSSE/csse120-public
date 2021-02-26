"""
Test 3, problem 3.

Authors: Mark Hays, Amanda Stouder, their colleagues,
         and PUT YOUR NAME HERE.  January 2015.
"""  # TODO: PUT YOUR NAME IN THE ABOVE LINE.


# import problem2 as p2
import tests.problem2 as p2
import rosegraphics as rg

def main():
    """ Calls the   TEST   functions in this module. """
    test_problem3()

def test_problem3():
    """Creates shapes and displays them on the screen."""
    # This code is ALREADY written for you. Write your code
    # in the NEXT function, problem3(), below.

    # rectangle tunnel
    window = rg.RoseWindow(400, 400)
    points = [rg.Point(10, 10), rg.Point(10, 350), rg.Point(390, 350), rg.Point(390, 10)]
    colors = ["red", "black", "white"]
    problem3(window, points, 3, colors)
    window.render()
    window.close_on_mouse_click()

    # triangle tunnel
    window = rg.RoseWindow(400, 400)
    points = [rg.Point(200, 10), rg.Point(100, 310), rg.Point(400, 110)]
    colors = ["red", "white", "black"]
    problem3(window, points, 5, colors)
    window.render()
    window.close_on_mouse_click()

    # pentagon tunnel
    window = rg.RoseWindow(400, 400)
    points = [rg.Point(200, 10), rg.Point(0, 110), rg.Point(100, 310), rg.Point(300, 310), rg.Point(400, 110)]
    colors = ["red", "orange", "yellow", "lightgreen", "blue", "purple"]
    problem3(window, points, 20, colors)
    window.render()
    window.close_on_mouse_click()

def problem3(window, points, n, colors):
    """
    See problem3.pdf and the related problem2.py.
    
    Constructs a "tunnel" of exactly n p2.Polygons.
    - The first polygon (k=1) is the biggest and constructed from the given points.
    - The kth polygon is the sub-polygon of the k-1th polygon; that is,
        the points of the kth polygon are the midpoints of the lines of the 
        k-1th polygon.
    
    The first polygon is drawn with the first color in the given
    sequence of colors, the next polygon with the next color in that
    sequence, and so forth.  If the list of colors is exhausted,
    the colors to be used 'wrap' in the list.
    
    """
    # TODO: implement and test this function
    list_of_polygons = []
    polygon = p2.Polygon(points)
    polygon.set_outline_color(colors[0])
    # list_of_polygons.append(polygon) # BUG
    for a in range(1, n):
        polygon = polygon.sub_polygon()
        polygon.set_outline_color(colors[a % len(colors)])
        list_of_polygons.append(polygon)
    for b in range(len(list_of_polygons)):
        list_of_polygons[b].attach_to(window)




#-----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
#-----------------------------------------------------------------------
if __name__ == '__main__':
    main()
