"""
THROW-AWAY Capstone Project. If you mess up this THROW-AWAY project,
  ** no worries. **
It lets you practice skills & concepts needed for the REAL Capstone Project.

This module contains a   DriveSystem   class that is the same as the full
DriveSystem class that you will implement later, but restricted to the methods
that are relevant to this THROW-AWAY project.

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
#    from . import rosebot_ev3dev_api as rose_ev3
#    import time
#  Make sure you understand WHY those imports are needed.
# -----------------------------------------------------------------------------
# SOLUTION CODE: Delete later.
import libs.rosebot_ev3dev_api as rose_ev3
import time


###############################################################################
#    DriveSystem
###############################################################################
class DriveSystem(object):
    """
    Controls the robot's motion via methods that (so far) include:
       go   stop    go_straight_for_seconds
    """
    # -------------------------------------------------------------------------
    # TODO: 4. Read and digest the following NOTE:
    #   To "go straight" means that both wheels move at the same speed.
    #     -- Positive speeds should make the robot move forward.
    #     -- Negative speeds should make the robot move backward.
    #   To "spin_in_place" means that the wheels move at speeds S and -S.
    #     -- Positive speeds should make the robot spin clockwise
    #          (i.e., left motor goes at speed S, right motor at speed -S).
    #     -- Negative speeds should make the robot spin counter-clockwise
    #          (i.e., left motor goes at speed -S, right motor at speed S).
    #   To "turn" means that one wheel does not move and the other does move:
    #     -- Positive speeds should make only the left motor move
    #          (and hence the turn is clockwise).
    #     -- Negative speeds should make only the right motor move
    #          (and hence the turn is counter-clockwise).
    #   All distances (inches or degrees) should be POSITIVE numbers.
    #   The RoseBot's "wheels" have diameter about 1.3 inches.
    #  _
    #  Once you understand the above, change this _TODO_ to DONE.
    # -------------------------------------------------------------------------

    def __init__(self, left_motor_port="B", right_motor_port="C"):
        """
        Constructs two Motor objects (for the left and right wheels), plugged
        into the given ports. Each Motor object must be a "large" motor.

        Stores those Motor objects as:
           self.left_motor
           self.right_motor
        ---
        :param left_motor_port:  Letter on EV3 brick where LEFT motor connects.
        :type  left_motor_port:  str
        :param right_motor_port: Letter on EV3 brick where RIGHT motor connects.
        :type  right_motor_port: str
        Each port must be "A", "B", "C", or "D" (defaults to "B" and "C").
          """
        # ---------------------------------------------------------------------
        # TODO: 5. With your instructor, implement this method.
        # ---------------------------------------------------------------------
        # SOLUTION, delete for final version:
        self.left_motor = rose_ev3.Motor(left_motor_port)
        self.right_motor = rose_ev3.Motor(right_motor_port)

    def go(self, left_wheel_speed, right_wheel_speed):
        """
        Makes the left and right wheel motors spin at the given speeds.
          (More accurately, at the given duty-cycle, which is a percent of
          the maximum possible speed given the current battery level.)

        Speeds are expected to be integers between -100 and 100,
          where positive means forward, negative means backward, and
          zero (0) means to coast to a stop (also see the  stop  method below).
        ---
        :param left_wheel_speed:  Speed (duty-cycle) for the LEFT motor.
        :type  left_wheel_speed:  int
        :param right_wheel_speed: Speed (duty-cycle) for the RIGHT motor.
        :type  right_wheel_speed: int
        """
        # ---------------------------------------------------------------------
        # TODO: 6. With your instructor, implement this method.
        # ---------------------------------------------------------------------
        # SOLUTION, delete for final version:
        self.left_motor.turn_on(left_wheel_speed)
        self.right_motor.turn_on(right_wheel_speed)

    def stop(self, stop_action="brake"):
        """
        Stops the left and right wheel motors.
          By default uses applies a "brake" in stopping, as opposed to
          setting a speed of 0 which allows the motor to "coast" to a stop.
        ---
        :param stop_action: String that represents the action by which to stop.
        :type  stop_action: str
        """
        # ---------------------------------------------------------------------
        # TODO: 7. With your instructor, implement this method.
        # ---------------------------------------------------------------------
        # SOLUTION, delete for final version:
        self.left_motor.turn_off(stop_action)
        self.right_motor.turn_off(stop_action)

    def go_straight_for_seconds(self, seconds, speed=50, stop_action="brake"):
        """
        Makes the robot go straight for the given number of seconds at the
        given speed, stopping using the given stop_action.

        Speed must be a non-zero integer between -100 and 100,
          where positive means forward and negative means backward.

        Prints an error message (and goes nowhere) if seconds <= 0
        or speed == 0.

        Implemented using the pattern:
          1. Start the wheel-motors moving at the specified speed
               (using the   go   method).
          2. "Sleep" (do nothing else) while the robot is moving, for the
               specified number of seconds (using the  time.sleep   function).
          3. Stop the wheel-motors (using the  stop   method).
        ---
        :param seconds: Seconds to move. Prints an error message if negative.
        :type  seconds: float
        :param speed:   Speed at which to move: forward if 1 to 100,
                        backward if -1 to -100, error otherwise.
        :type  speed:   int
        :param stop_action: String that represents the action by which to stop.
        :type  stop_action: str
        """
        # ---------------------------------------------------------------------
        # TODO: 8. Implement this method
        #          (with help from your instructor as needed).
        # ---------------------------------------------------------------------
        # SOLUTION, delete for final version:
        if seconds <= 0:
            print("The first argument (seconds to travel)")
            print("must be positive. You supplied:", seconds)
            print("No movement done!")
        elif speed == 0:
            print("The second argument (speed)")
            print("must not be zero. You supplied:", speed)
            print("No movement done!")
        else:
            self.go(speed, speed)
            time.sleep(seconds)
            self.stop(stop_action)
