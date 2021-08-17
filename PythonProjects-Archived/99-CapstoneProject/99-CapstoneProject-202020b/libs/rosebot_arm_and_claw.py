"""
Capstone Team Project.  Code to run on the EV3 robot (NOT on a laptop).

This code defines the ArmAndClow class, for making the arm move and claw grasp.

Authors:  Your professors (for the framework)
    and PUT_YOUR_NAMES_HERE.
Winter term, 2019-2020.
"""
# TODO: Put the name of EACH team member who contributes
#   to this module in the above.

import rosebot_ev3dev_api as rose_ev3
import time


###############################################################################
#    ArmAndClaw
###############################################################################
class ArmAndClaw(object):
    """ Controls the robot's arm and claw (which operate together). """

    # -------------------------------------------------------------------------
    # NOTE:
    #   A POSITIVE speed for the ArmAndClaw's motor moves the arm UP.
    #   A NEGATIVE speed for the ArmAndClaw's motor moves the arm DOWN.
    #   It takes about   14 revolutions    of the ArmAndClaw's motor
    #     to go from all the way UP to all the way DOWN.
    # -------------------------------------------------------------------------

    def __init__(self, port, touch_sensor):
        """
        Stores the given touch sensor for stopping the Arm in its UP position.
        Constructs the Arm's motor.
          :type  port:  str   (must be 'A', 'B', 'C' or 'D')
          :type  touch_sensor:  rosebot_touch_sensor.TouchSensor
        """
        # Whenever using the arm motor always use a 100% duty cycle for the speed.
        self.SPEED = 100
        # ---------------------------------------------------------------------
        # TODO: With your instructor, implement this method.
        # ---------------------------------------------------------------------


    def calibrate_arm(self):
        """
        Calibrates its Arm, that is:
          1. Raises its Arm until it is all the way UP
               (i.e., its touch sensor is pressed)
          2. Lowers its Arm until it is all the way down
               (i.e., 14 motor revolutions),
          3. Resets the motor's position to 0.
        """
        # ---------------------------------------------------------------------
        # TODO: With your instructor, implement this method.
        # ---------------------------------------------------------------------


    def raise_arm(self):
        """ Raises the Arm until its touch sensor is pressed. """
        # ---------------------------------------------------------------------
        # TODO: Implement this method.
        # ---------------------------------------------------------------------


    def move_arm_to_position(self, desired_arm_position):
        """
        Move its Arm to the given position, where 0 means all the way DOWN.
        If the robot has not yet calibrated its ArmAndClaw, it does so first.
        """
        # ---------------------------------------------------------------------
        # TODO: Implement this method.
        # ---------------------------------------------------------------------


    def lower_arm(self):
        """
        Lowers the Arm until it is all the way down, i.e., position 0.
        If the robot has not yet calibrated its ArmAndClaw, it does so first.
        """
        # ---------------------------------------------------------------------
        # TODO: Implement this method.
        # ---------------------------------------------------------------------

