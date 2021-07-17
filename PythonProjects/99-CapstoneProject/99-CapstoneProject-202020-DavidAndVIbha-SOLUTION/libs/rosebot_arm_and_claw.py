"""
Capstone Team Project.  Code to run on a ROBOT (NOT a laptop).

This code defines the   ArmAndClaw   class  that controls
the physical arm and the physical claw that works in tandem with the arm.

Authors:  Your professors (for the framework)
    and PUT_YOUR_NAME_HERE.
Winter term, 2019-2020.
"""
# TODO: 1. In the above, put the names of EACH team member who contributes
#  (in any way) to this module.

# -----------------------------------------------------------------------------
# TODO: 2. Note that this module uses two libraries from LIBS:
#     rosebot_touch_sensor
#     rosebot_ev3dev_api  (for its Motor class)
#  Change this _TODO_ to DONE after you have seen that.
# -----------------------------------------------------------------------------
import libs.rosebot_touch_sensor as touch
import libs.rosebot_ev3dev_api as rose_ev3


###############################################################################
#    ArmAndClaw
###############################################################################
class ArmAndClaw(object):
    """
    Controls the robot's arm and claw (which operate together).
    Contains methods:
      calibrate_arm   raise_arm   move_arm_to_position   lower_arm
    """
    # -------------------------------------------------------------------------
    # TODO: 3. Read the following IMPORTANT and CRITICAL Note, ASKING QUESTIONS
    #  AS NEEDED. Once you understand the note, change this _TODO_ to DONE.
    # -------------------------------------------------------------------------
    # NOTE:
    #   A POSITIVE speed for the ArmAndClaw's motor moves the arm UP.
    #   A NEGATIVE speed for the ArmAndClaw's motor moves the arm DOWN.
    #   It takes about   14 revolutions    of the ArmAndClaw's motor
    #     to go from all the way UP to all the way DOWN.
    # CRITICAL:  If your physical Arm gets stuck (because of an error in your
    #   code, probably, it will HEAT UP and eventually MELT the Arm's Motor.
    #   So be SURE that your physical Arm is not trying to go beyond what
    #   it can go. If you DO hear a clicky sound or the Arm's Motor gets hot,
    #   UNPLUG the Arm's Motor.
    # -------------------------------------------------------------------------
    def __init__(self, touch_sensor, port="A"):
        """
        Constructs the ArmAndClaw's motor that is plugged into the given port.
        Stores the given (already constructed) TouchSensor that is used to stop
        the ArmAndClaw in its UP position.

        :type  touch_sensor: touch.TouchSensor
        :type  port:  str
          The port must be "A", "B", "C", or "D" (defaults to "A").
        """
        # ---------------------------------------------------------------------
        # TODO: 4. Read the following, ASKING QUESTIONS AS NEEDED.
        #  Once you understand the code, change this _TODO_ to DONE.
        # ---------------------------------------------------------------------

        # The arm motor should always use a 100% duty cycle for its speed.
        self.speed = 100

        self.arm_touch_sensor = touch_sensor
        self.arm_motor = rose_ev3.Motor(port, motor_type="medium")
        self.is_calibrated = False

    def calibrate_arm(self):
        """
        Calibrates its Arm, that is:
          1. Turn on this ArmAndClaw's arm_motor at this ArmAndClaw's speed.
               (This will make the ArmAndClaw start going UP.)
          2. Wait for this ArmAndClaw's touch_sensor to be PRESSED.
               (This will make the ArmAndClaw go to its all-the-way UP position.
                Watch carefully to be sure that it does not get STUCK without
                ever pressing the physical Touch Sensor.)
          3. STOP this ArmAndClaw's arm_motor.
          4. Turn on this ArmAndClaw's arm_motor at the NEGATIVE of
             this ArmAndClaw's speed.
               (This will make the ArmAndClaw start going DOWN.)
          5. Wait for this ArmAndClaw's arm_motor to go 14 revolutions.
               (This will make the ArmAndClaw go all the way DOWN.
                Watch carefully to be sure that it does not get STUCK trying
                to go beyond what it physically can go.)
          6. Reset this ArmAndClaw's motor position to 0.
               (The   move_arm_to_position   method will make the assumption
                that this ArmAndClaw's motor position is 0 when the Arm is all
                the way DOWN; doing this reset is critical to ensure that fact.)
        Then sets self.is_calibrated to True,
        to indicate that this ArmAndClaw is now calibrated.
        """
        # ---------------------------------------------------------------------
        # TODO: 5. Implement this method, WITH YOUR INSTRUCTOR.
        # ---------------------------------------------------------------------
        # SOLUTION CODE: Delete from the project given to students.
        self.arm_motor.turn_on(self.speed)
        self.arm_touch_sensor.wait_until_pressed()
        self.arm_motor.turn_off()
        self.arm_motor.turn_on(-self.speed)
        self.arm_motor.reset_position()
        while True:
            current_position = self.arm_motor.get_position()
            if abs(current_position) > 14 * 360:
                self.arm_motor.turn_off()
                break
        self.is_calibrated = True

    def raise_arm(self):
        """ Raises the Arm until its physical Touch Sensor is pressed. """
        # ---------------------------------------------------------------------
        # TODO: 6. Implement this method; it is a ONE-LINER!
        # ---------------------------------------------------------------------
        # SOLUTION CODE: Delete from the project given to students.
        self.arm_touch_sensor.wait_until_pressed()

    def move_arm_to_position(self, desired_arm_position):
        """
        If this ArmAndClaw has not yet been calibrated, calibrate it now.
        Then move this ArmAndClaw to the given desired_arm_position,
        where 0 means all the way DOWN.
        """
        # ---------------------------------------------------------------------
        # TODO: 7. Implement this method, WITH YOUR INSTRUCTOR.
        # ---------------------------------------------------------------------
        # SOLUTION CODE: Delete from the project given to students.
        if not self.is_calibrated:
            self.calibrate_arm()

        starting_position = self.arm_motor.get_position()
        distance_to_move = abs(desired_arm_position - starting_position)
        if desired_arm_position > starting_position:
            self.arm_motor.turn_on(self.speed)
        else:
            self.arm_motor.turn_on(-self.speed)

        while True:
            current_position = self.arm_motor.get_position()
            distance_traveled = abs(current_position - starting_position)
            if distance_traveled >= distance_to_move:
                self.arm_motor.turn_off()
                break
        # Show the desired and actual positions, just for grins:
        message = "Desired position: {}.  Actual position reached: {}."
        print(message.format(desired_arm_position,
                             self.arm_motor.get_position()))

    def lower_arm(self):
        """
        Lowers the Arm until it is all the way down, i.e., position 0.
        If the robot has not yet calibrated its ArmAndClaw, it does so first.
        """
        # ---------------------------------------------------------------------
        # TODO: 8. Implement this method; it is a ONE-LINER!
        # ---------------------------------------------------------------------
        # SOLUTION CODE: Delete from the project given to students.
        self.move_arm_to_position(0)
