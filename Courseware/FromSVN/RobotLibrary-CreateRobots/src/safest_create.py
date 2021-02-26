"""
This module was once a slightly revised implementation of the
   create
module originally designed by Zach Dodds at Harvey Mudd.

It has undergone considerable changes in detail since then,
but its essential characteristics remain unchanged from Zach's version.
"""

import serial
import socket
import math
import time
import select
import traceback
import inspect
import collections
import _thread  # thread libs needed to lock serial port during transmissions


class Sensors():
    distance = 'DISTANCE'
    angle = 'ANGLE'

    bumps_and_wheel_drops = 'BUMPS_AND_WHEEL_DROPS'
    buttons = 'BUTTONS'

    cliff_front_left_signal = 'CLIFF_FRONT_LEFT_SIGNAL'
    cliff_front_right_signal = 'CLIFF_FRONT_RIGHT_SIGNAL'
    cliff_left_signal = 'CLIFF_LEFT_SIGNAL'
    cliff_right_signal = 'CLIFF_RIGHT_SIGNAL'

    ir_byte = 'IR_BYTE'
    wall_signal = 'WALL_SIGNAL'

    song_playing = 'SONG_PLAYING'

    cliff_left = 'CLIFF_LEFT'
    cliff_front_left = 'CLIFF_FRONT_LEFT'
    cliff_front_right = 'CLIFF_FRONT_RIGHT'
    cliff_right = 'CLIFF_RIGHT'
    wall = 'WALL'

    virtual_wall = 'VIRTUAL_WALL'
    overcurrents = 'OVERCURRENTS'
    charging_state = 'CHARGING_STATE'
    voltage = 'VOLTAGE'
    current = 'CURRENT'
    battery_temperature = 'BATTERY_TEMPERATURE'
    battery_charge = 'BATTERY_CHARGE'
    battery_Capacity = 'BATTERY_CAPACITY'

    user_digital_inputs = 'USER_DIGITAL_INPUTS'
    user_analog_input = 'USER_ANALOG_INPUT'
    charging_sources_available = 'CHARGING_SOURCES_AVAILABLE'
    oi_mode = 'OI_MODE'
    song_number = 'SONG_NUMBER'

    number_of_stream_packets = 'NUMBER_OF_STREAM_PACKETS'
    velocity = 'VELOCITY'
    radius = 'RADIUS'
    right_velocity = 'RIGHT_VELOCITY'
    left_velocity = 'LEFT_VELOCITY'

version = 3.1

# The Create's baudrate and timeout:
baudrate = 57600
timeout = 0.5
# some module-level definitions for the robot commands
START = chr(128)  # already converted to bytes...
BAUD = chr(129)  # + 1 byte
CONTROL = chr(130)  # deprecated for Create
SAFE = chr(131)
FULL = chr(132)
POWER = chr(133)
SPOT = chr(134)  # Same for the Roomba and Create
CLEAN = chr(135)  # Clean button - Roomba
COVER = chr(135)  # Cover demo - Create
MAX = chr(136)  # Roomba
DEMO = chr(136)  # Create
DRIVE = chr(137)  # + 4 bytes
LEDS = chr(139)  # + 3 bytes
SONG = chr(140)  # + 2N+2 bytes, where N is the number of notes
PLAY = chr(141)  # + 1 byte
SENSORS = chr(142)  # + 1 byte
FORCESEEKINGDOCK = chr(143)  # same on Roomba and Create
# the above command is called "Cover and Dock" on the Create
DRIVEDIRECT = chr(145)  # Create only
STREAM = chr(148)  # Create only
QUERYLIST = chr(149)  # Create only
PAUSERESUME = chr(150)  # Create only
WAITTIME = chr(155)  # Added by CAB, time in 1 data byte 1 in 10ths of a second
WAITDIST = chr(156)  # Added by CAB, distance in 16-bit signed in mm
WAITANGLE = chr(157)  # Added by CAB, angle in 16-bit signed in degrees
WAITEVENT = chr(158)  # Added by CAB, event in signed event number
# MB added these for scripting
DEFINE_SCRIPT = chr(152)
RUN_SCRIPT = chr(153)
# the four SCI modes
# the code will try to keep track of which mode the system is in,
# but this might not be 100% trivial...
OFF_MODE = 0
PASSIVE_MODE = 1
SAFE_MODE = 2
FULL_MODE = 3
# Command codes are opcodes sent to the Create via serial. They define the
# possible message types.

COULD_NOT_CONNECT_ERROR_MESSAGE = \
    """
ConnectionFailedError:
I am unable to make a physical connection to the robot.
There are many possible reasons.  Check these things:
  -- Is the robot turned on?
  -- Is the port an integer or 'sim'?
  -- Is the port the correct COM number?
  -- Is the robot's battery charge adequate?

If none of the above, maybe your robot is in
a funky state.  Fix that by:
  1. Turn the robot off, pause for a few seconds,
     turn the robot back on again.
  2. Check your code to be sure that it executes a
     robot.shutdown(), since failing to do so
     can leave the robot in a funky state.
  3. Try running your program again.

If all else fails, switch to another robot
(but keep the same BAM).
"""

DISCONNECTED_ROBOT_ERROR = \
    """
It appears that when you called
   {}
the robot was NOT connected, so THAT is
probably what went wrong.  Did you disconnect it?
"""

BAD_PORT_ERROR_MESSAGE = \
    """
BadPortError:
It is VERY LIKELY that you are attempting to use
an illegal argument for the  port  parameter.

If you are running Windows:
*** Check your  port  argument ***
    to be sure that it is EITHER
      -- the STRING 'sim' or
      -- an INTEGER (no COM, no quotes).
***
"""

ROBOT_COMMAND_ERROR_MESSAGE = \
    """
RobotCommandError:
Your call to   {}   failed.
Click on the bottom blue line in the Stack Trace above
to go to that call to   {}   in your code.
Check whether your arguments to it are correct.
"""

GARBAGE_DETECTED_ERROR_MESSAGE = \
    """
SensorGarbageDetectedError:
The robot has detected sensor garbage,
hence is shutting down.  Please:
1.  Turn the robot off, pause,
    then turn the robot on again.
2.  Run your program again.

If you want to OVERRIDE this
shutting-down-when-sensor-garbage behavior,
set the 2nd argument of the Create constructor to True.
"""

SIMULATOR_NOT_OPEN_ERROR_MESSAGE = \
    """
User Error: You must start the simulator BEFORE
running your robot program.  Do so and try again.
"""

SENSOR_READ_ERROR = \
    """
RobotCommandError:
Your call to   getSensor   failed to return a value.
This appears to have been a communication
failure, NOT something wrong with your code.

Simply try running your program again.
If the problem persists, switch to another robot
(but keep the same BAM).

To go straight to the line in your code that failed:
find your call to  {}  in the Stack Trace above,
and click on the blue link directly above it.
"""

