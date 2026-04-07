#include "ArduPID.h"

const int motorPin = 11;
const byte sensorPin = 3;
int motorSpeed=30;

int sensorValue;

// PID Settings
double Setpoint=550, Input; //Input is photo interrupter
double Output = 30; // motor
double consKp=0.001, consKi=0.000001, consKd=0.01;

ArduPID myController;


long Interval = 1000000;
unsigned long duration;
int temp;
int points; //number of measuring points
int Counter = 0;
unsigned long currTime = 0;
unsigned long prevTime = 0;


void setup() {
Serial.begin(9600);
pinMode(motorPin, OUTPUT);
pinMode(sensorPin, INPUT);

myController.begin(&Input, &Output, &Setpoint, consKp, consKi, consKd);

analogWrite(11, motorSpeed);
delay(5000);
attachInterrupt(digitalPinToInterrupt(sensorPin), Count, RISING);
}
void loop() {
  currTime = micros();
  if (currTime-prevTime>Interval){
    prevTime=currTime;
    Serial.print("RPM: ");
    Serial.print(Counter*30);
    Serial.print("  |  Output: ");
    Serial.println(Output);
    Input = Counter*30;
    Counter = 0;
  }

  myController.compute();
  analogWrite(motorPin, int(Output)); //motor is set to the output RPM
  delay(1);
}

void Count(){
  Counter ++;
}
