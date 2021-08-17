"""
Capstone Team Project.  Code to run on a ROBOT (NOT a laptop).

This code defines the   Led  and  Leds   classes  that control
the physical LEDs on the EV3 brick.

Authors:  Your professors (for the framework)
    and PUT_YOUR_NAME_HERE.
Winter term, 2019-2020.
"""
# TODO: 1. In the above, put the names of EACH team member who contributes
#  (in any way) to this module.

# -----------------------------------------------------------------------------
# TODO: 2. Note that this module uses a library from LIBS:
#  This module uses code that is in the "low-level" api in rosebot_ev3dev_api.
#  Change this _TODO_ to DONE after you have seen how to do it.
# -----------------------------------------------------------------------------
import libs.rosebot_ev3dev_api as ev3dev
import time


###############################################################################
#    Led  (a class for a SINGLE LED).
###############################################################################
class Led(object):
    """ A red-green LED. """
    def __init__(self, left_or_right):
        """
        Stores whether the LED is the one on the left ("left")
        or the one on the right ("right").

        :type left_or_right: str
          Must be "left" or "right"
        """
        # ---------------------------------------------------------------------
        # TODO: 3. Read the following, ASKING QUESTIONS AS NEEDED.
        #  Once you understand the code, change this _TODO_ to DONE.
        # ---------------------------------------------------------------------
        self._low_level_led = ev3dev.LowerLevelLed(left_or_right)
        self.left_or_right = left_or_right

    def set_color(self, color, percent_intensity=100):
        self._low_level_led.set_color(color, percent_intensity)

    def off(self):
        self._low_level_led.set_color("off")


###############################################################################
#    LEDs
###############################################################################
class Leds(object):
    """
    Controls the two red-green LEDs on the front of the EV3 brick.
    """

    # -------------------------------------------------------------------------
    # NOTE:
    #   These 2 LEDs are RG leds, meaning they are really a red and a green LED
    #   on the left side and a red and a green LED on the right side.
    # -------------------------------------------------------------------------

    def __init__(self):
        """
        Constructs two LED objects (for the left and right leds).
          """
        # ---------------------------------------------------------------------
        # TODO: With your instructor, implement this method.
        # ---------------------------------------------------------------------
        self.left = Led("left")
        self.right = Led("right")

    def turn_off(self):
        """ Turns both LEDs off. """
        # ---------------------------------------------------------------------
        # TODO: Implement this method.
        # ---------------------------------------------------------------------
        self.left.off()
        self.right.off()

    def set_color(self, side, color_name):
        """
          Sets the LEDs, based on the side requested and the color_name.
          Valid side values:
            "left" --> This command will effect only the left LED
            "right" --> This command will effect only the right LED
            "both" --> This command will effect both the left and right LEDs
          Valid color_names include "off", "red", "green", or "amber"
            "red" --> the red LED is on, the green LED is off
            "green" --> the red LED is off, the green LED is on
            "amber" --> the red LED is on, the green LED is on
            "off" --> the red LED is off, the green LED is off
        """
        # ---------------------------------------------------------------------
        # TODO: Implement this method.
        # ---------------------------------------------------------------------
        if side == "left":
            sensors = [self.left]
        elif side == "right":
            sensors = [self.right]
        else:
            sensors = [self.left, self.right]
        for sensor in sensors:
            sensor.set_color(color_name)