COMMANDS = {"START": chr(128),
            "BAUD": chr(129),
            "MODE_PASSIVE": chr(128),
            "MODE_SAFE": chr(131),
            "MODE_FULL": chr(132),
            "DEMO": chr(136),
            "DEMO_COVER": chr(135),
            "DEMO_COVER_AND_DOCK": chr(143),
            "DEMO_SPOT": chr(134),
            "DRIVE": chr(137),
            "DRIVE_DIRECT": chr(145),
            "LEDS": chr(139),
            "SONG": chr(140),
            "PLAY_SONG": chr(141),
            "SENSORS": chr(142),
            "QUERY_LIST": chr(149),
            "STREAM": chr(148),
            "PAUSE/RESUME_STREAM": chr(150),
            "DIGITAL_OUTPUTS": chr(147),
            "LOW_SIDE_DRIVERS": chr(138),
            "PWM_LOW_SIDE_DRIVERS": chr(144),
            "SEND_IR": chr(151),
            # MB added these for scripting
            "DEFINE_SCRIPT": chr(152),
            "RUN_SCRIPT": chr(153),
            }

# FIX ME: define the rest of the command codes in the SCI.
# Constants for array indices when sensors return an array
# Bumps and wheeldrops
WHEELDROP_CASTER = 0
WHEELDROP_LEFT = 1
WHEELDROP_RIGHT = 2
BUMP_LEFT = 3
BUMP_RIGHT = 4
# Buttons
BUTTON_ADVANCE = 0
BUTTON_PLAY = 1
# Overcurrents
LEFT_WHEEL = 0
RIGHT_WHEEL = 1
LD_2 = 2
LD_0 = 3
LD_1 = 4
# Use digital inputs
BAUD_RATE_CHANGE = 0
DIGITAL_INPUT_3 = 1
DIGITAL_INPUT_2 = 2
DIGITAL_INPUT_1 = 3
DIGITAL_INPUT_0 = 4
# Charging sources available
HOME_BASE = 0
INTERNAL_CHARGER = 1
# For the getSensor retry loop.
MIN_SENSOR_RETRIES = 2  # 1 s
RETRY_SLEEP_TIME = 0.5  # 50ms

# After this many seconds, time out when trying to make a connection:
TIMEOUT = 0.5


class SensorModule:

    def __init__(self, packetID, parseMode, packetSize):
        self.ID = packetID
        self.interpret = parseMode
        self.size = packetSize
# Sensor codes are used to ask for data along with a QUERY command.

SENSORS = {"BUMPS_AND_WHEEL_DROPS": SensorModule(chr(7), "ONE_BYTE_UNPACK", 1),
           "WALL": SensorModule(chr(8), "ONE_BYTE_UNSIGNED", 1),
           "CLIFF_LEFT": SensorModule(chr(9), "ONE_BYTE_UNSIGNED", 1),
           "CLIFF_FRONT_LEFT": SensorModule(chr(10), "ONE_BYTE_UNSIGNED", 1),
           "CLIFF_FRONT_RIGHT": SensorModule(chr(11), "ONE_BYTE_UNSIGNED", 1),
           "CLIFF_RIGHT": SensorModule(chr(12), "ONE_BYTE_UNSIGNED", 1),
           "VIRTUAL_WALL": SensorModule(chr(13), "ONE_BYTE_UNSIGNED", 1),
           "OVERCURRENTS": SensorModule(chr(14), "ONE_BYTE_UNPACK", 1),
           "IR_BYTE": SensorModule(chr(17), "ONE_BYTE_UNSIGNED", 1),
           "BUTTONS": SensorModule(chr(18), "ONE_BYTE_UNPACK", 1),
           "DISTANCE": SensorModule(chr(19), "TWO_BYTE_SIGNED", 2),
           "ANGLE": SensorModule(chr(20), "TWO_BYTE_SIGNED", 2),
           "CHARGING_STATE": SensorModule(chr(21), "ONE_BYTE_UNSIGNED", 1),
           "VOLTAGE": SensorModule(chr(22), "TWO_BYTE_UNSIGNED", 2),
           "CURRENT": SensorModule(chr(23), "TWO_BYTE_SIGNED", 2),
           "BATTERY_TEMPERATURE": SensorModule(chr(24), "ONE_BYTE_SIGNED", 1),
           "BATTERY_CHARGE": SensorModule(chr(25), "TWO_BYTE_UNSIGNED", 2),
           "BATTERY_CAPACITY": SensorModule(chr(26), "TWO_BYTE_UNSIGNED", 2),
           "WALL_SIGNAL": SensorModule(chr(27), "TWO_BYTE_UNSIGNED", 2),
           "CLIFF_LEFT_SIGNAL": SensorModule(chr(28), "TWO_BYTE_UNSIGNED", 2),
           "CLIFF_FRONT_LEFT_SIGNAL": SensorModule(chr(29),
                                                   "TWO_BYTE_UNSIGNED", 2),
           "CLIFF_FRONT_RIGHT_SIGNAL": SensorModule(chr(30),
                                                    "TWO_BYTE_UNSIGNED", 2),
           "CLIFF_RIGHT_SIGNAL": SensorModule(chr(31),
                                              "TWO_BYTE_UNSIGNED", 2),
           "USER_DIGITAL_INPUTS": SensorModule(chr(32), "ONE_BYTE_UNPACK", 1),
           "USER_ANALOG_INPUT": SensorModule(chr(33), "TWO_BYTE_UNSIGNED", 2),
           "CHARGING_SOURCES_AVAILABLE": SensorModule(chr(34),
                                                      "ONE_BYTE_UNSIGNED", 1),
           "OI_MODE": SensorModule(chr(35), "ONE_BYTE_UNSIGNED", 1),
           "SONG_NUMBER": SensorModule(chr(36), "ONE_BYTE_UNSIGNED", 1),
           "SONG_PLAYING": SensorModule(chr(37), "ONE_BYTE_UNSIGNED", 1),
           "NUMBER_OF_STREAM_PACKETS": SensorModule(chr(38),
                                                    "ONE_BYTE_UNSIGNED", 1),
           "VELOCITY": SensorModule(chr(39), "TWO_BYTE_SIGNED", 2),
           "RADIUS": SensorModule(chr(40), "TWO_BYTE_SIGNED", 2),
           "RIGHT_VELOCITY": SensorModule(chr(41), "TWO_BYTE_SIGNED", 2),
           "LEFT_VELOCITY": SensorModule(chr(42), "TWO_BYTE_SIGNED", 2)
           }

# Interpretation codes are used to tell how to deal with the raw data
# from a sensor query
# Note a negative value implies one byte of data is being dealt with (also
# includes 0), a positive implies 2 bytes
INTERPRET = {
    "ONE_BYTE_UNPACK": -1,
    "ONE_BYTE_SIGNED": -2,
    "ONE_BYTE_UNSIGNED": -3,
    "NO_HANDLING": 0,
    "TWO_BYTE_SIGNED": 1,
    "TWO_BYTE_UNSIGNED": 2
}
# some module-level functions for dealing with bits and bytes
#


