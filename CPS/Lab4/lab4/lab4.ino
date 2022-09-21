
#include <Wire.h>

void setup() {
  Wire.begin(8);                // join i2c bus with address #8
  Wire.onRequest(requestEvent); // register event
  Serial.begin(9600);
  pinMode(A3,INPUT);
  
}

void loop() {
  Serial.println(analogRead(A2));
  delay(500);
}

// function that executes whenever data is requested by master
// this function is registered as an event, see setup()
void requestEvent() {
//  byte val = analogRead(A3) / 4;
//  Serial.println(val);
  int val = analogRead(A3);
  Wire.write(val / 4); // respond with message of 6 bytes
  delay(200);
  // as expected by master
}
