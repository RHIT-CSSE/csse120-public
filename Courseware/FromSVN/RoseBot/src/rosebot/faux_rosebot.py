"""
This "faux" (fake) library simply PRINTs messages on the Console
when robot commands are given.  As such, it exposes the API and
can be useful for including mock code in GUI code.
"""

# The next is just for an Enum. TODO: All enums to a module.
from rosebot.command import SIGNAL

import sys
from enum import Enum, unique
import random


# TODO: Maybe just use Position for this:
@unique
class MOTORS_ENCODERS(Enum):
    left_wheel = 1
    right_wheel = 2

@unique
class Position(Enum):
    left = 1
    right = 2
    front = 3
    back = 4
    front_left = 5
    front_middle = 6
    front_right = 7
    # TODO Add to the above as needed.

@unique
class ConnectionType(Enum):
    wired = 1
    wireless = 2

class Status(Enum):
    off = 0
    on = 1
    maximum_value = 255


@unique
class SensorType(Enum):
    analog = 1
    digital = 2
    reflectance = 3
    proximity = 4
    bump = 5

# TODO allow a simulation mode?


class RoseBot(object):

    def __init__(self):
        """
        Initializes a RoseBot that has:
          -- self.connector:
                    To connect/disconnect to/from a RoseBot.
          -- self.motor_controller:
                    To make the RoseBot move.
          -- self.camera:
                    To manipulate the Pixy camera and get blobs from it.
          -- self.buzzer:
                    To play tones (i.e., make noises).
          -- self.led:
                    To turn the built-in RoseBot LED on/off.
          -- self.sensor_reader:
                    To sense the robot's environment
                    The standard sensors are:
              -- self.sensor_reader.left_bump_sensor
              -- self.sensor_reader.right_bump_sensor

              -- self.sensor_reader.left_reflectance_sensor
              -- self.sensor_reader.middle_reflectance_sensor
              -- self.sensor_reader.right_reflectance_sensor

              -- self.sensor_reader.left_proximity_sensor
              -- self.sensor_reader.front_proximity_sensor
              -- self.sensor_reader.right_proximity_sensor

              -- self.sensor_reader.button_sensor

              -- self.sensor_reader.left_encoder_sensor
              -- self.sensor_reader.right_encoder_sensor
                    These return how many "ticks" the wheel has turned.
        """
        self.connector = Connector()
        self.motor_controller = MotorController(self.connector)
#         self.camera = Camera(self.connector)
        self.buzzer = Buzzer(self.connector)
        self.led = LED(self.connector)
        self.sensor_reader = SensorReader(self.connector)


class Connector(object):
    """
    A Connector can connect to the RoseBot and disconnect from it.
    It also sets up the Communicator for the "under the hood"
    Python/Arduino communication.
    """
    def __init__(self):
        self._communicator = None  # Set when CONNECT runs.

    def connect(self, port=None, robot_number=None, simulate=False):
        """
        What comes in:  ONE of the following:
            -- port           -> Wired connection via that port
            -- robot_number   -> Wireless connection to the RoseBot
                               whose WiFly is labelled with that number
        What goes out:
           True if the connection was successful, else False.
        Side effects:
          -- Establishes a Communicator that is used "under the hood"
             for the Python program to send/receive messages and/or
             commands to/from the Arduino on the RoseBot.
        Examples:
            robot = rb.RoseBot()
               followed by ONE of the following:
            robot.connector.connect(port=4)           # Wired
            robot.connector.connect(robot_number=7)  # Wireless

        You can also use strings as port or robot_number, e.g.:
            robot.connector.connect(port='com4')
            robot.connector.connect(robot_number='r07')
        """
        print('Connected!  The faux (fake) robot is ready to run!')

    def connect_wired(self, port=None):
        print('Connected in WIRED mode!')
        print('The faux (fake) robot is ready to run!')

    def connect_wireless(self, robot_number=None):
        print('Connected in WIRELESS mode!')
        print('The faux (fake) robot is ready to run!')

    def disconnect(self):
        """ Disconnects from the RoseBot.  Program keeps running. """
        print('The robot is DISCONNECTED from this program.')

    def shutdown(self):
        """
        Disconnects from the RoseBot and exits the program gracefully.
        """
        print('Disconnecting from the robot gracefully ...')
        print('Shutting down this program gracefully ...')

    def _send_command(self, command, data):
        """ Private method to send commands to the robot. """
        print('Private method.  Students: Do NOT use this method')

    def _get_result(self):
        print('Private method.  Students: Do NOT use this method')


