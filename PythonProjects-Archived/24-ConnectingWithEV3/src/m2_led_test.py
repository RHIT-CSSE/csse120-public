"""
The goal of this module is to practice using the  rosebot_ev3dev_api  library
(API), aka rose_ev3.

Authors: David Mutchler, Vibha Alangar, Dave Fisher, and PUT_YOUR_NAME_HERE.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

# -----------------------------------------------------------------------------
# TODO: 2. As usual when there is a file of "library" code (here, the
#   rosebot_ev3dev_api.py file), Right-Click on the  src  folder
#   and select   Mark Directory As -> Sources Root.
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# TODO: 3.  Uncomment the IMPORT line below (the one that is commented-out).
#  Then open the file that is imported and search for the  Led   class
#  so that you can understand what it does.  ASK QUESTIONS AS DESIRED.
#  Change the above _TODO_ to DONE when you know how to:
#    -- Construct a Led object for a LED on the robot.
#    -- Set the color of the LED.
#    -- Turn the LED off.
#  (The code below may help you understand these.)
# -----------------------------------------------------------------------------
# import rosebot_ev3dev_api as rose_ev3
import time


def main():
    # -------------------------------------------------------------------------
    # TODO: 4. Create a Led object for the RIGHT LED by examining the code
    #          below for the LEFT LED and doing similarly for the RIGHT LED.
    # -------------------------------------------------------------------------
    left_led = rose_ev3.Led("left")

    # -------------------------------------------------------------------------
    # TODO: 5. Modify the example code below to make something interesting
    #          happen with the left and right LEDs. Perhaps police lights or ...
    # -------------------------------------------------------------------------
    print("Look at your EV3 robot -->")
    for k in range(10):
        left_led.set_color("red")
        time.sleep(0.25)
        left_led.turn_off()
        time.sleep(0.25)

    left_led.set_color("green")
    print("Goodbye")


main()
