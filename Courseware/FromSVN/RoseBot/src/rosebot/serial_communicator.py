import rosebot.communicator
import rosebot.command
import serial
import time


class SerialCommunicator(rosebot.communicator.Communicator):
    """ Uses a serial connection to send and receive messages. """

    BAUDRATE = 57600  # 57600  # Serial can go at 115200, but wifly only 57600
    READ_TIMEOUT = None  # in seconds. None means never timeout.
    SECONDS_AFTER_CONNECTING = 1  # TODO Tune this.
    TIME_BETWEEN_SENDS = 0.005  # TODO Tune this.

    def __init__(self,
                 port,
                 connect=True,
                 wait_for_acknowledgement=True,
                 send_acknowledgement=False,
                 is_debug=False):
        # TODO Allow search for port.
        self.port = port

        super().__init__(connect=connect,
                         wait_for_acknowledgement=wait_for_acknowledgement,
                         send_acknowledgement=send_acknowledgement,
                         is_debug=is_debug)

    # TODO implement a __repr__ and/or __str__

    def establish_connection(self):
        try:
            # TODO Confirm that the remaining parameters in the
            # following statement are not going to change no matter
            # what hardware we use (within reason).
            # Otherwise, make variables herein for those parameters.
            self.serial_connection = \
                serial.Serial(self.port,
                              baudrate=SerialCommunicator.BAUDRATE,
                              timeout=SerialCommunicator.READ_TIMEOUT)
            time.sleep(SerialCommunicator.SECONDS_AFTER_CONNECTING)
        except:
            # TODO Add error-handling, or leave to caller (as currently)
            raise

        print('Connected wired to', self.port)
        # WORKAROUND for now:  Send *HELLO**OPEN* as wireless does.
#         self.send_bytes(bytearray([42, 72, 69, 76, 76, 79, 42,
#                                    42, 79, 80, 72, 78, 42]))

    def disconnect(self):
        self.serial_connection.close()

    def send_bytes(self, bytes_to_send):
        """
        Sends the given message to the Arduino.
        Returns the number of bytes actually sent.
          :type message: bytes or bytearray
          :rtype int
        """
        return self.serial_connection.write(bytes_to_send)

#         # TODO Calulate the following.
#         time_since_previous_send = 0
#         first_sleep = max(0, SerialCommunicator.TIME_BETWEEN_SENDS
#                           - time_since_previous_send)
#
#         # TODO The following does writes one byte at a time,
#         # with a short pause after each.  Would it be more
#         # or less reliable to do a single multi-byte write?
#
#         for byte in message:
#             time.sleep(SerialCommunicator.TIME_BETWEEN_SENDS)
#             total_bytes_sent += self.serial_connection.write([byte_or_character])
#
#         return total_bytes_sent

    def receive_bytes(self, length_of_message_in_bytes=1):
        """
        Receives from the Arduino the given number of bytes.
        Returns a byte (integer between 0 and 255) if the given
        number of bytes is 1, otherwise returns a bytearray
        containing the bytes.

        Blocking behavior is determined by
          TIMEOUT_FOR_READ_IN_SECONDS
        which was set when this object was constructed.
          :rtype byte or bytearray
        """
        bytes_object = self.serial_connection.read(length_of_message_in_bytes)
#         print('received:', bytes_object)
        if len(bytes_object) == 1:
            return int(bytes_object[0])
        else:
            return bytes_object


########################################################################
# The rest of this module is for testing.
########################################################################

def main():
    port = '/dev/cu.usbserial-A9048GND'
    sc = SerialCommunicator(port)
#     test_send_command(sc)
    test_send_message(sc)
    test_receive_message(sc)
#     test_receive_command(sc)
#     test_analog_receive(sc)
    sc.disconnect()


def test_send_message(sc):
    """ Blink. """
    for _ in range(2):
        time.sleep(1)
        print('off')
        sc.send_message(bytes([0x03, 0x0d, 0x00]))
        time.sleep(1)
        print('on')
        sc.send_message(bytes([0x03, 0x0d, 0x01]))


def test_send_command(sc):
    """ Blink. """
    command = rosebot.command.DigitalWriteCommand(13)
    for _ in range(2):
        time.sleep(1)
        print('off')
        sc.send_command(command, 0)
        time.sleep(1)
        print('on')
        sc.send_command(command, 1)


def test_receive_message(sc):
    """ Get status of the button, pause and repeat. """
    print('Release the button')
    sc.send_message(bytes([0x02, 0x0c]))
    print('Should be 1 (not pressed): ', sc.receive_message())
    print('Press the button')
    time.sleep(2)
    sc.send_message(bytes([0x02, 0x0c]))
    print('Should be 0 (pressed): ', sc.receive_message())


def test_receive_command(sc):
    """ Get status of the button, pause and repeat. """
    command = rosebot.command.DigitalReadCommand(12)
    print('Release the button')
    sc.send_command(command)
    print('Should be 1 (not pressed): ', sc.receive_command_data(command))
    print('Press the button')
    time.sleep(2)
    sc.send_command(command)
    print('Should be 0 (pressed): ', sc.receive_command_data(command))


def test_analog_receive(sc):
    command = rosebot.command.AnalogReadCommand(0)
    for _ in range(10):
        sc.send_command(command)
        print('Value is: ', sc.receive_command_data(command))
        time.sleep(1)


if __name__ == '__main__':
    main()
