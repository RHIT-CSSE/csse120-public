"""
Capstone Team Project.  Code to run on a ROBOT (NOT a laptop).

This module is for testing STAND-ALONE code running on the ROBOT
(WITHOUT having LAPTOP GUI code running on the LAPTOP at the same time).
In particular, it tests the   Leds   class.

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
    """ Tests the   Leds   of a Snatch3r robot. """
    print()
    print("--------------------------------------------------")
    print("Testing the  Leds  of a robot")
    print("--------------------------------------------------")

    # -------------------------------------------------------------------------
    # TODO: 3. The following constructs a RoseBot object, then sends it as an
    #  argument to the TEST functions. In those TEST functions, you will
    #  access the RoseBot object's   leds   instance variable to make
    #  the physical LEDs turn on and off with various colors.
    #  Change this _TODO_ to DONE after you understand the following code.
    # -------------------------------------------------------------------------
    robot = rb.RoseBot()

    run_test_leds_on_off(robot)
    run_test_leds_colors(robot)


def run_test_leds_on_off(robot):
    """
    Tests the   turn_off   and set_color   method of the   Leds   class.
      :type robot: rb.RoseBot
    """
    print()
    print("--------------------------------------------------")
    print("Testing the  turn_off   and set_color   methods")
    print("  of the   Leds   class.")
    print("--------------------------------------------------")

    print()
    print("In the output that will appear, you should see:")
    print("  - both LEDs are on  RED  for 1 second,")
    print("  - then off for 1 second, repeating forever")
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
            #    Calls the  set_color  and  turn_off methods on the   leds
            #    of the robot, so that
            #      - "both" LEDs are on "red" for 1 second,
            #      - then off for 1 second
            #    (repeating forever, use Control-C to stop the program).
            #  In addition to the LEDs, print to the console
            #  "Both LEDs ON as RED" or "LEDs OFF" just before the LED change
            #  line of code (so you can see it and read it).
            # -----------------------------------------------------------------
            pass

    except KeyboardInterrupt:
        print()
        print("OK, you just did a keyboard interrupt (Control-C).")
        print("No worries. The program will keep running from here.")


def run_test_leds_colors(robot):
    """
        Tests the   leds_on_off   method of the   ArmAndClaw   class.
          :type robot: rb.RoseBot
        """
    print()
    print("--------------------------------------------------")
    print("MORE testing of the  turn_off   and set_color")
    print("  methods of the   Leds   class.")
    print("--------------------------------------------------")

    left_colors = ["red", "green", "amber", "off", "red", "off",
                   "green", "off", "amber", "off"]
    right_colors = ["red", "green", "amber", "off", "off",
                    "red", "off", "green", "off", "amber"]

    # -------------------------------------------------------------------------
    # TODO: 5. Call the  set_color  method of the   leds   of the robot,
    #  so that the color changes through each value in the lists above,
    #  one after the other. Instead of using a 1 second delay between colors,
    #  have the user press the enter key to change to the next colors.
    #  (See above for how to do that.)  After the final value in the list,
    #  turn off both LEDs.
    # -------------------------------------------------------------------------

