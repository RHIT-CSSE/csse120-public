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
    test_drive_system()


def test_drive_system():
    """ Test a robot's DRIVE SYSTEM. """
    print()
    print('--------------------------------------------------')
    print('Testing the  DRIVE SYSTEM  of a robot:')
    print('--------------------------------------------------')

    # -------------------------------------------------------------------------
    # Get the wheel speeds for this set of tests.
    # -------------------------------------------------------------------------
    print("Wheel speeds should be integers between -100 and 100.")
    left_wheel_speed = int(input("Enter an integer for left wheel speed: "))
    right_wheel_speed = int(input("Enter an integer for right wheel speed: "))

    # -------------------------------------------------------------------------
    # TODO: 2. Construct a robot, that is, a rosebot.RoseBot() object.
    # -------------------------------------------------------------------------
    robot = rosebot.RoseBot()

    # -------------------------------------------------------------------------
    # Test the GO and STOP methods of the  drive_system  of the robot:
    # -------------------------------------------------------------------------
    print()
    print("Testing the  GO  and  STOP  methods")
    print("of the  DRIVE_SYSTEM  of the robot.")
    input("Press the ENTER key when ready for the robot to start moving.")

    # -------------------------------------------------------------------------
    # TODO: 3. Call the  go  method of the   drive_system   of the robot,
    #   sending it the two wheel speeds.  Keep going (time.sleep) for 3 seconds.
    #   Then call the  stop  method of the   drive_system   of the robot.
    # -------------------------------------------------------------------------
    robot.drive_system.go(left_wheel_speed, right_wheel_speed)
    time.sleep(3)
    robot.drive_system.stop()

    # -------------------------------------------------------------------------
    # Test the GO_STRAIGHT_FOR_SECONDS method of the drive_system of the robot:
    # -------------------------------------------------------------------------
    print()
    print("Testing the  GO_STRAIGHT_FOR_SECONDS  method")
    print("of the  DRIVE_SYSTEM  of the robot.")
    seconds = float(input("Enter how many seconds to go (e.g., 2.3): "))
    input("Press the ENTER key when ready for the robot to start moving.")

    # -------------------------------------------------------------------------
    # TODO: 4. Call the  go_straight_for_seconds  method of the   drive_system
    #  of the robot, sending it the input  seconds  and  left_wheel_speed.
    #  (The go_straight_for_seconds method uses the same speed for both wheels.)
    # -------------------------------------------------------------------------
    robot.drive_system.go_straight_for_seconds(seconds, left_wheel_speed)

    # -------------------------------------------------------------------------
    # Test the GO_STRAIGHT_FOR_INCHES method of the drive_system of the robot:
    # -------------------------------------------------------------------------
    print()
    print("Testing the  GO_STRAIGHT_FOR_INCHES  method")
    print("of the  DRIVE_SYSTEM  of the robot.")
    inches = float(input("Enter how many inches to go (e.g., 12.4): "))
    input("Press the ENTER key when ready for the robot to start moving.")

    # -------------------------------------------------------------------------
    # TODO: 5. Call the  go_straight_for_inches  method of the   drive_system
    #  of the robot, sending it the input  inches  and  left_wheel_speed.
    #  (The go_straight_for_inches method uses the same speed for both wheels.)
    # -------------------------------------------------------------------------
    robot.drive_system.go_straight_for_inches(inches, left_wheel_speed)

    # -------------------------------------------------------------------------
    # TODO: 6. Add additional tests as needed to ensure that the other
    #  drive_system   methods (spin... and turn...) are working correctly.
    # -------------------------------------------------------------------------


main()
