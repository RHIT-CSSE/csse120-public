"""
<describe what this module has/does>

Created on Sep 3, 2016.
Written by: david.
"""
# TODO: Fix the above comment

import time
import serial
import sys


# TODO: Replace the following global variables by a SETTINGS object
# that reads a .settings file if one exists.
BAUD_RATE = 115200
TIMEOUT_FOR_READ_IN_SECONDS = None  # None means never timeout
TIME_BETWEEN_MESSAGES = 0.2
TIME_BETWEEN_BYTES = 0.05

ANALOG_READ_COMMAND = 0
ANALOG_WRITE_COMMAND = 1
DIGITAL_READ_COMMAND = 2
DIGITAL_WRITE_COMMAND = 3
PIN_MODE_COMMAND = 4
TONE_COMMAND = 5
NO_TONE_COMMAND = 6

PIN_LEFT_MOTOR_CONTROL_1 = 2
PIN_LEFT_MOTOR_CONTROL_2 = 4
PIN_LEFT_MOTOR_PWM = 5

PIN_RIGHT_MOTOR_CONTROL_1 = 7
PIN_RIGHT_MOTOR_CONTROL_2 = 8
PIN_RIGHT_MOTOR_PWM = 6

CODE_FOR_INPUT = 0
CODE_FOR_OUTPUT = 1
CODE_FOR_INPUT_PULLUP = 2

FORWARD = 1
BACKWARD = -1
STOP = 0

SIMULATE = False


def main():
    """ Calls the   TEST   functions in this module. """
    # TODO: Replace this by a more meaningful test.
    test2a();

class SimpleRoseBotWired(object):
    """
    A simple and restricted view of what a Rosebot can do.
    It assumes a wired connection that is established when
    the object is constructed.

    A SimpleRoseBotWired has:
      -- Left Motor and Right Motor
      -- Left, Center and Right LineSensors
      -- Buzzer
      -- LED

    """

class Command(object):
    """
    Represents a robot command that can be sent to the Arduino
    for execution.
    """

    def __init__(self, command_number, pin_number=None):
        self.command_number = command_number
        self.pin_number = pin_number

    def __repr__(self):
        pass

    def to_bytearray(self, data=None):
        """
        Default implementation:
          -- command_number is byte 1
          -- pin_number (if not None) is byte 2
          -- data is sent as one might expect:
               -- bytes as bytes
               -- strings as sequences of characters (left to right??)
               -- 16-bit ints as 2 bytes (big-endian??)
               -- TODO: floats et al.  Is there a library for this?
        """
        byte_array = bytearray()
        byte_array.append(self.command_number)
        if self.pin_number is not None:
            byte_array.append(self.pin_number)
        # FIXME: for now, assume data is a small integer.
        if data is not None:
            byte_array.append(data)

        # FIXME: Need error-handling with good messages here
        # and elsewhere.
        return byte_array

    def from_bytearray(self, byte_array):
        """
        Reconstruct into a 10-bit number if more than one byte.
        """

class MotorCommand(Command):
    pass






#     def __init__(self, port):
#         self.communicator = Communicator()
#         self.communicator.connect(port)
#
#         # Set up motors
#         self.communicator.send_command(PIN_MODE_COMMAND,
#                                        PIN_LEFT_MOTOR_CONTROL_1,
#                                        CODE_FOR_OUTPUT)
#         self.communicator.send_command(PIN_MODE_COMMAND,
#                                        PIN_LEFT_MOTOR_CONTROL_2,
#                                        CODE_FOR_OUTPUT)
#         # IMPORTANT: Is this the right mode for a motor???
#         self.communicator.send_command(PIN_MODE_COMMAND,
#                                        PIN_LEFT_MOTOR_PWM,
#                                        CODE_FOR_OUTPUT)
#
#         self.communicator.send_command(PIN_MODE_COMMAND,
#                                        PIN_RIGHT_MOTOR_CONTROL_1,
#                                        CODE_FOR_OUTPUT)
#         self.communicator.send_command(PIN_MODE_COMMAND,
#                                        PIN_RIGHT_MOTOR_CONTROL_2,
#                                        CODE_FOR_OUTPUT)
#         # IMPORTANT: Is this the right mode for a motor???
#         self.communicator.send_command(PIN_MODE_COMMAND,
#                                        PIN_RIGHT_MOTOR_PWM,
#                                        CODE_FOR_OUTPUT)
#
#     def forward_pwm(self, pwm):
#         self.drive_pwm(FORWARD, pwm, pwm)
#
#     def backward_pwm(self, pwm):
#         self.drive_pwm(BACKWARD, pwm, pwm)
#
#     def stop(self):
#         self.drive_pwm(STOP, 0, 0)
#
#     # TODO: FIX DRIVE_PWM. direction makes no sense.
#     # Use negatives for direction.
#
#     def drive_pwm(self, left_pwm, right_pwm=None):
#         if direction == FORWARD:
#             control1 = 1
#             control2 = 0
#         elif direction == BACKWARD:
#             control1 = 0
#             control2 = 1
#         else:  # STOP
#             control1 = 1
#             control2 = 1
#
#         if right_pwm is None:
#             right_pwm = left_pwm
#
#         for pins in [(PIN_LEFT_MOTOR_CONTROL_1,
#                       PIN_LEFT_MOTOR_CONTROL_2,
#                       PIN_LEFT_MOTOR_PWM,
#                       left_pwm),
#                      (PIN_RIGHT_MOTOR_CONTROL_1,
#                       PIN_RIGHT_MOTOR_CONTROL_2,
#                       PIN_RIGHT_MOTOR_PWM,
#                       right_pwm)]:
#             self.communicator.send_command(DIGITAL_WRITE_COMMAND,
#                                            pins[0],
#                                            control1)
#             self.communicator.send_command(DIGITAL_WRITE_COMMAND,
#                                            pins[1],
#                                            control2)
#             self.communicator.send_command(ANALOG_WRITE_COMMAND,
#                                            pins[2],
#                                            pins[3])



def test1():
    port = '/dev/cu.usbserial-A9048GND'
    c = Communicator()
    c.connect(port)

    for k in range(300):
        print(k, ' ', end='')
        c._send_message(bytearray([0]))  # bytearray(str(k), encoding='utf-8'))
#         if k % 2 == 0:
        print(str(c.get_message()))
        time.sleep(0.005)

def test2():
    # Blink 10 times
    port = '/dev/cu.usbserial-A9048GND'
    bot = RoseBot(port)
    bot.communicator.connect(port)

    for k in range(10):
        print(k)
        time.sleep(0.5)
        bot.communicator.send_command(DIGITAL_WRITE_COMMAND, 13, 1)
        time.sleep(0.5)
        bot.communicator.send_command(DIGITAL_WRITE_COMMAND, 13, 0)

def test2a():
    # Blink 10 times
    port = '/dev/cu.usbserial-A9048GND'
    talker = Communicator(port)

    command = Command(DIGITAL_WRITE_COMMAND, 13)

    for k in range(10):
        print('Blinking:', k)
        time.sleep(0.5)
        talker.send_command(command, 1)
        time.sleep(0.5)
        talker.send_command(command, 0)


def test3():
    # Go forwad slowly for 1 second.
    port = '/dev/cu.usbserial-A9048GND'
    bot = RoseBot()
#     bot.communicator.connect(port)

    bot.drive_pwm(FORWARD, 30, 30)
    time.sleep(1)
    bot.stop()

#-----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
#-----------------------------------------------------------------------
if __name__ == '__main__':
    main()
