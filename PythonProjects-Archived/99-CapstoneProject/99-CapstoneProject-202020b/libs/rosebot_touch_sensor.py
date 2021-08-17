"""
Capstone Team Project.  Code to run on the EV3 robot (NOT on a laptop).

This code defines the TouchSensor class, for the robot's touch sensor
that detects when the arm and claw are in the fully-up position.

Authors:  Your professors (for the framework)
    and PUT_YOUR_NAMES_HERE.
Winter term, 2019-2020.
"""
# TODO: Put the name of EACH team member who contributes
#   to this module in the above.


import rosebot_ev3dev_api as rose_ev3
import time

###############################################################################
#    TouchSensor
###############################################################################
class TouchSensor(object):
    """
    Methods for the TouchSensor on the robot, including:
      get_reading    is_pressed    wait_until_pressed
    """
    def __init__(self, port):
        """
        Constructs the underlying low-level version of this sensor.
          :type port: int  (Must be 1, 2, 3 or 4)
        """
        # ---------------------------------------------------------------------
        # TODO: With your instructor, implement this method.
        # ---------------------------------------------------------------------

    def is_pressed(self):
        """
        Returns True if this TouchSensor is pressed, else returns False.
          :rtype: bool
        """
        # ---------------------------------------------------------------------
        # TODO: Implement this method.
        # ---------------------------------------------------------------------

    def wait_until_pressed(self):
        """
        Sits in a loop, sleeping 0.05 seconds each time through the loop,
        waiting for the touch sensor to be pressed.
        """
        # ---------------------------------------------------------------------
        # TODO: Implement this method.
        # ---------------------------------------------------------------------
