#include <EEPROM.h>

struct MyObject{
  char serialNum[10];
  int size;
  char date[10];
  char name[4];
};

void setup() {
  
  int eeAddress = 0; //EEPROM address to start reading from

  Serial.begin(9600);
  Serial.print("Read float from EEPROM: ");

  eeAddress = sizeof(float); //Move address to the next byte after float 'f'.
  MyObject customVar; //Variable to store custom object read from EEPROM.
  EEPROM.get( eeAddress, customVar );
  Serial.println("Read custom object from EEPROM: ");
  Serial.println(customVar.serialNum);
  Serial.println(customVar.size);
//  Serial.println(customVar.date);
//  Serial.println(customVar.name);

}

void loop() {
  // put your main code here, to run repeatedly:

}
