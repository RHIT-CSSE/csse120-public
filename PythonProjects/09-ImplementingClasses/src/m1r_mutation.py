"""
This module demonstrates MUTATION and RE-ASSIGNMENT.

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher, Mark Hays,
         Derek Whitley, their colleagues, and PUT_YOUR_NAME_HERE.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

##############################################################################
# TODO: 2. Read the code, then run it.
#   Make sure you understand WHY it prints what it does.
#   ** ASK QUESTIONS IF ANY OF IT IS MYSTERIOUS TO YOU. **
#   Once you understand the code completely, then change the _TODO_ to DONE.
###############################################################################


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


def main():
    point1 = Point(10, 20)
    point2 = Point(30, 40)
    print()
    print("Point1 before:", point1.x, point1.y)
    print("Point2 before:", point2.x, point2.y)

    point3 = blah(point1, point2)
    print()
    print("Point1 after:", point1.x, point1.y)
    print("Point2 after:", point2.x, point2.y)
    print("Point3 after:", point3.x, point3.y)


def blah(one_point, another_point):
    one_point.x = 111
    third_point = one_point
    one_point = Point(88, 99)
    another_point.x = 333
    another_point = one_point
    fourth_point = third_point
    fourth_point.y = 555

    print()
    print("one_point inside:", one_point.x, one_point.y)
    print("another_point inside:", another_point.x, another_point.y)
    print("third_point inside:", third_point.x, third_point.y)
    print("fourth_point inside:", fourth_point.x, fourth_point.y)

    return fourth_point


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
