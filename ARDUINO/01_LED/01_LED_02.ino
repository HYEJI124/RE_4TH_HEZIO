int Blue_Pin = 10; // LED_BLUE
int Green_Pin = 11; // LED_GREEN
int Red_Pin = 12; // LED_RED

void setup() {
    pinMode(Blue_Pin, OUTPUT);
    pinMode(Green_Pin, OUTPUT);
    pinMode(Red_Pin, OUTPUT);
}

void loop() {
    // LED 켜기
    digitalWrite(Blue_Pin, HIGH);
    delay(500);
    digitalWrite(Green_Pin, HIGH);
    delay(500);
    digitalWrite(Red_Pin, HIGH);
    delay(500);

    // LED 끄기
    digitalWrite(Blue_Pin, LOW);
    delay(500);
    digitalWrite(Green_Pin, LOW);
    delay(500);
    digitalWrite(Red_Pin, LOW);
    delay(500);
}