#include <Servo.h>
#include <Wire.h>
#include <Adafruit_MotorShield.h>
#include "utility/Adafruit_PWMServoDriver.h"

Adafruit_MotorShield AFMSbot(0x61); 
//Adafruit_MotorShield AFMSbot =Adafruit_MotorShield(); 
Adafruit_MotorShield AFMStop(0x60);

Adafruit_StepperMotor *M2 = AFMSbot.getStepper(200, 2);
Adafruit_StepperMotor *M1 = AFMSbot.getStepper(200, 1);
Adafruit_DCMotor *M3 = AFMStop.getMotor(1);

Servo servo1;

int pos = 0;
int rpm = 300;
int boardLength = 0;
const int servoPin = 9;
const int ledXGreen = 12;
const int ledYGreen = 13;


int lengthSwitch = HIGH;
int widthSwitch = HIGH;

String inputString = "";
String x1;
String y1;
String x2;
String y2;

void setup() {
  // initialize serial communications at 9600 bps
  Serial.begin(9600);

  // initializes motors and stepper with shield  
  AFMSbot.begin();
  AFMStop.begin();
 
  pinMode(ledXGreen, INPUT);
  pinMode(ledYGreen, INPUT);
  
  servo1.attach(servoPin);
  servo1.write(0);
  
  M1->setSpeed(rpm);
  M2->setSpeed(rpm);
  inputString.reserve(200);
}

void runXY(int xVal, int yVal, boolean xMovement, boolean yMovement){

  if (xMovement){
    M1->step(4110*xVal, FORWARD, DOUBLE);
  } else {
    M1->step(*xVal, BACKWARD, DOUBLE);
  }
  
  M1->release();
  
  if (yMovement){
    M2->step(3850*yVal, FORWARD, DOUBLE);
  } else {
    M2->step(3850*yVal, BACKWARD, DOUBLE);
  }

  M2->release();
}

void zAxisPickUp(){

 Serial.println("going down");
  for(pos = 10; pos < 85; pos +=1)  // goes from 0 degrees to 180 degrees 
    {                                  // in steps of 1 degree 
      servo1.write(pos);              // tell servo to go to position in variable 'pos' 
      delay(50);                       // waits 15ms for the servo to reach the position 
    } 
    delay(2000);
        M3->setSpeed(240);
        M3->run(FORWARD);
    delay(5000);
  Serial.println("going up");
  for(pos = 85; pos> 10; pos-=1)
       // goes from 180 degrees to 0 degrees 
    {                                
      servo1.write(pos);              // tell servo to go to position in variable 'pos' 
      delay(50);                       // waits 15ms for the servo to reach the position 
    }    
  delay(2000);
}

void zAxisRelease(){

  Serial.println("going down");
  for(pos = 10; pos < 85; pos +=1)  // goes from 0 degrees to 180 degrees 
    {                                  // in steps of 1 degree 
      servo1.write(pos);              // tell servo to go to position in variable 'pos' 
      delay(50);                       // waits 15ms for the servo to reach the position 
    } 
    
       M3->setSpeed(40);
       M3->run(BACKWARD);
       delay(200);
       M3->setSpeed(0);
       M3->run(FORWARD);
    delay(2000);
  Serial.println("going up");
  for(pos = 85; pos> 10; pos-=1)
       // goes from 180 degrees to 0 degrees 
    {                                
      servo1.write(pos);              // tell servo to go to position in variable 'pos' 
      delay(50);                       // waits 15ms for the servo to reach the position 
    }    
      M3->setSpeed(50);
      M3->run(BACKWARD);
      delay(1000);
      M3->setSpeed(0);
      M3->run(FORWARD);
       
  delay(2000);
}

void goToOrigin(){
  
  while(digitalRead(ledXGreen)){
    M1->step(100, BACKWARD, DOUBLE);  
  }
  M1->release();
  while(digitalRead(ledYGreen)){
    M2->step(100, BACKWARD, DOUBLE);
  }
  M2->release();
}

void loop(){
  while(Serial.available()){
//    Serial.println("serial is open");
    char inChar = (char)Serial.read();
    inputString += inChar;
    delay(3);
  }
  if (inputString.length()>0){

    x1 = inputString.substring(1,2);
    y1 = inputString.substring(3,4);
    x2 = inputString.substring(5,6);
    y2 = inputString.substring(7,8);
    
    int x1val = x1.toInt();
    int y1val = y1.toInt();
    int x2val = x2.toInt();
    int y2val = y2.toInt();
    
    Serial.println("go to origin");    
    
    goToOrigin();
    Serial.println("moving to 1, 1");
    runXY(1, 0, true, true);
    
    Serial.println("moving");
    
    runXY(x1val-1, y1val-1, true, true);
    Serial.println("picking up");
    zAxisPickUp();
    
    boolean pickX;
    boolean pickY;
    
    if(x2val - x1val > 0){
      pickX = true; 
    }else{
      pickX = false; 
    }
    
    if(y2val - y1val > 0){
      pickY = true; 
    }else{
      pickY = false; 
    }
    
    x2val = abs(x2val - x1val);
    y2val = abs(y2val - y1val);
    
    Serial.println("second moving ");
    runXY(x2val, y2val, pickX, pickY);

    Serial.println("putting down");
    zAxisRelease();
  
    inputString = "";
    Serial.println("finished move");
    
    Serial.println("go to origin");    
    
    goToOrigin();

  
  }


}
