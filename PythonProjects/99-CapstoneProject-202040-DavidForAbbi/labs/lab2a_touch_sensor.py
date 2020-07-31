"""
Capstone Team Project.  Code to run on a ROBOT (NOT a laptop).

This module is for testing STAND-ALONE code running on the ROBOT
(WITHOUT having LAPTOP GUI code running on the LAPTOP at the same time).
In particular, it tests the   TouchSensor   class.

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
    """ Tests the   TouchSensor   of a Snatch3r robot. """
    print()
    print("--------------------------------------------------")
    print("Testing the  TOUCH SENSOR  of a robot")
    print("--------------------------------------------------")

    # -------------------------------------------------------------------------
    # TODO: 3. The following constructs a   TouchSensor   object,
    #  then sends it as an argument to the TEST functions. In those TEST
    #  functions, you will access the methods of the TouchSensor object.
    #  Change this _TODO_ to DONE after you understand the following code.
    # -------------------------------------------------------------------------
    robot = rb.RoseBot()

    run_test_get_reading(robot)
    run_test_is_pressed(robot)
    run_test_wait_until_pressed(robot)
    run_test_wait_until_released(robot)


def run_test_get_reading(robot):
    """
    Tests the   get_reading   method of the   TouchSensor   class.
       :type robot: rb.RoseBot
    """
    print()
    print("--------------------------------------------------")
    print("Testing the   get_reading   method")
    print("  of the   TouchSensor   class.")
    print("--------------------------------------------------")

    print()
    print("In the output that will appear, you should see:")
    print("  1  when the physical Touch Sensor is pressed")
    print("  0  when the physical Touch Sensor is NOT pressed")
    print("Stop this test by pressing  Control-C  when desired.")
    input("Press the ENTER key when ready to start getting readings.")
    try:
        while True:
            # -----------------------------------------------------------------
            # TODO: 4. This code is inside a   try ... except  clause so that
            #  when you press  Control-C  to stop the program, it "catches"
            #  that "exception" and allows the program to continue to the
            #  next set of tests.
            #  _
            #  Replace the  pass  statement below with code that:
            #    a. Calls the   get_reading   method on the given TouchSensor,
            #         storing the returned value in a variable if you like.
            #    b. Prints that returned value.
            #    c. Sleeps for 0.5 seconds so that you are not overwhelmed
            #         by the output.
            # -----------------------------------------------------------------
            pass

    except KeyboardInterrupt:
        print()
        print("OK, you just did a keyboard interrupt (Control-C).")
        print("No worries. The program will keep running from here.")


def run_test_is_pressed(robot):
    """
    Tests the   is_pressed   method of the   TouchSensor   class.
       :type robot: rb.RoseBot
    """
    print()
    print("--------------------------------------------------")
    print("Testing the   is_pressed   method")
    print("  of the   TouchSensor   class.")
    print("--------------------------------------------------")

    print()
    print("In the output that will appear, you should see:")
    print("  True   when the physical Touch Sensor is pressed")
    print("  False  when the physical Touch Sensor is NOT pressed")
    print("Stop this program by pressing  Control-C  when desired.")
    input("Press the ENTER key when ready to start getting readings.")
    try:
        while True:
            # -----------------------------------------------------------------
            # TODO: 5. This code is inside a   try ... except  clause so that
            #  when you press  Control-C  to stop the program, it "catches"
            #  that "exception" and allows the program to continue to the
            #  next set of tests.
            #  _
            #  Replace the  pass  statement below with code that:
            #    a. Calls the   is_pressed   method on the given TouchSensor,
            #         storing the returned value in a variable if you like.
            #    b. Prints that returned value.
            #    c. Sleeps for 0.5 seconds so that you are not overwhelmed
            #         by the output.
            # -----------------------------------------------------------------
            pass

    except KeyboardInterrupt:
        print()
        print("OK, you just did a keyboard interrupt (Control-C).")
        print("No worries. The program will keep running from here.")


def run_test_wait_until_pressed(robot):
    """
    Tests the   wait_until_pressed   method of the   TouchSensor   class.
       :type robot: rb.RoseBot
    """
    print()
    print("--------------------------------------------------")
    print("Testing the   wait_until_pressed   method")
    print("  of the   TouchSensor   class.")
    print("--------------------------------------------------")

    print()
    print("Press the ENTER key when ready to WAIT until the")
    print("Touch Sensor is pressed.  Then, when you are ready,")
    print("press the Touch Sensor, which should stop this test.")
    print("  If pressing the Touch Sensor does NOT stop this test,")
    input("  press Control-C to force this test to stop.")
    try:
        # ---------------------------------------------------------------------
        # TODO: 6. Replace the  pass  statement below with a call to
        #  the   wait_until_pressed   method on the given TouchSensor object.
        #  Then print a simple message like "Pressed!"
        # ---------------------------------------------------------------------
        pass

    except KeyboardInterrupt:
        print()
        print("OK, you just did a keyboard interrupt (Control-C).")
        print("No worries. The program will keep running from here.")


def run_test_wait_until_released(robot):
    """
    Tests the   wait_until_released   method of the   TouchSensor   class.
       :type robot: rb.RoseBot
    """
    print()
    print("--------------------------------------------------")
    print("Testing the   wait_until_released   method")
    print("  of the   TouchSensor   class.")
    print("--------------------------------------------------")

    print("Press the ENTER key when ready to WAIT until the")
    print("Touch Sensor is RELEASED.  That is, press and hold down")
    print("the Touch Sensor now, then press the ENTER key.")
    print("Then, when you are ready, RELEASE the Touch Sensor")
    input("which should stop this test.")
    print("  If releasing the Touch Sensor does NOT stop this test,")
    input("  press Control-C to force this test to stop.")
    try:
        # -------------------------------------------------------------------------
        # TODO: 7. Replace the  pass  statement below with a call to
        #  the   wait_until_released   method on the given TouchSensor object.
        #  Then print a simple message like "Released!"
        # -------------------------------------------------------------------------
        pass

    except KeyboardInterrupt:
        print()
        print("OK, you just did a keyboard interrupt (Control-C).")
        print("No worries. The program will keep running from here.")
