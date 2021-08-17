"""
Capstone Team Project.  Code to run on a ROBOT (NOT a laptop).

This module is for testing STAND-ALONE code running on the ROBOT
(WITHOUT having LAPTOP GUI code running on the LAPTOP at the same time).

Authors:  Your professors (for the framework)
    and PUT_YOUR_NAME_HERE.
Winter term, 2019-2020.
"""
# TODO: 1.  Put your name in the above.

import time
import rosebot


def main():
    """ Test a robot's color sensor and line following. """
    print()
    print('--------------------------------------------------')
    print('Testing the Color sensor (in two modes) of a robot')
    print('--------------------------------------------------')

    # -------------------------------------------------------------------------
    # TODO: 2. Construct a robot, that is, a rosebot.RoseBot() object.
    # -------------------------------------------------------------------------
    robot = rosebot.RoseBot()

    # -------------------------------------------------------------------------
    # STUDENTS: Do the work in this module as follows.
    #   Otherwise, you will be overwhelmed by the number of tests happening.
    #
    #   For each function that you implement:
    #     1. Locate the statements just below this comment that call TEST functions.
    #     2. UN-comment only one test at a time.
    #     3. Implement that function per its _TODO_.
    #     4. Implement as needed the appropriate class methods
    #     5. When satisfied with your work, move onto the next test,
    #        RE-commenting out the previous test to reduce the testing.
    # -------------------------------------------------------------------------

    # Color Sensor tests
    # run_test_display_color_names(robot)
    # run_test_drive_until_color(robot)
    # run_test_display_reflected_light_readings(robot)
    # run_test_calibrate_line_follower(robot)
    run_test_line_follower(robot)


def run_test_display_color_names(robot):
    """
    Tests the  get_color_as_name and get_color_as_number methods of the color_sensor of the robot.
    """
    print('--------------------------------------------------')
    print('Testing the get_color_as_name and get_color_as_number methods of the ColorSensor class')
    print('--------------------------------------------------')
    while True:
        time.sleep(1.0)
        # -------------------------------------------------------------------------
        # TODO: 3. Use the  get_color_as_name  method of the  color_sensor
        #  of the robot AND the get_color_as_number method
        #  to display the color that the sensor is above (i.e. the
        #  color that the robot is sitting on).
        #  Do 1 print each second as follows:
        #   Color name = White
        #   Color number = 6
        #   Color name = White
        #   Color number = 6
        #   Color name = Black
        #   Color number = 1
        #  Note the colors returned will be either:
        #   No Color, Black, Blue, Green, Yellow, Red, White, Brown
        # -------------------------------------------------------------------------

        # Solution to be removed
        # DAVE: I do not understand the above TODO.
        print("Color name =   {}.".format(
            robot.color_sensor.get_color_as_name()))
        print("Color number = {}.".format(
            robot.color_sensor.get_color_as_number()))


def run_test_drive_until_color(robot):
    """
    Tests the wait_for_color method of the color_sensor of the robot.
    """
    print('--------------------------------------------------')
    print('Testing the wait_for_color method of the ColorSensor class')
    print('--------------------------------------------------')
    print()
    print("Testing the  WAIT_UNTIL_COLOR  method")
    print(" of the  COLOR_SENSOR  of the robot.")
    input("Press the ENTER key when ready to wait until BLACK is sensed.")

    # -------------------------------------------------------------------------
    # TODO: 4. Start driving the robot forward at 35, 35 then...
    #  Call the  wait_until_color  method of the   color_sensor
    #  of the robot, checking to be sure that when it senses black
    #  (which you can simulate by lifting the robot).
    #  After black is seen stop the robot movement and then use an input
    #  to ask the user to press Enter to continue.
    # -------------------------------------------------------------------------

    # Solution to be removed.
    robot.drive_system.go(35, 35)
    robot.color_sensor.wait_for_color("black")
    robot.drive_system.stop()

    # -------------------------------------------------------------------------
    # TODO: 5. Add additional tests as needed to ensure that the wait_until_color  method
    #  works correctly with any of the 7 colors that it can sense.
    #  - Black, Blue, Green, Yellow, Red, White, Brown
    #  Test strings (upper, lower and mixed case).  Perhaps you could make a colors
    #  list and a loop to quickly test all colors.
    #  Consider using a statement like:
    #   input("Press the ENTER key when ready to wait until " + color + " is sensed.")
    # -------------------------------------------------------------------------

    # Solution to be removed.
    colors = ["Blue", "green", "YELLOW", "ReD", "White", "Brown"]
    for color in colors:
        input("Press the ENTER key when ready to wait until " + color + " is sensed.")
        robot.drive_system.go(35, 35)
        robot.color_sensor.wait_for_color(color)
        robot.drive_system.stop()