def bytesOfR(r):
    """ for looking at the raw bytes of a sensor reply, r """
    print('raw r is', r)
    for i in range(len(r)):
        print('byte', i, 'is', ord(r[i]))
    print('finished with formatR')


def bitOfByte(bit, byte):
    """ returns a 0 or 1: the value of the 'bit' of 'byte' """
    if bit < 0 or bit > 7:
        print('Your bit of', bit, 'is out of range (0-7)')
        print('returning 0')
        return 0
    return ((byte >> bit) & 0x01)


def toBinary(val, numBits):
    """ prints numBits digits of val in binary """
    if numBits == 0:
        return
    toBinary(val >> 1, numBits - 1)
    print((val & 0x01), end=' ')  # print least significant bit


def fromBinary(s):
    """ s is a string of 0's and 1's """
    if s == '':
        return 0
    lowbit = ord(s[-1]) - ord('0')
    return lowbit + 2 * fromBinary(s[:-1])


def twosComplementInt1byte(byte):
    """ returns an int of the same value of the input
    int (a byte), but interpreted in two's
    complement
    the output range should be -128 to 127
    """
    # take everything except the top bit
    topbit = bitOfByte(7, byte)
    lowerbits = byte & 127
    if topbit == 1:
        return lowerbits - (1 << 7)
    else:
        return lowerbits


def twosComplementInt2bytes(highByte, lowByte):
    """ returns an int which has the same value
    as the twosComplement value stored in
    the two bytes passed in

    the output range should be -32768 to 32767

    chars or ints can be input, both will be
    truncated to 8 bits
    """
    # take everything except the top bit
    topbit = bitOfByte(7, highByte)
    lowerbits = highByte & 127
    unsignedInt = lowerbits << 8 | (lowByte & 0xFF)
    if topbit == 1:
        # with sufficient thought, I've convinced
        # myself of this... we'll see, I suppose.
        return unsignedInt - (1 << 15)
    else:
        return unsignedInt


def toTwosComplement2Bytes(value):
    """ returns two bytes (ints) in high, low order
    whose bits form the input value when interpreted in
    two's complement
    """
    # if positive or zero, it's OK
    if value >= 0:
        eqBitVal = value
        # if it's negative, I think it is this
    else:
        eqBitVal = (1 << 16) + value

    return ((eqBitVal >> 8) & 0xFF, eqBitVal & 0xFF)


def displayVersion():
    print("pycreate version", version)


class CommunicationError(Exception):
    """
    This error indicates that there was a problem communicating with the
    Create. The string msg indicates what went wrong.
    """

    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return str(self.msg)

    def __repr__(self):
        return "CommunicationError(" + repr(self.msg) + ")"


class RobotError(Exception):
    pass


class SensorGarbageError (RobotError):
    pass


class RobotCommandError(RobotError):
    pass

# inspect.Traceback has  lineno  while other code in  inspect
# seems to want f_lineno.
Traceback_Fixed = collections.namedtuple('Traceback_Fixed',
                                         ['filename',
                                          'f_lineno',
                                          'function',
                                          'code_context',
                                          'index'])

# ======================The CREATE ROBOT CLASS (modified by CAB 8/08)=====


