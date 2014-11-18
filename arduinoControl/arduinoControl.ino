#include <Servo.h>

#include <Wire.h>
#include <Adafruit_MotorShield.h>
#include "utility/Adafruit_PWMServoDriver.h"

Adafruit_MotorShield AFMS = Adafruit_MotorShield(); 

Adafruit_StepperMotor *M1 = AFMS.getStepper(200, 2);
Adafruit_StepperMotor *M2 = AFMS.getStepper(200, 1);

int rpm = 1000;
int boardLength = 0;
int ls = 13;
int ws = 12;
int lengthSwitch = HIGH;
int widthSwitch = HIGH;
void setup() {
  // initialize serial communications at 9600 bps
  Serial.begin(9600);
  // initializes motor  with shield  
  AFMS.begin();
  // Initialize my motor
  
  pinMode(ls, INPUT);
  pinMode(ws, INPUT);
  
  M1->setSpeed(rpm);
  M2->setSpeed(rpm);
}

void loop(){
//  lengthSwitch = digitalRead(ls);
//  widthSwitch = digitalRead(ws);
  if(lengthSwitch != HIGH || widthSwitch != HIGH){
//    resetting to 0,0
    while(lengthSwitch != HIGH || widthSwitch !=HIGH){
      if(lengthSwitch != HIGH){
        M1->step(20, BACKWARD, SINGLE);
      }
      if(widthSwitch != HIGH){
        M2->step(20, BACKWARD, SINGLE);
      }
    }
  }
  
  M1->step(1000, BACKWARD, SINGLE);
  Serial.println("something");  
  M2->step(1000, BACKWARD, SINGLE);

}
