"""
This module contains the top-level code for the RoseBot robot library.

CSSE 120 students should use this module, NOT the rosebot_low_level
module that contains lower-level implementations.
"""

import rosebot_low_level as rbll
import collections
from enum import Enum, unique
import time

SIGNAL = collections.namedtuple('SIGNAL', ['pin_type', 'pin_number'])
LED_PIN = SIGNAL(rbll.RoseBotDigitalOutput, 13)
HIGH = 1
LOW = 0

SIMULATE = False
DC = None

class SENSOR_PINS(object):
    pins = {'left_bump_sensor': SIGNAL(rbll.RoseBotDigitalInput, 3),
            'right_bump_sensor': SIGNAL(rbll.RoseBotDigitalInput, 10),

            'left_proximity_sensor': SIGNAL(rbll.RoseBotAnalogInput, 0),
            'front_proximity_sensor': SIGNAL(rbll.RoseBotAnalogInput, 4),
            'right_proximity_sensor': SIGNAL(rbll.RoseBotAnalogInput, 5),

            'left_reflectance_sensor': SIGNAL(rbll.RoseBotAnalogInput, 3),
            'middle_reflectance_sensor': SIGNAL(rbll.RoseBotAnalogInput, 6),
            'right_reflectance_sensor': SIGNAL(rbll.RoseBotAnalogInput, 7),
            }


@unique
class MOTORS_ENCODERS(Enum):
    left_wheel = 1
    right_wheel = 2


class RoseBot(object):

    def __init__(self):
        """
        Initializes a RoseBot that has:
          -- self.connection: for Python-to-robot communication
          -- self.differential_drive:
                              for making the robot move
          -- self.camera:     for doing things with the Pixy camera
          -- self.buzzer:     for making noises
          -- self.led:        for turning the LED on and off
          -- Sensor objects for sensing its environment:
              -- self.left_bump_sensor
              -- self.right_bump_sensor

              -- self.left_reflectance_sensor
              -- self.middle_reflectance_sensor
              -- self.right_reflectance_sensor

              -- self.left_proximity_sensor
              -- self.front_proximity_sensor
              -- self.right_proximity_sensor

              -- self.left_encoder    for how many "ticks"
              -- self.right_encoder   a wheel has turned
        """
        self.connection = None  # Established via  connect_wifly
        self.differential_drive = DifferentialDrive()
        self.camera = None  # PixyCamera() established after connecting
        self.buzzer = None  # Buzzer() established after connecting
        self.led = LED()

        self.left_bump_sensor = BumpSensor('left')
        self.right_bump_sensor = BumpSensor('right')

        self.left_proximity_sensor = ProximitySensor('left')
        self.front_proximity_sensor = ProximitySensor('front')
        self.right_proximity_sensor = ProximitySensor('right')

        self.left_reflectance_sensor = ReflectanceSensor('left')
        self.middle_reflectance_sensor = ReflectanceSensor('middle')
        self.right_reflectance_sensor = ReflectanceSensor('right')

        self.left_encoder = Encoder(MOTORS_ENCODERS.left_wheel)
        self.right_encoder = Encoder(MOTORS_ENCODERS.right_wheel)

    def connect_wifly(self, robot_number):
        """
        What comes in: An integer that is the number written on the
          WiFly on the phyical RoseBot.
        What goes out: Nothing (i.e., None).
        Side effects:
          -- Establishes a Connection that is used "under the hood" to:
               -- Send commands from the Python program to the robot.
               -- Receive information from the robot.
          -- Sets this RoseBot's  connection  instance variable
               to that Connection.
        Raises a  ConnectionFailed  exception if the connection
        cannot be establish (e.g. if the robot is not turned on).

        Example:
          robot = rb.RoseBot()
          robot.connect_wifly(23)

        Note: This method accepts its argument in any of several
        equivalent forms, per these examples:
          robot.connect_wifly(23)
          robot.connect_wifly('23')
          robot.connect_wifly('r23')
          robot.connect_wifly('r23.wlan.rose-hulman.edu')
        """
        self.connection = Connection(robot_number)
        print('Connected!  Robot is ready to run!')

        if SIMULATE:
            print('Running in SIMULATION mode')
        self._establish_connections_for_subcomponents()

    def connect_wired(self, com_port=None):
        """
        Similar to connect_wifly, except a wired connection.
        """
        self.connection = Connection(None, com_port)
        print('Connected!  Robot is ready to run!')

        if SIMULATE:
            print('Running in SIMULATION mode')
        self._establish_connections_for_subcomponents()

    def _establish_connections_for_subcomponents(self):
        """
        Private method for establishing connections to the lower-level
        objects that do the heavy lifting.
        """
        if SIMULATE:
            board = None
        else:
            board = self.connection._low_level_connection
        self.camera = PixyCamera(board)
        self.buzzer = Buzzer(board)

        if SIMULATE:
            return
        lower_level_led = LED_PIN.pin_type(board, LED_PIN.pin_number)
        self.led._connect_to_board(lower_level_led)

        for sensor_name, pin in SENSOR_PINS.pins.items():
            sensor = self.__getattribute__(sensor_name)
            lower_level_sensor = pin.pin_type(board, pin.pin_number)
            sensor.connect_to_board(lower_level_sensor)


