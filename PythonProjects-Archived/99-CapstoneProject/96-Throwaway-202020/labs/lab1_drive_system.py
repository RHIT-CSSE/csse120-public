"""
THROW-AWAY Capstone Project. If you mess up this THROW-AWAY project,
  ** no worries. **
It lets you practice skills & concepts needed for the REAL Capstone Project.

This module contains code intended to run directly on the EV3 robot
(NOT on a laptop, NOT via a GUI running on a laptop).
It TESTS the   DriveSystem   class that is in the  libs  folder.

Authors:  Your professors (for the framework)
    and PUT_YOUR_NAMES_HERE.
Winter term, 2019-2020.
"""
# -----------------------------------------------------------------------------
# NOTE to students: Start this exercise WITH YOUR INSTRUCTOR.
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# TODO: 1.  If you have not already done so, with your instructor,
#  READ and UNDERSTAND the  HowToShareModules.pdf  document in this project.
#    -- If you understand it, change this _TODO_ to DONE.
#    -- Otherwise, ** do NOT modify this module **
#         and get help before continuing.
#  _
#  Throughout this module, ** use the process in HowToShareModules.pdf. **
#  _
#  In particular, *** only ONE team member should modify this file ***
#    (but often pair-programming using the same computer).
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# TODO: 2. Change the   PUT_YOUR_NAMES_HERE   above to the names of
#  EACH team member who contributes (in any way) to this module.
#  _
#  REMINDER: Use ONLY ** ONE ** team member's computer to make changes herein.
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# TODO: 3. With your instructor, import the modules needed herein:
#     libs.rosebot as rosebot
#     time
#  Make sure you understand WHY those imports are needed,
#  and why you do NOT need to import the  rosebot_drive_system   module.
# -----------------------------------------------------------------------------


def main():
    """ Calls the desired TEST functions. """
    run_test_drive_system()


def run_test_drive_system():
    """ Test the DRIVE SYSTEM of a Snatch3r robot. """
    print()
    print("--------------------------------------------------")
    print("Testing the  DRIVE SYSTEM  of a robot")
    print("--------------------------------------------------")

    # -------------------------------------------------------------------------
    # TODO: 4. With your instructor, construct a robot, that is,
    #          a   rosebot.RoseBot()   object.
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # TODO: 5. Un-comment the first TEST function below.
    #  Re-comment it when you are finished using its tests,
    #  and then proceed to the next TEST function below.
    # -------------------------------------------------------------------------
    run_test_go_stop(robot)
    run_test_go_straight_for_seconds(robot)


def run_test_go_stop(robot):
    """
    Tests the   go    and   stop   methods of the DriveSystem class.
    """
    print()
    print("--------------------------------------------------")
    print("Testing the  go   and  stop   methods")
    print("  of the   DriveSystem   class.")
    print("--------------------------------------------------")

    # -------------------------------------------------------------------------
    # Get the wheel speeds for this set of tests.
    # -------------------------------------------------------------------------
    speeds = [(100, 10), (-10, -100), (50, -50), (-50, 50)]

    for k in range(len(speeds)):
        # ---------------------------------------------------------------------
        # TODO: 6.
        #  a. Call the  go  method of the   drive_system   of the robot,
        #       sending it the two wheel speeds.
        #  b. Keep going (time.sleep) for 3 seconds.
        #  c. Call the  stop  method of the   drive_system   of the robot.
        # ---------------------------------------------------------------------
        pass

    # print()
    # print("Wheel speeds should be integers between -100 and 100.")
    # print("Enter  0  for BOTH wheel speeds to exit this test.")
    #
    # while True:
        # print()
        # left_wheel_speed = int(input("Enter an integer for left wheel speed: "))
        # right_wheel_speed = int(input(
        #     "Enter an integer for right wheel speed: "))
        # if left_wheel_speed == 0 and right_wheel_speed == 0:
        #     break
        # input("Press the ENTER key when ready for the robot to start moving.")


def run_test_go_straight_for_seconds(robot):
    """
    Tests the   go_straight_for_seconds   method of the DriveSystem class.
    """
    print("--------------------------------------------------")
    print("Testing the  go_straight_for_seconds  method")
    print("  of the   DriveSystem   class.")
    print("--------------------------------------------------")

    # -------------------------------------------------------------------------
    # Get the seconds-to-move and wheel speeds for this set of tests.
    # -------------------------------------------------------------------------
    seconds_speeds = [(3, 10), (1, 100), (5, -50), (3, 50)]

    for k in range(len(seconds_speeds)):
        # -------------------------------------------------------------------------
        # TODO: 7. Call the  go_straight_for_seconds  method of the
        #  drive_system of the robot, sending it the  seconds  and  speed.
        # -------------------------------------------------------------------------
        pass

    # -------------------------------------------------------------------------
    # Get the wheel speed and seconds-to-move for this set of tests.
    # -------------------------------------------------------------------------
    # print()
    # print("The  seconds-to-move  should be a non-negative number.")
    # print("Enter  0  for the seconds-to-move to exit this test.")
    # print("The  wheel speed  should be a non-negative integer")
    # print("between -100 and 100.")
    #
    # while True:
    #     print()
    #     seconds = float(input("Enter how many seconds to go (e.g., 2.3): "))
    #     if abs(round(seconds, 12)) < 0:
    #         break
    #     print("Enter a non-zero integer between -100 and 100")
    #     speed = int(input("for the speed of the wheels: "))
    #     input("Press the ENTER key when ready for the robot to start moving.")


main()
