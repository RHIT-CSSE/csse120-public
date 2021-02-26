from enum import Enum, unique

# TODO Throughout, decide whether instance variables that could be
#    an ENUM type should hold their ENUM (which indicates its meaning)
#    or their VALUE (which is usually just an integer).

# The following Enum specifies the code that should be sent to the
#   Arduino to determine the pin to use.


@unique
class SIGNAL(Enum):
    LED = 0
    buzzer = 1
    button_sensor = 2
    left_bump_sensor = 3
    right_bump_sensor = 4
    left_reflectance_sensor = 5
    middle_reflectance_sensor = 6
    right_reflectance_sensor = 7
    left_encoder = 8
    right_encoder = 9
    left_proximity_sensor = 10
    front_proximity_sensor = 11
    right_proximity_sensor = 12
    left_motor_control_1 = 13
    left_motor_control_2 = 14
    left_motor_pwm = 15
    right_motor_control_1 = 16
    right_motor_control_2 = 17
    right_motor_pwm = 18
    pixy_camera = 19


class COMMAND_NUMBER(Enum):
    analog_read = 0
    analog_write = 1
    digital_read = 2
    digital_write = 3
    pin_mode = 4
    tone = 5
    no_tone = 6  # Not used, implemented as a tone of 0 on Arduino
    pixy_camera = 7


class Command(object):
    """
    Represents a robot command that can be sent to the Arduino
    for execution.
    """

    def __init__(self, command_number, pin_number=None,
                 number_of_bytes_to_receive=1,
                 number_received_varies=False):
        self.command_number = command_number
        self.pin_number = pin_number
        self.number_of_bytes_to_receive = number_of_bytes_to_receive
        self.number_of_bytes_to_receive_varies = number_received_varies

    # TODO: implement a __repr__ and/or __str__

    def to_bytes(self, data=None):
        """
        This is a slow, default implementation.
        Subclasses can improve upon it.  In this implementation:
          -- The command_number is byte 1.
          -- The signal is byte 2.
          -- The data is sent as one might expect:
               -- byte as a byte
               The rest of this is not yet implemented:
               -- bytes as bytes
               -- strings as sequences of characters (left to right??)
               -- 16-bit ints as 2 bytes (big-endian??)
               -- TODO: floats et al.  Is there a library for this?
        """
        command_number_byte = self._enum_to_value(self.command_number)
        signal_number_byte = self._enum_to_value(self.pin_number)
        data = self._enum_to_value(data)

        byte_array = bytearray()
        byte_array.append(command_number_byte)

        if signal_number_byte is not None:
            byte_array.append(signal_number_byte)
        else:
            byte_array.append(0)  # Any byte would be fine here

        # FIXME: for now, assume data is a small integer
        # (that fits into a single byte).
        if data is not None:
            byte_array.append(data)
        else:
            byte_array.append(0)  # Any byte would be fine here

        # FIXME: Need error-handling with good messages here
        # and elsewhere.
        return bytes(byte_array)

    @staticmethod
    def _enum_to_value(x):
        return x.value if isinstance(x, Enum) else x


class LEDCommand(Command):

    def __init__(self):
        super().__init__(COMMAND_NUMBER.digital_write, SIGNAL.LED)


class BuzzerCommand(Command):

    def __init__(self):
        super().__init__(COMMAND_NUMBER.tone, 0)


class MotorControlCommand(Command):

    def __init__(self, signal):
        super().__init__(COMMAND_NUMBER.digital_write, signal)


class MotorPWMCommand(Command):

    def __init__(self, signal):
        super().__init__(COMMAND_NUMBER.analog_write, signal)


class LeftMotorCommand(Command):
    pass


class RightMotorCommand(Command):
    pass


class EncoderResetCommand(Command):

    def __init__(self, signal):
        super().__init__(COMMAND_NUMBER.digital_write, signal)


