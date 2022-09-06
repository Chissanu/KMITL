#include <EEPROM.h>

struct MyObject{
  char serialNum[10];
  int size;
  char date[10];
  char name[10];
};

void setup() {
  Serial.begin(9600);
  float f = 123.456f;  //Variable to store in EEPROM.
  int eeAddress = 0;   //Location we want the data to be put.


  //One simple call, with the address first and the object second.
  EEPROM.put(eeAddress, f);
  MyObject customVar = {
    "TH01234",
    65,
    "Oct7,2020",
    "SIIE"
  };
  EEPROM.put(eeAddress, customVar);
}

void loop() {
}
