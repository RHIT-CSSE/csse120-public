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
    """ Calls the desired TEST functions. """
    test_digital_io()


def test_digital_io():
    """ Test a robot's Remote Control, brick buttons, and LEDs. """
    print()
    print('--------------------------------------------------')
    print('Testing the  Remote Control, Brick Buttons, and LEDs  of a robot')
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

    # run_test_leds_on_off(robot)
    # run_test_leds_colors(robot)
    # run_test_brick_buttons(robot)
    run_test_remote_control(robot)


def run_test_leds_on_off(robot):
    """
    Tests the  set_color and  turn_off    methods of the Leds class.
    """
    print('--------------------------------------------------')
    print('Testing the  turn_on  turn_off    methods of the robot')
    print('--------------------------------------------------')
    while True:
        # -------------------------------------------------------------------------
        # TODO: 3. Call the  set_color  and  turn_off methods on the   leds   of the robot,
        #  so that "both" LEDs are on "red" for 1 second, then off for 1 second (repeating forever)
        #  In addition to the LEDs print to the console "Both LEDs On as Red" or "LEDs Off"
        #  just before the LED change line of code (so you can see it and read it).
        # -------------------------------------------------------------------------

        # Solution to be removed
        print("Both LEDs On as Red")
        robot.leds.set_color("both", "red")
        time.sleep(1.0)

        print("Both LEDs Off")
        robot.leds.turn_off()
        time.sleep(1.0)


def run_test_leds_colors(robot):
    """
    Tests the  set_color_by_name    methods of the ArmAndClaw class.
    """
    print('--------------------------------------------------')
    print('Testing the  set_color   methods of the robot')
    print('--------------------------------------------------')
    left_colors = ["red", "green", "amber", "off", "red", "off", "green", "off", "amber", "off"]
    right_colors = ["red", "green", "amber", "off", "off", "red", "off", "green", "off", "amber"]

    # -------------------------------------------------------------------------
    # TODO: 4. Call the  set_color  method of the   leds   of the robot,
    #  so that the color changes through each value in the lists above.
    #  Instead of using a 1 second delay between colors, have the user hit
    #  the enter key to change to the next colors.
    #
    # After the final value in the list, the program should turn off both LEDs and end.
    # Notice that this _TODO_ is not within a while True loop (unlike other parts)
    # -------------------------------------------------------------------------

    # Solution to be removed
    for k in range(len(left_colors)):
        robot.leds.set_color("left", left_colors[k])
        robot.leds.set_color("right", right_colors[k])
        input("Press the ENTER key to change to the next color.")

    robot.leds.turn_off()


def run_test_brick_buttons(robot):
    """
    Tests the  brick_buttons    methods of the BrickButton class.
    """
    print('--------------------------------------------------')
    print('Testing the  brick_buttons   methods of the robot')
    print('--------------------------------------------------')
    while True:
        time.sleep(0.05)

        # -------------------------------------------------------------------------
        # TODO: 5. Create a small program that will light the appropriate LEDs
        #   when buttons on the EV3 Brick are pressed:
        #    When up is pressed light both LEDs green
        #    When down is pressed light both LEDs red
        #    When left is pressed light the left LED amber
        #    When right is pressed light the right LED amber
        #    When backspace is pressed break from the loop and end the program
        #    When no button is pressed turn the LEDs off
        #
        #  Note, only 1 button will be pressed at a time.
        # -------------------------------------------------------------------------

        # Solution to be removed
        if robot.brick_buttons.is_up_pressed():
            robot.leds.set_color("both", "green")
        elif robot.brick_buttons.is_down_pressed():
            robot.leds.set_color("both", "red")
        elif robot.brick_buttons.is_left_pressed():
            robot.leds.set_color("left", "amber")
        elif robot.brick_buttons.is_right_pressed():
            robot.leds.set_color("right", "amber")
        elif robot.brick_buttons.is_backspace_pressed():
            print("Goodbye")
            break
        else:
            robot.leds.turn_off()


def run_test_remote_control(robot):
    """
    Tests the  remote_control    methods of the RemoteControl class.
    """
    print('--------------------------------------------------')
    print('Testing the  remote_control   methods of the robot')
    print('--------------------------------------------------')

    speed = 50
    while True:
        time.sleep(0.05)

        # -------------------------------------------------------------------------
        # TODO: 6. Create a small program that will move the motors of the robot as follows
        #   when buttons on the remote control are pressed:
        #    When channel 1 red up is pressed drive the left motor forward at speed
        #    When channel 1 red down is pressed drive the left motor backwards at -speed
        #         If neither channel 1 red up or red down is pressed the left motor should stop
        #    When channel 1 blue up is pressed drive the right motor forward at speed
        #    When channel 1 blue down is pressed drive the right motor backwards at -speed
        #         If neither channel 1 blue up or blue down is pressed the right motor should stop
        #    When channel 2 red up is pressed raise the arm
        #    When channel 2 red down is pressed lower the arm (note, a calibration is needed first)
        #    When channel 2 blue up is pressed calibrate the arm
        #    When backspace is pressed on the EV3 break from the loop and end the program
        #
        # Note, MULTIPLE buttons may be pressed at the same time in the program.
        # -------------------------------------------------------------------------

        # Solution to be removed
        if robot.remote_control.is_pressed(1, "red_up"):
            robot.drive_system.left_motor.turn_on(speed)
        elif robot.remote_control.is_pressed(1, "red_down"):
            robot.drive_system.left_motor.turn_on(-speed)
        else:
            robot.drive_system.left_motor.turn_off()

        if robot.remote_control.is_pressed(1, "blue_up"):
            robot.drive_system.right_motor.turn_on(speed)
        elif robot.remote_control.is_pressed(1, "blue_down"):
            robot.drive_system.right_motor.turn_on(-speed)
        else:
            robot.drive_system.right_motor.turn_off()

        if robot.remote_control.is_pressed(2, "red_up"):
            robot.arm_and_claw.raise_arm()
        if robot.remote_control.is_pressed(2, "red_down"):
            robot.arm_and_claw.lower_arm()
        if robot.remote_control.is_pressed(2, "blue_up"):
            robot.arm_and_claw.calibrate_arm()

        if robot.brick_buttons.is_backspace_pressed():
            print("Goodbye")
            break


main()
