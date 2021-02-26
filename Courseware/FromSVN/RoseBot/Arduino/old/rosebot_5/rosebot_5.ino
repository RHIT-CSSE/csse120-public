/*
   Code to run on the Arduino of the RoseBot.
   This version implements a simple protocal in which:
*/

#include "commands.h"
#define DEBUG gsldr

// TODO: All the following constants should be setable via a
// message that the Python program sends to the robot
// when making a connection.
#define MILLISECONDS_TO_DELAY_IN_READ_LOOP 50
#define BAUD_RATE 57600

// TODO: Improve this very simple protocol / encoding.
// Can compact the messages and perhaps should include
// error correction.

#define NUMBER_OF_DIGITAL_PINS 16

long number_of_bad_commands = 0;

// TODO: Can I leave communication error-handling to the Serial library?
// Maybe use error-correcting settings???

// TODO: Does a Serial WRITE also need a delay?

// TODO: At most 256 "top-level" commands.  In fact, will be fewer
// since we will encode the data for some commands in the opcode byte.
// Is limit of 256 adequate?  (I think so.)  DOCUMENT IT.

Command COMMANDS[MAX_NUMBER_OF_COMMANDS];

void setup() {
  // Once the pinMode command is working, the Python program
  // will set the following:
  Serial.begin(BAUD_RATE);
  delay(2000);
  
  pinMode(13, OUTPUT); // LED
  pinMode(12, INPUT_PULLUP);  // Button
  pinMode(A0, INPUT);

  // For the motors:
  pinMode(2, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(7, OUTPUT);
  pinMode(8, OUTPUT);
  
  digitalWrite(13, HIGH);

  //write_byte((byte) 97);

  // TODO: Is the following all that needs to happen here?
  

  COMMANDS[ANALOG_READ].opcode = ANALOG_READ;
  COMMANDS[ANALOG_READ].number_of_data_bytes = 0;

  COMMANDS[ANALOG_WRITE].opcode = ANALOG_WRITE;
  COMMANDS[ANALOG_WRITE].number_of_data_bytes = 1;

  COMMANDS[DIGITAL_READ].opcode = DIGITAL_READ;
  COMMANDS[DIGITAL_READ].number_of_data_bytes = 1;

  COMMANDS[DIGITAL_WRITE].opcode = DIGITAL_WRITE;
  COMMANDS[DIGITAL_WRITE].number_of_data_bytes = 1;

  COMMANDS[PIN_MODE].opcode = PIN_MODE;
  COMMANDS[PIN_MODE].number_of_data_bytes = 1;

  COMMANDS[ANALOG_READ].opcode = ANALOG_READ;
  COMMANDS[ANALOG_READ].number_of_data_bytes = 0;

  COMMANDS[TONE].opcode = TONE;
  COMMANDS[TONE].number_of_data_bytes = 2;

  COMMANDS[NO_TONE].opcode = NO_TONE;
  COMMANDS[NO_TONE].number_of_data_bytes = 0;
}

void loop() {
  Command* command;

  command = fetch_command();
  execute_command(command);
}

/*
   Reads from the stream that is sending robot commands
   for this program to execute.  Returns a pointer to
   the Command indicated by those bytes, after filling in
   the data read into the Command.
*/
Command* fetch_command() {
  byte opcode_byte;
  int opcode;
  Command* command;
  opcode_byte = read_byte();
  opcode = get_opcode(opcode_byte);
  command = &(COMMANDS[opcode]);

  command->opcode_byte = opcode_byte;
  command->pin = get_pin(command);
   read_bytes(command->data_bytes, command->number_of_data_bytes);
  command->value = get_value(command);
  // if (DEBUG) echo(command, "Fetch:   ");
  return command;
}

byte get_opcode(byte opcode_byte) {
  return opcode_byte;  // Simple implementation
  // return ((opcode_byte & 0xF0) >> 4);
}

byte get_pin(Command* command) {
  return read_byte(); // simple implementation
  // return (command->opcode_byte & 0x0F);
}

byte get_value(Command* command) {
  if (command->number_of_data_bytes > 0) {
    return command->data_bytes[0];
  } else {
    return 0;
  }
}

// Perform a Serial read of 1 byte.  This function must be used
// for ALL Serial reads herein, to ensure reliable communication.
byte read_byte() {
  while (1) {
    delay(MILLISECONDS_TO_DELAY_IN_READ_LOOP);
    if (Serial.available()) {
      byte received = Serial.read();
      return received;
    }
  }
}

void write_byte(byte byte_to_write) {
  Serial.write(byte_to_write);
}

// Perform a Serial read of n bytes, putting the results
// into the given array of bytes.
void read_bytes(byte bytearray[], int n) {
  for (int k = 0; k < n; ++k) {
    bytearray[k] = read_byte();
  }
}

void write_bytes(byte byte_array[], int number_of_bytes_to_write) {
  for (int k = 0; k < number_of_bytes_to_write; ++k) {
    write_byte(byte_array[k]);
  }
}

void blink(int msec) { // for testing
  for (int k = 0; k < 10; ++k) {
    digitalWrite(13, LOW);
    delay(msec);
    digitalWrite(13, HIGH);
    delay(msec);
  }
  delay(2000);
}

void echo(Command* command, char* message) { // for testing
  Serial.println(message);
  write_byte(command->opcode);
  write_byte(command->number_of_data_bytes);
  write_byte(command->opcode_byte);
  write_byte(command->pin);
  
  for (int k = 0; k < command->number_of_data_bytes; ++k) {
    write_byte(command->data_bytes[k]);
  }
}

// Execute the command stored in the given array of bytes.
void execute_command(Command* command) {
  write_byte((byte) (48 + command->opcode));
  command->pin = 12;
  write_byte((byte) (48 + command->pin));
  // if (DEBUG) blink(100); //echo(command, "Execute: ");
  switch (command->opcode) {
    case ANALOG_READ:
      // TODO: confirm that shift/cast is correct here for a 1-byte answer.
      write_byte((byte) (analogRead(A0 + command->pin) >> 2));
      break;
    case ANALOG_WRITE:
      analogWrite(command->pin, command->value);
      break;
    case DIGITAL_READ:
      write_byte((byte) 99);
      write_byte((byte) (digitalRead(command->pin)));
      break;
    case DIGITAL_WRITE:
      digitalWrite(command->pin, command->value);
      break;
    case PIN_MODE:
      pinMode(command->pin, command->value);
      break;
    case TONE:
      // TODO
      break;
    case NO_TONE:
      noTone(command->pin);
    default:
      // Signifies bad data.
      // For now, just keep track of how often this happens.
      // TODO: Error handling.
      ++ number_of_bad_commands;
  }
}