class Connection(object):
    """
    Handles communication between the Python program
    and the robot with which it is communicating.
    """

    def __init__(self, robot_number=None, com_port=None,
                 use_log_file=False):
        """
        Establishes the PyMata3 object that is used "under the hood" to:
          -- Send commands from the Python program to the robot.
          -- Receive information from the robot.
        Raises a  ConnectionFailed  exception if the connection
        cannot be establish (e.g. if the robot is not turned on).
        """
        if robot_number is not None:
            ip_address = str(robot_number)
            if len(ip_address) == 1:
                ip_address = '0' + ip_address
            if not ip_address.startswith('r'):
                ip_address = 'r' + ip_address
            if not ip_address.endswith('.wlan.rose-hulman.edu'):
                ip_address = ip_address + '.wlan.rose-hulman.edu'
        elif com_port is not None:
            ip_address = None
            com_port = str(com_port)
            if not com_port.startswith('COM'):
                com_port = 'COM' + com_port
        else:
            ip_address = None

        if SIMULATE:
            return
        connection = rbll.Connection(ip_address, com_port,
                                     use_log_file=use_log_file)
        self._low_level_connection = connection.board

    def sleep(self, seconds):
        """
        What comes in: A positive number.
        What goes out: Nothing (i.e., None).
        Side effects:
          Pauses the program for the given number of seconds.
        Example (assuming   connection   is a Connection for a RoseBot):
           connection.sleep(2.5)   [pauses the program for 2.5 seconds]

        Note that:
          1. The ROBOT continues doing whatever it was doing
               (e.g. moving).
          2. A Connection maintains a "heartbeat" to the robot.
             In part because of that, you must use the robot's
             connection.sleep   method and NOT the   time.sleep
             method to make the program pause.
        """
        if SIMULATE:
#             time.sleep(seconds)
            for _ in range(int(seconds / 0.01)):
                time.sleep(0.01)
                DC.root.update()
        else:
            self._low_level_connection.sleep(seconds)

    def shutdown(self):
        """ Shuts down the robot, leaving it in a "clean" state. """
        if SIMULATE:
            print('Robot is shut down (in simulation mode)')
            return
        self._low_level_connection.shutdown()


class DifferentialDrive(object):
    """ A  DifferentialDrive  controls all robot movement. """

    def __init__(self):
        """
        Establishes a connection to the low-level object
        that does the heavy lifting.
        """
        if SIMULATE:
            return
        self._lower_level_differential_drive = rbll.DifferentialDrive()

    def drive_pwm(self, left_wheel_power, right_wheel_power):
        """
        What comes in: Two integers, each between -255 and 255.
        What goes out: Nothing (i.e., None).
        Side effects:
          Makes the robot move at the given power levels, where
            -200 is full-speed backward and
             200 is full-speed forward.
        Examples (where   drive   is a DifferentialDrive object
        for a RoseBot that has established a Connection):
           drive.drive_pwm(200, 200)   [full speed forward]
           drive.drive_pwm(100, -100)  [spin clockwise in place]
           drive.drive_pwm(-50, -50)   [backwards, slowly]
           drive.drive_pwm(50, 180)    [forwards, veering to the left]
        Type hints:
          :type left_wheel_power:  int
          :type right_wheel_power: int
        """
        if SIMULATE:
            print('Robot is moving in simulation mode:')
            fstring = '  Left and right wheel speeds are: {:4} {:4}'
            print(fstring.format(left_wheel_power, right_wheel_power))
            DC.draw_line(0, 0, 100, 100)
            return
        self._lower_level_differential_drive.drive_pwm(left_wheel_power,
                                                       right_wheel_power)

    def stop(self):
        """
        What comes in: Nothing (i.e., no arguments).
        What goes out: Nothing (i.e., None).
        Side effects:  Makes the robot stop.
        Example (where   drive   is a DifferentialDrive object
        for a RoseBot that has established a Connection):
           robot.stop()
        """
        if SIMULATE:
            print('Robot is stopped (in simulation mode)')
            return
        self.drive_pwm(0, 0)


