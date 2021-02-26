#include <Pixy.h>

#define BAUD_RATE 57600
#define LED 13
#define BUZZER 9
Pixy pixy;

void setup() {
  pinMode(LED, OUTPUT);
  initialize_Pixy();
  Serial.begin(BAUD_RATE);

}

void loop() {
  int signature = 0;
  get_pixy_blocks(signature);
  delay(500);
}

void initialize_Pixy() {
  blink(3);
  pixy.init();
  delay(1000);
}

void get_pixy_blocks(byte signature) {
  uint16_t number_of_blocks;

  number_of_blocks = pixy.getBlocks();
  Serial.println(number_of_blocks);

  for (uint16_t k = 0; k < number_of_blocks; ++k) {
    if (pixy.blocks[k].width < 30) {
      continue;
    }
    buzz(4);
    Serial.print(pixy.blocks[k].signature);
    Serial.print(" ");
    Serial.print(pixy.blocks[k].x);
    Serial.print(" ");
    Serial.print(pixy.blocks[k].x);
    Serial.print(" ");
    Serial.print(pixy.blocks[k].width);
    Serial.print(" ");
    Serial.print(pixy.blocks[k].height);
    Serial.println("");
  }
}

// Buzz n times.
void buzz(int n) {
  for (int k = 0; k < n; ++k) {
    tone(BUZZER, 220);
    delay(250);
    noTone(BUZZER);
    delay(250);
  }
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