class Create:
    """ An abstraction of the iRobot Create's SCI Open Interface. """

    def __init__(self, port, run_despite_sensor_garbage=False,
                 starting_mode=FULL_MODE, sim_mode=False):
        """
        Opens a connection on the given port.
        Starts in FULL mode unless the starting_mode is specified.
        Uses the  SIMULATOR  if port is 'sim' or if sim_mode is True.

        If a connection is made and then sensor garbage is detected,
          raises a  SensorGarbageError UNLESS  start_despite_garbage  is
          True (in which case a warning is printed but no Exception is raised).
        """
        # FIX ME: check if we can _start in other modes...
        # ======================== Starting up and Shutting Down========
        try:
            displayVersion()

            # fields for simulator
            self.in_sim_mode = False
            self.sim_sock = None
            self.sim_host = '127.0.0.1'
            self.sim_port = 65000
            self.maxSensorRetries = MIN_SENSOR_RETRIES

            self.sensors = Sensors()
            self.is_connected = False
            self.comPort = port

            print('PORT is', port)

            # Attempt to connect:
            if isinstance(port, str):
                # Case 1: Using the SIMULATOR or running in Mac/Linux.

                if port == 'sim':
                    # Use SIMULATOR.
                    self._init_sim_mode()
                    self.ser = None
                else:
                    # Should be running in Mac/Linux, where we need
                    # to use the whole port name.
                    print('In Mac/Linux mode...')
                    try:
                        self.ser = serial.Serial(port,
                                                 baudrate=57600,
                                                 timeout=TIMEOUT)
                        if sim_mode:  # USE SIMULATOR
                            self._init_sim_mode()
                    except:
                        self._raise_robot_error(BAD_PORT_ERROR_MESSAGE)
            else:
                # Case 2: Running on a real robot under Windows.
                #    The -1 here is because Windows starts counting from 1
                #    in the hardware control panel, but not in pyserial,
                #    it seems.
                self.ser = serial.Serial(port - 1,
                                         baudrate=57600, timeout=TIMEOUT)

            # Did the serial port actually open?
            if self.in_sim_mode:
                print("In simulator mode, awaiting commands...")
            elif self.ser.isOpen():
                print('Create Robot is connected, awaiting commands...')
            else:
                self._raise_robot_error(COULD_NOT_CONNECT_ERROR_MESSAGE)

            self.is_connected = True

            # define the class' Open Interface mode
            self.sciMode = OFF_MODE
            if starting_mode == SAFE_MODE:
                print('Putting the robot into safe mode...')
                self.toSafeMode()
                time.sleep(0.3)
            if starting_mode == FULL_MODE:
                print('Putting the robot into full mode...')
                self.toFullMode()
                time.sleep(0.3)

            self.serialLock = _thread.allocate_lock()
            self.setLEDs(10, 255, 0, 0)  # MB: was 100, want more yellowish

            # Access all sensors, to initialize them.
            # Then re-access and print interesting ones.
            for sensor in SENSORS:
                self.getSensor(sensor)

            is_garbage_detected = self.print_all_interesting_sensors()
            if is_garbage_detected and not run_despite_sensor_garbage:
                self._raise_robot_error(GARBAGE_DETECTED_ERROR_MESSAGE,
                                        SensorGarbageError())

        except RobotError:
            raise  # Has already been dealt with.
        except:
            self._raise_robot_error(COULD_NOT_CONNECT_ERROR_MESSAGE)

    def _last_frame_in_this_file(self):
        """
        Returns the frame RECORD (which contains the frame OBJECT) for
        the last frame in this file, that is, the first one in the
        traceback (going back toward the caller) that was called
        from a frame NOT associated with this file.
        """
        stack = inspect.stack()
        try:
            # Start at 1 since we already know the current frame
            # is in this file.
            for k in range(1, len(stack)):
                frame = stack[k]
                file_that_failed = frame[1]
                tail = file_that_failed.split('\\')[-1]
                tail_of_this_file = __file__.split("\\")[-1]
                if tail != tail_of_this_file:
                    return stack[k - 1]

            return stack[0]  # Should never get here
        finally:
            del stack

    def _raise_robot_error(self, message=None, error=None):
        """
        Does a self.shutdown() in hopes that it will work (when needed).
        Does a traceback from the frame in the student's code that led
        to the Exception in this file.  Prints an appropriate message.
        """

        was_connected = self.is_connected
        self.try_shutdown()

        print("See red error message below (at the bottom).")
        print()
        time.sleep(1.0)  # To avoid intermingling PRINTs with traceback

        last_frame_record_in_this_code = self._last_frame_in_this_file()
        last_frame_in_this_code = last_frame_record_in_this_code[0]
        frame_for_traceback = last_frame_in_this_code.f_back
        try:
            traceback.print_stack(frame_for_traceback)

            if not error:
                if message:
                    error = RobotError()
                else:
                    error = RobotCommandError()

            command_that_failed = last_frame_record_in_this_code[3]
            if not message:
                format_string = ROBOT_COMMAND_ERROR_MESSAGE
                message = format_string.format(command_that_failed,
                                               command_that_failed)
                if not was_connected:
                    format_string = DISCONNECTED_ROBOT_ERROR
                    message += format_string.format(command_that_failed)

            traceback.print_exception(None, message, True, chain=False)
            raise error

        finally:
            del last_frame_in_this_code
            del last_frame_record_in_this_code
            del frame_for_traceback

    def print_all_interesting_sensors(self):
        try:
            sensors = ['DISTANCE', 'ANGLE',
                       'BUMPS_AND_WHEEL_DROPS', 'BUTTONS',
                       'CLIFF_FRONT_LEFT_SIGNAL', 'CLIFF_FRONT_RIGHT_SIGNAL',
                       'CLIFF_LEFT_SIGNAL', 'CLIFF_RIGHT_SIGNAL',
                       'WALL_SIGNAL',
                       'IR_BYTE', 'SONG_PLAYING',
                       'BATTERY_CHARGE', 'CURRENT', ]
            print()
            print('------------------ SENSOR VALUES: -----------------------')
            for sensor in sensors:
                value = self.getSensor(sensor)
                print('{:26}: {}'.format(sensor, value))
            print(
                '---------------------------------------------------------\n')

            # The rest of this method is a kludge fix by DCM.
            sensors_to_check = [
                'CLIFF_FRONT_LEFT_SIGNAL', 'CLIFF_FRONT_RIGHT_SIGNAL',
                'CLIFF_LEFT_SIGNAL', 'CLIFF_RIGHT_SIGNAL', 'WALL_SIGNAL',
                'IR_BYTE'
            ]

            garbages = []
            for sensor in sensors_to_check:
                value = self.getSensor(sensor)
                if value > 4096:
                    garbages.append((sensor, value))

            if len(garbages) > 0:
                print()
                print('   *** WARNING, WARNING, WARNING ***')
                print('The following sensors gave garbage values.')
                print('You MIGHT get more sensor garbage in this run.')
                print('Be sure to execute a  robot.shutdown()  next run.')

                for garbage in garbages:
                    print("{:26}: {:5}".format(garbage[0], garbage[1]))

                return True  # Garbage detected

            return False  # No garbage detected

        except RobotError:
            raise  # Already handled any RobotError, just pass it along.
        except Exception:
            self._raise_robot_error()

    def print_all_sensors(self):
        try:
            print('------------------ SENSOR VALUES: -----------------------')
            for sensor in SENSORS:
                value = self.getSensor(sensor)
                print('{:26}: {}'.format(sensor, value))
            print('---------------------------------------------------------')

        except RobotError:
            raise  # Already handled any RobotError, just pass it along.
        except Exception:
            self._raise_robot_error()

    def send(self, bytes1):
        try:
            if not self.is_connected:
                raise Exception('Not connected')
            if self.in_sim_mode:
                if self.ser:
                    self.ser.write((bytes(bytes1, encoding='Latin-1')))
                self.sim_sock.send((bytes(bytes1, encoding='Latin-1')))
            else:
                self.ser.write((bytes(bytes1, encoding='Latin-1')))

        except RobotError:
            raise  # Already handled any RobotError, just pass it along.
        except Exception:
            self._raise_robot_error()

    def read(self, bytes_to_read):
        try:

            if not self.is_connected:
                raise Exception('Not connected')
            message = ""
            if self.in_sim_mode:
                if self.ser:
                    self.ser.read(bytes_to_read)
                message = self.sim_sock.recv(bytes_to_read)
            else:
                message = self.ser.read(bytes_to_read)
            return str(message, encoding='Latin-1')

        except RobotError:
            raise  # Already handled any RobotError, just pass it along.
        except Exception:
            self._raise_robot_error()

    def _init_sim_mode(self):
        try:
            print('In simulated mode, connecting to simulator socket')
            self.in_sim_mode = True  # SRSerial('mapSquare.txt')
            self.sim_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sim_sock.connect((self.sim_host, self.sim_port))

        except RobotError:
            raise  # Already handled any RobotError, just pass it along.
        except Exception:
            self._raise_robot_error(SIMULATOR_NOT_OPEN_ERROR_MESSAGE)

    def reconnect(self, comPort):
        '''
        This method closes the existing connection and reestablishes it.
        When things get bad, this is the only method of recovery.
        '''
        try:
            if self.is_connected:
                # Just in case it was stuck moving somewhere, stop the Create:
                self.stop()
                # Close the connection:
                self._close()
                self.is_connected = False

            # Reestablish the serial connection to the Create:
            self.__init__(comPort)
            self._start()
            # The recommended 200ms+ pause after mode commands.
            time.sleep(0.25)

            if (self.sciMode == SAFE_MODE):
                print('Putting the robot into safe mode...')
                self.toSafeMode()
                time.sleep(0.3)
            if (self.sciMode == FULL_MODE):
                print('Putting the robot into full mode...')
                self.toSafeMode()
                time.sleep(0.3)
                self.toFullMode()
            # The recommended 200ms+ pause after mode commands.
            time.sleep(.25)

        except RobotError:
            raise  # Already handled any RobotError, just pass it along.
        except Exception:
            self._raise_robot_error(COULD_NOT_CONNECT_ERROR_MESSAGE)

    def _start(self):
        """ changes from OFF_MODE to PASSIVE_MODE """
        self.send(START)
        # they recommend 20 ms between mode-changing commands
        time.sleep(0.25)
        # change the mode we think we're in...
        return

    def try_shutdown(self):
        """ Tries a shutdown, but catches any exception silently."""
        try:
            self.shutdown()
        except:
            pass

    def shutdown(self):
        '''
        This method shuts down the connection to the Create, after first
        stopping the Create and putting the Create into passive mode.
        '''
        try:
            if not self.is_connected:
                return

            print('Shutting down the robot.')

            self.stop()
            # DCM: I think the following code changes the lights anyhow, not
            # sure.
            self.setLEDs(100, 255, 0, 0)
            self.__sendmsg(COMMANDS["MODE_PASSIVE"], '')
            # The recommended 200ms+ pause after mode commands.
            time.sleep(0.25)
            self.serialLock.acquire()
            self._start()  # send Create back to passive mode
            time.sleep(0.1)
            if self.in_sim_mode:
                self.sim_sock.close()
            else:
                self.ser.close()
            self.serialLock.release()

            self.is_connected = False

        except RobotError:
            raise  # Already handled any RobotError, just pass it along.
        except Exception:
            self._raise_robot_error()

    # MB: added back in as private method, since reconnect uses it.
    def _close(self):
        """ tries to shutdown the robot as kindly as possible, by
            clearing any remaining odometric data
            going to passive mode
            closing the serial port
        """
        self.serialLock.acquire()
        self._start()  # send Create back to passive mode
        time.sleep(0.1)
        self.ser.close()
        self.serialLock.release()
        return

    def _closeSer(self):
        """ just disconnects the serial port """
        self.serialLock.acquire()
        self.ser.close()
        self.serialLock.release()
        return

    def _openSer(self):
        self.serialLock.acquire()
        """ opens the port again """
        self.ser.open()
        self.serialLock.release()
        return

    # =============================== Serial Communication
    def __sendmsg(self, opcode, dataBytes):
        '''
        This method functions as the base of the protocol, sending a message
        with a particular opcode and the given data bytes. opcode should be
        a character; use the constants defined at the top of this file.
        data_bytes must be a string, and should have the proper length
        according to which opcode is used. See the Create serial protocol
        manual for more details.
        '''