class LED(object):

    def on(self):
        """ Turns the LED fully ON. """
        if SIMULATE:
            print('LED is ON (in simulation mode)')
            return
        self._lower_level_led.digital_write(HIGH)

    def off(self):
        """ Turns the LED fully OFF. """
        if SIMULATE:
            print('LED is OFF (in simulation mode)')
            return
        self._lower_level_led.digital_write(LOW)

    def _connect_to_board(self, lower_level_led):
        """
        Private method that establishes a connection to the low-level
        object that does the heavy lifting.
        """
        self._lower_level_led = lower_level_led


class Encoder(object):
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

    def __init__(self, which_encoder):
        self.which_encoder = which_encoder

        if which_encoder == MOTORS_ENCODERS.left_wheel:
            self.low_level_encoder = rbll.LeftWheelEncoder()
        else:
            self.low_level_encoder = rbll.RightWheelEncoder()

    def get_ticks(self):
        """
        Returns the number of "ticks" that this Encoder's associated
        Motor has spun since this Encoder was last reset.
        """
        if SIMULATE:
            print('The  get_ticks  method is not implemented in simulation mode')
            return 1
        return self.low_level_encoder.get_ticks()

    def reset(self):
        """
        Resets this Encoder for purposes of further reporting
        by self.get_ticks()
        """
        if SIMULATE:
            print('Encoder is reset to 0 (in simulation mode)')
            return
        return self.low_level_encoder.reset()

    def read(self):
        """ A synonym for get_ticks. """
        return self.get_ticks()


class Sensor(object):
    """
    A Sensor can return a reading (i.e., current value of the Sensor).
    """

    def __init__(self, position_on_robot, type_of_sensor):
        self.position_on_robot = position_on_robot
        self.name = (position_on_robot +
                     '_' + type_of_sensor +
                     '_sensor')

    def connect_to_board(self, lower_level_sensor):
        if SIMULATE:
            return
        self.lower_level_sensor = lower_level_sensor

    def read(self):
        """
        Returns the current value of this Sensor.
        """
        if SIMULATE:
            print('The  read  method is not implemented in simulation mode')
            return 1
        return self.lower_level_sensor.read()


class BumpSensor(Sensor):
    """ A BumpSensor can be bumped (1) or not bumped (0). """

    def __init__(self, position_on_robot):
        super().__init__(position_on_robot, 'bump')

    def is_pressed(self):
        """
        Returns True if this Bump Sensor is pressed, else returns False.
        """
        return self.read() == 0


class ProximitySensor(Sensor):
    """ A ProximitySensor returns distance: 0 (far) to 4095 (close). """

    def __init__(self, position_on_robot):
        super().__init__(position_on_robot, 'proximity')

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

    def __init__(self, position_on_robot):
        super().__init__(position_on_robot, 'reflectance')

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


class PixyCamera(rbll.RoseBotPixy):
    """
    Methods include:  get_block() and get_blocks().
    They return a PixyBlock and list of PixyBlocks, respectively.
    A PixyBlock has instance variables:  x, y, width, height,
    plus a method  size().
    """
    def __init__(self, board):
        if SIMULATE:
            return
        super().__init__(board)



class Buzzer(rbll.RoseBotBuzzer):
    """
    Methods include:
      - play_tone(n) plays tone  n  (try 220, 440 et al).
      - stop()
    """
    def __init__(self, board):
        if SIMULATE:
            return
        super().__init__(board)

    def play_tone(self, note, duration_s=None):
        if SIMULATE:
            fstring = 'Robot is playing note {}'
            print(fstring.format(note))
            return
        super().play_tone(note, duration_s=duration_s)

    def stop(self):
        if SIMULATE:
            print('Robot has stopped buzzing')
            return
        super().stop()

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

