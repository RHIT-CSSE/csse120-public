"""
Capstone Team Project.  Code to run on a ROBOT (NOT a laptop).

This module is for testing STAND-ALONE code running on the ROBOT
(WITHOUT having LAPTOP GUI code running on the LAPTOP at the same time).

Authors:  Your professors (for the framework)
    and PUT_YOUR_NAME_HERE.
Fall term, 2019-2020.
"""
# TODO: 1.  Put your name in the above.

import rosebot
import time


def main():
    """ Calls the desired TEST functions. """
    test_arm_and_claw()


def test_arm_and_claw():
    """ Test a robot's ARM and CLAW. """
    print()
    print('--------------------------------------------------')
    print('Testing the  ARM_AND_CLAW  of a robot:')
    print('--------------------------------------------------')

    # -------------------------------------------------------------------------
    # Get the arm speed for this set of tests.
    # -------------------------------------------------------------------------
    print("Arm speed should be an integer between 1 and 100.")
    arm_speed = int(input("Enter an integer for arm speed: "))

    # -------------------------------------------------------------------------
    # TODO: 2. Construct a robot, that is, a rosebot.RoseBot() object.
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # Test the  RAISE_ARM  method of the  arm_and_claw  of the robot:
    # -------------------------------------------------------------------------
    print()
    print("Testing the  RAISE_ARM  method")
    print(" of the  ARM_AND_CLAW  of the robot.")
    input("Press the ENTER key when ready for the arm to start moving.")

    # -------------------------------------------------------------------------
    # TODO: 3. Call the  raise_arm  method of the   arm_and_claw   of the robot.
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # Test the  CALIBRATE_ARM  method of the  arm_and_claw  of the robot:
    # -------------------------------------------------------------------------
    print()
    print("Testing the  CALIBRATE_ARM  method")
    print(" of the  ARM_AND_CLAW  of the robot.")
    input("Press the ENTER key when ready for the arm to start moving.")

    # -------------------------------------------------------------------------
    # TODO: 4. Call the  calibrate_arm  method of the   arm_and_claw
    #  of the robot, first using the input arm_speed,
    #  then (after a short pause) using the default arm speed.
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # Test the  MOVE_ARM_TO_POSITION  method of the  arm_and_claw  of the robot:
    # -------------------------------------------------------------------------
    print()
    print("Testing the  MOVE_ARM_TO_POSITION  method")
    print(" of the  ARM_AND_CLAW  of the robot.")

    print("Enter an integer for the position to which")
    desired_position = int(input("to move the arm (0 to about 5100: "))
    input("Press the ENTER key when ready for the arm to start moving.")

    # -------------------------------------------------------------------------
    # TODO: 5. Call the  move_arm_to_position  method of the   arm_and_claw
    #  of the robot, using the input position and input speed.
    #  Then (after a short pause) call it again, moving to position 0
    #  this time, at the default speed.  Then (after a short pause) call it
    #  once more, this time to position 5000.
    #  Finally, after another short pause, reset to False the instance variable
    #  that indicates whether or not the arm has been calibrated, then call
    #  move_arm_to_position(2000), confirming that it FIRST does a calibration.
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # Test the  LOWER_ARM  method of the  arm_and_claw  of the robot:
    # -------------------------------------------------------------------------
    print()
    print("Testing the  LOWER_ARM  method")
    print(" of the  ARM_AND_CLAW  of the robot.")
    input("Press the ENTER key when ready for the arm to start moving.")

    # -------------------------------------------------------------------------
    # TODO: 6. Call the  lower_arm  method of the   arm_and_claw
    #  of the robot, using the default arm speed.
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # TODO: 7. Add additional tests as needed to ensure that the arm_and_claw
    #  methods are working correctly.
    # -------------------------------------------------------------------------


main()
