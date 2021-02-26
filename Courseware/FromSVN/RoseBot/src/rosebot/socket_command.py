PINS = {"LED":0x00, "BUZZER":0x01, "BUTTON":0x02,
      "LBUMP":0x03, "RBUMP":0x04,
      "LLINE":0x05, "CLINE":0x06, "RLINE":0x07,
      "LENCODER":0x08, "RENCODER":0x09,
      "LDISTANCE":0x0a, "CDISTANCE":0x0b, "RDISTANCE":0x0c,
      "LMOTORCTRL1":0x0d, "LMOTORCTRL2":0x0e, "LMOTORPWM":0x0f,
      "RMOTORCTRL1":0x10, "RMOTORCTRL2":0x11, "RMOTORPWM":0x12}
COMMANDS = {"AREAD":0x00, "AWRITE":0x01, "DREAD":0x02, "DWRITE":0x03, "PINMODE":0x04, "TONE":0x05}

class Command(object):
    """
    Represents a robot command that can be sent to the Arduino
    for execution.
    """

    def __init__(self, command, pin="LED", value=0x00):
        self.command_number = command
        self.pin_number = pin
        self.value = value
        self.number_of_bytes_to_receive = 1

    # TODO: implement a __repr__ and/or __str__
    def to_bytes(self):
        b = bytearray()
        b.append(COMMANDS[self.command])
        b.append(PINS[self.pin])
        b.append(self.value)
        # TODO: Implementation that doesn't assume value is byte
        return b

    def value_of(self, bytes_received, data=None):
        """
        Returns the CommandData that the given bytes object encodes.
        """
        # TODO: Different Commands return different types of CommandData?
        # For now, assume an int in a single byte.
        return bytes_received

class AnalogReadCommand(Command):
    def __init__(self, item):
        super().__init__('AREAD', item)

class AnalogWriteCommand(Command):
    def __init__(self, item, value):
        super().__init__('AWRITE', item, value)

class DigitalReadCommand(Command):
    def __init__(self, item):
        super().__init__('DREAD', item)

class DigitalWriteCommand(Command):
    def __init__(self, item, value):
        super().__init__('DWRITE', item, value)


class MotorCommand(Command):
    def __init__(self, side, direction, pwm=0):
        if side not in ["LMOTOR", "RMOTOR"]:
            raise "Motor side must be either LMOTOR or RMOTOR"
        if direction == 'forward':
            ctrls = (0x01, 0x00)
        elif direction == 'backward':
            ctrls = (0x00, 0x01)
        elif direction == 'stop':
            ctrls(0x00, 0x00)
        elif direction == 'brake':
            ctrls(0x01, 0x01)
        else:
            raise "Incorrect direction in motor command--should be one of ['forward','backward','stop','brake']"
        self.ctrl1 = DigitalWriteCommand(side + "CTRL1", ctrls[0])
        self.ctrl2 = DigitalWriteCommand(side + "CTRL2", ctrls[1])
        super().__init__('AWRITE', side + "PWM", pwm)

    def to_bytes(self):
        b = bytearray()
        b.append(COMMANDS[self.command])
        b.append(PINS[self.pin])
        b.append(self.value)
        b.append(self.ctrl1.to_bytes())
        b.append(self.ctrl2.to_bytes())
        return b

def main():
    """ Calls the   TEST   functions in this module. """
    pass


#-----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
#-----------------------------------------------------------------------
if __name__ == '__main__':
    main()
