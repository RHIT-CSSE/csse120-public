"""
The top-level code for the "standard" RoseBot library.

CSSE 120 students should use ONLY the classes, instance variables
and methods defined in this module.  They should NOT use the low-level
modules that this library uses.  Nor should they use "private"
attributes (those that begin with an underscore) in any module.
"""

import rosebot.serial_communicator
import rosebot.socket_communicator
# The next is just for an Enum. TODO All enums to a module.
from rosebot.command import SIGNAL

import sys
from enum import Enum, unique
import time


# TODO Maybe just use Position for this:
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
class PixySignature(Enum):
    Red = 1
    Orange = 2
    Yellow = 3
    Green = 4
    Cyan = 5  # A light blue
    Blue = 6
    Violet = 7


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
        self.buzzer = Buzzer(self.connector)
        self.led = LED(self.connector)
        self.sensor_reader = SensorReader(self.connector)
        self.camera = PixyCamera(self.connector)


class Connector(object):
    """
    A Connector can connect to the RoseBot and disconnect from it.
    It also sets up the Communicator for the "under the hood"
    Python/Arduino communication.
    """

    def __init__(self, tk_root=None):
        self._communicator = None  # Set when CONNECT runs.
        self.port = None
        self.address = None
        self.tk_root = tk_root  # For a thread to get sensor readings.

    def connect(self, port=None, robot_number=None):
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
        # TODO Add a "simulate" mode that ...

        # TODO Do error-handling in the following.

        if port is not None:
            self.connect_wired(port)
        elif robot_number is not None:
            self.connect_wireless(robot_number)
        else:
            print('Connection FAILED:')
            print('You must specify either a PORT or a ROBOT-NUMBER.')
            return

        if self.tk_root:
            self.tk_root.after(self.sensor_read_rate,
                               self.update_sensor_readings)

    def connect_wired(self, port):
        # port can be specified as shown by the following examples:
        #   Integer: 4 -> 'COM4'
        #   String that represents an integer:  '4' -> 'COM4'
        #   Any other string: port is that string
        try:
            self.port = 'COM' + str(int(port))
        except:
            self.port = port

        self.connection_type = ConnectionType.wired
        self._communicator = (rosebot.serial_communicator.
                              SerialCommunicator(self.port,
                                                 connect=True))

        print('Connected (wired) to port: {}.'.format(self.port))

    def connect_wireless(self, robot_address):
        # address can be specified as shown by the following examples:
        #   Integer: 4  -> 'r04.wlan.rose-hulman.edu'
        #   Integer: 18 -> 'r18.wlan.rose-hulman.edu'
        #   String that represents an integer:  as above.
        #   'r' followed by string that represents an integer: as above.
        #   Any other string: address is that string
        suffix = '.wlan.rose-hulman.edu'

        robot_number = None
        if type(robot_address) is int:
            robot_number = robot_address
        else:
            try:
                if robot_address.lower().startswith('r'):
                    robot_number = int(robot_address[1:])
                else:
                    robot_number = int(robot_address)
            except:
                pass

        if robot_number:
            prefix = 'r0' if robot_number < 10 else 'r'
            self.address = prefix + str(robot_number) + suffix
        else:
            self.address = robot_address

        self.connection_type = ConnectionType.wireless
        print('Making a socket communicator')
        self._communicator = (rosebot.socket_communicator.
                              SocketCommunicator(self.address,
                                                 connect=True))
        print('Connected (wireless) to address: {}.'.
              format(self.address))

    def disconnect(self):
        """
        Disconnects gracefully from the RoseBot.
        The program keeps running.
        """
        self._communicator.disconnect()
        if self.port:
            print('Disconnected from wired connection on', self.port)
        elif self.address:
            print('Disconnected from wireless address', self.address)
        else:
            pass  # Should not happen.  TODO Add error handling

    def _send_command(self, command, data):
        """ Private method to send commands to the robot. """
        self._communicator.send_command(command, data)

    def _get_result(self, command):
        # TODO Deal with messages that are more than a single byte.
        return self._communicator.receive_command_data(command)


