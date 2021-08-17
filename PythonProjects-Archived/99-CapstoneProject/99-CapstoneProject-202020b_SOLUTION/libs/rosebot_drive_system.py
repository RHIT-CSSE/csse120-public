"""
Capstone Team Project.  Code to run on the EV3 robot (NOT on a laptop).

This code defines the DriveSystem class, for making the robot move.

Authors:  Your professors (for the framework)
    and PUT_YOUR_NAMES_HERE.
Winter term, 2019-2020.
"""
# TODO: Put the name of EACH team member who contributes
#   to this module in the above.


import rosebot_ev3dev_api as rose_ev3
import time


###############################################################################
#    DriveSystem
###############################################################################
class DriveSystem(object):
    """
    Controls the robot's motion via methods that include:
      go                         stop
      go_straight_for_seconds    go_straight_for_inches
      spin_in_place_for_seconds  spin_in_place_for_degrees
      turn_for_seconds           turn_for_degrees
    """

    # -------------------------------------------------------------------------
    # NOTE:
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
    #   The RoseBot's "wheels" have diameter about 1.3 inches.
    # -------------------------------------------------------------------------

    def __init__(self, left_motor_port, right_motor_port):
        """
        Constructs two Motor objects (for the left and right wheels).
          :type left_motor_port:  str  (must be 'A', 'B', 'C' or 'D')
          :type right_motor_port: str  (must be 'A', 'B', 'C' or 'D')
          """
        # ---------------------------------------------------------------------
        # TODO: With your instructor, implement this method.
        # ---------------------------------------------------------------------
        self.left_motor = rose_ev3.Motor("B")
        self.right_motor = rose_ev3.Motor("C")

    def go(self, left_wheel_speed, right_wheel_speed):
        """
        Makes the left and right wheel motors spin at the given speeds
        (which should each be integers between -100 and 100).
          :type left_wheel_speed:  int
          :type right_wheel_speed: int
        """
        # ---------------------------------------------------------------------
        # TODO: Implement this method.
        # ---------------------------------------------------------------------
        self.left_motor.turn_on(left_wheel_speed)
        self.right_motor.turn_on(right_wheel_speed)

    def stop(self):
        """ Stops the left and right wheel motors. """
        # ---------------------------------------------------------------------
        # TODO: Implement this method.
        # ---------------------------------------------------------------------
        self.left_motor.turn_off()
        self.right_motor.turn_off()

    def go_straight_for_seconds(self, seconds, speed=50):
        """
        Makes the robot go straight (forward if speed > 0, else backward)
        for the given number of seconds at the given speed.
          :type seconds: float
          :type speed:   int
        """
        # ---------------------------------------------------------------------
        # TODO: Implement this method.
        # ---------------------------------------------------------------------
        self.go(speed, speed)
        time.sleep(seconds)
        self.stop()

    def go_straight_for_inches(self, inches, speed=50):
        """
        Makes the robot go straight (forward if speed > 0, else backward)
        for the given number of inches at the given speed, using the
        encoder (degrees traveled sensor, "position") built into the motors.
          :type inches: float
          :type speed:  int
        """
        # ---------------------------------------------------------------------
        # TODO: Implement this method.
        # ---------------------------------------------------------------------
        self.go(speed, speed)
        target_degrees = self.left_motor.get_position() + inches * 80  # Roughly 1" = 90 degrees
        while True:
            time.sleep(0.1)
            # print("Target {}, current {}".format(target_degrees, self.left_motor.get_position()))
            if self.left_motor.get_position() >= target_degrees:
                break
        self.stop()

    def spin_in_place_for_seconds(self, seconds, speed=50):
        """
        Makes the robot spin in place for the given number of seconds
        at the given speed.
          :type seconds: float
          :type speed:   int
        """
        # ---------------------------------------------------------------------
        # TODO: Implement this method.
        # ---------------------------------------------------------------------
        self.go(speed, -speed)
        time.sleep(seconds)
        self.stop()

    def spin_in_place_for_degrees(self, degrees, speed=50):
        """
        Makes the robot spin in place the given number of degrees
        at the given speed.
          :type degrees: float
          :type speed:   int
        """
        # ---------------------------------------------------------------------
        # TODO: Implement this method.
        # ---------------------------------------------------------------------
        self.go(speed, -speed)
        target_degrees = self.left_motor.get_position() + degrees * 5  # Ballpark
        # TODO: Check for non-matching signs in the degrees and speed combos
        #  (i.e. go backwards, but wait for a forward value of degrees will go forever)
        while True:
            time.sleep(0.1)
            # print("Target {}, current {}".format(target_degrees, self.left_motor.get_position()))
            if self.left_motor.get_position() >= target_degrees:
                break
        self.stop()

    def turn_for_seconds(self, seconds, speed):
        """
        Makes the robot turn for the given number of seconds
        at the given speed.  The
          :type seconds: float
          :type speed:   int
        """
        # ---------------------------------------------------------------------
        # TODO: Implement this method.
        # ---------------------------------------------------------------------
        if speed > 0:
            self.go(speed, 0)
        else:
            self.go(0, speed)
        time.sleep(seconds)
        self.stop()

    def turn_for_degrees(self, degrees, speed):
        """
        Makes the robot turn the given number of degrees
        at the given speed.
          :type degrees: float
          :type speed:   int
        """
        # ---------------------------------------------------------------------
        # TODO: Implement this method.
        # ---------------------------------------------------------------------
        target_degrees = self.left_motor.get_position() + degrees * 10  # Roughly
        if speed > 0:
            self.go(speed, 0)
        else:
            self.go(0, speed)
            target_degrees = -target_degrees
        while True:
            time.sleep(0.1)
            # print("Target {}, current {}".format(target_degrees, self.left_motor.get_position()))
            if self.left_motor.get_position() >= target_degrees:
                break
        self.stop()
