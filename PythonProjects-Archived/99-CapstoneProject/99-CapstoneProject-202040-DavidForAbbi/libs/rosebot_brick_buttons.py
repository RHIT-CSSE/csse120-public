"""
Capstone Team Project.  Code to run on a ROBOT (NOT a laptop).

This code defines the   BrickButtons  class  that controls
the physical buttons on the front of the EV3 brick.

Authors:  Your professors (for the framework)
    and PUT_YOUR_NAME_HERE.
Winter term, 2019-2020.
"""
###############################################################################
# STUDENTS: This module is ALREADY IMPLEMENTED.
#   READ its code so that you know how to use the Buttons on the Brick
#   if you wish to do so.  You may also AUGMENT this module if you choose.
###############################################################################
import libs.rosebot_ev3dev_api as ev3dev
import time


###############################################################################
#    BrickButtons
###############################################################################
class BrickButtons(object):
    """
    Methods for the BrickButtons on the robot.
    """
    def __init__(self):
        """
        Constructs the underlying low-level version of this brick buttons.
        """
        self._low_level_buttons = ev3dev.LowerLevelBrickButtons()

    def is_up_pressed(self):
        """
        Returns True if the Up button on the EV3 is pressed,
        else returns False.
          :rtype: bool
        """
        return self._low_level_buttons.up()

    def is_down_pressed(self):
        """
        Returns True if the Down button on the EV3 is pressed,
        else returns False.
          :rtype: bool
        """
        return self._low_level_buttons.down()

    def is_left_pressed(self):
        """
        Returns True if the Left button on the EV3 is pressed,
        else returns False.
          :rtype: bool
        """
        return self._low_level_buttons.left()

    def is_right_pressed(self):
        """
        Returns True if the Right button on the EV3 is pressed,
        else returns False.
          :rtype: bool
        """
        return self._low_level_buttons.right()

    def is_backspace_pressed(self):
        """
        Returns True if the Backspace button on the EV3 is pressed,
        else returns False.
          :rtype: bool
        """
        return self._low_level_buttons.backspace()
