
// TODO: All the following constants should be setable via a
// message that the Python program sends to the robot
// when making a connection.
#define MILLISECONDS_TO_DELAY_IN_LOOP 50
#define MILLISECONDS_TO_DELAY_BETWEEN_READS 50
#define BAUD_RATE 115200

// TODO: Improve this very simple protocol / encoding.
// Can compact the messages and perhaps should include
// error correction.
#define ANALOG_READ_COMMAND 0
#define ANALOG_WRITE_COMMAND 1
#define DIGITAL_READ_COMMAND 2
#define DIGITAL_WRITE_COMMAND 3
#define SET_MODE_COMMAND 4

// TODO: Get this data from the Python program when it connects.
// TODO: Get initial values for OUTPUT pins; all set to HIGH for now.
// TODO: There are other modes too.
int number_of_pins_for_digital_input_pullup = 1;
int number_of_pins_for_digital_output = 5;
int number_of_pins_for_analog_input = 8;
int number_of_pins_for_output_for_PWM = 2;
int number_of_pins_for_analog_output_for_Servo = 0;
int number_of_pins_for_tone = 1;

int pins_for_digital_input_pullup[] = {12};
int pins_for_digital_output[] = {2, 4, 7, 8, 13};
int pins_for_analog_input[] = {0, 4, 5, 3, 6, 7, 2, 11};
int pins_for_output_for_PWM[] = {5, 6};
int pins_for_analog_output_for_Servo[] = {};
int pins_for_tone[] = {9};

long number_of_bad_packets = 0;

void setup() {
  // TODO: Is the following all that needs to happen here?
  Serial.begin(BAUD_RATE);

  setup_for_digital_input();
  setup_for_digital_output();
//  setup_for_PWM();  TODO: Test these after asking Dave about them.
//  setup_for_Servo();  I don't know how to do these.
//  setup_for_tone();   I think that these do not require setup.
//  setup_for_analog_input();  I think that these do not require setup.

}


void loop() {
    byte received = read_byte();
    Serial.println(received);

    switch (received) {
      case ANALOG_READ_COMMAND:
        process_analog_read_command(received);
        break;
      case ANALOG_WRITE_COMMAND:
        process_analog_write_command(received);
        break;
      case DIGITAL_READ_COMMAND:
        process_digital_read_command(received);
        break;
      case DIGITAL_WRITE_COMMAND:
        process_digital_write_command(received);
        break;
      case SET_MODE_COMMAND:
        process_set_mode_command(received);
        break;
      default:
        // Signifies bad data.
        // For now, just keep track of how often this happens.
        // TODO: Error handling.
        ++ number_of_bad_packets;
    }
}

byte read_byte() {
  while (! Serial.available()) {
    delay(MILLISECONDS_TO_DELAY_IN_LOOP);
  }
  return Serial.read();
}

void setup_for_digital_input() {
  for (int k = 0; k < number_of_pins_for_digital_input_pullup; ++k) {
    pinMode(pins_for_digital_input_pullup[k], INPUT_PULLUP);
  }
}

void setup_for_digital_output() {
  for (int k = 0; k < number_of_pins_for_digital_output; ++k) {
    pinMode(pins_for_digital_output[k], OUTPUT);
    // TODO: HIGH is not the right initial value for all these.
    digitalWrite(pins_for_digital_output[k], HIGH);
  }
}
void  setup_for_PWM() {
  for (int k = 0; k < number_of_pins_for_output_for_PWM; ++k) {
    // TODO: These are set as PWM in rosebot_low_level.
    // What does that mean here?
    pinMode(pins_for_output_for_PWM[k], OUTPUT);
    digitalWrite(pins_for_output_for_PWM[k], LOW);
  }
}
void  setup_for_Servo() {
  // TODO
}
void setup_for_tone() {
  
}
  
bool process_analog_read_command(byte command) {
  // The argument is the command.
  // It may eventually have other data packed with the command.

  // Next byte is the PIN number.
  // TODO: Error handling.
  delay(MILLISECONDS_TO_DELAY_BETWEEN_READS);
  byte pin = Serial.read();

  // Return the analog value at that pin.
  // For now, do so as a 256-bit number to simplify the protocol.
  // TODO: Return all 10 bits that are available.

  return analogRead(pin) / 4;
}

bool process_digital_read_command(byte command) {
  // The argument is the command.
  // It may eventually have other data packed with the command.

  // Next byte is the PIN number.
  // TODO: Error handling.
  delay(MILLISECONDS_TO_DELAY_BETWEEN_READS);
  byte pin = Serial.read();

  // Return the digital value at that pin.

  return digitalRead(pin);
}

void process_analog_write_command(byte command) {
  // The argument is the command.
  // It may eventually have other data packed with the command.

  // Next byte is the PIN number.
  // TODO: Error handling.
  delay(MILLISECONDS_TO_DELAY_BETWEEN_READS);
  byte pin = Serial.read();

  // The byte after that is either 1 (for HIGH) or 0 (for LOW).
  // TODO: Error handling.
  delay(MILLISECONDS_TO_DELAY_BETWEEN_READS);
  byte value = read_byte();

  // Set the pin to that value.
  analogWrite(pin, value);
}

void process_digital_write_command(byte command) {
  // The argument is the command.
  // It may eventually have other data packed with the command.

  // Next byte is the PIN number.
  // TODO: Error handling.
  delay(MILLISECONDS_TO_DELAY_BETWEEN_READS);
  byte pin = read_byte();
//  Serial.print("first ");
//  Serial.println(pin);

  // The byte after that is either 1 (for HIGH) or 0 (for LOW).
  // TODO: Error handling.
  delay(MILLISECONDS_TO_DELAY_BETWEEN_READS);
  byte value = read_byte();
  
  // Set the pin to that value.
  if (value == 1) {
    digitalWrite(pin, HIGH);
  } else if (value == 0) {
    digitalWrite(pin, LOW);
  } else {
    // Bad data for the value.
    // TODO: Error handling.
  }
}

void process_set_mode_command(byte command) {
  // TODO: Implement this.
}