class SensorCommand(Command):

    def __init__(self, command_number, pin_number,
                 number_of_bytes_to_receive=1,
                 number_received_varies=False):
        super().__init__(command_number, pin_number,
                         number_of_bytes_to_receive,
                         number_received_varies)

    def value_of(self, bytes_received):
        """
        Returns the CommandData that the given bytes object encodes.
        """
        # TODO: Implement CommandData so that we can encode data
        #   received if we want to.
        # TODO: Different Commands may return different types
        #       of CommandData, I think.
        #       For now, just pass along whatever the message contains,
        #       assuming that it is 2 bytes (10-bit analog for many sensors).

        if type(bytes_received) is int:
            return bytes_received
        else:
            return ((bytes_received[0] << 8)  # high 8 bits
                    + bytes_received[1])  # low 8 bits


class AnalogReadSensorCommand(SensorCommand):

    def __init__(self, signal):
        super().__init__(COMMAND_NUMBER.analog_read, signal, 2)


class DigitalReadSensorCommand(SensorCommand):

    def __init__(self, signal):
        super().__init__(COMMAND_NUMBER.digital_read, signal, 1)


class VariableBytesCommand(Command):

    def indicates_end_of_message(self, byte_received):
        # TODO Don't bury this rule here
        return byte_received == 0xff


class PixyBlock:
    """ An object that the Pixy Camera sees. """

    def __init__(self, x, y, width, height):
        # TODO Incorporate the signature and angle (and maybe ???)
        # self.signature = pixy_block_dictionary["signature"]
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        # self.angle = pixy_block_dictionary["angle"]

    def size(self):
        return self.width * self.height


class PixyCameraCommand(SensorCommand, VariableBytesCommand):

    def __init__(self):
        # TODO Verify that super is OK with this multiple inheritance
        super().__init__(COMMAND_NUMBER.pixy_camera, 1,
                         6, True)

    def value_of(self, bytes_received):
        if type(bytes_received) is int and bytes_received == 255:
            return None
        else:
            x = ((bytes_received[0] << 8)  # high bit for x
                 + bytes_received[1])  # low 8 bits for x
            y = bytes_received[2]
            width = ((bytes_received[3] << 8)  # high bit for width
                     + bytes_received[4])  # low 8 bits for width
            height = bytes_received[5]
            return PixyBlock(x, y, width, height)

# The current implementation of the Arduino code does not
#   support these 4 commands.


class AnalogReadCommand(Command):

    def __init__(self, pin_number):
        super().__init__(COMMAND_NUMBER.analog_read, pin_number)


class AnalogWriteCommand(Command):

    def __init__(self, pin_number):
        super().__init__(COMMAND_NUMBER.analog_write, pin_number)


class DigitalReadCommand(Command):

    def __init__(self, pin_number):
        super().__init__(COMMAND_NUMBER.digital_read, pin_number)


class DigitalWriteCommand(Command):

    def __init__(self, pin_number):
        super().__init__(COMMAND_NUMBER.digital_write, pin_number)

# PIN_LEFT_MOTOR_CONTROL_1 = 2
# PIN_LEFT_MOTOR_CONTROL_2 = 4
# PIN_LEFT_MOTOR_PWM = 5
#
# PIN_RIGHT_MOTOR_CONTROL_1 = 7
# PIN_RIGHT_MOTOR_CONTROL_2 = 8
# PIN_RIGHT_MOTOR_PWM = 6
#
# CODE_FOR_INPUT = 0
# CODE_FOR_OUTPUT = 1
# CODE_FOR_INPUT_PULLUP = 2
#
# FORWARD = 1
# BACKWARD = -1
# STOP = 0

# class MotorCommand(Command):
#     def __init__(self, pin_number):
#         super().__init__(COMMAND_NUMBERS['analog write'], pin_number)


def main():
    """ Calls the   TEST   functions in this module. """
    pass


#-----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
#-----------------------------------------------------------------------
if __name__ == '__main__':
    main()
