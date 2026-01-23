#include <SPI.h>
#include <MFRC522.h>

#define SS_PIN 10
#define RST_PIN 9 

MFRC522 mfrc(SS_PIN, RST_PIN);

#define LED_R 3
#define LED_B 4
#define PIEZO 6

void setup() {
    Serial.begin(9600);
    SPI.begin();
    mfrc.PCD_Init();

    pinMode(LED_R, OUTPUT);
    pinMode(LED_B, OUTPUT);
    pinMode(PIEZO, OUTPUT);
}

void loop() {
    if (!mfrc.PICC_IsNewCardPresent() || !mfrc.PICC_ReadCardSerial()) {
        delay(500);
        return;
    }

    // 흰 태그
    if (mfrc.uid.uidByte[0] == 129 && mfrc.uid.uidByte[1] == 9 && mfrc.uid.uidByte[2] == 46 && mfrc.uid.uidByte[3] == 93) {
        digitalWrite(LED_B, HIGH);
        digitalWrite(PIEZO, HIGH);
        delay(1000);
        digitalWrite(PIEZO, LOW);
        digitalWrite(LED_B, LOW);

        return;
    }

    // 파란 태그
    if (mfrc.uid.uidByte[0] == 193 && mfrc.uid.uidByte[1] == 190 && mfrc.uid.uidByte[2] == 107 && mfrc.uid.uidByte[3] == 6) {
        digitalWrite(LED_R, HIGH);
        digitalWrite(PIEZO, HIGH);
        delay(1000);
        digitalWrite(PIEZO, LOW);
        digitalWrite(LED_R, LOW);
        delay(1000);
        digitalWrite(LED_R, HIGH);
        digitalWrite(PIEZO, HIGH);
        delay(1000);
        digitalWrite(PIEZO, LOW);
        digitalWrite(LED_R, LOW);
        delay(1000);

        return;
    }
}