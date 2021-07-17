"""
Capstone Team Project.  Code to run on a ROBOT (NOT a laptop).

This module is for testing STAND-ALONE code running on the ROBOT
(WITHOUT having LAPTOP GUI code running on the LAPTOP at the same time).
In particular, it tests the rest of the   DriveSystem   class
(with Lab 1a having tested the previous part).

Authors:  Your professors (for the framework)
    and PUT_YOUR_NAME_HERE.
Winter term, 2019-2020.
"""
# TODO: 1. In the above, put the names of EACH team member who contributes
#  (in any way) to this module.

import libs.rosebot as rb
import time


def main():
    """ Tests the   DriveSystem   of a Snatch3r robot. """
    print()
    print("--------------------------------------------------")
    print("Testing the  DriveSystem class  of a RoseBot")
    print("--------------------------------------------------")

    ## -------------------------------------------------------------------------
    # TODO: 3. The following constructs a RoseBot object, then sends it as an
    #  argument to the TEST functions. In those TEST functions, you will access
    #  the RoseBot object's   drive_system   instance variable to make the robot
    #  move. Change this _TODO_ to DONE after you understand the following code.
    # -------------------------------------------------------------------------
    robot = rb.RoseBot()

    run_test_go_straight_for_inches(robot)
    run_test_spin_in_place_for_seconds(robot)
    run_test_spin_in_place_for_degrees(robot)
    run_test_turn_for_seconds(robot)
    run_test_turn_for_degrees(robot)


def run_test_go_straight_for_inches(robot):
    """
    Tests the   go_straight_for_inches   method of the DriveSystem class.
       :type robot: rb.RoseBot
    """
    print()
    print("--------------------------------------------------")
    print("Testing the  go_straight_for_inches  method")
    print("  of the   DriveSystem   class.")
    print("--------------------------------------------------")

    # -------------------------------------------------------------------------
    # TODO: 3. The following makes a LIST of PAIRS, where each PAIR specifies
    #  the  INCHES_TO_MOVE  and  SPEED_AT_WHICH_TO_MOVE.
    #  _
    #  Positive speeds mean move straight FORWARD; negative means BACKWARD.
    #  _
    #  Read the comments beside the pairs to see
    #  what kind of movement to expect from each pair.
    #  _
    #  ADD tests and/or CHANGE the tests as desired!
    #  _
    #  Once you understand how those  inches_to_move  and  speed
    #  yield the listed movements, change this _TODO_ to DONE.
    # -------------------------------------------------------------------------
    inches_speeds = [(12, 100),  # Straight FORWARD at FAST speed for 12 inches
                     (24, 100),  # Straight FORWARD at FAST speed for 24 inches
                     (6, 100),  # Straight FORWARD at FAST speed for 6 inches
                     (3.5, 20),  # Straight FORWARD SLOWLY for 3.5 inches
                     (6, -50),  # Straight BACKWARD at 50% POWER for 6 inches
                     (2, -30)]  # Straight BACKWARD at 30% POWER for 2 inches

    print()
    print("READ the tests to know what movement to expect")
    print("in the following tests.")
    print()

    # Loop through the inches_speeds pairs:
    for k in range(len(inches_speeds)):
        inches_to_move = inches_speeds[k][0]
        speed = inches_speeds[k][1]
        print("Press ENTER when you are ready to do")
        input("the next test of GO_STRAIGHT_FOR_INCHES.")

        # ---------------------------------------------------------------------
        # TODO: 4. To make the movement happen, call the
        #  go_straight_for_inches  method on the   drive_system   of the robot,
        #  sending it the  inches_to_move  and  speed.
        #  _
        #  NOTE: As you run these tests, adjust your constant in the
        #      libs/rosebot_drive_system module,
        #      DriveSystem class,
        #      go_straight_for_inches method,
        #  for converting from inches to degrees_the_motor_should_spin.
        #  _
        #  WARNING: Do NOT spend lots of time fine-tuning the constant!
        #    Instead, assign that task to a team member to do later.
        # ---------------------------------------------------------------------
        # SOLUTION CODE: Delete from the project given to students.
        robot.drive_system.go_straight_for_inches(inches_to_move, speed)


