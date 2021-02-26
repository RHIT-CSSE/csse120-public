int count, count2;

void setup() {
  // put your setup code here, to run once:
  count = 0;
  pinMode(13, OUTPUT);

  pinMode(A2, INPUT_PULLUP);
  pinMode(A1, INPUT_PULLUP);
  attachInterrupt(digitalPinToInterrupt(A2), button, FALLING);
  attachInterrupt(digitalPinToInterrupt(A1), button, FALLING);

  Serial.begin(57600);
}

void loop() {
  Serial.print(count);
  Serial.print(" ");
  Serial.println(count2);
  delay(3000);
  count = count + 1;
  digitalWrite(13, LOW);
  if (digitalRead(10) == 0) {
    Serial.println("pressed");
  }
}

void button() {
  digitalWrite(13, HIGH);
  count2 = count2 + 1;
}

