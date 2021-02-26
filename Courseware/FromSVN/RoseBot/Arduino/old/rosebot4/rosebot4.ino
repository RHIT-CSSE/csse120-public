/*
 * Code to run on the Arduino of the RoseBot.
 * This version implements a simple protocal in which:

 */
// TODO: All the following constants should be setable via a
// message that the Python program sends to the robot
// when making a connection.
#define MILLISECONDS_TO_DELAY_IN_READ_LOOP 50
#define BAUD_RATE 115200

// TODO: Improve this very simple protocol / encoding.
// Can compact the messages and perhaps should include
// error correction.
#define ANALOG_READ_COMMAND 0
#define ANALOG_WRITE_COMMAND 1
#define DIGITAL_READ_COMMAND 2
#define DIGITAL_WRITE_COMMAND 3
#define PIN_MODE_COMMAND 4
#define TONE_COMMAND 5
#define NO_TONE_COMMAND 6

#define CODE_FOR_INPUT 0
#define CODE_FOR_OUTPUT 1
#define CODE_FOR_INPUT_PULLUP 2

#define NUMBER_OF_DIGITAL_PINS 16

long number_of_bad_commands = 0;

void setup() {
  // Replace following once done testing.
  pinMode(13, OUTPUT);
  digitalWrite(13, HIGH);
  
  // TODO: Is the following all that needs to happen here?
  Serial.begin(BAUD_RATE);
}


void loop() {
  digitalWrite(13, LOW);
  delay(2000);
  byte command_byte = read_byte();
  digitalWrite(13, HIGH);
  delay(2000);
  Serial.write(command_byte);
  
  //Serial.println(command_byte);
  
/*
  switch (command_byte) {
    case ANALOG_READ_COMMAND:
      process_analog_read_command(command_byte);
      break;
    case ANALOG_WRITE_COMMAND:
      process_analog_write_command(command_byte);
      break;
    case DIGITAL_READ_COMMAND:
      process_digital_read_command(command_byte);
      break;
    case DIGITAL_WRITE_COMMAND:
      process_digital_write_command(command_byte);
      break;
    case PIN_MODE_COMMAND:
      process_pin_mode_command(command_byte);
      break;
    case TONE_COMMAND:
      process_tone_command(command_byte);
      break;
    case NO_TONE_COMMAND:
      process_no_tone_command(command_byte);
      break;
    default:
      // Signifies bad data.
      // For now, just keep track of how often this happens.
      // TODO: Error handling.
      ++ number_of_bad_commands;
    }
    */
}

byte read_byte() {
  // This should be used for ALL Serial reads.
  // It always does at least one delay, so any two Serial reads
  // are always separated by at least one delay.
  while (1) {
    delay(MILLISECONDS_TO_DELAY_IN_READ_LOOP);
    if (Serial.available()) {
      byte received = Serial.read();
//      Serial.println(received);
      return received;
    }
  }
}

// Both   get_pin_number  and  get_byte_to_write  have the
// command_byte as a parameter, anticipating that eventually
// some of the information will be packed within the command_byte.
// Currently, the Serial byte immediately following the command_byte
// encodes the pin number, and (for writes) the Serial byte
// after that is the value to be written (or the mode to set).
// TODO: Make a better encoding.

int get_pin_number(byte command_byte) {
  int pin_number = read_byte();

  // Numbers up to NUMBER_OF_DIGITAL_PINS are digital pin number.
  // After that comes A0, A1, ...
  
  // CRITICAL TODO: Confirm that A0, A1, ... are sequential.
  // Also confirm that reads want an INT not a BYTE.
  
  if (pin_number < NUMBER_OF_DIGITAL_PINS) {
    return pin_number;
  } else {
    return pin_number - NUMBER_OF_DIGITAL_PINS + A0;
  }
  // TODO: Error handling in the above.
}

byte get_byte_to_write(byte command_byte) {
  byte received = read_byte();
  return received;
}

byte get_mode(byte command_byte) {
  return get_byte_to_write(command_byte);
}

// All of the following have the command_byte as a parameter
// because eventually other information may be packed inside it.
// TODO: error handling, return code for success/failure.

bool process_analog_read_command(byte command_byte) {
  int pin = get_pin_number(command_byte);

  // Send via Serial the analog value at that pin.
  // For now, do so as a 256-bit number to simplify the protocol.
  // TODO: Return all 10 bits that are available.

  Serial.write(analogRead(pin) / 4);
}

bool process_analog_write_command(byte command_byte) {
  int pin = get_pin_number(command_byte);
  int value = get_byte_to_write(command_byte);
  analogWrite(pin, value);
}

bool process_digital_read_command(byte command_byte) {
  int pin = get_pin_number(command_byte);
  Serial.write(digitalRead(pin));
}

bool process_digital_write_command(byte command_byte) {
  Serial.print("digitalwrite\n");
  int pin = get_pin_number(command_byte);
  Serial.print(pin);
  int value = get_byte_to_write(command_byte);
  Serial.print(value);
  if (value == 1) {
    digitalWrite(13, HIGH);
  } else {
    digitalWrite(13, LOW);
  }
}

bool process_pin_mode_command(byte command_byte) {
  int pin = get_pin_number(command_byte);
  int mode = get_mode(command_byte);
  switch (mode) {
    case CODE_FOR_INPUT: pinMode(pin, INPUT); break;
    case CODE_FOR_OUTPUT: pinMode(pin, OUTPUT); break;
    case CODE_FOR_INPUT_PULLUP: pinMode(pin, INPUT_PULLUP); break;
//    default: // TODO: Error handling.
  }
}

bool process_tone_command(byte command_byte) {
  // TODO
}

bool process_no_tone_command(byte command_byte) {
  int pin = get_pin_number(command_byte);
  noTone(pin);

}


