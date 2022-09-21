#include <EEPROM.h>

struct MyObject{
  char serialNum[20];
  int ssize;
  char date[20];
  char uname[20];
};

void setup() {
  
  int eeAddress = 0; //EEPROM address to start reading from

  Serial.begin(9600);
  Serial.print("Read float from EEPROM: ");

  MyObject customVar; //Variable to store custom object read from EEPROM.
  EEPROM.get( eeAddress, customVar );
  Serial.println("Read custom object from EEPROM: ");
  Serial.println(customVar.serialNum);
  Serial.println(customVar.ssize);
  Serial.println(customVar.date);
  Serial.println(customVar.uname);

}

void loop() {
  // put your main code here, to run repeatedly:

}
