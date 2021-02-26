
#define PIN_PUSHBUTTON 12
#define PIN_LED_ON_BOARD 13

int pushbuttonState;

void setup() {
  Serial.begin(115200);

  // Rx setup
  pinMode(PIN_LED_ON_BOARD, OUTPUT);
  digitalWrite(PIN_LED_ON_BOARD, HIGH);

  // Tx setup
  pinMode(PIN_PUSHBUTTON, INPUT_PULLUP);
}

void loop() {
  if (Serial.available()) {
    byte received = Serial.read();
    if (received % 2 == 0) {
        digitalWrite(PIN_LED_ON_BOARD, HIGH);
    } else {
        digitalWrite(PIN_LED_ON_BOARD, LOW);
    }
    pushbuttonState = digitalRead(PIN_PUSHBUTTON);
//    Serial.print("Button = ");
    Serial.write((char) (48 + pushbuttonState));
    delay(1000);
  }
}