class RobotComponent(object):
    """
    Every RobotConnection (e.g. its LED) has a Connector
    that it can use to send its Commands to the robot.
    """
    # TODO It is not clear to me what the default should be
    #   for abort_if_failure.

    def __init__(self, connector, abort_if_failure=True):
        self.connector = connector
        self.command = None  # Each component has its own Command(s).
        self.abort_if_failure = abort_if_failure

    def _send_command(self, command, data=None, source=None):
        is_failure = False
        try:
            self.connector._send_command(command, data)
        except AttributeError:
            is_failure = True
            if self.connector is None:
                RobotError_NoConnector(source).print_message()
        except:
            is_failure = True
            if self.abort_if_failure:
                raise

        return is_failure

    def _get_result(self, command):
        # TODO Add error-handling.
        return self.connector._get_result(command)


class LED(RobotComponent):

    def __init__(self, connector):
        super().__init__(connector)

    def turn_on(self):
        """ Turns the LED fully ON. """
        self._send_command(rosebot.command.LEDCommand(), 1,
                           source='"on" method of the "LED"')

    def turn_off(self):
        """ Turns the LED fully OFF. """
        self._send_command(rosebot.command.LEDCommand(), 0,
                           source='"off" method of the "LED"')
    # CONSIDER Should this sensor do an ANALOG write,
    # in which case it could set the level of the light?
    # Then we woud have another method which sets the light
    # level to (say) a percent of maximum or (perhaps) 0 to 255.


class Buzzer(RobotComponent):
    """
    Methods include:
      - play_tone(n) plays tone  n  (try 220, 440 et al).
      - stop()
    """

    def __init__(self, connector):
        super().__init__(connector)

    # TODO Maybe implement duration.
    def play_tone(self, tone):
        self._send_command(rosebot.command.BuzzerCommand(), tone,
                           source='"play_tone" method of the "Buzzer"')

    def stop(self):
        self._send_command(rosebot.command.BuzzerCommand(), 0,
                           source='"stop" method of the "Buzzer"')


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
        self._wheel_control(SIGNAL.left_motor_control_1,
                            SIGNAL.left_motor_control_2,
                            left_wheel_pwm)
        self._wheel_control(SIGNAL.right_motor_control_1,
                            SIGNAL.right_motor_control_2,
                            right_wheel_pwm)
        self._wheel_pwm(SIGNAL.left_motor_pwm, left_wheel_pwm)
        self._wheel_pwm(SIGNAL.right_motor_pwm, right_wheel_pwm)

    def left_wheel_pwm(self, left_wheel_pwm):
        self._wheel_control(SIGNAL.left_motor_control_1,
                            SIGNAL.left_motor_control_2,
                            left_wheel_pwm)
        self._wheel_pwm(SIGNAL.left_motor_pwm, left_wheel_pwm)

    def right_wheel_pwm(self, right_wheel_pwm):
        self._wheel_control(SIGNAL.right_motor_control_1,
                            SIGNAL.right_motor_control_2,
                            right_wheel_pwm)
        self._wheel_pwm(SIGNAL.right_motor_pwm, right_wheel_pwm)

    def _wheel_control(self, control_signal_1, control_signal_2, pwm):
        command1 = rosebot.command.MotorControlCommand(control_signal_1)
        command2 = rosebot.command.MotorControlCommand(control_signal_2)
        source = '"_wheel_control" method of the "MotorController"'
        if pwm > 0:
            self._send_command(command1, 1, source)
            self._send_command(command2, 0, source)
        else:
            self._send_command(command1, 0, source)
            self._send_command(command2, 1, source)

    def _wheel_pwm(self, pwm_signal, pwm):
        command3 = rosebot.command.MotorPWMCommand(pwm_signal)
        source = '"_wheel_pwm" method of the "MotorController"'
        if pwm > 0:
            self._send_command(command3, pwm, source)
        else:
            self._send_command(command3, -pwm, source)

    def stop(self):
        # This is NOT right.  Should use control 1-1 or 0-0, I think.
        #    TODO Which should be the default: brake or stop?
        self.drive_pwm(0, 0)