def run_test_spin_in_place_for_seconds(robot):
    """
    Tests the   spin_in_place_for_seconds   method of the DriveSystem class.
       :type robot: rb.RoseBot
    """
    print()
    print("--------------------------------------------------")
    print("Testing the  spin_in_place_for_seconds  method")
    print("  of the   DriveSystem   class.")
    print("--------------------------------------------------")

    # -------------------------------------------------------------------------
    # TODO: 5. The following makes a LIST of PAIRS, where each PAIR specifies
    #  the  SECONDS_TO_SPIN  and  SPEED_AT_WHICH_TO_SPIN.
    #  _
    #  Positive speeds mean spin CLOCKWISE; negative means COUNTER-CLOCKWISE.
    #  _
    #  Read the comments beside the pairs to see
    #  what kind of movement to expect from each pair.
    #  _
    #  ADD tests and/or CHANGE the tests as desired!
    #  _
    #  Once you understand how those  seconds_to_spin  and  speed
    #  yield the listed movements, change this _TODO_ to DONE.
    # -------------------------------------------------------------------------
    seconds_speeds = [(3, 100),  # Spin CLOCKWISE at FAST speed for 3 seconds
                      (4.5, 20),  # Spin CLOCKWISE SLOWLY for 4.5 seconds
                      (5, -50),  # Spin COUNTER-CW at 50% POWER for 5 seconds
                      (2, 30)]  # Spin CLOCKWISE at 30% POWER for 2 seconds

    print()
    print("READ the tests to know what movement to expect")
    print("in the following tests.")
    print()

    # Loop through the seconds_speeds pairs:
    for k in range(len(seconds_speeds)):
        seconds_to_spin = seconds_speeds[k][0]
        speed = seconds_speeds[k][1]
        print("Press ENTER when you are ready to do")
        input("the next test of SPIN_IN_PLACE_FOR_SECONDS.")

        # ---------------------------------------------------------------------
        # TODO: 6. To make the movement happen, call the
        #  spin_in_place_for_seconds  method on the  drive_system  of the robot,
        #  sending it the  seconds_to_spin  and  speed.
        # ---------------------------------------------------------------------
        # SOLUTION CODE: Delete from the project given to students.
        robot.drive_system.spin_in_place_for_seconds(seconds_to_spin, speed)


def run_test_spin_in_place_for_degrees(robot):
    """
    Tests the   spin_in_place_for_degrees   method of the DriveSystem class.
       :type robot: rb.RoseBot
    """
    print()
    print("--------------------------------------------------")
    print("Testing the  spin_in_place_for_degrees  method")
    print("  of the   DriveSystem   class.")
    print("--------------------------------------------------")

    # -------------------------------------------------------------------------
    # TODO: 7. The following makes a LIST of PAIRS, where each PAIR specifies
    #  the  DEGREES_TO_SPIN  and  SPEED_AT_WHICH_TO_SPIN.
    #  The DEGREES_TO_SPIN are the number of degrees that the ROBOT should spin.
    #  _
    #  Positive speeds mean spin CLOCKWISE; negative means COUNTER-CLOCKWISE.
    #  _
    #  Read the comments beside the pairs to see
    #  what kind of movement to expect from each pair.
    #  _
    #  ADD tests and/or CHANGE the tests as desired!
    #  _
    #  Once you understand how those  degrees_robot_should_spin  and  speed
    #  yield the listed movements, change this _TODO_ to DONE.
    # -------------------------------------------------------------------------
    degrees_speeds = [(90, 50),  # Spin 90 degrees CW at MEDIUM speed
                      (90, -100),  # Spin 90 degrees CCW at FAST speed
                      (45, 30),  # Spin 45 degrees CW at 30% POWER
                      (45, 100),  # Spin 45 degrees CW at FAST speed
                      (360, 50),  # Spin 360 degrees CW at 50% POWER
                      (180, -50),  # Spin 180 degrees CCW at 50% POWER
                      (30, 20)]  # Spin 30 degrees CW at SLOW speed
    print()
    print("READ the tests to know what movement to expect")
    print("in the following tests.")
    print()

    # Loop through the degrees_speeds pairs:
    for k in range(len(degrees_speeds)):
        degrees_robot_should_spin = degrees_speeds[k][0]
        speed = degrees_speeds[k][1]
        print("Press ENTER when you are ready to do")
        input("the next test of SPIN_IN_PLACE_FOR_DEGREES.")

        # ---------------------------------------------------------------------
        # TODO: 8. To make the movement happen, call the
        #  spin_in_place_for_degrees  method on the  drive_system   of the
        #  robot, sending it the   degrees_robot_should_spin   and  speed.
        #  _
        #  NOTE: As you run these tests, adjust your constant in the
        #      libs/rosebot_drive_system module,
        #      DriveSystem class,
        #      spin_in_place_for_degrees method,
        #  for converting from degrees that the ROBOT should spin
        #  to degrees that the MOTOR should spin.
        #  _
        #  WARNING: Do NOT spend lots of time fine-tuning the constant!
        #    Instead, assign that task to a team member to do later.
        # ---------------------------------------------------------------------
        # SOLUTION CODE: Delete from the project given to students.
        robot.drive_system.spin_in_place_for_degrees(degrees_robot_should_spin,
                                                     speed)


