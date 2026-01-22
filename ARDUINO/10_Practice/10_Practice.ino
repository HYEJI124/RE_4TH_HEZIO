/*
가스 센서 기준값
A0 < 300 -> 파랑(정상)
300 <= A0 < 600 -> 초록(주의)
A0 >= 600 -> 빨강(위험)
*/

#include "DHT.h"

#define DHTPIN 3
#define DHTTYPE DHT11

#define GAS_A A0

#define LED_R 4
#define LED_G 5
#define LED_B 6

#define TRIG 9
#define ECHO 8

#define PIEZO 12
#define SWITCH 13

DHT dht(DHTPIN, DHTTYPE);

bool isDanger = false; // 가스 농도가 600 이상인 경우 true로 전환

float getDistance() {
    // 실수 값을 반환하는 함수를 만들 때
    digitalWrite(TRIG, HIGH);
    delayMicroseconds(10);
    digitalWrite(TRIG, LOW);

    float duration = pulseIn(ECHO, HIGH);
    float distance = ((34000 * duration)/1000000)/2;

    return distance; // 초음파센서가 측정한 거리 값을 받음
}

void setup() {
    Serial.begin(9600);
    dht.begin();

    pinMode(GAS_A, INPUT);

    pinMode(LED_R, OUTPUT);
    pinMode(LED_G, OUTPUT);
    pinMode(LED_B, OUTPUT);

    pinMode(TRIG, OUTPUT);
    pinMode(ECHO, INPUT);

    pinMode(PIEZO, OUTPUT);
    pinMode(SWITCH, INPUT_PULLUP); // 기본적으로 HIGH 상태

    delay(1000);
}

void loop() {
    delay(2000);

    // 온습도 시리얼 모니터에 출력
    float h = dht.readHumidity(); // 습도
    flaot c = dht.readTemperature(); // 온도

    // 가스 센서 A0 값 출력
    int gasVal = analogRead(GAS_A);

    // 초음파센서 거리
    float distance = getDistance();

    // 스위치 상태(눌렀을 때 LOW)
    int switchState = digitalRead(SWITCH);

    // 초음파센서로 5cm 거리에 물체 존재 여부 확인
    isDanger = false;

    Serial.print('DHT11 온습도 출력');
    Serial.println("습도: " + String(h) + "% 온도: " + String(c) + "°C");
    Serial.println('가스 센서 농도 출력');
    Serial.println('가스 농도(A0): ' + String(gasVal));
    Serial.println('거리: ' + String(distance) + 'cm');

    if (gasVal > 600) {
        isDanger = true;
        // 빨간색 LED ON
        digitalWrite(LED_R, HIGH);
        digitalWrite(LED_G, LOW);
        digitalWrite(LED_B, LOW);
    } else if (gasVal >= 300) {
        // 초록색 LED ON
        digitalWrite(LED_R, LOW);
        digitalWrite(LED_G, HIGH);
        digitalWrite(LED_B, LOW);
    } else {
        // 파란색 LED ON
        digitalWrite(LED_R, LOW);
        digitalWrite(LED_G, LOW);
        digitalWrite(LED_B, HIGH);
    }

    while (isDanger && distance <= 5.0) {
        digitalWrite(LED_R, HIGH);
        delay(100);
        digitalWrite(LED_R, LOW);
        delay(100);

        switchState = digitalRead(SWITCH); // 스위치 눌림 여부 확인

        if(switchState == LOW && isDanger) {
            digitalWrite(PIEZO, HIGH);
        } else {
            digitalWrite(PIEZO, LOW);
        }

        distance = getDistance(); // 무한 루프를 빠져나오는 코드
    }
    
    delay(500);
}