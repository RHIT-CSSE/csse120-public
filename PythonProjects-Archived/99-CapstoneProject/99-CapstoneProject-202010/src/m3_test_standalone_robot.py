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
import rosebot_color_sensor
import time


def main():
    """ Calls the desired TEST functions. """
    test_color_sensor()


def test_color_sensor():
    """ Test a robot's COLOR SENSOR. """
    print()
    print('--------------------------------------------------')
    print('Testing the  COLOR_SENSOR  of a robot:')
    print('--------------------------------------------------')

    # -------------------------------------------------------------------------
    # TODO: 2. Construct a robot, that is, a rosebot.RoseBot() object,
    #  which itself constructs its   color_sensor   instance variable.
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # Test the  get_reading   and   get_detected_color_name   methods
    # of the  color_sensor  of the robot:
    # -------------------------------------------------------------------------
    print()
    print("Testing the  GET_READING  and   GET_DETECTED_COLOR_NAME  methods")
    print(" of the  COLOR_SENSOR  of the robot.")
    input("Press the ENTER key when ready to start printing the color sensed.")

    # -------------------------------------------------------------------------
    # TODO: 3. With the robot's color_sensor, repeatedly:
    #    -- Call its   get_reading   method and print the result (an integer)
    #    -- Call its   get_detected_color_name   method
    #         and print the result (a string that is the name of a color)
    #  each time through the loop asking for input,
    #  and stopping when the user enters a string other than the empty string.
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # Test the  wait_until_color  method of the  color_sensor  of the robot:
    # -------------------------------------------------------------------------
    print()
    print("Testing the  WAIT_UNTIL_COLOR  method")
    print(" of the  COLOR_SENSOR  of the robot.")
    input("Press the ENTER key when ready to wait until BLACK is sensed.")

    # -------------------------------------------------------------------------
    # TODO: 4. Call the  wait_until_color  method of the   color_sensor
    #  of the robot, checking to be sure that when it senses black
    #  (which you can simulate by lifting the robot) the code continues.
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # TODO: 5. Add additional tests as needed to ensure that the
    #  wait_until_color  method works correctly with each of the 7 colors
    #  that it can sense.  Test strings (upper, lower and mixed case)
    #  and numbers for the colors.
    # -------------------------------------------------------------------------


main()
