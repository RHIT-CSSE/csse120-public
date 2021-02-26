/************************************************************************
 * Code to run on the Arduino of the RoseBot.
 *
 * Arduino:
 *   1. Open a Serial connection.
 *   2. Complete a handshake protocol.
 *   2. Repeatedly:
 *        a. Read bytes that form a COMMAND and its data.
 *        b. [Optionally] Write an acknowledgement.
 *        c. Execute the COMMAND, possibly writing more bytes
 *             as directed by the COMMAND.
 *      Until a QUIT_COMMAND is received and executed.
 *
 * Currently:
 *   -- The bytes-read are always 3 bytes where:
 *        Byte 1 encodes the COMMAND.
 *        Byte 2 encodes the SIGNAL for the command (e.g. LED), if any.
 *        Byte 3 encodes the DATA for the command
 *          (e.g. a digital value to write), if any.
 *   -- The acknowledgement is the first of the bytes that it read
 *          for the COMMAND.
 *   -- 10-bit sensor data is sent as one byte,
 *         truncating each item by 2 bits.
 *
 * Authors:  Valerie Galluzzi and David Mutchler, based on work by Dave Fisher.
 *           November, 2016.
 ***********************************************************************/

// TODO: Improve the simple communication protocol being used, by:
//         -- Compact messages to improve performance.
//         -- Add error detection and recovery.
//         -- Allow additional commands.
//   Allow wired to go at a faster baud rate (and perhaps wireless too).

#define BAUD_RATE 57600

struct COMMAND {
	byte command;
	byte pin;
};

byte HANDSHAKE[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
int HANDSHAKE_LENGTH = 10;
byte READY_MESSAGE = 256;

void setup() {
	Serial.begin(BAUD_RATE);
	do_handshake();
}

void loop() {
	fetch_command(command);
	send_acknowledgement(command);
	execute_command(command);
}

// Read bytes until the HANDSHAKE sequence is received.
// As each byte is read, echo the byte.
// When the handshake concludes, send a READY message.
void do_handshake() {
	byte received[HANDSHAKE_LENGTH];
	int k = 0;
	while (1) {
		received[k] = read_byte();
		write_byte(received[k]);

		if (received_matches_handshake(received, k)) {
			break;
		}
		k = (k + 1) % HANDSHAKE_LENGTH;
	}
	write_byte(READY_MESSAGE);
}

bool received_matches_handshake(byte received[], int current_position) {
	int k;
	int matching_position = (current_position + 1) % HANDSHAKE_LENGTH;
	for (k = 0; k < HANDSHAKE_LENGTH; ++k) {
		if (received[matching_position] != HANDSHAKE[k]) {
			return false;
		}
		matching_position = (matching_position + 1) % HANDSHAKE_LENGTH;
	}
	return true;
}


