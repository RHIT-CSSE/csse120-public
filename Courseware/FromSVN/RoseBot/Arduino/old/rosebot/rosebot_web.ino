/************************************************************************
 * Code to run on the Arduino of the RoseBot.
 * This version implements a simple protocal in which the Arduino:
 *   1. Reads bytes until there are no more to be read.
 *        These come from the WiFLy device and connection,
 *        not from the Python program.
 *   2. Repeatedly:
 *        a. Reads bytes that form a COMMAND and its data.
 *        b. Writes an acknowledgement.
 *        c. Executes the COMMAND, possibly sending more bytes
 *             as directed by the COMMAND.
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

#include <SPI.h>
#include <Pixy.h>

// TODO: Allow all constants to be set by the Python program via an
//       initialization protocol.

#define MILLISECONDS_TO_DELAY_IN_READ_LOOP 10
#define BAUD_RATE 57600
#define MESSAGE_SIZE 3

// Commands that the user can send to this program:
enum actions {
  ANALOG_READ, ANALOG_WRITE, DIGITAL_READ, DIGITAL_WRITE, PIN_MODE, TONE,
  DRIVE, GET_PIXY_BLOCK
  };

// Connected sensors/devices the user might want to use:
enum signals {LED, BUZZER, BUTTON,
              L_BUMPER, R_BUMPER,
              L_LINE, C_LINE, R_LINE,
              L_ENCODER, R_ENCODER,
              L_DISTANCE, C_DISTANCE, R_DISTANCE,
              L_MOTOR_CTRL_1, L_MOTOR_CTRL_2, L_MOTOR_PWM,
              R_MOTOR_CTRL_1, R_MOTOR_CTRL_2, R_MOTOR_PWM};

// The pin that each of these sensors/devices is on:
int pinmap[19] = {13, 9, 12,
                  3, 10,
                  A3, A6, A7, 
                  A2, A1, 
                  A0, A4, A5,
                  2, 4, 5, 
                  7, 8, 6};

// The pin modes for each of these sensors/devices:

#define number_of_output_pin_devices 8
int output_pin_mode_devices[number_of_output_pin_devices] = {
  LED, BUZZER,
  L_MOTOR_CTRL_1,  L_MOTOR_CTRL_2, L_MOTOR_PWM,
  L_MOTOR_CTRL_1,  L_MOTOR_CTRL_2, R_MOTOR_PWM
};

#define number_of_input_pin_devices 8
int input_pin_mode_devices[number_of_input_pin_devices] = {
  L_LINE, C_LINE, R_LINE,
  L_ENCODER, R_ENCODER,
  L_DISTANCE, C_DISTANCE, R_DISTANCE
};

#define number_of_input_pullup_pin_devices 3
int input_pullup_pin_mode_devices[number_of_input_pullup_pin_devices] = {
  BUTTON, L_BUMPER, R_BUMPER
};

Pixy pixy;
volatile long left_encoder_count;
volatile long right_encoder_count;

bool pixy_is_initialized = false;  // First Pixy command initializes the Pixy.

void setup() {
  
  // Set pin modes for the pins of all the sensors/devices on the robot:
  for (int k = 0; k < number_of_output_pin_devices; ++k) {
    pinMode(pinmap[output_pin_mode_devices[k]], OUTPUT);
  }
  for (int k = 0; k < number_of_input_pin_devices; ++k) {
    pinMode(pinmap[input_pin_mode_devices[k]], INPUT);
  }
  for (int k = 0; k < number_of_input_pullup_pin_devices; ++k) {
    pinMode(pinmap[input_pullup_pin_mode_devices[k]], INPUT_PULLUP);
  }

  // Start with the LED on (to indicate that the Arduino loop is running):
  // TODO: Have a better indicator.
  digitalWrite(pinmap[LED], HIGH);

  // The Pixy initialization is run
  // when the first Pixy request arrives.

  // Set up the Encoders.  Hard-coding PIN numbers for now.
  left_encoder_count = 0;
  right_encoder_count = 0;
  
//  pinMode(A1, INPUT_PULLUP);
//  attachInterrupt(A1,
//     update_right_encoder_count, CHANGE);
//     
//  pinMode(A2, INPUT_PULLUP);
//  attachInterrupt(A2,
//     update_left_encoder_count, CHANGE);
     
  // Begin communication:
  Serial.begin(BAUD_RATE);

  // "Eat" all the bytes that are sent right away.
  //   (Wait 1 second to be sure that all of them arrive.)
  // These come from the WiFly, not from the Python program.
  delay(1000);
  read_until_ready_to_start();

  // Blink to indicate that the code has entered the
  // fetch, acknowledge, execute loop.
  blink(4);
}

void loop() {
  byte command[MESSAGE_SIZE];
  
  fetch_command(command);
  send_acknowledgement(command);
  execute_command(command);
}

/************************************************************************
 * Interrupt handlers and associated resets.
 ***********************************************************************/
