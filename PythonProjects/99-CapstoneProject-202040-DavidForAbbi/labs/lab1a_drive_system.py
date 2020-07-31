"""
Capstone Team Project.  Code to run on a ROBOT (NOT a laptop).

This module is for testing STAND-ALONE code running on the ROBOT
(WITHOUT having LAPTOP GUI code running on the LAPTOP at the same time).
In particular, it tests part of the   DriveSystem   class.

Authors:  Your professors (for the framework)
    and PUT_YOUR_NAME_HERE.
Winter term, 2019-2020.
"""
# TODO: 1. In the above, put the names of EACH team member who contributes
#  (in any way) to this module.

# -----------------------------------------------------------------------------
# TODO: 2. Note that you will use the  rosebot  library (shorthand: rb).
#  Then change this _TODO_ to DONE.
# -----------------------------------------------------------------------------
import libs.rosebot as rb
import time


def main():
    """ Tests the   DriveSystem   of a Snatch3r robot. """
    print()
    print("--------------------------------------------------")
    print("Testing the  DRIVE SYSTEM  of a robot")
    print("--------------------------------------------------")

    # -------------------------------------------------------------------------
    # TODO: 3. The following constructs a RoseBot object, then sends it as an
    #  argument to the TEST functions. In those TEST functions, you will access
    #  the RoseBot object's   drive_system   instance variable to make the robot
    #  move. Change this _TODO_ to DONE after you understand the following code.
    # -------------------------------------------------------------------------
    robot = rb.RoseBot()

    run_test_go_stop(robot)
    run_test_go_straight_for_seconds(robot)


def run_test_go_stop(robot):
    """
    Tests the   go    and   stop   methods of the DriveSystem class.
      :type robot: rb.RoseBot
    """
    print()
    print("--------------------------------------------------")
    print("Testing the  go   and  stop   methods")
    print("  of the   DriveSystem   class.")
    print("--------------------------------------------------")

    # -------------------------------------------------------------------------
    # TODO: 4. The following makes a LIST of PAIRS, where each pair specifies
    #  the LEFT_WHEEL_SPEED and the RIGHT_WHEEL_SPEED. Read the comments
    #  beside the pairs to see what kind of movement to expect from each pair.
    #  Once you understand how those speeds yield the listed movements,
    #  change this _TODO_ to DONE.
    # -------------------------------------------------------------------------
    speeds = [(100, 10),  # Both wheels forward, one FAST and the other SLOW
              (-10, -100),  # Both wheels backward, one SLOW and the other FAST
              (50, -50),  # SPIN in place CLOCKWISE at a MEDIUM speed
              (-10, 10),  # SPIN in place COUNTER-CLOCKWISE at a SLOW speed
              (50, 0),  # TURN RIGHT at a MEDIUM speed
              (0, 100),  # TURN LEFT at a FAST speed
              (75, 25),  # VEER to the RIGHT
              (-50, -100)  # VEER BACKWARDS
              ]

    print()
    print("READ the tests to know what movement to expect")
    print("in the following tests.")
    print()

    # Loop through the speeds pairs:
    for k in range(len(speeds)):
        left_wheel_speed = speeds[k][0]
        right_wheel_speed = speeds[k][1]
        print("Press ENTER when you are ready to do")
        input("the next test of GO/STOP.")

        # ---------------------------------------------------------------------
        # TODO: 5.  Implement the following three statements
        #  to make the movement happen:
        #    a. Call the  go  method on the   drive_system   of the robot,
        #         sending it the two wheel speeds.
        #    b. Keep going for 2 seconds, by using:  time.sleep(2).
        #    c. Call the  stop  method of the   drive_system   of the robot.
        # ---------------------------------------------------------------------


def run_test_go_straight_for_seconds(robot):
    """
    Tests the   go_straight_for_seconds   method of the DriveSystem class.
       :type robot: rb.RoseBot
    """
    print()
    print("--------------------------------------------------")
    print("Testing the  go_straight_for_seconds  method")
    print("  of the   DriveSystem   class.")
    print("--------------------------------------------------")

    # -------------------------------------------------------------------------
    # TODO: 6. The following makes a LIST of PAIRS, where each PAIR specifies
    #  the  SECONDS_TO_MOVE  and  SPEED_AT_WHICH_TO_MOVE. Positive speeds mean
    #  move straight FORWARD; negative means straight BACKWARD. Read the
    #  comments beside the pairs to see what kind of movement to expect from
    #  each pair. Once you understand how those  seconds_to_move  and  speed
    #  yield the listed movements, change this _TODO_ to DONE.
    # -------------------------------------------------------------------------
    seconds_speeds = [(3, 100),  # Straight FORWARD at FAST speed for 3 seconds
                      (3.5, 10),  # Straight FORWARD SLOWLY for 3.5 seconds
                      (5, -50),  # Straight BACKWARD at 50% POWER for 5 seconds
                      (2, 30)]  # Straight FORWARD at 30% POWER for 2 seconds

    print()
    print("READ the tests to know what movement to expect")
    print("in the following tests.")
    print()

    # Loop through the seconds_speeds pairs:
    for k in range(len(seconds_speeds)):
        seconds_to_move = seconds_speeds[k][0]
        speed = seconds_speeds[k][1]
        print("Press ENTER when you are ready to do")
        input("the next test of GO_STRAIGHT_FOR_SECONDS.")

        # ---------------------------------------------------------------------
        # TODO: 7. To make the movement happen, call the
        #  go_straight_for_seconds  method on the  drive_system   of the robot,
        #  sending it the  seconds_to_move  and  speed.
        # ---------------------------------------------------------------------
