// 매개변수화
// 함수에는 매개변수를 사용해서 더 확장성 있는 함수를 선언할 수 있음

int leds[] = {10, 11, 12};
int count = 3;
int delayMs = 500;

void blinkAll(bool state) {
    for (int i = 0; i < count; i++) {
        digitalWrite(leds[i], state ? HIGH : LOW);
        delay(delayMs);
    }
}

void setup() {
    for (int i = 0; i < count; i++) {
        pinMode(leds[i], OUTPUT);
    }
}

void loop() {
    blinkAll(true);
    blinkAll(false);
}
