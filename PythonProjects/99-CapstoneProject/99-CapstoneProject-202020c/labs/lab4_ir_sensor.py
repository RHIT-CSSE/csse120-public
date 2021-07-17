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
    """ Test a robot's IR sensor (proximity and beacon seeking). """
    print()
    print('--------------------------------------------------')
    print('Testing the Infrared sensor (in two modes) of a robot')
    print('--------------------------------------------------')

    # -------------------------------------------------------------------------
    # TODO: 2. Construct a robot, that is, a rosebot.RoseBot() object.
    # -------------------------------------------------------------------------


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

    # run_test_sounds(robot)
    # run_test_proximity_readings(robot)
    # run_test_drive_until_distance(robot)

    # run_test_beacon_sensor(robot)
    # run_test_spin_until_beacon_seen(robot)
    # run_test_spin_to_track_beacon(robot)
    # run_test_drive_towards_beacon(robot)


def run_test_sounds(robot):
    """
    Tests the methods of the Sound  class.
      :type robot: rosebot.RoseBot
    """
    print('--------------------------------------------------')
    print('Testing the methods of the Sound class of the robot')
    print('--------------------------------------------------')
    while True:
        print("Which Sound method would you like to test?\n\t1: Beep\n\t2: Speak\n\t3: Tone\n\t" +
              "4: Tone Sequence\n\t5: Wav file\n\t0: Exit")
        menu_option = int(input("Sound option: "))
        print(menu_option)
        if menu_option == 1:
            print("Playing a beep")
            # -------------------------------------------------------------------------
            # TODO: 3. Call the  beep   method of the    sound field  of the robot
            # -------------------------------------------------------------------------

        elif menu_option == 2:
            phrase = input("What would you like to say? ")
            print("Speaking")
            # -------------------------------------------------------------------------
            # TODO: 4. Call the  speak   method of the   sound field   of the robot
            # -------------------------------------------------------------------------


        elif menu_option == 3:
            print("Tone:")
            frequency = int(input("What frequency (Hz) would you like (300-600)? "))
            duration_ms = int(input("What duration (ms) would you like (50-3000)? "))
            print("Playing a tone")
            # -------------------------------------------------------------------------
            # TODO: 5. Call the  play_tone   method of the   sound field   of the robot
            # -------------------------------------------------------------------------


        elif menu_option == 4:
            print("Vader song")
            # -------------------------------------------------------------------------
            # TODO: 6. Call the  play_vader_song   method of the   sound field   of the robot
            # -------------------------------------------------------------------------


        elif menu_option == 5:
            print("Lego song")
            # -------------------------------------------------------------------------
            # TODO: 7. Call the  play_lego_wav_file   method of the   sound field   of the robot
            # -------------------------------------------------------------------------


        elif menu_option == 0:
            print("Goodbye")
            break
        else:
            print("Unknown menu option [" + str(menu_option) + "].")
        print("--------------------------------------------------")


def run_test_proximity_readings(robot):
    """
    Tests the   get_distance   methods of the infrared_proximity_sensor  class.
        :type robot: rosebot.RoseBot
    """
    print('--------------------------------------------------')
    print('Testing the  get_distance   method of the robot')
    print('--------------------------------------------------')

    print()
    print("As this test runs, repeatedly")
    print("put your hand in front of the IR sensor.")
    print("Keep it in place for a second or so.")
    print("Then try another position.")
    print("  REMINDER: The sensor is inconsistent")
    print("  when < 4 inches or so from the object.")
    input("Press ENTER when ready to begin this test.")

    while True:
        time.sleep(1.0)
        # -------------------------------------------------------------------------
        # TODO: 8. Use the  get_distance  method of the  infrared_proximity_sensor
        #  of the robot to display the inches to the nearest target every second.
        #  Format each print statement as follows:
        #   Distance = 3.34 inches
        #   Distance = 3.35 inches
        #   Distance = 1.09 inches
        #  Hint: print("Distance = {:.2f} inches".format(some_value))
        #  Additionally...
        #  If the target is less than 5 inches away beep!
        # -------------------------------------------------------------------------

        distance_in = 6  # Edit this line of code for this _todo_

        print("Distance = {:.2f} inches".format(distance_in))
        if distance_in < 5:
            print("Distance is < 5, so BEEP!")
            print("  REMINDER: The sensor is inconsistent")
            print("  when < 4 inches or so from the object.")
            robot.sound.beep()


