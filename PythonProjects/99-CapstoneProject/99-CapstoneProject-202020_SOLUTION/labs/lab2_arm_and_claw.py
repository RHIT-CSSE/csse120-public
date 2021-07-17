"""
Capstone Team Project.  Code to run on a ROBOT (NOT a laptop).

This module is for testing STAND-ALONE code running on the ROBOT
(WITHOUT having LAPTOP GUI code running on the LAPTOP at the same time).

Authors:  Your professors (for the framework)
    and PUT_YOUR_NAME_HERE.
Winter term, 2019-2020.
"""
# TODO: 1.  Put your name in the above.

import rosebot
import time


def main():
    """ Test a robot's ARM AND CLAW. """
    print()
    print('--------------------------------------------------')
    print('Testing the  ARM AND CLAW  of a robot')
    print('--------------------------------------------------')

    # -------------------------------------------------------------------------
    # TODO: 2. Construct a robot, that is, a rosebot.RoseBot() object.
    # -------------------------------------------------------------------------
    robot = rosebot.RoseBot()

    # -------------------------------------------------------------------------
    # STUDENTS: Do the work in this module as follows.
    #   Otherwise, you will be overwhelmed by the number of tests happening.
    #
    #   For each function that you implement:
    #     1. Locate the statements just below this comment that call TEST functions.
    #     2. UN-comment only one test at a time.
    #     3. Implement that function per its _TODO_.
    #     4. Implement as needed the appropriate class methods
    #     5. When satisfied with your work, move onto the next test,
    #        RE-commenting out the previous test to reduce the testing.
    # -------------------------------------------------------------------------

    # run_test_touch_sensor(robot)
    # run_test_calibrate(robot)
    # run_test_raise_and_lower(robot)
    run_test_move_arm_to_position(robot)


def run_test_touch_sensor(robot):
    """
    Tests the  touch_sensor_is_pressed    methods of the ArmAndClaw class.
    """
    print('--------------------------------------------------')
    print('Testing the  touch_sensor.is_pressed   methods of the robot')
    print('--------------------------------------------------')

    while True:
        time.sleep(0.5)
        # -------------------------------------------------------------------------
        # TODO: 3. Call the  touch_sensor.is_pressed  method of the   arm_and_claw   of the robot.
        # If the Touch sensor is pressed, print "Pressing Touch Sensor!"
        # If the Touch sensor is not pressed, print "Touch sensor - NOT - pressed"
        # -------------------------------------------------------------------------

        # Solution to be removed
        if robot.arm_and_claw.touch_sensor.is_pressed():
            print("Pressing Touch Sensor!")
        else:
            print("Touch sensor - NOT - pressed")


def run_test_calibrate(robot):
    """
    Tests the  calibrate    methods of the ArmAndClaw class.
    """
    print('--------------------------------------------------')
    print('Testing the  calibrate   methods of the robot')
    print('--------------------------------------------------')
    while True:
        input("Press the ENTER key when ready for the robot to start moving.")

        # -------------------------------------------------------------------------
        # TODO: 4. Call the  calibrate_arm  method of the   arm_and_claw   of the robot,
        #   sending it the arm_speed.
        # -------------------------------------------------------------------------

        # Solution to be removed
        robot.arm_and_claw.calibrate_arm()


def run_test_raise_and_lower(robot):
    """
    Tests the  raise   and  lower    methods of the ArmAndClaw class.
    """
    print('--------------------------------------------------')
    print('Testing the  raise   and  lower   methods of the robot')
    print('--------------------------------------------------')
    input("Press the ENTER key when ready for the robot to calibrate the arm.")

    # -------------------------------------------------------------------------
    # TODO: 5. Before you can use the lower_arm method you have to calibrate the arm.
    #  So call the  calibrate_arm  method of the   arm_and_claw   of the robot once.
    # -------------------------------------------------------------------------

    # Solution to be removed
    robot.arm_and_claw.calibrate_arm()

    while True:
        input("Press the ENTER key when ready for the robot to start moving up.")

        # -------------------------------------------------------------------------
        # TODO: 6. Call the  raise_arm  method of the   arm_and_claw   of the robot.
        # -------------------------------------------------------------------------

        # Solution to be removed
        robot.arm_and_claw.raise_arm()

        input("Press the ENTER key when ready for the robot to start moving back down.")

        # -------------------------------------------------------------------------
        # TODO: 7. Call the  lower_arm  method of the   arm_and_claw   of the robot.
        # -------------------------------------------------------------------------

        # Solution to be removed
        robot.arm_and_claw.lower_arm()


def run_test_move_arm_to_position(robot):
    """
    Tests the  move_arm_to_position    methods of the ArmAndClaw class.
    """
    print('--------------------------------------------------')
    print('Testing the  move_arm_to_position  method of the robot')
    print('--------------------------------------------------')

    while True:
        print("Enter an integer for the position to which")
        desired_position = int(input("to move the arm (0 to about 5100): "))
        if desired_position < 0 or desired_position > 5100:
            print("Goodbye")
            break
        print()
        input("Press the ENTER key when ready for the robot to start moving.")

        # -------------------------------------------------------------------------
        # TODO: 8. Call the  move_arm_to_position   of the robot
        # NOTICE: Your move_arm_to_position should notice that the arm has NOT
        # been calibrated and do a calibration.  You don't need to call calibrate
        # from here, your library method should notice the lack of calibration and
        # just do it before the move!
        # -------------------------------------------------------------------------

        # Solution to be removed
        robot.arm_and_claw.move_arm_to_position(desired_position)


main()
