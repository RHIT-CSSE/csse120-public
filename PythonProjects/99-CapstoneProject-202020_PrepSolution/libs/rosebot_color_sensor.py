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

    def get_reading(self):
        """
        Returns the color detected by the sensor, as best the sensor can judge
        from shining red, then green, then blue light and measuring the
        intensities returned.  The returned value is a string:
          - 0: No Color
                  (that is, cannot classify the color as one of the following)
          - 1: Black
          - 2: Blue
          - 3: Green
          - 4: Yellow
          - 5: Red
          - 6: White
          - 7: Brown
        :rtype: str
        """
        # ---------------------------------------------------------------------
        # TODO: With your instructor, implement this method.
        # ---------------------------------------------------------------------
        self.sensor.get_color()

    def wait_for_color(self, color):
        """
        Sits in a loop, sleeping 0.05 seconds each time through the loop,
        waiting for the given color (as an string) to be detected.
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
