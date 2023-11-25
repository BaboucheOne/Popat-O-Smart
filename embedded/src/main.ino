
const int BAUD_RATE = 9600;
const int CAPACITIVE_SOIL_SENSOR_PIN = A0;
const int PUMP_PIN = 7;

const int CAPACITIVE_SOIL_DRY_RAW = 500;
const int CAPACITIVE_SOIL_WET_RAW = 100;
const int CAPACITIVE_SOIL_MAX_VALUE = 100;
const int CAPACITIVE_SOIL_MIN_VALUE = 0;

const int TURN_ON_PUMP_HUMIDITY_THRESHOLD = 25;
const int TURN_OFF_PUMP_HUMIDITY_THRESHOLD = 85;

enum State {READ_VALUE, TURN_ON_PUMP, FILL, TURN_OFF_PUMP};
State currentState = READ_VALUE;

void setup() {
    Serial.begin(BAUD_RATE);
    pinMode(PUMP_PIN, OUTPUT);
}

int capacitiveSoilVoltageToHumidity(int value) {
    return map(value, CAPACITIVE_SOIL_WET_RAW, CAPACITIVE_SOIL_DRY_RAW,
        CAPACITIVE_SOIL_MIN_VALUE, CAPACITIVE_SOIL_MAX_VALUE);
}

int readCapacitiveSoilSendor() {
    int capacitiveSoilSensorRaw = analogRead(CAPACITIVE_SOIL_SENSOR_PIN);
    return capacitiveSoilSensorHumidity(capacitiveSoilSensorRaw);
}

void loop() {
    int capacitiveSoilSensorRaw = analogRead(CAPACITIVE_SOIL_SENSOR_PIN);
    int capacitiveSoilSensorHumidity = capacitiveSoilSensorHumidity(capacitiveSoilSensorRaw);

    switch (currentState)
    {
        case READ_VALUE:
            ReadValueState();
            break;

        case TURN_ON_PUMP:
            TurnOnPumpState();
            break;

        case FILL:
            FillState();
            break;

        case TURN_OFF_PUMP:
            TurnOffPumpState();
            break;
    
        default:
        DefaultState();
            break;
    }
}

void ReadValueState() {
    int capacitiveSoilSensorHumidity = readCapacitiveSoilSendor();
    if(capacitiveSoilSensorHumidity < TURN_ON_PUMP_HUMIDITY_THRESHOLD)
    {
        currentState = TURN_ON_PUMP;
    }
}

void TurnOnPumpState() {
    digitalWrite(PUMP_PIN, HIGH);
    currentState = FILL;
}

void FillState() {
    int capacitiveSoilSensorHumidity = readCapacitiveSoilSendor();
    if(TURN_OFF_PUMP_HUMIDITY_THRESHOLD <= capacitiveSoilSensorHumidity)
    {
        currentState = TURN_OFF_PUMP;
    }
}

void TurnOffPumpState() {
    digitalWrite(PUMP_PIN, LOW);
    currentState = READ_VALUE;
}

void DefaultState() {
    digitalWrite(PUMP_PIN, LOW);
}
