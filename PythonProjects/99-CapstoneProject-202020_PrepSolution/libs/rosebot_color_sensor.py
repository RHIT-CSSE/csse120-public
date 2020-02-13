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
        self.sensor = rose_ev3.ColorSensor(port)

    def get_color(self):
        """
        Returns the color detected by the sensor, as best the sensor can judge
        from shining red, then green, then blue light and measuring the
        intensities returned.  The returned value is a string:
          - No Color, Black, Blue, Green, Yellow, Red, White, Brown
        :rtype: str
        """
        # ---------------------------------------------------------------------
        # TODO: With your instructor, implement this method.
        # ---------------------------------------------------------------------
        self.sensor.get_color()

    def wait_for_color(self, color):
        """
        Sits in a loop, sleeping 0.05 seconds each time through the loop,
        waiting for the given color (as a string) to be detected.
        The string can be in any case (lower, upper or mixed), e.g. BLaCk.
          :type color: str
        """
        # ---------------------------------------------------------------------
        # TODO: Implement this method.
        # ---------------------------------------------------------------------
        target_color = color.lower()
        while True:
            time.sleep(0.05)
            if target_color == self.sensor.get_color().lower():
                break

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
        return self.sensor.get_reflected_light_intensity()
