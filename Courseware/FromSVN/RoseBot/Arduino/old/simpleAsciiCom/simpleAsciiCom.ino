#define PIN_PUSHBUTTON 12
#define PIN_LED_ON_BOARD 13

// Related to Rx
String inputString = "";
boolean stringComplete = false;

// Related to Tx
int pushbuttonState;
unsigned long currentTimeMs;
unsigned long lastTransmitTimeMs = 0;
int TRANSMIT_INTERVAL_MS = 1000;

void setup() {
  Serial.begin(115200);

  // Rx setup
  inputString.reserve(200);
  pinMode(PIN_LED_ON_BOARD, OUTPUT);

  // Tx setup
  pinMode(PIN_PUSHBUTTON, INPUT_PULLUP);
}

void loop() {

  // Rx
  if (stringComplete) {
    // TODO: Parse the message.  Here thre is no 'real' parsing just looking at the whole message.
    if (inputString.equalsIgnoreCase("LED ON")) {
      digitalWrite(PIN_LED_ON_BOARD, HIGH);
    } else if (inputString.equalsIgnoreCase("LED OFF")) {
      digitalWrite(PIN_LED_ON_BOARD, LOW);
    }    
    inputString = "";
    stringComplete = false;
  }

  // Tx
  currentTimeMs = millis();
  if ((currentTimeMs - lastTransmitTimeMs) > TRANSMIT_INTERVAL_MS) {
    lastTransmitTimeMs = currentTimeMs;
    pushbuttonState = digitalRead(PIN_PUSHBUTTON);
    Serial.print("Button = ");
    Serial.println(pushbuttonState);
  }
}

// Rx
void serialEvent() {
  while (Serial.available()) {
    char inChar = (char)Serial.read();
    if (inChar == '\n') {
      stringComplete = true;
    } else {    
      inputString += inChar;
    }
  }
}