// The following ignores direction, as a first stab at this:
void update_right_encoder_count() {
  ++ right_encoder_count;
//  if (right_encoder_count % 2 == 0) {
//    digitalWrite(pinmap[LED], LOW);
//  } else {
//    digitalWrite(pinmap[LED], HIGH);
//  }
}

void update_left_encoder_count() {
  ++ left_encoder_count;
}

void reset_right_encoder_count() {
  right_encoder_count = 0;
}

void reset_left_encoder_count() {
  right_encoder_count = 0;
}

void reset_encoder_counts() {
  reset_right_encoder_count();
  reset_left_encoder_count();
}

/************************************************************************
 * Communication Protocol Functions.
 ***********************************************************************/

// Read Serial data until the Startup Sequence appears.
// Approach 1:  Read 13 bytes (expecting *HELLO**OPEN*).
// Approach 2:  Read until it sees 255 three times in a row.
//              Echo what it reads.

 void read_until_ready_to_start() {

  // Approach 3:  Read until there is nothing available.
  while (Serial.available()) {
      Serial.read();
    }
    
    
  // Approach 1. Seemed unreliable.
//  for (int k = 0; k < 13; ++k) {
//    delay(100);
//    byte byte_read = read_byte();
//    delay(100);
//    write_byte(byte_read);
//  }

  // Approach 2:
//  int count = 0;
//  
//  while (true) {
//    if (count >= 3) {
//      break;
//    }
//    int byte_read = read_byte();
//    write_byte(byte_read);
//    if (byte_read == 255) {
//      ++count;
//    } else {
//        count = 0;
//    }
//  }
}


// Current implementation:  Sends 254 3 times.
void send_start_message() {
  write_byte(254);
  write_byte(254);
  write_byte(254);
}

// Current implementation: Always reads 3 bytes, where:
//        Byte 1 encodes the COMMAND.
//        Byte 2 encodes the SIGNAL for the command (e.g. LED), if any.
//        Byte 3 encodes the DATA for the command
//          (e.g. a digital value to write), if any.
 void fetch_command(byte buffer[]) {
  read_message(MESSAGE_SIZE, buffer);
}

// Current implementation: writes the first byte of the command message.
void send_acknowledgement(byte command[]) {
  write_byte(command[0]);
}

/************************************************************************
 * Command Processing Functions.
 ***********************************************************************/

