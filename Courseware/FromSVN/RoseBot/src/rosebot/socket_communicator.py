import rosebot.communicator
import socket
import time

class SocketCommunicator(rosebot.communicator.Communicator):
    """Uses a socket to send and receive messages to/from the robot
    """
    def __init__(self,
                 address,
                 connect=True,
                 wait_for_acknowledgement=True,
                 send_acknowledgement=False,
                 is_debug=False):
        self.address = address
        self.read_buffer_size = 4096
        self.bytes_read_but_not_yet_returned = bytearray()

        super().__init__(connect=connect,
                         wait_for_acknowledgement=wait_for_acknowledgement,
                         send_acknowledgement=send_acknowledgement,
                         is_debug=is_debug)

    # TODO implement a __repr__ and/or __str__

    def establish_connection(self):
        try:
            print(self.address)
            self.socket_connection = socket.socket(socket.AF_INET,
                                                   socket.SOCK_STREAM)
            self.socket_connection.connect((self.address, 2000))
        except:
            raise  # TODO Error handling.

        time.sleep(1)
        bytes_read = self.socket_connection.recv(self.read_buffer_size)
        print('Initial bytes read:', bytes_read)

        # At this point, the wifly sends to the Arduino:
        #  *HELLO* followed (possibly) by other bytes.
        # The Arduino will "eat" those bytes immediately,
        # without echoing them, so that when this Python
        # program sends a command the Arduino is ready for it.

        # The following is previous attempts to address
        # the above issue.  Will delete when we have
        # a tested approach that works.

#         print('Reading the preliminary 13 bytes:')
#         for _ in range(13):
#             byte_received = self.receive_bytes(1)
#             time.sleep(0.1)
#             print(byte_received, chr(byte_received))
#         print('Done reading the preliminary 13 bytes.')
#
#         # Send 255s repeatedly until get 3 254s in a row.
#         print('Starting 255s and 254s')
#         count = 0
#         bytes_read = bytearray()
#         while True:
#             if count >= 3:
#                 break
#             bytes_read = (bytes_read
#                           + self.socket_connection.recv(self.read_buffer_size))
#
#             if len(bytes_read) == 0:
#                 print('Sending 255 after 1 second.')
#                 time.sleep(1)
#                 self.send_bytes(bytearray([255]))
#             else:
#                 print('Read:', bytes_read)
#                 if 254 in bytes_read:
#                     break
#                 bytes_read = bytearray()

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

    def receive_bytes(self, number_of_bytes_to_return=1):
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
        num_bytes = number_of_bytes_to_return
        while True:
            if self.is_debug:
                print('bytes in buffer:',
                      self.bytes_read_but_not_yet_returned)
            if len(self.bytes_read_but_not_yet_returned) >= num_bytes:
                result = self.bytes_read_but_not_yet_returned[:num_bytes]
                self.bytes_read_but_not_yet_returned = self.bytes_read_but_not_yet_returned[num_bytes:]
                break

            bytes_read = self.socket_connection.recv(self.read_buffer_size)
            if self.is_debug:
                print('bytes read:', bytes_read)
            self.bytes_read_but_not_yet_returned += bytes_read

        if self.is_debug:
            print('result:', result)

        if len(result) == 1:
            return int(result[0])
        else:
            return result
