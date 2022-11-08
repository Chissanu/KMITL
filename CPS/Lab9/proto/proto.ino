#include <pt.h>
#define LED_1_PIN 9

static struct pt p1;

static int protothreadBlinkLed1(struct pt *pt) {
  static unsigned long lastTimeBlink = 0;
  PT_BEGIN(p1);
  while (1) {
    lastTImeBlink = millis();
    PT_WAIT_UNTIL(pt,millis() - lastTimeBlink > 1000);
    digitalWrite(LED_1_PIN,HIGH);
    lastTImeBlink = millis();
    PT_WAIT_UNTIL(pt,millis() - lastTimeBlink > 1000);
    digitalWrite(LED_1_PIN,LOW);
  }
  PT_END(pt);
}

void setup() {
  // put your setup code here, to run once:
  pinMode(LED_1_PIN,OUTPUT);
  PT_INIT(&pt1);

}

void loop() {
  // put your main code here, to run repeatedly:
  protothreadBlinkLed(&pt1);

}

