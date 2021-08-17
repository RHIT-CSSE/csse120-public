"""
Capstone Team Project.  Code to run on a ROBOT (NOT a laptop).

This code defines the   BrickButtons  class  that controls
the physical buttons on the front of the EV3 brick.

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
        # ---------------------------------------------------------------------
        # TODO: 3. Read the following, ASKING QUESTIONS AS NEEDED.
        #  Once you understand the code, change this _TODO_ to DONE.
        # ---------------------------------------------------------------------
        self._low_level_buttons = ev3dev.LowerLevelBrickButtons()

    def is_up_pressed(self):
        """
        Returns True if this Up button on the EV3 is pressed, else returns False.
          :rtype: bool
        """
        # ---------------------------------------------------------------------
        # TODO: 4. Implement this method.
        # ---------------------------------------------------------------------
        return self._low_level_buttons.up()

    def is_down_pressed(self):
        """
        Returns True if this Down button on the EV3 is pressed, else returns False.
          :rtype: bool
        """
        # ---------------------------------------------------------------------
        # TODO: 5. Implement this method.
        # ---------------------------------------------------------------------
        return self._low_level_buttons.down()

    def is_left_pressed(self):
        """
        Returns True if this Left button on the EV3 is pressed, else returns False.
          :rtype: bool
        """
        # ---------------------------------------------------------------------
        # TODO: Implement this method.
        # ---------------------------------------------------------------------
        return self._low_level_buttons.left()

    def is_right_pressed(self):
        """
        Returns True if this Right button on the EV3 is pressed, else returns False.
          :rtype: bool
        """
        # ---------------------------------------------------------------------
        # TODO: Implement this method.
        # ---------------------------------------------------------------------
        return self._low_level_buttons.right()

    def is_backspace_pressed(self):
        """
        Returns True if this Backspace button on the EV3 is pressed, else returns False.
          :rtype: bool
        """
        # ---------------------------------------------------------------------
        # TODO: Implement this method.
        # ---------------------------------------------------------------------
        return self._low_level_buttons.backspace()