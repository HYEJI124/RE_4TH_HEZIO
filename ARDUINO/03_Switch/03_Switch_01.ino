int BTN = 2; // 연결 핀 변수 선언

void setup() {
    Serial.begin(9600); // PC와 시리얼 통신 시작, 통신 속도 = 9600 baud
    pinMode(BTN, INPUT); // 2핀에 연결된 스위치가 눌렸는지 읽어들이기 위해 INPUT 모드 설정    
}

void loop() {
    int buttonState = digitalRead(BTN); // 스위치 on, off 확인
    Serial.println(buttonState); // 시리얼 통신으로 읽은 값 전송
    delay(1);
}