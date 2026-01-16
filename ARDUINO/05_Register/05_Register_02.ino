void setup() {
    Serial.begin(9600);
    pinMode(10, OUTPUT); // LED 조정('~'있는 디지털 핀에 연결해야 함)
}

void loop() {
    int resistor = analogRead(A0);
    Serial.println(resistor);
    // map()이라는 내장함수를 사용해 입력값(0~1023)을 출력값(0~255)으로 변환
    // map(매핑하려는 값, 입력 범위의 최솟값, 입력 범위의 최댓값, 출력 범위의 최솟값, 출력 범위의 최댓값)
    resistor = map(resistor, 0, 1023, 0, 255);
    analogWrite(10, resistor);
    delay(100);
}