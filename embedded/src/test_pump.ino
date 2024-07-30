
const int BAUD_RATE = 9600;
const int PUMP_PIN = 7;

void setup() {
    Serial.begin(BAUD_RATE);
    pinMode(PUMP_PIN, OUTPUT);
}

void loop() {
    digitalWrite(PUMP_PIN, LOW);
    delay(3000);
    digitalWrite(PUMP_PIN, HIGH);
    delay(3000);
}

void TurnOnPumpState() {
    digitalWrite(PUMP_PIN, HIGH);
}

void TurnOffPumpState() {
    digitalWrite(PUMP_PIN, LOW);
}
