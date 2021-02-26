/*
 * Code to run on the Arduino of the RoseBot.
 * This version implements a simple protocal in which:

 */
// TODO: All the following constants should be setable via a
// message that the Python program sends to the robot
// when making a connection.
#define MILLISECONDS_TO_DELAY_IN_READ_LOOP 50
#define BAUD_RATE 57600
#define MESSAGE_SIZE 3

// TODO: Improve this very simple protocol / encoding.
// Can compact the messages and perhaps should include
// error correction.

#define CODE_FOR_INPUT 0
#define CODE_FOR_OUTPUT 1
#define CODE_FOR_INPUT_PULLUP 2

#define NUMBER_OF_DIGITAL_PINS 16

//Types of actions the user can do
enum actions {ANALOG_READ, ANALOG_WRITE, DIGITAL_READ, DIGITAL_WRITE, PIN_MODE, TONE};
//List of connected sensors/devices the user could want to use
enum signals {LED, BUZZER, BUTTON,
              L_BUMPER, R_BUMPER,
              L_LINE, C_LINE, R_LINE,
              L_ENCODER, R_ENCODER,
              L_DISTANCE, C_DISTANCE, R_DISTANCE,
              L_MOTOR_CTRL_1, L_MOTOR_CTRL_2, L_MOTOR_PWM,
              R_MOTOR_CTRL_1, R_MOTOR_CTRL_2, R_MOTOR_PWM};
//The pin that each of these things is on
int pinmap[19] = {13, 9, 12,
                  3, 10,
                  A3, A6, A7, 
                  A2, A1, 
                  A0, A4, A5,
                  2, 4, 5, 
                  7, 8, 6};

void setup() {
  // Set pin modes for all pins on robot
  pinMode(pinmap[LED], OUTPUT);
  pinMode(pinmap[BUZZER], OUTPUT);
  pinMode(pinmap[BUTTON], INPUT_PULLUP);
  pinMode(pinmap[L_BUMPER], INPUT_PULLUP);
  pinMode(pinmap[R_BUMPER], INPUT_PULLUP);
  pinMode(pinmap[L_LINE], INPUT);
  pinMode(pinmap[C_LINE], INPUT);
  pinMode(pinmap[R_LINE], INPUT);
  pinMode(pinmap[L_ENCODER], INPUT);
  pinMode(pinmap[R_ENCODER], INPUT);
  pinMode(pinmap[L_DISTANCE], INPUT);
  pinMode(pinmap[C_DISTANCE], INPUT);
  pinMode(pinmap[R_DISTANCE], INPUT);
  pinMode(pinmap[L_MOTOR_CTRL_1], OUTPUT);
  pinMode(pinmap[L_MOTOR_CTRL_2], OUTPUT);
  pinMode(pinmap[L_MOTOR_PWM], OUTPUT);
  pinMode(pinmap[R_MOTOR_CTRL_1], OUTPUT);
  pinMode(pinmap[R_MOTOR_CTRL_2], OUTPUT);
  pinMode(pinmap[R_MOTOR_PWM], OUTPUT);

  digitalWrite(13, HIGH);
  // TODO: Is the following all that needs to happen here?
  Serial.begin(BAUD_RATE);
}


void loop() {
  byte command[MESSAGE_SIZE];
  fetch_command(command);
  execute_command(command);
}

/**********************************************************
 * Command Processing Functions
 **********************************************************/
void fetch_command(byte buffer[]){
  read_message(buffer);
}

void execute_command(byte command[]){
  byte command_type=command[0];
  byte command_pin=pinmap[command[1]]; //Pulls actual HW pin from pinmap (as compared to theoretical map given by message)
  byte command_value=command[2];
  //write_bytes(command,3);
  switch (command_type){
    case ANALOG_READ:
      // TODO: confirm that shift/cast is correct here.
      write_bytes("ac",2);
      write_byte(command_type);
      write_byte(command_pin);
      Serial.write((byte) (analogRead(command_pin) / 4));
      break;
    case ANALOG_WRITE:
      write_bytes("ack2",4);
      analogWrite(command_pin, command_value);
      break;
    case DIGITAL_READ:
      write_bytes("ack3", 4);
      Serial.write((digitalRead(command_pin)));
      break;
    case DIGITAL_WRITE:
      write_bytes("ack4",4);
      digitalWrite(command_pin, command_value);
      break;
    case PIN_MODE:
      write_bytes("ack5",4);
      pinMode(command_pin, command_value);
      break;
    case TONE:
      write_bytes("ack6",4);
      process_tone_command(command_value);
      break;
    default:
      // Signifies bad data.
      // For now, just keep track of how often this happens.
      // TODO: Error handling.
      write_bytes("bad ",4);
  }
 
}

bool process_tone_command(byte command_byte) {
  int pin = pinmap[BUZZER];
  if (command_byte == 0) noTone(pin);
  else{
    //Calculate frequency
    int fn = 440 * pow(1.059463094359,(command_byte-40));//equation from: http://www.phy.mtu.edu/~suits/NoteFreqCalcs.html
    // int fn = (int) (4978  * (command_byte / 255.0));
    tone(pin,fn);
  }

}
/**********************************************************
 * Communication Functions
 **********************************************************/
 
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

//This both writes out to output and clears input buffer
void write_byte(byte byte_to_write) {
  flush_serial();
  Serial.write(byte_to_write);
}

void flush_serial(){
  while (Serial.available()){
    byte clear=Serial.read();
  }
}

// Perform a Serial read of n bytes, putting the results
// into the given array of bytes.
void read_message(byte bytearray[]) {
  for (int k = 0; k < MESSAGE_SIZE; ++k) {
    bytearray[k] = read_byte();
  }
}

void write_bytes(byte byte_array[], int number_of_bytes_to_write) {
  for (int k = 0; k < number_of_bytes_to_write; ++k) {
    write_byte(byte_array[k]);
  }
}

