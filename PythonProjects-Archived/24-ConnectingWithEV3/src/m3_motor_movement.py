"""
The goal of this module is to again use the rosebot library, but with a motor

Authors: David Mutchler, Vibha Alangar, Dave Fisher, and PUT_YOUR_NAME_HERE.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

# -----------------------------------------------------------------------------
# TODO: 2.  Add an IMPORT like like that in the previous module, that is:
#        import rosebot_ev3dev_api as rose_ev3
#  Then open the file that is imported and search for the  Motor   class
#  so that you can understand what it does.  ASK QUESTIONS AS DESIRED.
#  Change the above _TODO_ to DONE when you know how to:
#    -- Construct a  Motor  object that is connected to a robot wheel/tread.
#    -- Make the Motor turn on.
#    -- Make the Motor turn off.
#    -- Use  time.sleep(...)  to provide time during which the Motor(s) turn
#       and hence the robot moves.
#  (The code below may help you understand these.)
# -----------------------------------------------------------------------------
import time


def main():
    # -------------------------------------------------------------------------
    # TODO: 3. Create a  Motor  object connected to Port C
    #  (that is, connected to the Large Motor that controls the RIGHT
    #  motor/wheel/tread) by examining the code below for the LEFT
    #  motor/wheel/tread and doing similarly for the RIGHT motor/wheel/tread.
    # -------------------------------------------------------------------------
    left_motor = rose_ev3.Motor("B")

    # -------------------------------------------------------------------------
    # TODO: 4.  Modify the example code below to make the robot move
    #   in some interesting way (using the motors), perhaps
    #   following the circumference of a circle or driving in a square.
    # -------------------------------------------------------------------------
    print("Look at your EV3 robot -->")
    input("Press the ENTER key when ready for the robot to start moving.")
    for k in range(3):
        left_motor.turn_on(30)
        time.sleep(3)
        left_motor.turn_on(80)
        time.sleep(0.5)
        left_motor.turn_off()
        time.sleep(2)

    print("Goodbye")


main()
