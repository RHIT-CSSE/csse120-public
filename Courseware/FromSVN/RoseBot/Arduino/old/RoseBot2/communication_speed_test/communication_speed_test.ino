
/*
 * Uses the master/slave architecture that RoseBot uses:
 *   -- External program (typically the student's Python prograam)
 *      is the master.
 *   -- This Arduino program is the slave.
 * 
 * In this simple version:
 *   -- The master is expected to repeatedly send an 8-bit number (byte).
 *   -- Upon reception of a byte, this slave sends that byte plus 1 (wrapping to 0).
 */
 
#define BAUD_RATE 57600
#define LED 13

void setup() {
  pinMode(13, OUTPUT);
  Serial.begin(BAUD_RATE);
//  blink(4);
}

void loop() {
  byte n;

  n = read_byte();
//  blink(2);
  write_byte((byte) (n + 1));
}

// Perform a Serial read of 1 byte.  This function must be used
// for ALL Serial reads herein, to ensure reliable communication.
byte read_byte() {
  while (1) {
//    delay(MILLISECONDS_TO_DELAY_IN_READ_LOOP);
    if (Serial.available()) {
      byte received = Serial.read();
      return received;
    }
  }
}

void write_byte(byte byte_to_write) {
//  flush_serial();
  Serial.write(byte_to_write);
}

// Blink n times.
void blink(int n) {
  for (int k = 0; k < n; ++k) {
    digitalWrite(LED, LOW);
    delay(250);
    digitalWrite(LED, HIGH);
    delay(250);
  }
}

