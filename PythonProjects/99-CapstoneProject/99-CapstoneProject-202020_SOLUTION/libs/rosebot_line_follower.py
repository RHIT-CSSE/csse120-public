"""
Capstone Team Project.  Code to run on the EV3 robot (NOT on a laptop).

This code defines the LineFollower class.  The LineFollower uses the
reflected light intensity to drive the robot.

Authors:  Your professors (for the framework)
    and PUT_YOUR_NAMES_HERE.
Winter term, 2019-2020.
"""
# TODO: Put the name of EACH team member who contributes
#   to this module in the above.

import time
import rosebot_ev3dev_api as rose_ev3
import rosebot_color_sensor
import rosebot_drive_system


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
          :type color_sensor: rosebot_color_sensor.ColorSensor
          :type drive_system: rosebot_drive_system.DriveSystem
        """
        # ---------------------------------------------------------------------
        # TODO: With your instructor, implement this method.
        # ---------------------------------------------------------------------
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
        print("Place the robot on a white surface.")
        input("Press the ENTER key when you are ready to take the white_reading.")
        # ---------------------------------------------------------------------
        # TODO: Implement the rest of method.
        # ---------------------------------------------------------------------

        # Solution to be removed.
        self.white_reading = self.color_sensor.get_reflected_light_intensity()
        print("Place the robot on a black surface.")
        input("Press the ENTER key when you are ready to take the black_reading.")
        self.black_reading = self.color_sensor.get_reflected_light_intensity()

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
        # ---------------------------------------------------------------------
        # TODO: Implement this method.
        # ---------------------------------------------------------------------

        # Solution to be removed
        start_time_s = time.time()
        turn_intensity = 5  # Greater values do sharper turns
        light_threshold = (self.white_reading + self.black_reading) / 2
        while True:
            time.sleep(0.05)
            light_amount = self.color_sensor.get_reflected_light_intensity()
            if time.time() > start_time_s + duration_s:
                break
            if light_amount < light_threshold:
                # Robot on black
                self.drive_system.go(max_speed / turn_intensity, max_speed)
            else:
                # Robot on white
                self.drive_system.go(max_speed, max_speed)
        self.drive_system.stop()

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
        # ---------------------------------------------------------------------
        # TODO: Implement this method.
        # Hint towards implementing the duration_s requirement...
        # start_time_s = time.time()
        # while True:
        #     time.sleep(0.05)
        #     if time.time() > start_time_s + duration_s:
        #         break
        # ---------------------------------------------------------------------

        # Solution to be removed
        start_time_s = time.time()
        turn_intensity = 3  # Greater values do sharper turns
        light_threshold = (self.white_reading + self.black_reading) / 2
        is_checking_left = True
        checking_start_time_s = 0
        max_checking_time_s = 6
        while True:
            time.sleep(0.05)
            light_amount = self.color_sensor.get_reflected_light_intensity()
            if time.time() > start_time_s + duration_s:
                break
            if light_amount < light_threshold:
                is_checking_left = True  # Always check left first
                # The initial left check should be for *half* the max duration
                checking_start_time_s = time.time() + max_checking_time_s / 2
                self.drive_system.go(max_speed, max_speed)
            else:
                if is_checking_left:
                    self.drive_system.go(max_speed / turn_intensity, -max_speed / turn_intensity)
                else:
                    self.drive_system.go(-max_speed / turn_intensity, max_speed / turn_intensity)
                if time.time() > checking_start_time_s + max_checking_time_s:
                    is_checking_left = not is_checking_left
                    checking_start_time_s = time.time()

        self.drive_system.stop()