class RobotComponent(object):
    """
    Every RobotConnection (e.g. its LED) has a Connector
    that it can use to send its Commands to the robot.
    """
    def __init__(self, connector, abort_if_failure=True):
        self.connector = connector
        self.command = None  # Each component has its own Command(s).
        self.abort_if_failure = abort_if_failure

    def _send_command(self, command, data=None, source=None):
        print('Private method.  Students: Do NOT use this method')

    def _get_result(self):
        print('Private method.  Students: Do NOT use this method')


class LED(RobotComponent):
    def __init__(self, connector):
        super().__init__(connector)

    def turn_on(self):
        """ Turns the LED fully ON. """
        print('The LED is fully ON.')


    def turn_off(self):
        """ Turns the LED fully OFF. """
        print('The LED is fully OFF.')


class Buzzer(RobotComponent):
    """
    Methods include:
      - play_tone(n) plays tone  n  (try 220, 440 et al).
      - stop()
    """
    def __init__(self, connector):
        super().__init__(connector)

    def play_tone(self, tone):
        print('Playing tone: {} on the Buzzer.'.format(tone))

    def stop(self):
        print('The Buzzer has STOPPED making any noise.')


class MotorController(RobotComponent):
    """ A  MotorController  controls the robot's motors on its wheels. """

    def __init__(self, connector):
        super().__init__(connector)

    def drive_pwm(self, left_wheel_pwm, right_wheel_pwm):
        """
        What comes in: Two integers, each between -255 and 255.
        What goes out: Nothing (i.e., None).
        Side effects:
          Makes the robot move at the given power levels, where
            -255 is full-speed backward and
             255 is full-speed forward.
        Examples (where   drive   is a DifferentialDrive object
        for a RoseBot that has established a Connection):
           drive.drive_pwm(255, 255)   [full speed forward]
           drive.drive_pwm(100, -100)  [spin clockwise in place]
           drive.drive_pwm(-50, -50)   [backwards, slowly]
           drive.drive_pwm(50, 180)    [forwards, veering to the left]
        Note: Depending on the power source, the actual pwm may
              be throttled to a smaller number than 255.
        Type hints:
          :type left_wheel_power:  int
          :type right_wheel_power: int
        """
        print('Making the left and right wheels turn at pwm:')
        print('  Left: {}.  Right: {}'.format(left_wheel_pwm,
                                              right_wheel_pwm))
        print('Both are on a scale of -255 to 255.')

    def left_wheel_pwm(self, left_wheel_pwm):
        print('Making the LEFT wheel turn at pwm:')
        print('  Left: {}.'.format(left_wheel_pwm))
        print('Scale of -255 to 255.')

    def right_wheel_pwm(self, right_wheel_pwm):
        print('Making the RIGHT wheel turn at pwm:')
        print('  Right: {}.'.format(right_wheel_pwm))
        print('Scale of -255 to 255.')

    def _wheel_pwm(self, control_signal_1, control_signal_2, pwm_signal,
                   pwm):
        print('    Private method.  Students: Do NOT use this method')

    def stop(self):
        print('Making both wheels STOP.')


class SensorReader(RobotComponent):
    def __init__(self, connector):
        super().__init__(connector)

        self.left_bump_sensor = BumpOrButtonSensor(connector, SIGNAL.left_bump_sensor)
        self.right_bump_sensor = BumpOrButtonSensor(connector, SIGNAL.right_bump_sensor)
        self.button_sensor = BumpOrButtonSensor(connector, SIGNAL.button_sensor)

        self.left_proximity_sensor = ProximitySensor(connector, SIGNAL.left_proximity_sensor)
        self.front_proximity_sensor = ProximitySensor(connector, SIGNAL.front_proximity_sensor)
        self.right_proximity_sensor = ProximitySensor(connector, SIGNAL.right_proximity_sensor)

        self.left_reflectance_sensor = ReflectanceSensor(connector, SIGNAL.left_reflectance_sensor)
        self.middle_reflectance_sensor = ReflectanceSensor(connector, SIGNAL.middle_reflectance_sensor)
        self.right_reflectance_sensor = ReflectanceSensor(connector, SIGNAL.right_reflectance_sensor)

#         self.left_encoder = Encoder(connector, SIGNAL.left_encoder)
#         self.right_encoder = Encoder(connector, SIGNAL.right_encoder)


class Sensor(RobotComponent):

    def __init__(self, connector, signal, is_analog=True):
        super().__init__(connector)
        self.signal = signal
        self.is_analog = is_analog

    def read(self):
        """ Returns the current value of this Sensor. """
        print('Reading a sensor: {}:'.format(self.signal))
        print('  Received a (fake) message from the (fake) robot.')
        print('  Returning a (fake) result that is chosen at random:')
        if self.analog:
            value_to_return = random.randrange(1024)
        else:
            value_to_return = random.randrange(2)
        print('    Value returned = {}.'.format(value_to_return))

        return value_to_return


