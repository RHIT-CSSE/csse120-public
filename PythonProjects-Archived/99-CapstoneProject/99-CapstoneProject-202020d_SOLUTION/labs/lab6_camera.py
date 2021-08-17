"""
Capstone Team Project.  Code to run on a ROBOT (NOT a laptop).

This module is for testing STAND-ALONE code running on the ROBOT
(WITHOUT having LAPTOP GUI code running on the LAPTOP at the same time).

Authors:  Your professors (for the framework)
    and PUT_YOUR_NAME_HERE.
Winter term, 2019-2020.
"""
# TODO: 1.  Put your name in the above.

import time
import rosebot


def main():
    """ Test a robot's camera. """
    print()
    print('--------------------------------------------------')
    print('Testing the Camera of a robot')
    print('--------------------------------------------------')

    # -------------------------------------------------------------------------
    # TODO: 2. Construct a robot, that is, a rosebot.RoseBot() object.
    #          Then  ** ENABLE ITS CAMERA. **
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
    robot.camera.enable()

    # run_test_blob_readings(robot)
    # run_test_spin_until_color_seen(robot)
    run_test_spin_to_track_color(robot)


def run_test_blob_readings(robot):
    """
    Tests the   get_biggest_blob   methods of the Camera  class.
    """
    print('--------------------------------------------------')
    print('Testing the  get_biggest_blob   method of the camera of the robot')
    print('--------------------------------------------------')
    while True:
        time.sleep(1.0)
        # -------------------------------------------------------------------------
        # TODO: 8. Use the  get_biggest_blob  method of the  camera
        #  of the robot to display Blob readings once per second.
        #  Print the blob (it has a __repr__ method so it can be printed)
        # -------------------------------------------------------------------------

        # Solution to be removed
        blob = robot.camera.get_biggest_blob()
        print(blob)


def run_test_spin_until_color_seen(robot):
    """
    Tests the  spin_until_color_seen    method of the   class.
    :type robot: rosebot.RoseBot
    """
    print('--------------------------------------------------')
    print('Testing the   spin_until_color_seen  method of the robot')
    print('--------------------------------------------------')
    while True:
        print()
        speed = int(input("Enter an integer for the max wheel speed (1 to 100): "))
        if speed == 0:
            break
        blob_area_threshold = int(input("What is your Blob area threshold? (10000 for a 100x100) "))
        if blob_area_threshold == 0:
            break
        input("Press the ENTER key when ready for the robot to start moving.")

        # -------------------------------------------------------------------------
        # TODO: 10. Call the  spin_until_color_seen  method of the   camera_tracker
        #  of the robot passing in the blob_area_threshold.
        #  Once the target is found make the robot beep.
        # -------------------------------------------------------------------------

        # Solution to be removed
        robot.camera_tracker.spin_until_color_seen(speed, blob_area_threshold)
        robot.sound.beep()


def run_test_spin_to_track_color(robot):
    """
    Tests the  spin_until_beacon_seen and spin_to_track_beacon    methods of the   class.
    :type robot: rosebot.RoseBot
    """
    print('--------------------------------------------------')
    print('Testing the spin_to_track_beacon method of the BeaconSeeker')
    print('--------------------------------------------------')
    while True:
        print()
        speed = int(input("Enter an integer for the max wheel speed (1 to 100): "))
        if speed == 0:
            break
        tracking_duration_s = int(input("How long would you like to track the color (seconds)? "))
        if tracking_duration_s == 0:
            break
        input("Press the ENTER key when ready for the robot to start moving.")

        # -------------------------------------------------------------------------
        # TODO: 11. Call the  spin_to_track_beacon  method of the  beacon_seeker
        #  of the robot passing in the tracking_duration_s
        #  Once the tracking_duration_s is over make the robot beep.
        # Info:
        #  - The heading is in degrees in the range -25 to 25 with:
        #      - 0 means straight ahead
        #      - negative degrees mean the Beacon is to the left
        #      - positive degrees mean the Beacon is to the right
        #  - Distance is from 0 to 100, where 100 is about 70 cm
        # -------------------------------------------------------------------------

        # Solution to be removed
        robot.camera_tracker.spin_to_track_color(speed, tracking_duration_s)
        robot.sound.beep()


main()
