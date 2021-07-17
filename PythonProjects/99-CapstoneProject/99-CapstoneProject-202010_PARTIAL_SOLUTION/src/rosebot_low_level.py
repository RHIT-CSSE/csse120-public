"""
Capstone Team Project.  Code to run on the EV3 robot (NOT on a laptop).

This code contains lower-level code that interacts with the EV3 robot library.

STUDENTS:  *** Do NOT change ANYTHING in this module. ***

Fall term, 2019-2020.
"""

import ev3dev.ev3 as ev3


###############################################################################
# STUDENTS:  *** Do NOT change ANYTHING in this module. ***
###############################################################################

###############################################################################
#    Motor
###############################################################################
class Motor(object):
    # Future enhancements: Add additional methods from the many things
    # an ev3.Motor can do.

    def __init__(self, port, motor_type='large'):
        # port must be 'A', 'B', 'C', or 'D'.
        if motor_type == 'large':
            self._motor = ev3.LargeMotor('out' + port)
        else:
            self._motor = ev3.MediumMotor('out' + port)

    def turn_on(self, speed):  # speed must be -100 to 100
        self._motor.run_direct(duty_cycle_sp=speed)

    def turn_off(self):
        self._motor.stop(stop_action="brake")

    def get_position(self):  # Units are degrees (that the motor has rotated).
        return self._motor.position

    def reset_position(self):
        self._motor.position = 0


###############################################################################
#    TouchSensor
###############################################################################
class TouchSensor(object):
    def __init__(self, port):  # port must be 1, 2, 3 or 4
        self._touch_sensor = ev3.TouchSensor('in' + str(port))

    def is_pressed(self):
        """ Returns True if this TouchSensor is pressed, else returns False """
        return self._touch_sensor.is_pressed


###############################################################################
#    ColorSensor
###############################################################################
class ColorSensor(object):
    def __init__(self, port):  # port must be 1, 2, 3 or 4
        self._color_sensor = ev3.ColorSensor('in' + str(port))
        self.color_names = (
            'NoColor',
            'Black',
            'Blue',
            'Green',
            'Yellow',
            'Red',
            'White',
            'Brown',
        )

    def get_color(self):
        """
        Returns the color detected by the sensor, as best the sensor can judge
        from shining red, then green, then blue light and measuring the
        intensities returned.  The returned value is an integer between
        0 and 7, where the meanings of the integers are:
          - 0: No color
                  (that is, cannot classify the color as one of the following)
          - 1: Black
          - 2: Blue
          - 3: Green
          - 4: Yellow
          - 5: Red
          - 6: White
          - 7: Brown
        """
        return self._color_sensor.color
