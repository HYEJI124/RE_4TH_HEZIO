int leds[] = {10, 11, 12};
int count = 3;

void turnOnAll() {
    for (int i = 0; i < count; i++) {
        digitalWrite(leds[i], HIGH);
        delay(500);
    }
}

void turnOffAll() {
    for (int i = 0; i < count; i++) {
        digitalWrite(leds[i], LOW);
        delay(500);
    }
}

void setup() {
    for (int i = 0; i < count; i++) {
        pinMode(leds[i], OUTPUT);
    }
}

void loop() {
    turnOnAll();
    turnOffAll();
}