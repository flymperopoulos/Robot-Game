#include <Servo.h> 
#include <Adafruit_MotorShield.h>
#include <Wire.h>
#include "utility/Adafruit_PWMServoDriver.h"

//Adafruit_MotorShield AFMS= Adafruit_MotorShield(); 
Adafruit_MotorShield AFMS(0x60);

Adafruit_DCMotor *M3 = AFMS.getMotor(3);


Servo myservo;  
int pos = 0;    

String inputString = "";

void setup() {
  // initialize serial communications at 9600 bps
  Serial.begin(9600);
  // initializes motor  with shield  
  myservo.attach(13);
  AFMS.begin();

  inputString.reserve(200);
  
} 

void loop() 
{ 
//  while (Serial.available()){
//    char inChar = (char)Serial.read();
//    inputString += inChar;
//    
//    Serial.println("serial");
//    Serial.println(inputString);
//    delay(3);
//  }
//    if (inputString.length()>0){
//      Serial.println("inside the if loop");
//      Serial.println(inputString);
//        if (inputString[0] == 'U') {
//          Serial.println("inside the up");
//          for(pos = 0; pos < 90; pos += 1)  // goes from 0 degrees to 180 degrees 
//            {                                  // in steps of 1 degree
//              myservo.write(pos);              // tell servo to go to position in variable 'pos' 
//              delay(15);                       // waits 15ms for the servo to reach the position 
//            } 
//          }
//        else if (inputString[0] == 'D') {
//          Serial.println("inside the down");
//          for(pos = 90; pos>=1; pos-=1)     // goes from 180 degrees to 0 degrees 
//            {                                
//              myservo.write(pos);              // tell servo to go to position in variable 'pos' 
//              delay(15);                       // waits 15ms for the servo to reach the position 
//            }
//          }
//          delay(5000);
//          inputString = "";
////    } 

//M3->setSpeed(200);
// M3->run(FORWARD);
// delay(1000);

Serial.println("going down");
for(pos = 60; pos < 300; pos +=1)  // goes from 0 degrees to 180 degrees 
  {                                  // in steps of 1 degree 
    myservo.write(pos);              // tell servo to go to position in variable 'pos' 
    delay(15);                       // waits 15ms for the servo to reach the position 
  } 
      M3->setSpeed(240);
      M3->run(FORWARD);
  delay(5000);
Serial.println("going up");
for(pos = 300; pos> 60; pos-=1)
     // goes from 180 degrees to 0 degrees 
  {                                
    myservo.write(pos);              // tell servo to go to position in variable 'pos' 
    delay(15);                       // waits 15ms for the servo to reach the position 
  } 
      
  delay(5000);
  
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
  delay(5000);
Serial.println("going up");
for(pos = 300; pos> 60; pos-=1)
     // goes from 180 degrees to 0 degrees 
  {                                
    myservo.write(pos);              // tell servo to go to position in variable 'pos' 
    delay(15);                       // waits 15ms for the servo to reach the position 
  } 
     
  delay(5000);

} 

