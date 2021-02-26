import serial
import socket
import time


class SimpleSerialCommunicator(object):
    """ Uses a serial connection to send and receive messages. """

    # Serial can go at 115200, but wifly is currently set to 57600
    BAUDRATE = 57600
    READ_TIMEOUT = None  # in seconds. None means never timeout.

    def establish_connection(self, port, delay=None):
        try:
            # TODO Confirm that the remaining parameters in the
            # following statement are not going to change no matter
            # what hardware we use (within reason).
            # Otherwise, make variables herein for those parameters.
            baudrate = SimpleSerialCommunicator.BAUDRATE
            timeout = SimpleSerialCommunicator.READ_TIMEOUT
            self.serial_connection = serial.Serial(port,
                                                   baudrate=baudrate,
                                                   timeout=timeout)

            if delay:
                time.sleep(delay)
        except:
            # TODO Add error-handling, or leave to caller (as currently)
            raise

        print('Connected WIRED to port:', port)

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
        if len(bytes_object) == 1:
            return int(bytes_object[0])
        else:
            return bytes_object


class SimpleSocketCommunicator(object):
    """Uses a socket to send and receive messages to/from the robot
    """

    def establish_connection(self, address):
        try:
            self.socket_connection = socket.socket(socket.AF_INET,
                                                   socket.SOCK_STREAM)
            self.socket_connection.connect((address, 2000))
        except:
            raise  # TODO Error handling.

        print('Connected WIRELESS (WiFly) to address:', address)
        print('Eating what the WiFly itself sends, here:')
        time.sleep(1)  # TODO Tune this (maybe delete it)
        result = self.receive_bytes()
        print('  ', result)
        time.sleep(1)  # TODO Tune this (maybe delete it)

    def disconnect(self):
        """ Does whatever is needed to close the connection cleanly. """
        return self.socket_connection.shutdown(socket.SHUT_RDWR)

    def send_bytes(self, bytes_to_send):
        """
        Sends the given message to the Arduino.
        Returns the number of bytes actually sent.
          :type message: bytes or bytearray
          :rtype int
        """
        self.socket_connection.sendall(bytes_to_send)
        return len(bytes_to_send)

    def receive_bytes(self, _=None):
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
        max_bytes_to_read = 4096
        bytes_read = self.socket_connection.recv(max_bytes_to_read)

        if len(bytes_read) == 1:
            return int(bytes_read[0])
        else:
            return bytes_read


########################################################################
# The rest of this module is for testing.
########################################################################
def main():
    test_wired()
#     test_wireless()


def test_wireless():
    robot_number = 15
    suffix = '.wlan.rose-hulman.edu'
    address = 'r' + str(robot_number) + suffix

    test_wired_or_wireless(SimpleSocketCommunicator, address)


def test_wired():
    port = '/dev/cu.usbserial-A9048GNE'
    test_wired_or_wireless(SimpleSerialCommunicator, port)


def test_wired_or_wireless(communicatorType, port_or_address):
    # ------------------------------------------------------------------
    # After a  serial.Serial  is constructed, there must be a delay
    # (sleep) before sending any bytes.  Otherwise, the Arduino
    # will miss the first few bytes that are sent.
    # The following determines experimentally what delay is necessary.
    # ------------------------------------------------------------------
    #     delay = find_delay_needed_after_connecting(port_or_address,
    #                                                communicatorType)
    #     test_delay_needed_after_connecting(port_or_address, delay, communicatorType)

    # ------------------------------------------------------------------
    # The following assumes that the Arduino reads and sends in blocks
    # of 1 byte. More precisely, it assumes that the Arduino repeatedly:
    #   -- reads a byte
    #   -- sends a byte
    # ------------------------------------------------------------------

    # ------------------------------------------------------------------
    # This tests the throughput under different block sizes
    # in THIS program.  (Remember, we are assuming that the Arduino
    # does 1 byte blocks herein.)
    #
    # Blocksize makes a BIG difference, something like:
    #   -- 60    bytes per second using blocks of size 1
    #   -- 5,000 bytes per second using blocks of size 300 or more.
    # ------------------------------------------------------------------

    #     return
    delay = 1.6
    for k in range(10, 200, 10):
        test_throughput(port_or_address, delay, communicatorType,
                        bytes_per_block=k,
                        blocks_to_send=(200 // k))


def find_delay_needed_after_connecting(port_or_address,
                                       communicatorType):
    if communicatorType is SimpleSerialCommunicator:
        start = 15
    else:
        start = 0

    for k in range(start, 100):
        time.sleep(2)  # To allow for prior effects
        communicator = communicatorType()
        communicator.establish_connection(port_or_address)
        time.sleep(k / 10)

#         if communicatorType is SimpleSocketCommunicator:
#             eat_this = first_byte_received(communicator, 2)
#             print(eat_this)

        answer = first_byte_received(communicator, 50)
        communicator.disconnect()

        print(k, answer)
        if answer == 1:
            break

    print()
    print('A sleep of {:4.1f} seconds'.format(k / 10))
    print('after the construction of a  serial.Serial  allowed the')
    print('Arduino to catch the first number sent from this program.')

    return (k / 10)


def test_delay_needed_after_connecting(port_or_address, delay, communicatorType):
    print()
    print('Testing whether a sleep of {:4.1f} seconds'.format(delay))
    print('after the construction of a  serial.Serial  allows the')
    print('Arduino to catch the first number sent from this program.')

    time.sleep(2)  # To allow for prior effects
    sc = communicatorType()
    sc.establish_connection(port_or_address)
    time.sleep(delay)

    print(' Starting test. If it HANGS here, then the test FAILS:')
    sc.send_bytes(bytes([100]))
    answer = sc.receive_bytes()
    if answer == 101:
        print(' PASSED test')
    else:
        print(' FAILED test. Answer was', answer)

    print()
    print('Now testing that LESS sleep causes')
    print('the Arduino to MISS the first byte sent.')

    time.sleep(2)  # To allow for prior effects
    sc = SimpleSerialCommunicator()
    sc.establish_connection(port_or_address)
    time.sleep(max(delay - 0.1, 0))

    print(' Starting test. If it HANGS here, then the test PASSES:')
    sc.send_bytes(bytes([100]))
    answer = sc.receive_bytes()
    if answer == 101:
        print(' PASSED test')
    else:
        print(' FAILED test. Answer was', answer)


def first_byte_received(communicator, bytes_to_send=50):
    for k in range(bytes_to_send):
        communicator.send_bytes(bytes([k % 256]))
        time.sleep(0.01)
    answer = communicator.receive_bytes()
    return answer


def test_throughput(port_or_address, delay, communicatorType,
                    bytes_per_block=100,
                    blocks_to_send=100):
    communicator = communicatorType()
    if communicatorType is SimpleSerialCommunicator:
        communicator.establish_connection(port_or_address, delay)
    else:
        communicator.establish_connection(port_or_address)

    block = []
    for k in range(bytes_per_block):
        block.append(k % 256)
    bytes_to_send = bytes(block)

    start = time.perf_counter()
    for k in range(blocks_to_send):
        communicator.send_bytes(bytes_to_send)
        communicator.receive_bytes(bytes_per_block)
        # TODO Add a check that the correct values were received.
#         print(k)
    stop = time.perf_counter()

    elapsed = stop - start
    throughput = blocks_to_send * bytes_per_block / elapsed
    message = 'Throughput at {} bytes per block sent/received:'
    print(message.format(bytes_per_block))
    print('  {:0.1f} bytes per second'.format(throughput))

if __name__ == '__main__':
    main()
