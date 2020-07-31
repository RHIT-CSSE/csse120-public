"""
Capstone Team Project.  Code to run on a ROBOT (NOT a laptop).

This module is for testing STAND-ALONE code running on the ROBOT
(WITHOUT having LAPTOP GUI code running on the LAPTOP at the same time).
In particular, it tests the   BrickButtons   class.

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
    """ Tests the   BrickButtons   of a Snatch3r robot. """
    print()
    print("--------------------------------------------------")
    print("Testing the  BrickButtons  of a robot")
    print("--------------------------------------------------")

    # -------------------------------------------------------------------------
    # TODO: 3. The following constructs a RoseBot object, then sends it as an
    #  argument to the TEST functions. In those TEST functions, you will
    #  access the RoseBot object's   brick_buttons   instance variable to make
    #  the physical buttons on the EV3 Brick do things.
    #  Change this _TODO_ to DONE after you understand the following code.
    # -------------------------------------------------------------------------
    robot = rb.RoseBot()
    run_test_brick_buttons(robot)


def run_test_brick_buttons(robot):
    """
    Tests the  is...pressed    methods of the BrickButtons class.
      :type robot: rb.RoseBot
    """
    print('--------------------------------------------------')
    print('Testing the  is...pressed   methods')
    print("  of the   BrickButtons   class.")
    print('--------------------------------------------------')

    print()
    print("In the output that will appear, you should see:")
    print("  OUTPUT indicating brick buttons are pressed and")
    print("  LEDs changing colors in response, as described.")
    print("  in the testing code.")
    print("Stop this test by pressing  Control-C  when desired.")
    input("Press the ENTER key when ready to start blinking LEDs.")

    try:
        while True:
            # -----------------------------------------------------------------
            # TODO: 4. This code is inside a   try ... except  clause so that
            #  when you press  Control-C  to stop the program, it "catches"
            #  that "exception" and allows the program to continue to the
            #  next set of tests.
            #  _
            #  Replace the  pass  statement below with code that:
            #  will light the appropriate LEDs
            #  when buttons on the EV3 Brick are pressed:
            #      [IF TEAM MEMBER HAS NOT YET DONE
            #          lab3a_leds
            #       then replace the following with PRINT statements for now
            #       and return to LED action after   lab3a_leds   is done]
            #    - When up is pressed, light both LEDs green
            #    - When down is pressed, light both LEDs red
            #    - When left is pressed, light the left LED amber
            #    - When right is pressed, light the right LED amber
            #    - When backspace is pressed, break from the loop
            #        and end the program
            #    - When no button is pressed turn the LEDs off
            #  Note, only 1 button will be pressed at a time.
            # -----------------------------------------------------------------
            pass

    except KeyboardInterrupt:
        print()
        print("OK, you just did a keyboard interrupt (Control-C).")
        print("No worries. The program will keep running from here.")