def run_test_drive_until_distance(robot):
    """
    Tests the  wait_until_distance_less_than    methods of the   class.
        :type robot: rosebot.RoseBot
    """
    print('--------------------------------------------------')
    print('Testing the  wait_until_distance_less_than method of the robot')
    print('--------------------------------------------------')
    while True:
        print()
        speed = int(input("Enter an integer for the wheel speed (1 to 100): "))
        if speed == 0:
            break
        requested_distance_away = int(input("Enter a distance threshold in inches: "))
        if requested_distance_away == 0:
            break
        print("After this test begins, slowly move your hand closer")
        print("  to the robot.  When your hand is the specified distance")
        print("  away from the IR sensor, the robot should stop moving.")
        input("Press the ENTER key when ready for the robot to start moving.")

        # -------------------------------------------------------------------------
        # TODO: 9. Make the robot drive straight at the given speed at a wall.
        #  Call the wait_until_distance_less_than   method of the
        #  infrared_proximity_sensor of the robot to determine when the distance
        #  is below the requested value.
        #  Then stop the robot
        # -------------------------------------------------------------------------



def run_test_beacon_sensor(robot):
    """
    Tests the   get_heading and get_distance   methods of the beacon_sensor  class.
        :type robot: rosebot.RoseBot
    """
    print('--------------------------------------------------')
    print('Testing the  get_heading and get_distance   method of the BeaconSensor')
    print('--------------------------------------------------')

    print()
    print("As this test runs, repeatedly")
    print("put the IR Remote into Beacon mode (top button)")
    print("Keep it in place for a second or so.")
    print("Then try another position.")
    input("Press ENTER when ready to begin this test.")

    while True:
        time.sleep(1.0)
        # -------------------------------------------------------------------------
        # TODO: 8. Use the  get_distance  method of the  infrared_proximity_sensor
        #  of the robot to display the inches to the nearest target every second.
        #  Format each print statement as follows:
        #   Distance = 100   Heading = 23 degrees
        #   Distance = 63   Heading = 13 degrees

        #  Hint: print("Distance = {}     Heading = {}     ".format(distance, heading))
        #  Additionally...
        #  If the distance is less than 3 away beep!
        # -------------------------------------------------------------------------

        # Solution to be removed
        distance = 6  # Edit this line of code for this _todo_
        heading = 0  # Edit this line of code for this _todo_
        print("Distance = {}     Heading = {}     ".format(distance, heading))
        if distance == -128:
            print("No beacon sensor found at all.")
        elif distance < 5:
            print("Distance to beacon is < 3, so BEEP!")
            robot.sound.beep()


def run_test_spin_until_beacon_seen(robot):
    """
    Tests the  spin_until_beacon_seen    method of the   class.
      :type robot: rosebot.RoseBot
    """
    print('--------------------------------------------------')
    print('Testing the   spin_until_beacon_seen  method of the robot')
    print('--------------------------------------------------')
    while True:
        print()
        speed = int(input("Enter an integer for the max wheel speed (1 to 100): "))
        if speed == 0:
            break
        heading_threshold = int(input("What would you like to use for the heading threshold (0 to 10)? "))
        if heading_threshold == 0:
            break
        input("Press the ENTER key when ready for the robot to start moving.")

        # -------------------------------------------------------------------------
        # TODO: 10. Call the  spin_until_beacon_seen  method of the   beacon_seeker
        #  of the robot passing in the heading_threshold.
        #  Once the target is found make the robot beep.
        # Info:
        #  - The heading is in degrees in the range -25 to 25 with:
        #      - 0 means straight ahead
        #      - negative degrees mean the Beacon is to the left
        #      - positive degrees mean the Beacon is to the right
        # -------------------------------------------------------------------------




def run_test_spin_to_track_beacon(robot):
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
        tracking_duration_s = int(input("How long would you like to track the beacon (seconds)? "))
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




def run_test_drive_towards_beacon(robot):
    """
    Tests the  spin_until_beacon_seen and spin_to_track_beacon    methods of the   class.
        :type robot: rosebot.RoseBot
    """
    print('--------------------------------------------------')
    print('Testing the drive_to_beacon method of the BeaconSeeker')
    print('--------------------------------------------------')
    while True:
        input("Press the ENTER key when ready for the robot to start moving.")

        # -------------------------------------------------------------------------
        # TODO: 12. Call the  drive_to_beacon  method of the      of the robot
        #  Once the beacon is found (distances near 0) make the robot beep.
        #  Note: the drive_to_beacon will stop the motors, but make the beep here.
        # Info:
        #  - The heading is in degrees in the range -25 to 25 with:
        #      - 0 means straight ahead
        #      - negative degrees mean the Beacon is to the left
        #      - positive degrees mean the Beacon is to the right
        #  - Distance is from 0 to 100, where 100 is about 70 cm
        # -------------------------------------------------------------------------




        # -------------------------------------------------------------------------
        # TODO: 13. VERY optional extra
        #  Once the beacon is found (distances at 0) make the robot pick up the beacon
        #  with the arm.  If you have the remote control in the air with the arm
        #  you win some big prize! (not really, but it would be cool to see)
        #  Note: this also requires that the remote is in the stand so that it
        #  can be pickup up easily.
        # -------------------------------------------------------------------------


main()
