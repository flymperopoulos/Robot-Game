#include <Servo.h>
#include <Wire.h>
#include <Adafruit_MotorShield.h>
#include "utility/Adafruit_PWMServoDriver.h"

Adafruit_MotorShield AFMSbot(0x60); 
Adafruit_MotorShield AFMStop(0x61);


Adafruit_StepperMotor *M1 = AFMSbot.getStepper(200, 2);
Adafruit_StepperMotor *M2 = AFMSbot.getStepper(200, 1);
Adafruit_DCMotor *M3 = AFMStop.getMotor(1);

Servo servo1;

int pos = 0;
int rpm = 300;
int boardLength = 0;
int ls = 13;
int ws = 12;
int lengthSwitch = HIGH;
int widthSwitch = HIGH;
String inputString = "";
String x;
String y;
void setup() {
  // initialize serial communications at 9600 bps
  Serial.begin(9600);
  // initializes motor  with shield  
  AFMSbot.begin();
  // Initialize my motor
  
  pinMode(ls, INPUT);
  pinMode(ws, INPUT);
  servo1.attach(9);
  
  M1->setSpeed(rpm);
  M2->setSpeed(rpm);
  M3->setSpeed(100);
  inputString.reserve(200);
  
}

void loop(){
//  Serial.println("Hello World");

  while(Serial.available()){
//    Serial.println("serial is open");
    char inChar = (char)Serial.read();
    inputString += inChar;
    delay(3);
  }
  if (inputString.length()>0){
    for (int i =0 ; i< inputString.length(); i++){
      if (inputString[i] == 'Y'){
        x = inputString.substring(1,i);
        y = inputString.substring(i+1,inputString.length());
//        Serial.println(y);
//        Serial.print(x+",");
//        Serial.println(y);
      }
    }
//    Serial.println(x);
    int xval = x.toInt();
    int yval = y.toInt();
//         Serial.println(yval);
    Serial.println(xval);
    M1->step(400*xval, FORWARD, SINGLE);
    M1->step(0, RELEASE,SINGLE);

    Serial.println(yval);
    M2->step(400*yval, FORWARD, SINGLE);
    M2->step(0, RELEASE,SINGLE);


    Serial.println("run");
//    servo1.write(180);
//    M3-> setSpeed(100);
//    M3-> run(FORWARD);
    
    inputString = "";
    for(pos = 160; pos > 100; pos -=1)  // goes from 0 degrees to 180 degrees 
  {                                  // in steps of 1 degree 
    servo1.write(pos);              // tell servo to go to position in variable 'pos' 
    delay(15);                       // waits 15ms for the servo to reach the position 
  } 
  Serial.println("hand");
    M3->setSpeed(200);
      M3->run(FORWARD);
  delay(5000);
  for(pos = 100; pos<=160; pos+=1)     // goes from 180 degrees to 0 degrees 
  {                                
      servo1.write(pos);              // tell servo to go to position in variable 'pos' 
      delay(15);                       // waits 15ms for the servo to reach the position 
  } 
      M3->setSpeed(0);
      M3->run(FORWARD);
    delay(5000);
    
  }
  

  
//  lengthSwitch = digitalRead(ls);
//  widthSwitch = digitalRead(ws);
//  if(lengthSwitch != HIGH || widthSwitch != HIGH){
////    resetting to 0,0
//    while(lengthSwitch != HIGH || widthSwitch !=HIGH){
//      if(lengthSwitch != HIGH){
//        M1->step(20, BACKWARD, SINGLE);
//      }
//      if(widthSwitch != HIGH){
//        M2->step(20, BACKWARD, SINGLE);
//      }
//    }
//  }
  
//  M1->step(3000, FORWARD,SINGLE);
//  Serial.println("something");  
//  M2->step(1000, FORWARD, SINGLE);

}