def run_test_turn_for_seconds(robot):
    """
    Tests the   turn_for_seconds   method of the DriveSystem class.
       :type robot: rb.RoseBot
    """
    print()
    print("--------------------------------------------------")
    print("Testing the  turn_for_seconds  method")
    print("  of the   DriveSystem   class.")
    print("--------------------------------------------------")

    # -------------------------------------------------------------------------
    # TODO: 9. The following makes a LIST of PAIRS, where each PAIR specifies
    #  the  SECONDS_TO_TURN  and  SPEED_AT_WHICH_TO_TURN.
    #  Positive speeds mean turn to the RIGHT (clockwise);
    #  negative means turn to the left (counter-clockwise).
    #  _
    #  Read the comments beside the pairs to see
    #  what kind of movement to expect from each pair.
    #  _
    #  ADD tests and/or CHANGE the tests as desired!
    #  _
    #  Once you understand how those  seconds_to_turn  and  speed
    #  yield the listed movements, change this _TODO_ to DONE.
    # -------------------------------------------------------------------------
    seconds_speeds = [(3, 100),  # Turn to the RIGHT at FAST speed for 3 seconds
                      (4.5, -20),  # Turn to the LEFT SLOWLY for 4.5 seconds
                      (5, 50),  # Turn to the RIGHT at 50% POWER for 5 seconds
                      (2, -30)]  # Turn to the LEFT at 30% POWER for 2 seconds
    print()
    print("READ the tests to know what movement to expect")
    print("in the following tests.")
    print()

    # Loop through the seconds_speeds pairs:
    for k in range(len(seconds_speeds)):
        seconds_to_turn = seconds_speeds[k][0]
        speed = seconds_speeds[k][1]
        print("Press ENTER when you are ready to do")
        input("the next test of TURN_FOR_SECONDS.")

        # ---------------------------------------------------------------------
        # TODO: 10. To make the movement happen, call the
        #  turn_for_seconds  method on the  drive_system  of the robot,
        #  sending it the  seconds_to_turn  and  speed.
        # ---------------------------------------------------------------------
        # SOLUTION CODE: Delete from the project given to students.
        robot.drive_system.turn_for_seconds(seconds_to_turn, speed)


def run_test_turn_for_degrees(robot):
    """
    Tests the   turn_for_degrees   method of the DriveSystem class.
       :type robot: rb.RoseBot
    """
    print()
    print("--------------------------------------------------")
    print("Testing the  turn_for_degrees  method")
    print("  of the   DriveSystem   class.")
    print("--------------------------------------------------")

    # -------------------------------------------------------------------------
    # TODO: 11. The following makes a LIST of PAIRS, where each PAIR specifies
    #  the  DEGREES_TO_TURN  and  SPEED_AT_WHICH_TO_TURN.
    #  The DEGREES_TO_TURN are the number of degrees that the ROBOT should turn.
    #  _
    #  Positive speeds mean turn to the RIGHT (clockwise);
    #  negative means turn to the left (counter-clockwise).
    #  _
    #  Read the comments beside the pairs to see
    #  what kind of movement to expect from each pair.
    #  _
    #  ADD tests and/or CHANGE the tests as desired!
    #  _
    #  Once you understand how those  degrees_robot_should_turn  and  speed
    #  yield the listed movements, change this _TODO_ to DONE.
    # -------------------------------------------------------------------------
    degrees_speeds = [(90, 50),  # Turn 90 degrees CW at MEDIUM speed
                      (90, -100),  # Turn 90 degrees CCW at FAST speed
                      (45, 30),  # Turn 45 degrees CW at 30% POWER
                      (45, 100),  # Turn 45 degrees CW at FAST speed
                      (360, 50),  # Turn 360 degrees CW at 50% POWER
                      (180, -50),  # Turn 180 degrees CCW at 50% POWER
                      (30, 20)]  # Turn 30 degrees CW at SLOW speed
    print()
    print("READ the tests to know what movement to expect")
    print("in the following tests.")
    print()

    # Loop through the degrees_speeds pairs:
    for k in range(len(degrees_speeds)):
        degrees_robot_should_turn = degrees_speeds[k][0]
        speed = degrees_speeds[k][1]
        print("Press ENTER when you are ready to do")
        input("the next test of TURN_FOR_DEGREES.")

        # ---------------------------------------------------------------------
        # TODO: 12. To make the movement happen, call the
        #  turn_for_degrees  method on the  drive_system   of the
        #  robot, sending it the   degrees_robot_should_turn   and  speed.
        #  _
        #  NOTE: As you run these tests, adjust your constant for converting
        #    from degrees that the ROBOT turns to degrees that the MOTOR
        #    should spin.
        #  _
        #  WARNING: Do NOT spend lots of time fine-tuning the constant!
        #    Instead, assign that task to a team member to do later.
        # ---------------------------------------------------------------------
        # SOLUTION CODE: Delete from the project given to students.
        robot.drive_system.turn_for_degrees(degrees_robot_should_turn, speed)
