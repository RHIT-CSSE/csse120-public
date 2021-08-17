"""
Capstone Team Project.  Code to run on the EV3 robot (NOT on a laptop).

This code defines the ColorSensor class, for the robot's downward-facing
sensor that repeated shines right, green and blue light and measures the
intensity of the reflections.

Authors:  Your professors (for the framework)
    and PUT_YOUR_NAMES_HERE.
Winter term, 2019-2020.
"""
# TODO: Put the name of EACH team member who contributes
#   to this module in the above.

import rosebot_ev3dev_api as rose_ev3
import time


###############################################################################
#    ColorSensor
###############################################################################
class ColorSensor(object):
    """
    Methods for the downward-facing ColorSensor on the robot, including:
      get_reading    get_detected_color_name     wait_until_color
    """

    def __init__(self, port):
        """
        Constructs the underlying low-level ColorSensor.
          :type port: int
        """
        # ---------------------------------------------------------------------
        # TODO: With your instructor, implement this method.
        # ---------------------------------------------------------------------


    def get_color_as_name(self):
        """
        Returns the color detected by the sensor, as best the sensor can judge
        from shining red, then green, then blue light and measuring the
        intensities returned.  The returned value is a string:
          - No Color, Black, Blue, Green, Yellow, Red, White, Brown
        :rtype: str
        """
        # ---------------------------------------------------------------------
        # TODO: Implement this method.
        # ---------------------------------------------------------------------


    def get_color_as_number(self):
        """
        Returns the color detected by the sensor, as best the sensor can judge
        from shining red, then green, then blue light and measuring the
        intensities returned.  The returned value is a number:
          - 0 (No Color), 1 (Black), 2 (Blue),  3 (Green),
            4 (Yellow),   5 (Red),   6 (White), 7 (Brown)
        :rtype: int
        """
        # ---------------------------------------------------------------------
        # TODO: Implement this method.
        # ---------------------------------------------------------------------


    def wait_for_color(self, color):
        """
        Sits in a loop, sleeping 0.05 seconds each time through the loop,
        waiting for the given color (as a string) to be detected.
        The string can be in any case (lower, upper or mixed), e.g. BLaCk,
        but must be a string (NOT a number representing a string).
          :type color: str
        """
        # ---------------------------------------------------------------------
        # TODO: Implement this method.
        # ---------------------------------------------------------------------


    def get_reflected_light_intensity(self):
        """
        Shines red light and returns the intensity of the reflected light.
        The returned value is from 0 to 100,
        but in practice more like 3 to 90+ in our classroom lighting with our
        downward-facing sensor that is about 0.25 inches from the ground.
        :return: Amount of light reflected 0 (no light reflected) to 100 (super bright)
        :rtype: int
        """
        # ---------------------------------------------------------------------
        # TODO: Implement this method.
        # ---------------------------------------------------------------------

