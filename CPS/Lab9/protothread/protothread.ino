#define LED_1_PIN 9
#define LED_2_PIN 10
#define LED_3_PIN 11

#define POTENTIOMETER_PIN A0

#define BUTTON_PIN 5

unsigned long previousTimeLed1 = millis();
long timeIntervalLed1 = 1000;
int ledState1 = LOW;

unsigned long previousTimeLed2 = millis();
long timeIntervalLed2 = 2000;
int ledState2 = LOW;

unsigned long previousTimeSerialPrintPotentiometer = millis();
long timeIntervalSerialPrint = 2000;

const int trigPin = 2;
const int echoPin = 3;
long duration;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  
  pinMode(LED_1_PIN, OUTPUT);
  pinMode(LED_2_PIN, OUTPUT);
  pinMode(LED_3_PIN, OUTPUT);
  pinMode(BUTTON_PIN, INPUT);

  pinMode(trigPin, OUTPUT);
  pinMode(echoPin,INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  unsigned long currentTime = millis();

  // task 1
  if(currentTime - previousTimeLed1 > timeIntervalLed1) {
    previousTimeLed1 = currentTime;

    if (ledState1 == HIGH) {
      ledState1 = LOW;
    }
    else {
      ledState1 = HIGH;
    }

    digitalWrite(LED_1_PIN, ledState1);
  }
  // task 2
  digitalWrite(trigPin,LOW);
  delayMicroseconds(2);

  digitalWrite(trigPin,HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin,LOW);

  duration = pulseIn(echoPin,HIGH);
  if (digitalRead(BUTTON_PIN) == HIGH) {
    Serial.println(duration);
  } else {
    delay(300);
  }
  // task 3
  if(currentTime - previousTimeLed2 > timeIntervalLed2) {
    previousTimeLed2 = currentTime;

    if (ledState2 == HIGH) {
      ledState2 = LOW;
    }
    else {
      ledState2 = HIGH;
    }

    digitalWrite(LED_2_PIN, ledState2);
  }

  // task 4
  //Serial.println(analogRead(A0));
  if (analogRead(A0) > 512) {
    digitalWrite(LED_3_PIN, HIGH);
  } else{
    digitalWrite(LED_3_PIN, LOW);
  }

}