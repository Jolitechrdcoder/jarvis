int bombilloPin = 13;
char incomingByte;

void setup() {
  Serial.begin(9600);
  pinMode( bombilloPin, OUTPUT);

  // Enciende el bombillo al inicio
  digitalWrite( bombilloPin, HIGH);;
}

void loop() {
  if (Serial.available() > 0) {
    incomingByte = Serial.read();
    if (incomingByte == '1') {
      digitalWrite( bombilloPin, LOW);  // Enciende el bombillo (lógica inversa)
    } else if (incomingByte == '0') {
      digitalWrite( bombilloPin, HIGH);  // Apaga el bombillo(lógica inversa)
    }
  }
}
