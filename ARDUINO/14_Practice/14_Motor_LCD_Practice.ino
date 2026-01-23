#include <Servo.h>
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C myLCD(0x27, 16, 2);
Servo myServo;
int angle = 0;

void setup() {
    myServo.attach(10);
    myLCD.init();
    myLCD.backlight();
}

void loop() {
    int val = analogRead(A0);
    angle = map(val, 0, 1023, 0, 180);

    myServo.write(angle);

    myLCD.setCursor(0, 0);
    myLCD.print('Servo Motor');
    myLCD.setCursor(0, 1);
    myLCD.print(angle);

    delay(1000);

    myLCD.clear(); // 다음 값 입력이 잘 될 수 있도록
}