// Current implementation:
//        Byte 1 encodes the COMMAND.
//        Byte 2 encodes the SIGNAL for the command (e.g. LED), if any.
//        Byte 3 encodes the DATA for the command
//          (e.g. a digital value to write), if any.
void execute_command(byte command[]) {
  byte command_type = command[0];
  
   //Pulls actual HW pin from pinmap (as compared to theoretical map given by message)
  byte command_pin = pinmap[command[1]];
  
  byte command_value = command[2];
  
  switch (command_type) {
    case ANALOG_READ:
//      tone(pinmap[BUZZER], 10 * right_encoder_count);
//      delay(5 * right_encoder_count);
//      noTone(pinmap[BUZZER]);
      // TODO: confirm that shift/cast is correct here.
//      write_byte((byte) right_encoder_count);
      write_byte((byte) (analogRead(command_pin) / 4));
      break;
    case ANALOG_WRITE:
      analogWrite(command_pin, command_value);
      break;
    case DIGITAL_READ:
      write_byte((digitalRead(command_pin)));
      break;
    case DIGITAL_WRITE:
      digitalWrite(command_pin, command_value);
      break;
    case PIN_MODE:
      pinMode(command_pin, command_value);
      break;
    case TONE:
      process_tone_command(command_value);
      break;
    case DRIVE:
//      process_drive_command(command_pin, command_value);
      break;
    case GET_PIXY_BLOCK:
      process_get_pixy_block_command(command_value);
      break;
    default:
      break;
      // Signifies bad data.
      // TODO: Error handling.
  }
}

void process_tone_command(byte tone_byte) {
  int pin = pinmap[BUZZER];
  
  if (tone_byte == 0) {
    noTone(pin);
  } else {
    // Calculate frequency, via equation from:
    //    http://www.phy.mtu.edu/~suits/NoteFreqCalcs.html
    int fn = 440 * pow(1.059463094359, (tone_byte - 40));
    tone(pin, fn);
  }
}

// Current implementation returns only the biggest block,
// or 255 to indicate no blocks are seen.
void process_get_pixy_block_command(byte signature) {
  uint16_t number_of_blocks;
  byte bytes[6];

  if (! pixy_is_initialized) {
    initialize_Pixy();
    pixy_is_initialized = true;
  }

  number_of_blocks = pixy.getBlocks();
  for (int k = 0; k < number_of_blocks; ++k) {
    if (pixy.blocks[k].signature == signature) {
      // send info from pixy.blocks[k]:
      bytes[0] = highByte(pixy.blocks[k].x);
      bytes[1] = lowByte(pixy.blocks[k].x);
      bytes[2] = pixy.blocks[k].y;
      bytes[3] = highByte(pixy.blocks[k].width);
      bytes[4] = lowByte(pixy.blocks[k].width);
      bytes[5] = pixy.blocks[k].height;
      write_bytes(bytes, 6);
      return;
    }
  }
  
  write_byte(255);  // indicates no blocks of given signature
}


void initialize_Pixy() {
  blink(3);
  pixy.init();
  delay(1000);
}

void process_drive_command(byte left_wheel_pwm, byte right_wheel_pwm) {
}

/************************************************************************
 * Communication Functions.
 ***********************************************************************/
 
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
// DCM: Why flush the input buffer?  At most do it in write_bytes?
void write_byte(byte byte_to_write) {
  flush_serial();
  Serial.write(byte_to_write);
}

void flush_serial() {
  while (Serial.available()) {
    byte clear=Serial.read();
  }
}

// Perform a Serial read of n bytes, putting the results
// into the given array of bytes.  The given array must be big enough.
void read_message(int n, byte bytearray[]) {
  for (int k = 0; k < n; ++k) {
    bytearray[k] = read_byte();
  }
}

void write_bytes(byte byte_array[], int number_of_bytes_to_write) {
  for (int k = 0; k < number_of_bytes_to_write; ++k) {
    write_byte(byte_array[k]);
  }
}

/************************************************************************
 * Functions for Testing.
 ***********************************************************************/
 // Repeatedly read bytes.  When the startup sequence is read,
 // write a byte (first 0, then 1, then 2, ... 255, and wrapping thereafter).
 void test_read_bytes_until_the_startup_sequence() {
  byte count = 0;
  while (true) {
    read_until_ready_to_start();
    write_byte(count);
    count = (count + 1) % 255;
  }
}

 // Repeatedly reads a byte and writes that byte.
 void echo() {
  byte b = read_byte();
  write_byte(b);
}

// Blink n times.
void blink(int n) {
  for (int k = 0; k < n; ++k) {
    digitalWrite(pinmap[LED], LOW);
    delay(250);
    digitalWrite(pinmap[LED], HIGH);
    delay(250);
  }
}



