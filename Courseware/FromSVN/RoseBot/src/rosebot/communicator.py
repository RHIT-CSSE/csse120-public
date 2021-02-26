import abc
import time


class Communicator(abc.ABC):
    """
    A Communicator:
      -- Establishes a connection with the robot's onboard controller
           (e.g., an Arduino).
      -- Implements the message-passing protocol on Commands:
           -- send_command,
                optionally followed by receiving an acknowledgement.
           -- receive_command_data,
                optionally followed by sending an acknowledgement.

    Subclasses must implement the following functions for
    message-passing on bytes (as opposed to Commands):
      -- establish_connection
      -- send_bytes
      -- receive_bytes

    CONSIDER What else should a Communicator be able to do?  Maybe:
      -- Sleep safely (while any concurrent processes are running).
      -- Return the type of connection.
      -- ??
    """
    # TODO Add a DEBUG mode that prints messages
    #     and applies to any subclass.

    # Subclasses should define their own __init__ which then calls
    # this one:
    def __init__(self,
                 connect=True,
                 wait_for_acknowledgement=True,
                 send_acknowledgement=False,
                 is_debug=False):
        self.should_wait_for_acknowledgement = wait_for_acknowledgement
        self.should_send_acknowledgement = send_acknowledgement
        self.is_debug = is_debug

        if connect:
            self.connect()
        self.is_connected = True

#         self.send_startup_sequence()
#         self.receive_startup_sequence()

    def connect(self):
        """
        Does whatever is needed to establish a connection to the
        robot's onboard controller (e.g., an Arduino).
        """
        try:
            # Subclass implements the following:
            self.establish_connection()
        except:
            raise  # TODO Error handing

    def send_startup_sequence(self):
        """ Current implementation: send 255 3 times. """
        # Sleep a bit in hopes to make this FOLLOW the
        # *HELLO**DONE* of the socket connection.
        if self.is_debug:
            print('SENDING startup sequence in 2 seconds:')

        time.sleep(2)
        for _ in range(20):
            self.send_message(bytearray([255]))
            time.sleep(0.1)

        if self.is_debug:
            print('Done SENDING startup sequence.')

    def receive_startup_sequence(self):
        """ Read until we get 254 three times in a row. """
        if self.is_debug:
            print('Waiting to RECEIVE startiup sequence...')

        count = 0
        while True:
            if count >= 3:
                break
            byte_read = self.receive_message(1)
            if byte_read == 254:
                count = count + 1
            else:
                count = 0

        if self.is_debug:
            print('Done RECEIVING startup sequence.')

    def send_command(self, command, data=None):
        """
        Encodes and then sends to the Arduino the given command
        with the given data. Waits for an acknowledgement if this
        Communicator is set to do so.  Returns the number of bytes sent.
          :type command: Command
          :type data: CommandData
          :rtype int
        """
        message = command.to_bytes(data)
        bytes_sent = self.send_message(message)

        if self.should_wait_for_acknowledgement:
            self.wait_for_acknowledgement(message[0])

        return bytes_sent

    def receive_command_data(self, command):
        """
        Waits for and receives whatever data the given Command
        expects back from the Arduino.  Sends an acknowledgement
        if this Communicator is set to do so.
        Returns the received data in whatever form the Command expects.
          :type data: CommandData
        """
        if command.number_of_bytes_to_receive_varies:
            bytes_received = self._receive_variable_bytes(command)
        else:
            num_bytes = command.number_of_bytes_to_receive
            bytes_received = self.receive_message(num_bytes)

        if self.should_send_acknowledgement:
            self.send_acknowledgement()

        return command.value_of(bytes_received)

    def _receive_variable_bytes(self, command):
        beginning = self.receive_message(1)
#         print('Beginning:', beginning)
        if command.indicates_end_of_message(beginning):
            return beginning
        else:
            rest = self.receive_message(command.
                                        number_of_bytes_to_receive - 1)
#             print('Rest: ', end='')
#             for k in range(len(rest)):
#                 print(rest[k], end=' ')
#             print(type(rest))
            if type(rest) is int:
                return bytearray([beginning]) + bytearray([rest])
            else:
                return bytearray([beginning]) + rest

    def wait_for_acknowledgement(self, expected_acknowledgement):
        # TODO Encapsulate this into a class that allows different
        #      kinds of acknowledgements.
        if self.is_debug:
            print('Waiting for acknowledgement.')

        # TODO Improve error detection and handling
        response = self.receive_message(1)
        if response != expected_acknowledgement:
            print()
            print('COMMUNICATION ERROR!')
            print('  Expected:', expected_acknowledgement)
            print('  Received:', response)
            print('  TELL YOUR INSTRUCTOR THAT THIS HAPPENED.')
            print('  Include the above 2 numbers when doing so.')
            print()

        if self.is_debug:
            print('Received acknowledgement')

    def send_acknowledgement(self):
        # TODO Encapsulate this into a class that allows different
        #      kinds of acknowledgements.
        pass  # Not currently implemented

    @abc.abstractmethod
    def establish_connection(self):
        """
        Does whatever is needed to establish a connection to the
        robot's onboard controller (e.g., an Arduino).
        """
        # Subclass must implement this method.

    @abc.abstractmethod
    def disconnect(self):
        """ Does whatever is needed to close the connection cleanly. """
        # Subclass must implement this method.

    def send_message(self, message):
        """
        Sends the given message to the Arduino.
          :type message: bytes or bytearray
          :rtype int
        """
        if self.is_debug:
            print('Sending: {}.'.format(message))

        # Subclass must implement the following method:
        number_of_bytes_sent = self.send_bytes(message)

        if self.is_debug:
            print('Sent {} bytes.'.format(number_of_bytes_sent))

        return number_of_bytes_sent

    def receive_message(self, number_of_bytes_to_receive=1):
        """
        Receives from the Arduino the given number of bytes.
        Returns a byte (integer between 0 and 255) if the given
        number of bytes is 1, otherwise returns a bytearray
        containing the bytes.
          :rtype byte or bytearray
        """

        if self.is_debug:
            print('Waiting to receive {} bytes.'.format(
                number_of_bytes_to_receive))

        # Subclass must implement the following method:
        message = self.receive_bytes(number_of_bytes_to_receive)

        if self.is_debug:
            print('Received: ', message)

        return message

    @abc.abstractmethod
    def send_bytes(self, bytes_to_send):
        """ Sends the given bytes. """
        # Subclass must implement this method.

    @abc.abstractmethod
    def receive_bytes(self, number_of_bytes):
        """ Receives the given number of bytes. """
        # Subclass must implement this method.
