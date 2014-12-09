#include <Servo.h> 
#include <Adafruit_MotorShield.h>
#include <Wire.h>
#include "utility/Adafruit_PWMServoDriver.h"

// Shield definition used for pump
Adafruit_MotorShield AFMS(0x60);
Adafruit_DCMotor *M3 = AFMS.getMotor(3);

// Servo definition initialization
Servo myservo;  
int pos = 0;    

// String that gets populated with coordinates to move to
String inputString = "";

// Definition of Pins - stepPin, dirPin, motorXPin, motorYPin
const int stepXPin = 13;     
const int dirXPin =  12;  
const int motorXPin = 11;

const int stepYPin = 10;     
const int dirYPin =  9;  
const int motorYPin = 8;

// The number of steps in one full motor rotation
const int stepsInFullRound = 400;

// Set pins
void setup() {

  // initialize serial communications at 9600 bps
  Serial.begin(9600);

  // initializes motor  with shield  
  myservo.attach(7);
  AFMS.begin();

  // step and dir pins for motorX
  pinMode(stepXPin, OUTPUT);      
  pinMode(dirXPin, OUTPUT);

  // step and dir pins for motorY
  pinMode(stepYPin, OUTPUT);      
  pinMode(dirYPin, OUTPUT);

  digitalWrite(stepXPin, LOW);
  digitalWrite(dirXPin, LOW); 

  digitalWrite(stepYPin, LOW);
  digitalWrite(dirYPin, LOW); 

  inputString.reserve(200);
}

// Runs the motor in X according to a chosen direction, speed (rounds per seconds) and the number of steps
void runX(boolean runForward, double speedRPS, int stepCount) {
  digitalWrite(dirXPin, runForward);
  for (int i = 0; i < stepCount; i++) {
    digitalWrite(stepXPin, HIGH);
    holdHalfCylce(speedRPS);
    digitalWrite(stepXPin, LOW);
    holdHalfCylce(speedRPS);
  }
}

// Runs the motor in X according to a chosen direction, speed (rounds per seconds) and the number of steps 
void runY(boolean runForward, double speedRPS, int stepCount) {
  digitalWrite(dirYPin, runForward);
  for (int i = 0; i < stepCount; i++) {
    digitalWrite(stepYPin, HIGH);
    holdHalfCylce(speedRPS);
    digitalWrite(stepYPin, LOW);
    holdHalfCylce(speedRPS);
  }
}

// A custom delay function used in the run()-method
void holdHalfCylce(double speedRPS) {
  long holdTime_us = (long)(1.0 / (double) stepsInFullRound / speedRPS / 2.0 * 1E6);
  int overflowCount = holdTime_us / 65535;
  for (int i = 0; i < overflowCount; i++) {
    delayMicroseconds(65535);
  }
  delayMicroseconds((unsigned int) holdTime_us);
}

// Runs the motors to the position of the checker piece
void runToPlace(double speedRPS, int rounds) {
  // Moves to the place the piece is
  runX(true, speedRPS, stepsInFullRound * rounds);
  delay(1000);
  runY(true, speedRPS, stepsInFullRound * rounds);
  delay(1000); 
}

// Picks up the checker piece
void zAxisPickUp(){

  Serial.println("going down");
  for(pos = 60; pos < 300; pos +=1)  // goes from 0 degrees to 180 degrees 
    {                                  // in steps of 1 degree 
      myservo.write(pos);              // tell servo to go to position in variable 'pos' 
      delay(15);                       // waits 15ms for the servo to reach the position 
    } 
        M3->setSpeed(240);
        M3->run(FORWARD);
    delay(2000);
  Serial.println("going up");
  for(pos = 300; pos> 60; pos-=1)
       // goes from 180 degrees to 0 degrees 
    {                                
      myservo.write(pos);              // tell servo to go to position in variable 'pos' 
      delay(15);                       // waits 15ms for the servo to reach the position 
    }    
  delay(2000);
}


// Re-positions the checkers piece
void runToNewPlace(double speedRPS, int rounds, boolean moveDirX, boolean modeDirY) {
  // Moves to the place the piece is
  runX(moveDirX, speedRPS, stepsInFullRound * rounds);
  delay(1000);
  runY(modeDirY, speedRPS, stepsInFullRound * rounds);
  delay(1000); 
}

// Releases piece to new place
void zAxisRelease(){

  Serial.println("going down");
  for(pos = 60; pos < 300; pos +=1)  // goes from 0 degrees to 180 degrees 
    {                                  // in steps of 1 degree 
      myservo.write(pos);              // tell servo to go to position in variable 'pos' 
      delay(15);                       // waits 15ms for the servo to reach the position 
    } 
       M3->setSpeed(40);
       M3->run(BACKWARD);
       delay(200);
       M3->setSpeed(0);
       M3->run(FORWARD);
    delay(2000);
  Serial.println("going up");
  for(pos = 300; pos> 60; pos-=1)
       // goes from 180 degrees to 0 degrees 
    {                                
      myservo.write(pos);              // tell servo to go to position in variable 'pos' 
      delay(15);                       // waits 15ms for the servo to reach the position 
    }    
  delay(2000);
}

// Runs the motors to the the start position
void runToStart(double speedRPS, int rounds) {
  // Moves back to the start
  runX(false, speedRPS, stepsInFullRound * rounds);
  delay(1000);
  runY(false, speedRPS, stepsInFullRound * rounds);
  delay(1000);
}

// Tests various speeds for 10 full rotations
void loop(){

  runToPlace(1,10);
  zAxisPickUp();
  runToNewPlace(1, 10, true, true);
  zAxisRelease();
  runToStart(1,10);

  // runBackAndForth(1, 10);
  // runBackAndForth(5, 10);
  // runBackAndForth(7, 10);
}
