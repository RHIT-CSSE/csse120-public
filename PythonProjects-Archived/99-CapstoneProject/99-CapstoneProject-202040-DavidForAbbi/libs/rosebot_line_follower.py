"""
Capstone Team Project.  Code to run on the EV3 robot (NOT on a laptop).

This code defines the LineFollower class which is used to follow a black line
by using the downward-facing Color Sensor.

Authors:  Your professors (for the framework)
    and PUT_YOUR_NAMES_HERE.
Winter term, 2019-2020.
"""
# TODO: Put the name of EACH team member who contributes
#   to this module in the above.

import time
import libs.rosebot_ev3dev_api as ev3dev
import libs.rosebot_color_sensor as color
import libs.rosebot_drive_system as drive


###############################################################################
# STUDENTS: OPTIONALLY, extend the code in this module to contain methods like
#   those specified below.
###############################################################################


###############################################################################
#    LineFollower
###############################################################################
class LineFollower(object):
    """
    Methods using the reflected light intensity to drive the robot.
    """

    def __init__(self, color_sensor, drive_system):
        """
        Constructs LineFollower to track black lines.
          :type color_sensor: color.ColorSensor
          :type drive_system: drive.DriveSystem
        """
        self.color_sensor = color_sensor
        self.drive_system = drive_system
        self.white_reading = 95  # Approximation until a calibration is done.
        self.black_reading = 5  # Approximation until a calibration is done.

    def calibrate(self):
        """
        Calibrates the white and black values for the given room conditions.
        Asks the user to place the robot on white first, then hit enter to
        take the reading.  Prints (and stores) the white_reading.  Then this
        method asks the user to place the robot on black, then hit enter to
        take the black reading.  Prints (and stores) the black_reading.
        """

    def follow_line_inside_ccw(self, max_speed, duration_s):
        """
        Makes the robot follow a line around in a circle.  In this version of
        line following the robot goes straight on white and does an arc left
        turn when on black.
         - White is might be 90+ values of the reflected light intensity
         - Black is might be as low as 5 on the reflected light intensity
        but here white is anything above light_threshold, otherwise black.
        This method should make the robot follow the inside of a line in a
        counter-clockwise direction at the given speed.
        After duration_s seconds have passed this method will stop both motors.
        :param max_speed: 1 to 100 value for the max wheel motor speed
        :type max_speed: int
        :param duration_s: How long to continue this action (in seconds)
        :type duration_s: float
        """

    def stay_on_line(self, max_speed, duration_s):
        """
        Makes the robot follow a arbitrary line that turns left and right.
        When the robot is on black it continues straight, but when the robot
        is on white it stops and looks (arcs left for a while, arcs right for
        while) to try to find the line.  Once the line is found again it
        continues moving forward.
        After duration_s seconds have passed this method will stop both motors.
        :param max_speed: 1 to 100 value for the max wheel motor speed
        :type max_speed: int
        :param duration_s: How long to continue this action (in seconds)
        :type duration_s: float
        """