class BumpOrButtonSensor(Sensor):
    """ A BumpOrButtonSensor can be bumped (1) or not bumped (0). """

    def __init__(self, connector, signal):
        super().__init__(connector, signal, is_analog=False)

    def is_pressed(self):
        """
        Returns True if this Bump Sensor is pressed, else returns False.
        """
        print('Reading the sensor: {}'.format(self.signal))
        return self.read() == 0


class ProximitySensor(Sensor):
    """ A ProximitySensor returns distance: 0 (far) to 4095 (close). """

    def __init__(self, connector, signal):
        super().__init__(connector, signal, is_analog=True)

    def distance_to_object_seen(self):
        """
        Returns a number from 0 to 4095 that indicates the distance
        that the nearest object detected by this Proximity Sensor
        is from this Proximity Sensor.
          small -> far distance
                    (i.e., the object is far from this Proximity Sensor)
          big   -> close distance
                    (i.e., the object is close to this Proximity Sensor)

        The readings depend on many factors including the physical
        characteristics of the sensor (no two are exactly alike),
        the ambient light, and more.
        """
        print('Reading the sensor: {}'.format(self.signal))
        return self.read()


class ReflectanceSensor(Sensor):
    """ A ReflectanceSensor returns light: 0 (low) to 4095 (lots). """

    def __init__(self, connector, signal):
        super().__init__(connector, signal, is_analog=True)

    def reflectance_reading(self):
        """
        Returns a number from 0 to 4095 that indicates the amount
        of light that is bouncing back to this Reflectance Sensor.
          0    -> very little light is bouncing back.
          2048 -> lots of light is bouncing back.

        The readings depend on many factors including the physical
        characteristics of the sensor (no two are exactly alike),
        the ambient light, and more.
        """
        print('Reading the sensor: {}'.format(self.signal))
        return self.read()


# class Encoder(object):
#     """
#     An Encoder measures the rate (and hence also the distance)
#     at which its associated Motor spins.
#
#     It uses "ticks" as its units of distance, where "ticks" is a
#     motor/encoder-dependent unit.
#
#     The WheelSystem that includes this Encoder along with its
#     associated Motor and the actual wheel itself could convert
#     from "ticks" to centimeters per second that the wheel itself
#     turned / traveled.
#     """
#
#     def __init__(self, which_encoder):
#         self.which_encoder = which_encoder
#
# #         if which_encoder == MOTORS_ENCODERS.left_wheel:
# #             self.low_level_encoder = rbll.LeftWheelEncoder()
# #         else:
# #             self.low_level_encoder = rbll.RightWheelEncoder()
#
#     def get_ticks(self):
#         """
#         Returns the number of "ticks" that this Encoder's associated
#         Motor has spun since this Encoder was last reset.
#         """
# #         return self.low_level_encoder.get_ticks()
#
#     def reset(self):
#         """
#         Resets this Encoder for purposes of further reporting
#         by self.get_ticks()
#         """
# #         return self.low_level_encoder.reset()
#
#     def read(self):
#         """ A synonym for get_ticks. """
#         return self.get_ticks()





class Camera(object):
    """
    Methods include:  get_block() and get_blocks().
    They return a PixyBlock and list of PixyBlocks, respectively.
    A PixyBlock has instance variables:  x, y, width, height,
    plus a method  size().
    """
    def __init__(self):
        # TODO
        pass




class RobotError(Exception):
    default_message = """
    The error might have been caused by a bug in our code
    (if so, submit a bug report to your instuctor)
    or by a hardware failure (if so, get help as needed)
    or by something your code does wrong in using this library.
    """

    def __init__(self, message=None, output_file=sys.stderr):
        self.message = message
        self.output_file = output_file

    def print_message(self):
        print('An error has occurred in the RoseBot code.')
        if self.message :
            print(self.message)
        elif self.message is None:
            print(RobotError.default_message, file=self.output_file)


class RobotError_NoConnector(RobotError):
    def __init__(self, source=None):
        message = "I can't do the action you requested"
        if source:
            message += 'in the  ' + source + '  class'
        message += 'because this program is not currently'
        message += 'connected to a robot.  Nothing done.'

        super().__init__(message)


class RobotError_UnknownError(RobotError):
    pass


class __FreezeClass__ (type):
    """
    Students: IGNORE this class!  It just works behind the scenes
    to help you learn to use the  DataContainer  below.
    """
    def __setattr__(self, name, _):  # Value argument is unused.
        err = "You tried to set the instance variable '" + name + "'\n"
        err += "on the CLASS '" + self.__name__ + "'.\n"
        err += "You probably meant to set that instance variable\n"
        err += "on an INSTANCE of that CLASS.  Did you forget\n"
        err += "the () after to the word '" + self.__name__ + "',\n"
        err += "on the line where you CONSTRUCTED the instance?"

        raise SyntaxError(err)

