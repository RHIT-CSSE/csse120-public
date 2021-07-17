"""
Capstone Team Project.  Code to run on the EV3 robot (NOT on a laptop).

This code defines the RemoteControl class, for the robot's remote
control that detects when the arm and claw are in the fully-up position.

Authors:  Your professors (for the framework)
    and PUT_YOUR_NAMES_HERE.
Winter term, 2019-2020.
"""
# TODO: Put the name of EACH team member who contributes
#   to this module in the above.


import rosebot_ev3dev_api as rose_ev3


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
        # TODO: With your instructor, implement this method.
        # ---------------------------------------------------------------------

    def is_up_pressed(self):
        """
        Returns True if this Up button on the EV3 is pressed, else returns False.
          :rtype: bool
        """
        # ---------------------------------------------------------------------
        # TODO: Implement this method.
        # ---------------------------------------------------------------------

    def is_down_pressed(self):
        """
        Returns True if this Down button on the EV3 is pressed, else returns False.
          :rtype: bool
        """
        # ---------------------------------------------------------------------
        # TODO: Implement this method.
        # ---------------------------------------------------------------------

    def is_left_pressed(self):
        """
        Returns True if this Left button on the EV3 is pressed, else returns False.
          :rtype: bool
        """
        # ---------------------------------------------------------------------
        # TODO: Implement this method.
        # ---------------------------------------------------------------------

    def is_right_pressed(self):
        """
        Returns True if this Right button on the EV3 is pressed, else returns False.
          :rtype: bool
        """
        # ---------------------------------------------------------------------
        # TODO: Implement this method.
        # ---------------------------------------------------------------------

    def is_backspace_pressed(self):
        """
        Returns True if this Backspace button on the EV3 is pressed, else returns False.
          :rtype: bool
        """
        # ---------------------------------------------------------------------
        # TODO: Implement this method.
        # ---------------------------------------------------------------------