# lock
        self.serialLock.acquire()  # note: blocking
        successful = False
        while not successful:
            try:
                self.send(opcode + dataBytes)
                successful = True
            except select.error:
                pass
        self.serialLock.release()
# unlock

    def __sendOpCode(self, opcode):
        '''
        This method functions as the base of the protocol, sending a message
        with a particular opcode and the given data bytes. opcode should be
        a character; use the constants defined at the top of this file.
        data_bytes must be a string, and should have the proper length
        according to which opcode is used. See the Create serial protocol
        manual for more details.
        '''
# lock
        self.serialLock.acquire()  # note: blocking
        successful = False
        while not successful:
            try:
                self.send(opcode)
                successful = True
            except select.error:
                pass
        self.serialLock.release()
# unlock

    def __recvmsg(self, numBytes):
        '''
        This method is used internally for receiving data from the Create.
        It blocks for at most timeout seconds, and then returns as a string
        the bytes of the message received. It reads num_bytes bytes from the
        serial connection. If no message exists, it returns the empty
        string.
        '''
# lock
        self.serialLock.acquire()
        successful = False
        favor = None
        while not successful:
            try:
                favor = self.read(numBytes)
                successful = True
            except select.error:
                pass
        self.serialLock.release()
# unlock
        return favor

    def __sendAndRecvMsg(self, opcode, dataSendBytes, numBytesExpected):
        # lock
        self.serialLock.acquire()
        # send
        successful = False
        while not successful:
            try:
                self.send(opcode + dataSendBytes)
                successful = True
            except select.error:
                pass
        # wait?
        # receive
        successful = False
        favor = None
        while not successful:
            try:
                favor = self.read(numBytesExpected)
                successful = True
            except select.error:
                pass
        self.serialLock.release()
