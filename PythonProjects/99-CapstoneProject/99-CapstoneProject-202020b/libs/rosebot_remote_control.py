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
import time

###############################################################################
#    RemoteControl
###############################################################################
class RemoteControl(object):
    """
    Methods for the RemoteControl on the robot, including:
      get_reading    is_pressed    wait_until_pressed
    """
    def __init__(self):
        """
        Constructs the underlying low-level versions of this RemoteControl.
        Creates a single instance variables named:
           remote_controls
        which is a list, in order, of the four possible remote control objects.
        """
        # ---------------------------------------------------------------------
        # TODO: With your instructor, implement this method.
        # ---------------------------------------------------------------------

    def is_pressed(self, channel, button_name):
        """
        Returns True if the requested button is pressed.
        Valid button_names:
          "red_up", "red_down", "blue_up", "blue_down"
          :rtype: bool
        """
        # ---------------------------------------------------------------------
        # TODO: Implement this method.
        # ---------------------------------------------------------------------

    def wait_until_pressed(self, channel, button):
        """
        Sits in a loop, sleeping 0.05 seconds each time through the loop,
        waiting for the requested button to be pressed
        """
        # ---------------------------------------------------------------------
        # TODO: Implement this method.
        # ---------------------------------------------------------------------