def run_test_display_reflected_light_readings(robot):
    """
    Tests the  get_reflected_light_intensity method of the color_sensor of the robot.
    """
    print('--------------------------------------------------')
    print('Testing the get_reflected_light_intensity method of the ColorSensor class')
    print('--------------------------------------------------')
    while True:
        time.sleep(1.0)
        # -------------------------------------------------------------------------
        # TODO: 6. Use the  get_reflected_light_intensity  method of the  color_sensor
        #  of the robot to display the amount of light that is reflected from the
        #  surface that is below the sensor. Do 1 print each second as follows:
        #   Reflected light percentage = 94
        #   Reflected light percentage = 95
        #   Reflected light percentage = 91
        #   Reflected light percentage = 17
        #   Reflected light percentage = 5
        #   Reflected light percentage = 3
        #   Reflected light percentage = 3
        #  Note: The returned value is from 0 to 100, but in practice more like 3-5 to 90+
        #  in our classroom lighting. Near 0 is no light (black), near 100 lots of
        #  light reflected (white).  Test on both white and black!
        # -------------------------------------------------------------------------

        # Solution to be removed
        print("Reflected light percentage = {}.".format(
            robot.color_sensor.get_reflected_light_intensity()))

        # -------------------------------------------------------------------------
        # TODO: 7. In addition to the number print either "White" or "Black" on the
        #   same line as the value.  For example:
        #   Reflected light percentage = 94  White
        #   Reflected light percentage = 95  White
        #   Reflected light percentage = 91  White
        #   Reflected light percentage = 17  Black
        #   Reflected light percentage = 5  Black
        #   Reflected light percentage = 3  Black
        #   Reflected light percentage = 3  Black
        # -------------------------------------------------------------------------


def run_test_calibrate_line_follower(robot):
    """
    Tests the   calibrate   method of the LineFollower  class.
    """
    print('--------------------------------------------------')
    print('Testing the  calibrate   method of LineFollower')
    print('--------------------------------------------------')

    while True:
        input("Press ENTER when ready to do a calibration.")
        # -------------------------------------------------------------------------
        # TODO: 8. Call the  calibrate  method of the  line_follower    of the robot.
        #  After the calibration print the white_reading and the black_reading.
        #  Additionally print a good threshold value to use that is the average of
        #  the two numbers that could be used to decide if the reading is white or
        #  black.
        # -------------------------------------------------------------------------

        # Solution to be removed
        robot.line_follower.calibrate()
        black = robot.line_follower.black_reading
        white = robot.line_follower.white_reading
        average = (black + white) // 2
        print("Black, White, Average: {:3} {:3} {:3}.".format(
            black, white, average))

        # -------------------------------------------------------------------------
        # TODO: 9. After running this step update the initial white_reading and
        # black_reading values set in  LineFollower __init__
        # They won't be perfect since rooms change, but they should work ok.
        # -------------------------------------------------------------------------


def run_test_line_follower(robot):
    """
    Tests the   follow_line_inside_ccw   method of the LineFollower  class.
    """
    print('--------------------------------------------------')
    print('Testing the  follow_line_inside_ccw   methods of the LineFollower')
    print('--------------------------------------------------')
    while True:
        print()
        speed = int(input("Enter an integer for the max wheel speed (1 to 100): "))
        if speed == 0:
            break
        duration_s = int(input("How long would you like to follow the line (seconds)? "))
        if duration_s == 0:
            break
        input("Press the ENTER key when ready for the robot to start moving.")

        # -------------------------------------------------------------------------
        # TODO: 10. Call the follow_line_inside_ccw   method of the   line_follower   of the robot
        # -------------------------------------------------------------------------

        # Solution to be removed
        robot.line_follower.follow_line_inside_ccw(speed, duration_s)

        # -------------------------------------------------------------------------
        # TODO: 11. Optional
        #  Call the stay_on_line   method of the   line_follower   of the robot to
        #  see if you could follow any arbitrary line the turns left and right.
        # -------------------------------------------------------------------------


main()