# unlock
        return favor

    # ========================= Moving Around ==========================
    def stop(self):
        """ Stop the robot's movement. """
        try:
            byteList = chr(0) + chr(0) + chr(0) + chr(0)
            self.__sendmsg(DRIVEDIRECT, byteList)
        except RobotError:
            raise  # Already handled any RobotError, just pass it along.
        except Exception:
            self._raise_robot_error()

    def go(self, cmPerSec=0, degPerSec=0):
        """ go(cmPerSec, degPerSec) sets the robot's linear velocity to
               cmPerSec centimeters per second and its angular velocity to
               degPerSec degrees per second
            go() is equivalent to go(0,0) [which means stop]
        """
        try:
            if cmPerSec == 0:
                # just handle rotation
                # convert to radians
                radPerSec = math.radians(degPerSec)
                # make sure the direction is correct
                if radPerSec >= 0:
                    dirstr = 'CCW'
                else:
                    dirstr = 'CW'
                # compute the velocity, given that the robot's
                # radius is 258mm/2.0
                velMmSec = math.fabs(radPerSec) * (258.0 / 2.0)
                # send it off to the robot
                self.drive(velMmSec, 0, dirstr)

            elif degPerSec == 0:
                # just handle forward/backward translation
                velMmSec = 10.0 * cmPerSec
                bigRadius = 32767
                # send it off to the robot
                self.drive(velMmSec, bigRadius)

            else:
                # move in the appropriate arc
                radPerSec = math.radians(degPerSec)
                velMmSec = 10.0 * cmPerSec
                radiusMm = velMmSec / radPerSec
                # check for extremes
                if radiusMm > 32767:
                    radiusMm = 32767
                if radiusMm < -32767:
                    radiusMm = -32767
                self.drive(velMmSec, radiusMm)

        except RobotError:
            raise  # Already handled any RobotError, just pass it along.
        except Exception:
            self._raise_robot_error()

    def driveDirect(self, leftCmSec=0, rightCmSec=0):
        """ sends velocities of each wheel independently
               left_cm_sec:  left  wheel velocity in cm/sec (capped at +- 50)
               right_cm_sec: right wheel velocity in cm/sec (capped at +- 50)
        """
        try:
            if leftCmSec < -50:
                leftCmSec = -50
            if leftCmSec > 50:
                leftCmSec = 50
            if rightCmSec < -50:
                rightCmSec = -50
            if rightCmSec > 50:
                rightCmSec = 50

            # convert to mm/sec, ensure we have integers
            leftHighVal, leftLowVal = toTwosComplement2Bytes(
                int(leftCmSec * 10))
            rightHighVal, rightLowVal = toTwosComplement2Bytes(
                int(rightCmSec * 10))
            # send these bytes and set the stored velocities
            byteList = (rightHighVal, rightLowVal, leftHighVal, leftLowVal)
            if type(byteList) in (list, tuple, set):
                temp = ''
                for char in byteList:
                    temp += chr(char)
            byteList = temp
            self.__sendmsg(DRIVEDIRECT, byteList)
            # self.send( DRIVEDIRECT )
            # self.send( chr(rightHighVal) )
            # self.send( chr(rightLowVal) )
            # self.send( chr(leftHighVal) )
            # self.send( chr(leftLowVal) )
        except RobotError:
            raise  # Already handled any RobotError, just pass it along.
        except Exception:
            self._raise_robot_error()

    def sendMessage(self, opcode, databytes):
        try:
            self.__sendmsg(opcode, databytes)
        except RobotError:
            raise  # Already handled any RobotError, just pass it along.
        except Exception:
            self._raise_robot_error()

    def waitTime(self, seconds):
        """
        robot waits for the specified time to past (tenths of secs)
        before executing the next command (CAB)
        """
        try:
            timeVal = twosComplementInt1byte(int(seconds))

            # send the command to the Create:
            self.__sendmsg(WAITTIME, chr(timeVal))
        except RobotError:
            raise  # Already handled any RobotError, just pass it along.
        except Exception:
            self._raise_robot_error()

    def waitEvent(self, eventNumber):
        """
        robot waits for the specified event to happen
        before executing the next command (CAB)
        """
        try:
            eventVal = twosComplementInt1byte(int(eventNumber))

            # Send the command to the Create:
            self.__sendmsg(WAITEVENT, chr(eventVal))
        except RobotError:
            raise  # Already handled any RobotError, just pass it along.
        except Exception:
            self._raise_robot_error()

    def waitDistance(self, centimeters):
        """
        robot waits for the specified distance
        before executing the next command (CAB)
        """
        try:
            distInMm = 10 * centimeters
            distHighVal, distLowVal = toTwosComplement2Bytes(int(distInMm))

            # Send the command to the Create:
            self.__sendmsg(WAITDIST, chr(distHighVal) + chr(distLowVal))
        except RobotError:
            raise  # Already handled any RobotError, just pass it along.
        except Exception:
            self._raise_robot_error()

    def waitAngle(self, degrees):
        """
        robot waits for the specified angle
        before executing the next command (CAB)
        """
        try:
            anglHighVal, anglLowVal = toTwosComplement2Bytes(int(degrees))

            # Send the command for data to the Create:
            self.__sendmsg(WAITANGLE, chr(anglHighVal) + chr(anglLowVal))
        except RobotError:
            raise  # Already handled any RobotError, just pass it along.
        except Exception:
            self._raise_robot_error()

    def drive(self, roombaMmSec, roombaRadiusMm, turnDir='CCW'):
        """ implements the drive command as specified
            the turnDir should be either 'CW' or 'CCW' for
            clockwise or counterclockwise - this is only
            used if roombaRadiusMm == 0 (or rounds down to 0)
            other drive-related calls are available
        """
        try:
            # first, they should be ints
            #   in case they're being generated mathematically
            if not isinstance(roombaMmSec, int):
                roombaMmSec = int(roombaMmSec)
            if not isinstance(roombaRadiusMm, int):
                roombaRadiusMm = int(roombaRadiusMm)

            # we check that the inputs are within limits
            # if not, we cap them there
            if roombaMmSec < -500:
                roombaMmSec = -500
            if roombaMmSec > 500:
                roombaMmSec = 500

            # if the radius is beyond the limits, we go straight
            # it doesn't really seem to go straight, however...
            if roombaRadiusMm < -2000:
                roombaRadiusMm = 32768
            if roombaRadiusMm > 2000:
                roombaRadiusMm = 32768

            # get the two bytes from the velocity
            # these come back as numbers, so we will chr them
            velHighVal, velLowVal = toTwosComplement2Bytes(roombaMmSec)

            # get the two bytes from the radius in the same way
            # note the special cases
            if roombaRadiusMm == 0:
                if turnDir == 'CW':
                    roombaRadiusMm = -1
                else:  # default is 'CCW' (turning left)
                    roombaRadiusMm = 1
            radiusHighVal, radiusLowVal = toTwosComplement2Bytes(
                roombaRadiusMm)

            # print 'bytes are', velHighVal, velLowVal, radiusHighVal,
            # radiusLowVal

            # send these bytes and set the stored velocities
            byteList = (velHighVal, velLowVal, radiusHighVal, radiusLowVal)
            if type(byteList) in (list, tuple, set):
                temp = ''
                for char in byteList:
                    temp += chr(char)
            byteList = temp
            self.__sendmsg(DRIVE, byteList)
            # self.send( DRIVE )
            # self.send( chr(velHighVal) )
            # self.send( chr(velLowVal) )
            # self.send( chr(radiusHighVal) )
            # self.send( chr(radiusLowVal) )
        except RobotError:
            raise  # Already handled any RobotError, just pass it along.
        except Exception:
            self._raise_robot_error()

    # ========================== SENSORS ==============================
    def sensorDataIsOK(self):
        """
        Detects data incoherency.
        Returns False if incoherent ("sensor junk").
        """
        try:
            # This function is probably wrong.  DCM.
            time.sleep(1)
            self.stop()
            self.getSensor('DISTANCE')
            distance = self.getSensor('DISTANCE')
            # Both angle and distance should be ~0.
            # If not, then the sensor was filled
            # with junk initially, so we reconnect.
            if abs(distance) > 10:
                # self.reconnect(self.comPort)
                time.sleep(1)
                print("Sensors could not be validated.")
                # self.shutdown()
                return False

            return True
        except RobotError:
            raise  # Already handled any RobotError, just pass it along.
        except Exception:
            self._raise_robot_error()

    def setMaxSensorTimeout(self, newTimeout):
        ''' Allows the user to wait longer for the robot
        to return sensor data to the computer. Each retry takes 50 ms.'''
        try:
            self.maxSensorRetries = newTimeout / RETRY_SLEEP_TIME
            self.maxSensorRetries = max(newTimeout, MIN_SENSOR_RETRIES)
        except RobotError:
            raise  # Already handled any RobotError, just pass it along.
        except Exception:
            self._raise_robot_error()

    def getSensor(self, sensorToRead):
        """
        Reads the value of the requested sensor from the robot
        and returns it.
        """
        try:
            # Send the request for data to the Create:
            self.__sendmsg(COMMANDS["QUERY_LIST"],
                           chr(1) + SENSORS[sensorToRead].ID)
            # Receive the reply:
            # MB: Added ability to retry in case a user is querying the sensors
            # while the robot is executing a wait command.
            msg = self.__recvmsg(SENSORS[sensorToRead].size)
            nRetries = 0
            while len(msg) < SENSORS[sensorToRead].size and \
                    nRetries < self.maxSensorRetries:
                # Serial receive appears to block for 0.5 sec, so we don't
                # need to sleep
                msg = self.__recvmsg(SENSORS[sensorToRead].size)
                nRetries += 1
            # print nRetries, "retries needed"

            # Was this:
            #   Last resort: return None and force the user to deal with it,
            #   rather than crashing.
            # DCM changed to (as previously, it seems) raise an Exception.
            if len(msg) < SENSORS[sensorToRead].size:
                msg = "Improper sensor query response length: "
                raise CommunicationError(msg)