class SensorReader(RobotComponent):

    def __init__(self, connector):
        super().__init__(connector)

        self.left_bump_sensor = BumpOrButtonSensor(
            connector, SIGNAL.left_bump_sensor)
        self.right_bump_sensor = BumpOrButtonSensor(
            connector, SIGNAL.right_bump_sensor)
        self.button_sensor = BumpOrButtonSensor(
            connector, SIGNAL.button_sensor)

        self.left_proximity_sensor = ProximitySensor(
            connector, SIGNAL.left_proximity_sensor)
        self.front_proximity_sensor = ProximitySensor(
            connector, SIGNAL.front_proximity_sensor)
        self.right_proximity_sensor = ProximitySensor(
            connector, SIGNAL.right_proximity_sensor)

        self.left_reflectance_sensor = ReflectanceSensor(
            connector, SIGNAL.left_reflectance_sensor)
        self.middle_reflectance_sensor = ReflectanceSensor(
            connector, SIGNAL.middle_reflectance_sensor)
        self.right_reflectance_sensor = ReflectanceSensor(
            connector, SIGNAL.right_reflectance_sensor)

        self.left_encoder = Encoder(connector, SIGNAL.left_encoder)
        self.right_encoder = Encoder(connector, SIGNAL.right_encoder)


class Sensor(RobotComponent):

    def __init__(self, connector, signal, is_analog=True):
        super().__init__(connector)
        self.signal = signal
        self.is_analog = is_analog
        self.cached_reading = None
        self.cached_timestamp = None

        # Get a reading from the cached copy if the cached copy
        # was within this many seconds of the current time.
        self.when_stale = 0

    def read(self):
        """ Returns the current value of this Sensor. """
        if not self._is_stale():
            print('c', end='')
            return self.cached_reading

        if self.is_analog:
            command = rosebot.command.AnalogReadSensorCommand(self.signal)
        else:
            command = rosebot.command.DigitalReadSensorCommand(self.signal)

        # TODO Make the source be the subclass actually running here.
        source = '"read" method of sensor'
        self._send_command(command, source=source)

#         OLD:
#         Currently analog results are right-shifted 2 bits
#         to make the 10-bit result fit in an 8-bit byte.
#         So multiply the result by 4 for analog.
        result = self._get_result(command)

        self._cache(result)
        return result

    def _cache(self, reading):
        """ Cache (store) the given reading for fast lookup later. """
        self.cached_reading = reading
        self.cached_timestamp = time.time()

    def _is_stale(self):
        return (self.cached_reading is None) or (
            time.time() - self.cached_timestamp >= self.when_stale)


class BumpOrButtonSensor(Sensor):
    """ A BumpOrButtonSensor can be bumped (1) or not bumped (0). """

    def __init__(self, connector, signal):
        super().__init__(connector, signal, is_analog=False)

    def is_pressed(self):
        """
        Returns True if this Bump Sensor is pressed, else returns False.
        """
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
        return self.read()


class Encoder(Sensor):
    """
    An Encoder measures the rate (and hence also the distance)
    at which its associated Motor spins.

    It uses "ticks" as its units of distance, where "ticks" is a
    motor/encoder-dependent unit.

    The WheelSystem that includes this Encoder along with its
    associated Motor and the actual wheel itself could convert
    from "ticks" to centimeters per second that the wheel itself
    turned / traveled.
    """

    def __init__(self, connector, encoder_signal):
        super().__init__(connector, encoder_signal, is_analog=True)

    def get_ticks(self):
        """
        Returns the number of "ticks" that this Encoder's associated
        Motor has spun since this Encoder was last reset.
        """
        return self.read()

    def reset(self):
        """
        Resets this Encoder for purposes of further reporting
        by self.get_ticks()
        """
        self._send_command(rosebot.command.EncoderResetCommand(self.signal),
                           source='"reset" method of the "Encoder"')


class PixyCamera(RobotComponent):
    """
    Methods include:  get_block() and get_blocks().
    They return a PixyBlock and list of PixyBlocks, respectively.
    A PixyBlock has instance variables:  x, y, width, height,
    plus a method  size().
    """

    def __init__(self, connector):
        super().__init__(connector)

    def get_block(self, signature=PixySignature.Red):
        """ Turns the LED fully ON. """
        command = rosebot.command.PixyCameraCommand()
        self._send_command(command, signature,
                           source='"get_block" method of the "PixyCamera"')
        return self._get_result(command)


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
        if self.message:
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
