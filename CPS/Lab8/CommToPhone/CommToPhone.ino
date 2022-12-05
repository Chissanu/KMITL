#include <SoftwareSerial.h>
SoftwareSerial BLESerial(2,3); // RX = 2, TX = 3

long previousMillis_BLE = 0;
long previousMillis_SRE = 0;

int interval_BLE = 100;
int interval_SRE = 200;

int potPin = A3;
String text;

void setup() {
  Serial.begin(9600);
  BLESerial.begin(9600);
  while(!Serial) {
    ;
  }
  Serial.println("Ready to go");
}

void loop() {
  unsigned long currentMillis = millis();
  if (currentMillis - previousMillis_BLE > interval_BLE) {
    previousMillis_BLE = currentMillis;
    while (BLESerial.available() > 0) {
      String in_str = BLESerial.readString();
      text = in_str;
      text.replace("\n","");
      while (text == "read") {
        Serial.println(analogRead(A0));
        BLESerial.print(analogRead(A0));
        in_str = BLESerial.readString();
        if (in_str == "stop") {
          break;
        }
        delay(3000);
      }
      if (in_str.length() == 0); else Serial.println(in_str);
    }
  }
  if (currentMillis - previousMillis_SRE > interval_BLE) {
    previousMillis_SRE = currentMillis;
    while (Serial.available()) {
      BLESerial.print((char) Serial.read());
    }
  }

  // if (Serial.available()>0) {
  //   BLESerial.write(Serial.read());
  // }
}