#                 return None
            msg_len = len(msg)
            sensor_bytes = [ord(b) for b in msg[0:msg_len]]
            return self._interpretSensor(sensorToRead, sensor_bytes)
        except RobotError:
            raise  # Already handled any RobotError, just pass it along.
        except Exception:
            self._raise_robot_error(SENSOR_READ_ERROR)

    def _interpretSensor(self, sensorToRead, raw_data):
        """
        interprets the raw binary data form a sensor
        into its appropriate form for use.
        This function is for internal use - DO NOT CALL
        """
        data = None
        interpret = SENSORS[sensorToRead].interpret
        if len(raw_data) < SENSORS[sensorToRead].size:
            return None
        if interpret == "ONE_BYTE_SIGNED":
            data = self._getOneByteSigned(raw_data[0])
        elif interpret == "ONE_BYTE_UNSIGNED":
            data = self._getOneByteUnsigned(raw_data[0])
        elif interpret == "TWO_BYTE_SIGNED":
            data = self._getTwoBytesSigned(raw_data[0], raw_data[1])
        elif interpret == "TWO_BYTE_UNSIGNED":
            data = self._getTwoBytesUnsigned(raw_data[0], raw_data[1])
        elif interpret == "ONE_BYTE_UNPACK":
            if sensorToRead == "BUMPS_AND_WHEEL_DROPS":
                data = self._getLower5Bits(raw_data[0])
            elif sensorToRead == "BUTTONS":
                data = self._getButtonBits(raw_data[0])
            elif sensorToRead == "USER_DIGITAL_INPUTS":
                data = self._getLower5Bits(raw_data[0])
            if sensorToRead == "OVERCURRENTS":
                data = self._getLower5Bits(raw_data[0])
        elif interpret == "NO_HANDLING":
            data = raw_data
        return data

    # ======================= CARGO BAY OUTPUTS ========================
    def setDigitalOutputs(self, digOut2, digOut1, digOut0):
        """
        sets the digital output pins of the cargo bay connector
        to the specifed value (1 or 0)
        """
        try:
            data_byte = int(
                "00000" + str(digOut2) + str(digOut1) + str(digOut0), 2)
            self.__sendmsg(COMMANDS["DIGITAL_OUTPUTS"], chr(data_byte))
        except RobotError:
            raise  # Already handled any RobotError, just pass it along.
        except Exception:
            self._raise_robot_error()

    def setLowSideDrivers(self, driver2, driver1, driver0):
        """
        sets the low side driver output pins of the cargo bay connector
        to the specifed value (1 or 0)
        """
        try:
            data_byte = int(
                "00000" + str(driver2) + str(driver1) + str(driver0), 2)
            self.__sendmsg(COMMANDS["LOW_SIDE_DRIVERS"], chr(data_byte))
        except RobotError:
            raise  # Already handled any RobotError, just pass it along.
        except Exception:
            self._raise_robot_error()

    def setPWMLowSideDrivers(self, dutyCycle2, dutyCycle1, dutyCycle0):
        """
        sets the low side driver output pins of the cargo bay connector
        to the specifed value (0 to 255)
        """
        try:
            self.__sendmsg(COMMANDS["PWM_LOW_SIDE_DRIVERS"],
                           chr(dutyCycle2) + chr(dutyCycle1) + chr(dutyCycle0))
        except RobotError:
            raise  # Already handled any RobotError, just pass it along.
        except Exception:
            self._raise_robot_error()

    def sendIR(self, byteValue):
        """
        send the requested byte out of low side driver 1
        (pin 23 on Cargo Bay Connector) (0-255)
        """
        try:
            self.__sendmsg(COMMANDS["SEND_IR"], chr(byteValue))
        except RobotError:
            raise  # Already handled any RobotError, just pass it along.
        except Exception:
            self._raise_robot_error()

    def startIR(self, byteValue):
        '''FIX ME: implement script send to begin sending passed value'''
        """Uses a script so that the robot can receive and perform other
        commands concurrently. Alternative to threading. """
        try:
            print("sending byte", byteValue)

            byteList = chr(3)  # script has 3 bytes
            byteList += COMMANDS["SEND_IR"]
            byteList += chr(byteValue)  # IR value
            byteList += RUN_SCRIPT  # (running at end of def sets up recursion)
            self.__sendmsg(DEFINE_SCRIPT, byteList)
            self.__sendOpCode(RUN_SCRIPT)  # actually run the script
        except RobotError:
            raise  # Already handled any RobotError, just pass it along.
        except Exception:
            self._raise_robot_error()

    def stopIR(self):
        '''TO DO: send null script to end IR streaming'''
        """Uses a script so that the robot can receive and perform other
        commands concurrently. Alternative to threading. """
        try:
            self.__sendmsg(DEFINE_SCRIPT, chr(0))  # define null script
        except RobotError:
            raise  # Already handled any RobotError, just pass it along.
        except Exception:
            self._raise_robot_error()

    # ========================== LIGHTS ================================
    def setLEDs(self, powerColor, powerIntensity, play, advance):
        """ The setLEDs method sets each of the three LEDs, from left to right:
            the power LED, the play LED, and the status LED.
            The power LED at the left can display colors
            from green (0) to red (255)
            and its intensity can be specified, as well.
            Hence, power_color and power_intensity are values from 0 to 255.
            The other two LED inputs should either be 0 (off) or 1 (on).
        """
        try:
            # make sure we're within range...
            if advance != 0:
                advance = 1
            if play != 0:
                play = 1
            try:
                power = int(powerIntensity)
                powercolor = int(powerColor)
            except TypeError:
                power = 128
                powercolor = 128
                print('Type exception caught in setAbsoluteLEDs in roomba.py')
                print('Your powerColor or powerIntensity was not an integer.')
            if power < 0:
                power = 0
            if power > 255:
                power = 255
            if powercolor < 0:
                powercolor = 0
            if powercolor > 255:
                powercolor = 255
            # create the first byte
            # firstByteVal = (status << 4) | (spot << 3) | \
            #     (clean << 2) | (max << 1) | dirtdetect
            firstByteVal = (advance << 3) | (play << 1)

            # send these as bytes
            # print 'bytes are', firstByteVal, powercolor, power
            self.send(LEDS)
            self.send(chr(firstByteVal))
            self.send(chr(powercolor))
            self.send(chr(power))
        except RobotError:
            raise  # Already handled any RobotError, just pass it along.
        except Exception:
            self._raise_robot_error()

    # ==================== DEMOS ======================
    def seekDock(self):
        """sends the force-seeking-dock signal """
        try:
            self.demo(1)
        except RobotError:
            raise  # Already handled any RobotError, just pass it along.
        except Exception:
            self._raise_robot_error()

    def demo(self, demoNumber=-1):
        """ runs one of the built-in demos for Create
            if demoNumber is
              <omitted> or
              -1 stop current demo
               0 wander the surrounding area
               1 wander and dock, when the docking station is seen
               2 wander a more local area
               3 wander to a wall and then follow along it
               4 figure 8
               5 "wimp" demo: when pushed, move forward
                 when bumped, move back and away
               6 home: will home in on a virtual wall, as
                 long as the back and sides of the IR receiver
                 are covered with tape
               7 tag: homes in on sequential virtual walls
               8 pachelbel: plays the first few notes of the canon in D
               9 banjo: plays chord notes according to its cliff sensors
                 chord key is selected via the bumper
        """
        try:
            if (demoNumber < -1 or demoNumber > 9):
                demoNumber = -1  # stop current demo

            self.send(DEMO)
            if demoNumber < 0 or demoNumber > 9:
                # invalid values are equivalent to stopping
                self.send(chr(255))  # -1
            else:
                self.send(chr(demoNumber))
        except RobotError:
            raise  # Already handled any RobotError, just pass it along.
        except Exception:
            self._raise_robot_error()

    # ==================== MUSIC ======================
    def setSong(self, songNumber, noteList):
        """ this stores a song to roomba's memory to play later
           with the playSong command
           songNumber must be between 0 and 15 (inclusive)
           songDataList is a list of (note, duration) pairs (up to 16)
           note is the midi note number, from 31 to 127
           (outside this range, the note is a rest)
           duration is from 0 to 255 in 1/64ths of a second
        """
        try:
            # any notes to play?
            if not isinstance(noteList, list) and not isinstance(noteList,
                                                                 tuple):
                print('The noteList must be a list or tuple')
                print('noteList was', noteList)
                raise Exception('Bad notelist')

            if len(noteList) < 1:
                print('No data in the noteList')
                raise Exception('Bad notelist')

            if songNumber < 0:
                songNumber = 0
            if songNumber > 15:
                songNumber = 15

            # indicate that a song is coming
            self.send(SONG)
            self.send(chr(songNumber))

            L = min(len(noteList), 16)
            self.send(chr(L))

            # loop through the notes, up to 16
            for note in noteList[:L]:
                # make sure its a tuple, or else we rest for 1/4 second
                if isinstance(note, tuple) or isinstance(note, list):
                    # more error checking here!
                    self.send(chr(note[0]))  # note number
                    self.send(chr(note[1]))  # duration
                else:
                    self.send(chr(30))  # a rest note
                    self.send(chr(16))  # 1/4 of a second

        except RobotError:
            raise  # Already handled any RobotError, just pass it along.
        except Exception:
            self._raise_robot_error()

    def playSong(self, noteList):
        """ The input to <tt>playSong</tt> should be specified as a list
            of pairs of ( note_number, note_duration ) format. Thus,
            r.playSong( [(60,8),(64,8),(67,8),(72,8)] ) plays a quick C chord.
        """
        # implemented by setting song #1 to the notes and then playing it
        try:
            self.setSong(1, noteList)
            self.playSongNumber(1)
        except RobotError:
            raise  # Already handled any RobotError, just pass it along.
        except Exception:
            self._raise_robot_error()

    def playSongNumber(self, songNumber):
        """ plays song songNumber """
        try:
            if songNumber < 0:
                songNumber = 0
            if songNumber > 15:
                songNumber = 15
            self.send(PLAY)
            self.send(chr(songNumber))
        except RobotError:
            raise  # Already handled any RobotError, just pass it along.
        except Exception:
            self._raise_robot_error()

    def playNote(self, noteNumber, duration, songNumber=0):
        """ plays a single note as a song (at songNumber)
            duration is in 64ths of a second (1-255)
            the note number chart is on page 12 of the open interface manual
        """
        try:
            # set the song
            self.setSong(songNumber, [(noteNumber, duration)])
            self.playSongNumber(songNumber)
        except RobotError:
            raise  # Already handled any RobotError, just pass it along.
        except Exception:
            self._raise_robot_error()

    # ==================== Modes ======================
    def toSafeMode(self):
        """ changes the state (from PASSIVE_MODE or FULL_MODE)
            to SAFE_MODE
        """
        try:
            self._start()
            time.sleep(0.03)
            # now we're in PASSIVE_MODE, so we repeat the above code...
            self.send(SAFE)
            # they recommend 20 ms between mode-changing commands
            time.sleep(0.03)
            # change the mode we think we're in...
            self.sciMode = SAFE_MODE
            # no response here, so we don't get any...
        except RobotError:
            raise  # Already handled any RobotError, just pass it along.
        except Exception:
            self._raise_robot_error()

    def toFullMode(self):
        """ changes the state from PASSIVE to SAFE to FULL_MODE
        """
        try:
            self._start()
            time.sleep(0.03)
            self.toSafeMode()
            time.sleep(0.03)
            self.send(FULL)
            time.sleep(0.03)
            self.sciMode = FULL_MODE
        except RobotError:
            raise  # Already handled any RobotError, just pass it along.
        except Exception:
            self._raise_robot_error()

    # ==================== Class Level Math functions =============
    def _getButtonBits(self, r):
        """ r is one byte as an integer """
        return [bitOfByte(2, r), bitOfByte(0, r)]

    def _getLower5Bits(self, r):
        """ r is one byte as an integer """
        return [bitOfByte(4, r), bitOfByte(3, r), bitOfByte(2, r),
                bitOfByte(1, r), bitOfByte(0, r)]

    def _getOneBit(self, r):
        """ r is one byte as an integer """
        if r == 1:
            return 1
        else:
            return 0

    def _getOneByteSigned(self, r):
        """ r is one byte as a signed integer """
        return twosComplementInt1byte(r)

    def _getOneByteUnsigned(self, r):
        """ r is one byte as an integer """
        return r

    def _getTwoBytesSigned(self, r1, r2):
        """ r1, r2 are two bytes as a signed integer """
        return twosComplementInt2bytes(r1, r2)

    def _getTwoBytesUnsigned(self, r1, r2):
        """ r1, r2 are two bytes as an unsigned integer """
        return r1 << 8 | r2

    def _rawSend(self, listofints):
        for x in listofints:
            self.send(chr(x))

    def _rawRecv(self):
        nBytesWaiting = self.ser.inWaiting()
        # print 'nBytesWaiting is', nBytesWaiting
        r = self.read(nBytesWaiting)
        r = [ord(x) for x in r]
        # print 'r is', r
        return r

    def _rawRecvStr(self):
        nBytesWaiting = self.ser.inWaiting()
        # print 'nBytesWaiting is', nBytesWaiting
        r = self.ser.read(nBytesWaiting)
        return r

    def getMode(self):
        """ returns one of OFF_MODE, PASSIVE_MODE, SAFE_MODE, FULL_MODE """
        try:
            # but how right is it?
            return self.sciMode
        except RobotError:
            raise  # Already handled any RobotError, just pass it along.
        except Exception:
            self._raise_robot_error()

# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    import m3_robot_test
    m3_robot_test.main()
