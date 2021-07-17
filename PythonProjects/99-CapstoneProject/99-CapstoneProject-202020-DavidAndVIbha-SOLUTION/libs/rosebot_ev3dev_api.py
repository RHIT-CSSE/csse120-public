"""
Capstone Team Project.  Contains the lower-level code for (only)
the devices used in this Capstone Team Project.

Winter term, 2019-2020.
"""

###############################################################################
# STUDENTS:  *** Do NOT change ANYTHING in this module. ***
###############################################################################
import ev3dev.ev3 as ev3


###############################################################################
#    Motor
###############################################################################
class Motor(object):
    """
    Controls a single EV3 Motor.  Our robot has 2 "large" motors for the wheels
    and a "medium" motor to control the arm/claw.
    """

    def __init__(self, port, motor_type='large'):
        """
        Constructs a Motor based on the input parameters.  Valid ports:
          'A', 'B', 'C', or 'D'
          Our "large" motors are in ports "B" and "C"
          Our "medium" motor is in port "A"
        Valid motor_types: "medium" or "large"
        ---
        :param port: Letter on EV3 brick where motor connects
        :type port: str
        :param motor_type: Motor types are either "medium" or "large"
        :type motor_type: str
        """
        if motor_type == 'large':
            self._motor = ev3.LargeMotor('out' + port)
        else:
            self._motor = ev3.MediumMotor('out' + port)

    def turn_on(self, speed):
        """
        Turns on the motor at the requested speed. Valid speeds:
          -100 up to 100
        For example:
          -100 full speed in reverse
          -50 slow reverse
          0 coast to a stop
          30 slow forwards
          60 pretty fast forwards
          100 max speed forwards
        ---
        :param speed: Duty cycle percentage for motor
        :type speed: int
        """
        self._motor.run_direct(duty_cycle_sp=speed)

    def turn_off(self, stop_action="brake"):
        """
        Stops the motor.
        Note: turn_off is similar to turn_on(0), but turn_off
              tries to stop the motion a bit faster using the  brake  option.
        """
        self._motor.stop(stop_action=stop_action)

    def get_position(self):
        """
        Returns the position of the motor since the last reset.
        Units are in degrees
        :return: Position of the motor in degrees
        :rtype: int
        """
        return self._motor.position

    def reset_position(self):
        """

        :return:
        """
        self._motor.position = 0


###############################################################################
#    TouchSensor
###############################################################################
class LowLevelTouchSensor(object):
    """
    An object associated with a physical Touch Sensor that is plugged into
    a port (1, 2, 3, or 4).  It can report whether or not the Touch Sensor
    is pressed or not.
    """
    def __init__(self, port=None):
        """
        The  port  must be 1, 2, 3, 4, or None, where  None  means to attempt
        to autodetect a port into which a physical Touch Sensor is plugged.
        ---
        :param port:  The port (1, 2, 3, or 4) into which a Touch Sensor is
                      plugged, or None to attempt to autodetect such a port.
        :type port: int | None
        """
        if port not in (1, 2, 3, 4, None):
            message = "The port for a TouchSensor must be\n"
            message += "1, 2, 3, or 4, or None to attempt\n"
            message += "to autodetect a physical Touch Sensor."
            raise ValueError(message)

        if port is not None:
            self._touch_sensor = ev3.TouchSensor('in' + str(port))
        else:
            self._touch_sensor = ev3.TouchSensor()  # Attempt to autodetect

    def get_reading(self):
        """
        Returns 1 if this the physical Touch Sensor associated with this
        TouchSensor is pressed, else returns 0.
        ---
        :rtype: int
        """
        return self._touch_sensor.is_pressed  # 1 (pressed) or 0 (not pressed)
